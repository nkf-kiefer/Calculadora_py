# ➕ Calculator ➖
> This project was made initially to study and improve my logical and technical skills using Python and good programming practices, as well as to practice English for technology.

---

![python](https://img.shields.io/badge/python-3.12%2B-blue)
![Flet](https://img.shields.io/badge/flet-0.28%2B-00A6ED)


---

## 📜 Table of Contents

1. [About](#About)  
2. [Features](#Features)  
3. [Screenshoots](#Screenshots)  
4. [Tech Stack](#TechStack)  
5. [Prerequisites](#Prerequisites)  
6. [Installation](#Installation)  
7. [Usage](#Usage)  
8. [Roadmap](#Roadmap)  
9. [Author](#Author)  

---

## 📌 About

> A simple, clean calculator application built to practice and improve programming skills, documentation, and code quality. It supports essential arithmetic and a few extra operations, with a focus on readability and a straightforward UI.

---

## 💻 Features

- Sum: Addition of numbers
- Subtraction: Difference between values
- Division: Quotient of two numbers
- Square root: Extracts the root of a value
- Exponentiation: Raises a number to a power (e.g., square)
- Remainder: Returns the modulo of a division
- Reciprocal: Converts a value to its fraction form (1/x)

| Feature | Status | Notes |
|---|---:|---|
| Addition | ✅ | Implemented |
| Subtraction | ✅ | Implemented |
| Multiplication | ✅ | Implemented |
| Division | ✅ | Error handling |
| Square root | ✅ | Validates input |
| Exponentiation | ✅ | x² supported |
| Modulo (%) | ✅ | Implemented |
| Reciprocal (1/x) | ✅ | Zero check |
| Clear / Backspace | ✅ | C and CE |
| Keyboard input | ❌ | Buttons only |
| Localization | ❌ | English only |
| Tests | ❌ | Not yet |


---

## 📸 Screenshots

![screenshot main](images/image.png)


---

## 🛠️ Tech Stack

| Layer | Technology / Library |
|---|---|
| Language | Python 3.12+ |
| UI toolkit | Flet (Page, Text, Container, Row, Column, ElevatedButton) |
| Operations | eval for +, −, ×, ÷, %, custom funcs for √, x², 1/x |
| Event handling | Flet callbacks (on_click) |
| State management | Local variable with nonlocal (values) |
| Rendering | page.add(...), page.update() |


---


## ⚙️ Prerequisites

- Python 3.12+
- pip (package manager)
- Virtual environment (venv recommended)
- Flet installed


---


## 🔨 Installation

```bash
git clone <REPO_URL>
cd <project-folder>
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```


---

## 🖥️ Usage

```bash
python Calculator.py
```


---


## 🛤️ Roadmap

| Version | Goal |
|---|---|
| v0.1 | MVP: basic calculator (+, −, ×, ÷, %, √, x², 1/x) |
| v0.2 | Input validation, keyboard input, error messages |
| v0.3 | Unit tests, code cleanup, docs |
| v0.4 | Packaging (exe) and settings |
| v1.0 | Web interface (Flet web) and polish |


---

## 😎 Author

**Natália Kiefer** — [GitHub](https://github.com/nkf-kiefer)

---
