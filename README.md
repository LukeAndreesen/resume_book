````
# Resume Book Setup Guide

This guide provides step-by-step instructions to prepare attendee data and run the resume book program.

---

## Step 1: Download the Files from GitHub

### 1. Download the Repository

#### macOS
1. Click the **green "Code" button** on the top right of this page.
2. Click **"Download ZIP"**.
3. Once the download is complete, locate the ZIP file in **Finder** (typically in the "Downloads" folder).
4. **Double-click** the ZIP file to extract it. This will create a folder named **`resume_book-main`**.

#### Windows
1. Click the **green "Code" button** on the top right of this page.
2. Click **"Download ZIP"**.
3. Once the download is complete, locate the ZIP file in **File Explorer** (typically in the "Downloads" folder).
4. **Right-click** the ZIP file and select **"Extract All"**, then follow the prompts to extract the files.

### 2. Locate the Downloaded Files

#### macOS
To determine the exact path where the files are stored:
1. Open **Finder**.
2. Navigate to where the **`resume_book-main`** folder is located (e.g., "Desktop" or "Downloads").
3. **Right-click** on the `resume_book-main` folder and hold the option key, then select "Copy resume_book-main" as Pathname. This will copy the path to the file to the clipboard, which will look something like "/Users/username/Downloads/resume_book-main".

#### Windows
To determine the exact path where the files are stored:
1. Open **File Explorer**.
2. Navigate to where the **`resume_book-main`** folder is located (e.g., "Desktop" or "Downloads").
3. **Right-click** on the `resume_book-main` folder and select **"Properties"**.
4. Copy the "Location" value and append `\resume_book-main` to get the full path.

---

## Step 2: Prepare Your Data in Excel

The file **`resumes.xlsm`** is in the folder you downloaded. Open and edit it as follows:

### 1. Open the `resumes.xlsm` File

#### macOS
1. Navigate to the **`resume_book-main`** folder.
2. Double-click on **`resumes.xlsm`** to open it in **Microsoft Excel**.
3. Select the "Enable Macros" option when prompted (this enables the custom formula to get the PDF link).

#### Windows
1. Navigate to the **`resume_book-main`** folder.
2. Double-click on **`resumes.xlsm`** to open it in **Microsoft Excel**.
3. Click **Enable Macros** when prompted.

### 2. Copy and Paste New Entries

- Go to the **"Attendees - Raw"** sheet.
- Copy new attendee data from the CSV file you downloaded from **Wufoo**.
- Paste it into this sheet.

### 3. Sort Entries Alphabetically

- Highlight the new data.
- Click on **Sort & Filter** in Excel.
- Choose **Sort A to Z** (by **First Name**).

### 4. Remove Duplicates

- Highlight all newly added data.
- Click on **Data** → **Remove Duplicates**.

### 5. Move Cleaned Data

- Copy the cleaned data from **"Attendees - Raw"**.
- Paste it into the **"Attendees - Cleaned"** sheet.

### 6. Apply Hyperlink Formula

- In **Column Y**, drag the formula (`=GetHyperlink(cell)`) down to apply it to new entries.

### 7. Save the Spreadsheet

- Click **File** → **Save**.

---

## Step 3: Setting Up the Program

### 1. Open Terminal or Command Prompt

#### macOS
- Press **Command (⌘) + Spacebar**, type **"Terminal"**, and press **Enter**.

#### Windows
- Press **Windows + R**, type **"cmd"**, and press **Enter**.

### 2. Navigate to the `resume_book-main` Folder (using the path you copied earlier)

#### macOS
Type the following command and press **Enter**:

```sh
cd path/to/resume_book-main
````

#### Windows

Type the following command and press **Enter**:

```sh
cd "C:\path\to\resume_book-main"
```

### 3. Run the Setup Script

#### macOS

Type the following command and press **Enter**:

```sh
source start.sh
```

If a **password prompt** appears, enter your **computer password** and press **Enter** (nothing will appear as you type).

If prompted for confirmation, press **Enter**.

#### Windows

Type the following command and press **Enter**:

```sh
start.bat
```

If prompted for confirmation, press **Enter**.

---

## Step 4: Running the Resume Program

### 1. Extract the Resume PDFs

Run the following command:

```sh
python3 resumes.py
```

### 2. Convert any .docx to .pdf

Some resumes have been uploaded in .docx format, which will need to be converted manually. Open up all of the .docx files in Word and convert them to PDF, then move them back to the "resume\_to\_merge" folder, replacing the .docx versions with .pdf files.

### 3. Merge the Resumes

Run the following command:

```sh
python3 merge.py
```

The merged resume file will be saved in the `resume_book-main` folder.

---

## Troubleshooting

### "Permission Denied" Error

#### macOS

If you see a "permission denied" error, run:

```sh
chmod +x start.sh
```

Then retry:

```sh
bash start.sh
```

#### Windows

If you see a "permission denied" error, run Command Prompt as Administrator and try again.

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

## Setup Complete

```
```
