# 📘 Resume Book Setup Guide

This guide will walk you through preparing attendee data and running the resume book program, even if you've **never used a terminal or written code before**. Follow the steps carefully, and you'll be set up in no time!

---

## 📝 **Step 1: Prepare Your Data in Excel**

Before setting up the program, you need to organize the attendee data in **Excel**.

### 1️⃣ Download the Latest Attendee Data

- Log in to **Wufoo** and download the latest **attendee data** as a **CSV file** (this is a type of spreadsheet file).

### 2️⃣ Open the CSV File in Excel

- **Double-click** the downloaded CSV file to open it in **Microsoft Excel**.

### 3️⃣ Copy and Paste New Entries into the Master File

- **Open** the file called **`resumes.xlsm`** in Excel.
- Go to the **"Attendees - Raw"** sheet.
- Copy the new attendees from the CSV file and **paste them into this sheet**.

### 4️⃣ Sort Entries Alphabetically

- **Highlight** the new data you just pasted.
- Click on the **Sort & Filter** button (usually found in the Excel toolbar).
- Choose **Sort A to Z** (by **First Name**).

### 5️⃣ Remove Duplicates

- **Highlight** all the newly added data.
- Click on **Data** → **Remove Duplicates** (Excel will automatically delete any repeated entries).

### 6️⃣ Move the Cleaned Data

- Copy the **cleaned** data from **"Attendees - Raw"**.
- Paste it into the **"Attendees - Cleaned"** sheet.

### 7️⃣ Apply Hyperlink Formula

- In the **"Attendees - Cleaned"** sheet, find **Column Y**.
- Click on the first empty cell in Column Y.
- Drag the formula (`=GetHyperlink(cell)`) **down** so it applies to all new entries.

### 8️⃣ Save the Spreadsheet

- Click **File** → **Save** to make sure you don’t lose any changes.

---

## 🖥️ **Step 2: Setting Up the Program on Your Computer**

Now that your data is ready, let’s **install the software** and **run the program**.

### 1️⃣ Download the Program

1. **Go to the Resume Book project website**:  
   [GitHub: Resume Book](https://github.com/LukeAndreesen/resume_book)
2. Click the **green "Code" button**.
3. Click **"Download ZIP"**.
4. Once it finishes downloading, **double-click the ZIP file** to extract it.
5. Move the extracted **"resume_book"** folder to your **Desktop**.

---

## 🚀 **Step 3: Running the Program (No Coding Experience Needed!)**

To run the program, we’ll use an app called **Terminal**. Don’t worry if you’ve never heard of it! Just follow these steps:

### 1️⃣ Open Terminal

- If you're on **Mac**, press **Command (⌘) + Spacebar**, type **"Terminal"**, and press **Enter**.
- If you're on **Windows**, open the **Start Menu**, type **"Command Prompt"**, and click on it.

**(You’ll see a black or white window appear. This is where we type commands.)**

### 2️⃣ Navigate to the Resume Book Folder

Type this command and press **Enter**:

```sh
cd Desktop/resume_book
```

### 3️⃣ Start the Setup

Type this command and press **Enter**:

```sh
bash start.sh
```

🔹 If you see a **password prompt**, type your **computer password** and press **Enter**.  
🔹 (The password won’t appear as you type—this is normal.)  
🔹 If asked to **confirm any installations**, just press **Enter**.

---

## 📂 **Step 4: Running the Resume Program**

After the setup is done, you can now **extract resumes** and **combine them** into a single file.

### 1️⃣ Extract the Resume PDFs

Type this command and press **Enter**:

```sh
python3 resumes.py
```

### 2️⃣ Merge the Resumes

Type this command and press **Enter**:

```sh
python3 merge.py
```

The merged resumes will be saved in the same **resume_book** folder.

---

## 🔧 **Troubleshooting (Fixing Common Issues)**

### 🛑 "Permission Denied" Error

If you get an error saying **"permission denied"**, type this and press **Enter**:

```sh
chmod +x start.sh
```

Then try running the setup again:

```sh
bash start.sh
```

---

### 🛑 "Python Not Found" Error

If you see an error saying **"Python not recognized"**, you may need to install Python. Here’s how:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Click **Download Python** and install it.
3. Restart your computer.
4. Try running the program again.

To check if Python is installed, type:

```sh
python3 --version
```

You should see something like **"Python 3.x.x"** appear.

---

## 🎯 **Final Steps: Install Extra Tools (If Needed)**

If the program asks for missing tools, install them by typing:

```sh
pip install -r requirements.txt
```

Once installed, **you’re all set! 🚀**

---

## 🎉 **You're Done!**

You’ve successfully:

✅ Prepared the attendee data in Excel  
✅ Installed the program on your computer  
✅ Extracted and merged the resumes

If you need help, reach out to the team for support. 🎯
