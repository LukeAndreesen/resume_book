# Resume Book Setup Guide

## Introduction

This guide provides step-by-step instructions to set up Python on your macOS computer and install the necessary dependencies to run the **Resume Book** program.

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

Once the setup is complete, you can start using the **Resume Book** program.

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
