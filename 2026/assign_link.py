import csv
import re

CSV_FILE = "all_links.csv"
HTML_FILE = "Challenges.html"
OUTPUT_FILE = "updated_page.html"

# Load links from CSV into dictionary: {"A1": "link", "A2": "link", ...}
links = {}
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        links[row["ID"].strip()] = row["Link"].strip()

# Read HTML file
with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Process each ID and replace the following iframe src
for ID, link in links.items():
    # This pattern finds: <h2>A1</h2> ... <iframe src="...">
    pattern = rf'(<h2>{ID}</h2>[\s\S]*?<iframe\s+src=")([^"]*)"'
    replacement = rf'\1{link}"'
    html, count = re.subn(pattern, replacement, html)

    print(f"{ID}: replaced {count} link(s)")


# Save result
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("\nDone! Updated file saved as:", OUTPUT_FILE)
