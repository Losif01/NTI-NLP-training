
---
# 🧑‍🤝‍🧑 NTI-NLP-training Repository

Welcome to the **NTI-NLP-training** repository!  
This is a shared space where all students can upload their tasks and work throughout the training program.

Each contributor should:

- Create a **branch named after themselves**
- Add a **folder with their name**
- Store their personal work inside this folder
- Submit a **Pull Request (PR)** for review before merging

---

## 📌 Instructions for Contributors

### 1. 🛠️ Setup (One-Time Only)

If you haven't already, [set up Git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) on your machine and link it to your GitHub account.

```bash
git config --global user.name "YourName"
git config --global user.email "youremail@example.com"
```

> This sets your global username and email for all Git commits.

---

### 2. 🔄 Clone the Repository

Open your terminal (Linux/macOS) or Git Bash (Windows), then run:

```bash
git clone https://github.com/Losif01/NTI-NLP-training.git
cd NTI-NLP-training
```

---

### 3. 🔀 Create Your Branch

Each person should work in their **own branch**, named after them.

```bash
git checkout -b your-name
```

Example:
```bash
git checkout -b mohamed_hamza
```

---

### 4. 📁 Copy Your Folder Into the Repo (if you have an existing folder with your work)

You want to copy your local folder into the repo as a new folder named after you.

#### ✅ For Linux/macOS:

```bash
cp -r ~/absolute/path/of/your/folder your-branch-name/
```

Example:
```bash
cp -r ~/Desktop/FAIButBetter/ALL_TASKS_GIT_REPO/ mohamed_hamza/
```

> This will create a new folder called `mohamed_hamza/` inside the repo and copy all contents of `ALL_TASKS_GIT_REPO` into it.

If you'd prefer to rename the folder during copy:

```bash
mkdir mohsen
cp -r ~/Desktop/FAIButBetter/ALL_TASKS_GIT_REPO/* mohsen/
```

#### 💻 For Windows (Using Git Bash):

Make sure you're using **Git Bash** (comes with Git for Windows), not Command Prompt or PowerShell.

```bash
cp -r /c/Users/YourUsername/Desktop/FAIButBetter/ALL_TASKS_GIT_REPO/ mohamed_hamza/
```

Or, if you need to create a new folder first:

```bash
mkdir mohsen
cp -r /c/Users/YourUsername/Desktop/FAIButBetter/ALL_TASKS_GIT_REPO/* mohsen/
```

> ⚠️ Replace `YourUsername` with your actual Windows username.

---

### 5. 🚀 Commit and Push Changes

Add, commit, and push your changes to your branch:

```bash
git add .  # adds everything in the current folder
git commit -m "Add my work folder"
git push origin your-branch-name
```

---

### 6. 🧩 Open a Pull Request (Important)

After pushing your branch to GitHub:

1. Go to: [https://github.com/Losif01/NTI-NLP-training](https://github.com/Losif01/NTI-NLP-training)
2. You’ll see a banner saying:
   > "Compare & pull request" for your recently pushed branch.
3. Click on **"Compare & pull request"**
4. Fill in a clear title and description explaining what you added or changed.
5. Click **"Create pull request"**

A project maintainer will review your changes and merge them into the main branch if everything looks good.

---

## 📜 Contributing Guidelines

- Keep all files inside your own folder.
- Do not edit others' folders.
- Use descriptive commit messages and PR titles.
- Branch names should match your folder name.
- Always open a Pull Request for your changes to be reviewed before merging.
