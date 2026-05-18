Here is your **complete, clean, professional Day 1 Markdown file** (ready to copy into `README.md`):

````markdown id="day1-full-md"
# 📄 Day 1 Documentation — Environment & Git Setup

This document describes the setup of the development environment and basic Git workflow for version control.

---

## 🎯 Objective

To set up Python development environment, configure VS Code, initialize Git, and practice basic Git commands.

---

## 1. 🐍 Python Installation

Python was installed on the system and verified successfully.

### ✅ Verification Command:
```bash
python --version
````

📸 Screenshot:
![Python Version](week1/day1/assets/python-version.png)

---

## 2. 🧪 Virtual Environment Setup

A virtual environment was created to isolate project dependencies and ensure clean package management.

### ✅ Create Virtual Environment:

```bash id="v1p2xq"
python -m venv venv
```

### ✅ Activate Virtual Environment (Ubuntu/Linux):

```bash id="c8m9ld"
source venv/bin/activate
```

📸 Screenshot:
![Virtual Environment Activation](week1/day1/assets/venv-activation.png)

---

## 3. 🖥️ VS Code Setup

Visual Studio Code was configured as the primary development environment for Python development.

### Steps Performed:

* Installed Visual Studio Code
* Opened project folder (`inventory-management-package`)
* Installed Python extension (Microsoft)
* Verified Python interpreter selection
* Configured workspace for development

### 📸 Screenshots:

* VS Code workspace opened
  ![VS Code Workspace](week1/day1/assets/vscode-workspace.png)

* Python extension installed
  ![VS Code Extensions](week1/day1/assets/vscode-extensions.png)

---

## 4. 🧾 Git Installation & Configuration

Git was installed and configured for version control and tracking changes in the project.

---

### 4.1 🔍 Git Version Check

```bash id="k3x8mp"
git --version
```

📸 Screenshot:
[Create Repository Button](week1/day1/assests/image copy.png)


---

### 4.2 👤 User Configuration

Git was configured with user identity for commit tracking.

```bash id="m9v4ld"
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

📸 Screenshot:
[Create Repository Button](week1/day1/assests/image.png)


---

## 5. 🌐 GitHub Repository Setup

A GitHub repository was created and linked to the local project.

### Steps Performed:

* Created repository on GitHub
* Cloned repository locally

```bash id="p2n7qx"
git clone <repo-url>
```

📸 Screenshot:
[Create Repository Button](week1/day1/assests/image copy.png)


---

## 6. ⚙️ Core Git Commands Practiced

Basic Git workflow commands were practiced for version control.

### Commands Used:

```bash id="t5v8mp"
git status
git add .
git commit -m "Initial setup"
git push origin main
```

📸 Screenshot:
[Create Repository Button](week1/day1/assests/image copy.png)
---

## 🎯 Outcome

By completing this task, the following skills were achieved:

* Python successfully installed and verified
* Virtual environment created and activated
* VS Code configured for development
* Git installed and configured
* GitHub repository connected
* Basic Git workflow understood and practiced

---

## 📁 Project Structure (Day 1)

```text id="r8m2vn"
inventory-management-package/
│
├── venv/
├── week1/
│   └── day1/
│       └── assets/
│           ├── python-version.png
│           ├── venv-activation.png
│           ├── vscode-workspace.png
│           ├── vscode-extensions.png
│           ├── git-version.png
│           ├── git-config.png
│           ├── git-clone.png
│           └── git-push.png
│
├── main.py
└── README.md
```

---

