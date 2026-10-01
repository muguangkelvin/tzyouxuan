import os
import glob
import re

md_files = glob.glob("content/**/*.md", recursive=True)

print("--- Article Character Count Audit ---")
valid_count = 0
for filepath in sorted(md_files):
    if "_index.md" in filepath or "about.md" in filepath or "contact.md" in filepath:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Strip frontmatter
    parts = text.split("---")
    body = parts[2] if len(parts) >= 3 else text
    
    # Count Chinese characters
    cn_chars = len(re.sub(r'[^\u4e00-\u9fa5]', '', body))
    filename = os.path.basename(filepath)
    print(f"{filename:<20} | CN Chars: {cn_chars}")
    if cn_chars >= 1200:
        valid_count += 1

print(f"\nAudit finished. Total audited articles: {valid_count}")
