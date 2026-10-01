import os
import json
import csv

os.makedirs("data", exist_ok=True)
os.makedirs("docs", exist_ok=True)
os.makedirs("content/categories/recommend", exist_ok=True)
os.makedirs("content/categories/tutorial", exist_ok=True)
os.makedirs("content/services", exist_ok=True)
os.makedirs("content/providers", exist_ok=True)
os.makedirs("content/faq", exist_ok=True)
os.makedirs("content/guides", exist_ok=True)
os.makedirs("content/reviews", exist_ok=True)
os.makedirs("layouts/_default", exist_ok=True)
os.makedirs("layouts/partials", exist_ok=True)
os.makedirs("layouts/categories", exist_ok=True)
os.makedirs("layouts/faq", exist_ok=True)
os.makedirs("layouts/services", exist_ok=True)
os.makedirs("layouts/providers", exist_ok=True)
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)

print("Directories initialized successfully.")
