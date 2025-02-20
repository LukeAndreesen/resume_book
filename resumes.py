import os
import pandas as pd
import requests
from tqdm import tqdm

# Path to your CSV file
csv_file = "resumes.csv"

# Folder to store the downloaded resumes
output_folder = "resume_to_merge"
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file
df = pd.read_csv(csv_file, usecols=["Resume URL"], encoding="ISO-8859-1")  # or "Windows-1252"

# Ensure the column exists
if "Resume URL" not in df.columns:
    raise ValueError("The CSV file does not contain a 'Resume URL' column.")

# Iterate over the resume URLs and download each file
for idx, url in tqdm(enumerate(df["Resume URL"]), total=len(df)):
    if pd.isna(url):  # Skip if URL is missing
        continue

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors

        # Generate a filename based on the index
        filename = os.path.join(output_folder, f"resume_{idx+1}.pdf")

        # Save the PDF file
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"Downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

print("All resumes have been downloaded.")
