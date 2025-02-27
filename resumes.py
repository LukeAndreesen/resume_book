import os
import pandas as pd
import requests
import shutil
from tqdm import tqdm

# Paths
xlsm_file = "resumes.xlsm"  # Replace with the actual file path
sheet_name = "Attendees - Cleaned"
csv_file = "resumes.csv"
output_folder = "resume_to_merge"

# Remove existing CSV file and folder if they exist
if os.path.exists(csv_file):
    os.remove(csv_file)
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

# Create a fresh output folder
os.makedirs(output_folder, exist_ok=True)

# Load the specific sheet from the .xlsm file and save as CSV
df = pd.read_excel(xlsm_file, sheet_name=sheet_name, usecols=["Resume URL", "Name", "Last"], engine="openpyxl")
df.to_csv(csv_file, index=False, encoding="ISO-8859-1")  # Save as CSV

# Ensure necessary columns exist
required_columns = ["Resume URL", "Name", "Last"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"The CSV file does not contain a '{col}' column.")

# Iterate over the resume URLs and download each file
for idx, row in tqdm(df.iterrows(), total=len(df)):
    url = row["Resume URL"]
    first_name = str(row["Name"]).strip().replace(" ", "_")
    last_name = str(row["Last"]).strip().replace(" ", "_")

    if pd.isna(url):  # Skip if URL is missing
        continue

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors

        # Generate a filename based on first and last name
        if pd.notna(first_name) and pd.notna(last_name) and first_name and last_name:
            filename = os.path.join(output_folder, f"{first_name}_{last_name}.pdf")
        else:
            filename = os.path.join(output_folder, f"resume_{idx+1}.pdf")

        # Save the PDF file
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"Downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

print("All resumes have been downloaded.")
