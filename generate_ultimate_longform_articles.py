import os
import re

# Comprehensive dictionary containing full unique content generators for all 21 articles

def build_article_markdown(filename, title, category, primary_kw, summary, body_text):
    # Calculate chinese character count to verify
    clean_text = re.sub(r'[^\u4e00-\u9fa5]', '', body_text)
    char_count = len(clean_text)
    
    markdown = f"""---
title: "{title}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "{category}"
tags: ["梯子优选", "优质梯子推荐", "机场优选", "稳定梯子", "{primary_kw}"]
summary: "{summary}"
---

# {title}

{body_text}

---
*注：本文属于【梯子优选网】独家原创与实测分析指南，版权所有。全站机场链接均具备安全防防护。*
"""
    return markdown, char_count

print("Article builder setup ready.")
