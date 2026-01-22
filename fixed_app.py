from flask import Flask, render_template, request, Response
import google.generativeai as genai
import re

# ---------------- APP CONFIG ----------------
app = Flask(__name__)

# 🔒 ADD YOUR GEMINI API KEY HERE
GEMINI_API_KEY = "AIzaSyDxCMGVTByVBnBjLJRROTpcxpRQQi7JMPI"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"

LANGUAGE_FILE_EXT = {
    "Python": "py",
    "Java": "java",
    "C++": "cpp",
    "JavaScript": "js"
}

# ---------------- LANGUAGE DETECTION ----------------
def detect_language(code, filename=None):
    scores = {
        "Python": 0,
        "Java": 0,
        "C++": 0,
        "JavaScript": 0
    }

    if filename:
        ext = filename.split(".")[-1].lower()
        if ext == "py":
            scores["Python"] += 5
        elif ext == "java":
            scores["Java"] += 5
        elif ext in ["cpp", "c"]:
            scores["C++"] += 5
        elif ext == "js":
            scores["JavaScript"] += 5

    python_patterns = [r"\bdef\b", r"\bimport\b", r":\s*\n", r"^\s{4,}\S"]
    java_patterns = [r"\bpublic class\b", r"\bstatic void main\b", r"System\.out\.println"]
    cpp_patterns = [r"#include\s*<", r"\bstd::\b", r"\bint\s+main\s*\("]
    js_patterns = [r"\bconsole\.log\b", r"\bfunction\b", r"\blet\b", r"\bconst\b", r"=>"]

    for p in python_patterns:
        if re.search(p, code, re.MULTILINE):
            scores["Python"] += 2
    for p in java_patterns:
        if re.search(p, code):
            scores["Java"] += 2
    for p in cpp_patterns:
        if re.search(p, code):
            scores["C++"] += 2
    for p in js_patterns:
        if re.search(p, code):
            scores["JavaScript"] += 2

    detected = max(scores, key=scores.get)
    return detected if scores[detected] >= 3 else None

# ---------------- PROMPT BUILDER ----------------
def build_prompt(code, language, style, output_format, complexity, summary):
    summary_instruction = ""
    if summary:
        summary_instruction = """
AFTER annotating the code, provide a SHORT and BRIEF explanation
(3-5 lines) explaining what the program does as a whole.
Label it clearly as:
--- Program Explanation ---
"""

    return f"""
You are a professional code annotation assistant.

TASK:
Add clear, accurate, short and brief annotations to the given code.

PARAMETERS:
- Programming Language: {language}
- Explanation Style: {style}
- Output Format: {output_format}
- Include Time & Space Complexity: {complexity}

RULES:
1. Do NOT change program logic.
2. Do NOT remove existing code.
3. Add annotations as comments only.
4. Match comment syntax of the language.

{summary_instruction}

CODE:
{code}
"""

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None, language=None, error=None)

@app.route("/annotate", methods=["POST"])
def annotate():
    code = request.form.get("code", "").strip()
    uploaded_file = request.files.get("file")

    filename = None
    
    # Prioritize file upload over textarea
    if uploaded_file and uploaded_file.filename:
        filename = uploaded_file.filename
        try:
            code = uploaded_file.read().decode("utf-8")
        except Exception as e:
            return render_template("index.html", error=f"❌ Failed to read file: {str(e)}", result=None, language=None)

    if not code:
        return render_template("index.html", error="⚠️ Please provide code input.", result=None, language=None)

    language = detect_language(code, filename)
    if not language:
        return render_template("index.html", error="❌ This programming language is not supported.", result=None, language=None)

    style = request.form.get("style", "Beginner")
    output_format = request.form.get("format", "Inline Comments")
    complexity = "Yes" if request.form.get("complexity") else "No"
    summary = True if request.form.get("summary") else False

    prompt = build_prompt(code, language, style, output_format, complexity, summary)

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        annotated_code = response.text
    except Exception as e:
        return render_template("index.html", error=f"❌ Error: {str(e)}", result=None, language=None)

    return render_template(
        "index.html",
        result=annotated_code,
        language=language,
        error=None
    )

@app.route("/download", methods=["POST"])
def download():
    annotated_code = request.form.get("annotated_code", "")
    language = request.form.get("language", "")

    if not annotated_code:
        return "No code to download", 400

    ext = LANGUAGE_FILE_EXT.get(language, "txt")
    filename = f"annotated_code.{ext}"

    return Response(
        annotated_code,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=True)