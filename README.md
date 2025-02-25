# 📘 Resume Book Setup Guide

This guide provides step-by-step instructions to prepare attendee data and run the resume book program.

---

## 📝 **Step 1: Download the Files from GitHub**

### 1️⃣ Download the Repository


1. Click the **green "Code" button** on the top right of this page.
2. Click **"Download ZIP"**.
3. Once the download is complete, locate the ZIP file in **Finder** (typically in the "Downloads" folder).
4. **Double-click** the ZIP file to extract it. This will create a folder named **`resume_book-main`**.
5. Move the **`resume_book-main`** folder to your **Desktop**.

### 2️⃣ Locate the Downloaded Files

To determine the exact path where the files are stored:

1. Open **Finder**.
2. Navigate to where the **`resume_book-main`** folder is located (e.g., "Desktop" or "Downloads").
3. **Right-click** on the `resume_book-main` folder and select **"Get Info"**.
4. Look at the **"Where"** field to see the full file path.

---

## 📝 **Step 2: Prepare Your Data in Excel**

The file **`resumes.xlsm`** is included in the GitHub repository. Open and edit it as follows:

### 1️⃣ Open the `resumes.xlsm` File

1. Navigate to the **`resume_book-main`** folder.
2. Double-click on **`resumes.xlsm`** to open it in **Microsoft Excel**.

### 2️⃣ Copy and Paste New Entries

- Go to the **"Attendees - Raw"** sheet.
- Copy new attendee data from the CSV file you downloaded from **Wufoo**.
- Paste it into this sheet.

### 3️⃣ Sort Entries Alphabetically

- Highlight the new data.
- Click on **Sort & Filter** in Excel.
- Choose **Sort A to Z** (by **First Name**).

### 4️⃣ Remove Duplicates

- Highlight all newly added data.
- Click on **Data** → **Remove Duplicates**.

### 5️⃣ Move Cleaned Data

- Copy the cleaned data from **"Attendees - Raw"**.
- Paste it into the **"Attendees - Cleaned"** sheet.

### 6️⃣ Apply Hyperlink Formula

- In **Column Y**, drag the formula (`=GetHyperlink(cell)`) down to apply it to new entries.

### 7️⃣ Save the Spreadsheet

- Click **File** → **Save**.

---

## 🖥️ **Step 3: Setting Up the Program**

### 1️⃣ Open Terminal

- Press **Command (⌘) + Spacebar**, type **"Terminal"**, and press **Enter**.

### 2️⃣ Navigate to the `resume_book-main` Folder

Type the following command and press **Enter**:

```sh
cd path/to/resume_book-main
```

To determine the correct path:

1. Open **Finder**.
2. Locate **`resume_book-main`**.
3. Right-click on the folder and select **"Get Info"**.
4. Copy the file path from the **"Where"** field.
5. In Terminal, type `cd ` (with a space) and paste the copied path.
6. Press **Enter**.

### 3️⃣ Run the Setup Script

Type the following command and press **Enter**:

```sh
source start.sh
```

If a **password prompt** appears, enter your **computer password** and press **Enter** (nothing will appear as you type).

If prompted for confirmation, press **Enter**.

---

## 📂 **Step 4: Running the Resume Program**

### 1️⃣ Extract the Resume PDFs

Run the following command:

```sh
python3 resumes.py
```

### 2️⃣ Merge the Resumes

Run the following command:

```sh
python3 merge.py
```

The merged resume file will be saved in the `resume_book-main` folder.

---

## 🔧 **Troubleshooting**

### "Permission Denied" Error

If you see a "permission denied" error, run:

```sh
chmod +x start.sh
```

Then retry:

```sh
bash start.sh
```

### "Python Not Found" Error

Check if Python is installed:

```sh
python3 --version
```

If Python is not installed:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Download and install Python.
3. Restart your computer and retry.

### Install Missing Dependencies

If the program requires additional tools, install them with:

```sh
pip install -r requirements.txt
```

---

## **Setup Complete**
