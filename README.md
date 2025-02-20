# Resume Book Setup Guide

## Data Preparation Steps

Before setting up the environment, you need to prepare the data in **Excel** by following these steps:

1. **Export Data as CSV**

   - Download the latest attendee data from **Wufoo** as a **CSV file**.

2. **Open Data in Excel**

   - Open the exported CSV file in a **new Excel window**.

3. **Copy and Paste New Entries**

   - Copy the new attendee entries from the CSV file.
   - Paste them into the **"Attendees - Raw"** sheet of the file **`resumes.xlsm`**.

4. **Sort Alphabetically by First Name**

   - Select the data range.
   - Use the **Sort** function in Excel to arrange the entries alphabetically by **First Name**.

5. **Remove Duplicates**

   - Highlight the newly added entries.
   - Use the **Remove Duplicates** function to eliminate duplicate records.

6. **Copy and Paste Cleaned Entries**

   - Copy the **de-duplicated** entries from **"Attendees - Raw"**.
   - Paste them into the **"Attendees - Cleaned"** sheet.

7. **Apply Hyperlink Formula**

   - Drag the formula in **Column Y** (`=GetHyperlink(cell)`) down to apply it to the new entries.

8. **Save the Spreadsheet**
   - Make sure to **save** `resumes.xlsm` before closing Excel.

---

## Installation Instructions

### 1. Run the Setup Script

Open **Terminal**, navigate to the project folder, and execute the setup script:

```sh
cd path/to/resume_book
bash start.sh
```

### 2. Enter Your Password (If Prompted)

If the script asks for your **computer password**, type it and press **Enter**.  
(Note: You won’t see the password as you type, but it is being entered.)

### 3. Accept Installations

If prompted, simply **press Enter** to accept and continue the installation.

### 4. Running the Program

Once the setup is complete, you can extract resume pdfs by running:

```sh
python3 resumes.py
```

Then you can merge the resumes by running:

```sh
python3 merge.py
```

The merged resumes will be saved in the same folder as a single file.

---

## Troubleshooting

### Permission Denied Error

If you get a **permission denied** error when running `start.sh`, grant execution permissions by running:

```sh
chmod +x start.sh
```

Then try running the script again:

```sh
bash start.sh
```

### Python Not Recognized

If Python is still not recognized after installation, restart your terminal and check if it's installed:

```sh
python3 --version
```

---

## Next Steps

Once Python is installed, you can install additional dependencies by running:

```sh
pip install -r requirements.txt
```

You're all set! 🚀
