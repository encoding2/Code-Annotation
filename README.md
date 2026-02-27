🤖 AI Code Annotator & README Generator

An AI-powered web application that automatically annotates source code, generates brief explanations with time & space complexity analysis, and creates professional README.md and requirements.txt files using Google's Gemini 2.5 Flash model.

Built with Python (Flask) and integrated with Google Generative AI, this tool acts as a lightweight AI developer assistant.

🚀 Features
🔹 Code Annotation

Supports Python, Java, C++, and JavaScript

Automatically detects programming language

Adds very brief block-style comments

Preserves original logic (no modification)

Displays:

📘 Short program explanation

⏱ Time complexity

📦 Space complexity

Download annotated file in its original format (.py, .java, .cpp, .js)

🔹 README & Documentation Generator

Generates a professional README.md

Adds language badges

Extracts and generates requirements.txt (for Python projects)

Supports:

Pasted project code

Uploaded source files

Full project ZIP uploads

🛠 Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS

AI Model: Google Gemini 2.5 Flash

Other Tools: Regex-based language detection, ZIP extraction

📂 Supported Languages

Python (.py)

Java (.java)

C++ (.cpp)

JavaScript (.js)

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-code-annotator.git
cd ai-code-annotator
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Your Gemini API Key

Open app.py and replace:

GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

with your actual API key.

▶️ Run the Application
python app.py

Then open in browser:

http://127.0.0.1:5000/
🧠 How It Works

User pastes or uploads code.

Backend detects the programming language using pattern matching.

Code is sent to Gemini model with controlled prompts.

AI returns:

Annotated code (brief block comments)

Separate explanation

Time & space complexity

User can download annotated file in original format.

For documentation:

User uploads project or ZIP file.

System extracts source files.

Gemini generates README and requirements (if Python).

Files are displayed and downloadable.

📸 Screenshots (Optional)

You can add screenshots here:

![Annotation Page](screenshots/annotation.png)
![README Generator](screenshots/readme.png)
🎯 Use Cases

Students learning new programming languages

Understanding competitive programming solutions

Quickly documenting GitHub projects

Interview preparation

Code review assistance

🔮 Future Enhancements

Syntax highlighting

Copy-to-clipboard button

AI-based language detection (instead of regex)

Docker deployment

Authentication system

Cloud hosting support

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Vignesh Vishal
Artificial Intelligence & Data Science
Passionate about AI-driven developer tools 🚀

If you want, I can now give you:

🔥 A more advanced README (with badges + shields.io)

🎓 A resume-ready project description

📊 A system architecture diagram explanation
