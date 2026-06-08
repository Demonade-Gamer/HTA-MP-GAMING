import os
import csv

def search_csvs(search_term):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    matches = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(".csv"):
            file_path = os.path.join(folder_path, file)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    reader = csv.reader(f)

                    for line_num, row in enumerate(reader, start=1):
                        row_text = ",".join(row)

                        if search_term.lower() in row_text.lower():
                            match = f"{file} | line {line_num} | {row_text}"
                            print(match)
                            matches.append(match)

            except Exception as e:
                print(f"Error reading {file}: {e}")

    print(f"\nDone. Found {len(matches)} matches.")


if __name__ == "__main__":
    term = input("Enter search string: ").strip()
    search_csvs(term)