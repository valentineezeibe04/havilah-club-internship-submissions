# Day 15 — Python Automation Project
# Option A: File Organiser
# Task: Scans a folder and moves files into subfolders based on file extensions.

import os
import shutil

# ── Configuration ─────────────────────────────────────────────────────────────
INPUT_PATH = "week-3/day-15-automation-project/data/"
OUTPUT_PATH = "week-3/day-15-automation-project/data/output/"


# ── Core Functions ─────────────────────────────────────────────────────────────

def ensure_directories_exist(input_path, output_path):
    """Function 1: Ensures both input and output directories exist."""
    if not os.path.exists(input_path):
        os.makedirs(input_path)
        print(f"Created missing input directory: {input_path}")
        
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Created output directory: {output_path}")


def get_category_folder(file_extension):
    """Function 2: Maps file extensions to descriptive folder names."""
    ext = file_extension.lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif']:
        return "Images"
    elif ext in ['.pdf', '.doc', '.docx', '.txt']:
        return "Documents"
    elif ext in ['.csv', '.xlsx', '.json']:
        return "Data"
    elif ext in ['.mp3', '.wav']:
        return "Audio"
    elif ext in ['.mp4', '.mkv']:
        return "Videos"
    else:
        return "Others"


def organize_files(input_path, output_path):
    """Function 3: Scans input_path and moves files into organized category folders."""
    try:
        files = os.listdir(input_path)
    except FileNotFoundError:
        print(f"Error: Directory '{input_path}' not found.")
        return

    # Edge Case Handle: Check if folder is empty
    if not files:
        print(f"No files found in '{input_path}' to organize.")
        return

    moved_count = 0
    for file_name in files:
        file_full_path = os.path.join(input_path, file_name)

        # Skip directories (only process files)
        if os.path.isdir(file_full_path):
            continue

        # Extract file extension
        _, file_extension = os.path.splitext(file_name)

        # Edge Case Handle: File with no extension
        if not file_extension:
            category = "No_Extension"
        else:
            category = get_category_folder(file_extension)

        category_folder_path = os.path.join(output_path, category)
        if not os.path.exists(category_folder_path):
            os.makedirs(category_folder_path)

        destination_path = os.path.join(category_folder_path, file_name)
        shutil.move(file_full_path, destination_path)
        print(f"Moved: '{file_name}' -> '{category}/'")
        moved_count += 1

    print(f"\nAutomation Complete: Organised {moved_count} file(s).")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Starting File Organiser Automation...")
    ensure_directories_exist(INPUT_PATH, OUTPUT_PATH)
    organize_files(INPUT_PATH, OUTPUT_PATH)
    print("Done.")


if __name__ == "__main__":
    main()