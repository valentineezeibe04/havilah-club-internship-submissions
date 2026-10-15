# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean text fields and convert score to float
                cleaned_row = {
                    "name": row["name"].strip(),
                    "score": float(row["score"].strip()),
                    "grade": row["grade"].strip().upper()
                }
                rows.append(cleaned_row)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Make sure the file exists.")
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    total_rows = len(rows)
    print(f"\n--- Dataset Summary ---")
    print(f"Total Records: {total_rows}")
    
    if total_rows == 0:
        return

    scores = [row["score"] for row in rows]
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / total_rows

    print(f"Score Statistics:")
    print(f"  - Minimum Score: {min_score}")
    print(f"  - Maximum Score: {max_score}")
    print(f"  - Average Score: {avg_score:.2f}\n")


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above or equal to 70.

def filter_data(rows):
    # Filtering students with a score of 70 or higher
    filtered = [row for row in rows if row["score"] >= 70]
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    # Sort rows by 'score' in descending order (highest score first)
    sorted_rows = sorted(rows, key=lambda x: x["score"], reverse=True)
    
    fieldnames = ["name", "score", "grade"]
    
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)
    except Exception as e:
        print(f"Error writing to file: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    if rows:
        print_summary(rows)
        filtered = filter_data(rows)
        save_data(filtered, OUTPUT_FILE)
        print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()