# 🤖 AI Code Annotator & Documentation Generator

![Python](https://img.shields.io/badge/Language-Python-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered web application that automatically annotates source code and generates professional project documentation using Google Gemini AI.

---

## 🚀 Overview

The **AI Code Annotator & Documentation Generator** is a developer assistant web application built using **Python (Flask)** and integrated with **Google Gemini 2.5 Flash**.

It allows users to:

- Automatically annotate code with concise block-style comments  
- Generate brief explanations of how a program works  
- Analyze time and space complexity  
- Create professional `README.md` files  
- Generate `requirements.txt` from Python projects  
- Upload and analyze full project ZIP files  

This tool is designed to improve code readability, accelerate documentation, and support learning.

---

## 🧠 Features

### 📝 Code Annotation
- Supports **Python, Java, C++, and JavaScript**
- Intelligent language detection (works for competitive coding formats like LeetCode)
- Adds **brief block-style comments**
- Displays:
  - Program explanation
  - Time complexity
  - Space complexity
- Download annotated file in original format (.py, .java, .cpp, .js)

---

### 📄 README Generator
- Generates professional GitHub-ready `README.md`
- Adds language badges automatically
- Extracts project structure details
- Accepts:
  - Single source files
  - Entire project ZIP uploads

---

### 📦 Requirements Generator
- Detects Python dependencies
- Generates `requirements.txt`
- Available when Python is detected

---

## 🏗️ System Architecture

### Backend
- Python
- Flask
- Google Generative AI SDK
- Regex-based language detection
- ZIP extraction handling

### Frontend
- HTML
- CSS (Dark Developer Theme)
- Separate pages for:
  - Annotation
  - README Generation

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-code-annotator.git
cd ai-code-annotator
