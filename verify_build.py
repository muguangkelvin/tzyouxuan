import os
import re
import glob

print("--- Starting Build Output Audit ---")

public_dir = "public"
html_files = glob.glob(os.path.join(public_dir, "**/*.html"), recursive=True)

print(f"Total HTML files generated: {len(html_files)}")

affiliate_domains = [
    "gcvipaff.com", "flycatvipaff.cc", "twilightaff.com", "breezenetaff.com",
    "invisibleaff.com", "wavenetaff.com", "ladderaff.com", "flyvaff.com",
    "xingdaomeng.com", "gsyaff.com", "v2yunvipaff.com", "vipaff.cc", "jlyvipaff.com",
    "gntaff.com", "sogoyunaff.cc", "yuzoucloud.cc", "2maoyunaff.cc", "1flyunaff.cc",
    "edgenovaaff.cc", "kosingaff.com", "speedworldaff.cc", "kuailicloud.cc",
    "worryfreeaff.com", "civetaff.com", "flashleapaff.com", "fireflyaff.com", "kuajieaff.com"
]

missing_rel_links = []
valid_aff_links = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for tag in re.finditer(r'<a\s+[^>]*>', content, re.IGNORECASE):
        tag_str = tag.group(0)
        href_match = re.search(r'href=["\']([^"\']+)["\']', tag_str, re.IGNORECASE)
        if href_match:
            href = href_match.group(1)
            is_aff = any(domain in href for domain in affiliate_domains)
            if is_aff:
                valid_aff_links += 1
                if 'rel="sponsored nofollow noopener"' not in tag_str and "rel='sponsored nofollow noopener'" not in tag_str:
                    missing_rel_links.append((file_path, href, tag_str))

print(f"Total affiliate link instances checked: {valid_aff_links}")
if missing_rel_links:
    print(f"WARNING: Found {len(missing_rel_links)} affiliate links missing rel attributes!")
    for item in missing_rel_links[:5]:
        print(item)
else:
    print("[SUCCESS] All affiliate links strictly include rel='sponsored nofollow noopener'!")

tg_link = "https://t.me/+XUkYwrYRQ_c0ODA1"
header_has_tg = False
contact_has_tg = False

index_path = os.path.join(public_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        if tg_link in f.read():
            header_has_tg = True

contact_path = os.path.join(public_dir, "contact", "index.html")
if os.path.exists(contact_path):
    with open(contact_path, "r", encoding="utf-8") as f:
        if tg_link in f.read():
            contact_has_tg = True

print(f"Header & Homepage contains TG Channel link: {header_has_tg}")
print(f"Contact Page contains TG Channel link: {contact_has_tg}")

faq_files = glob.glob(os.path.join(public_dir, "faq", "**/*.html"), recursive=True)
print(f"Total FAQ pages/items generated: {len(faq_files)}")

provider_files = glob.glob(os.path.join(public_dir, "providers", "**/*.html"), recursive=True)
print(f"Total Provider pages generated: {len(provider_files)}")

print("--- Audit Completed ---")
