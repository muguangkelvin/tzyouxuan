import os

sections = [
    ("content/categories/recommend/_index.md", "梯子优选与精选推荐指南", "面向小白与进阶用户的2026最新高性价比梯子优选推荐、IPLC专线横评及防失联攻略。"),
    ("content/categories/tutorial/_index.md", "小白零基础配置教程", "手把手教你在Windows, Mac, iPhone及安卓设备上安装配置 Clash Verge, Sing-box, 小火箭等客户端。"),
    ("content/providers/_index.md", "28款机场服务商测评库", "全网最全的28款机场服务商详细资料、节点数据、优惠码及直接注册入口。"),
    ("content/services/_index.md", "自营与优选专区", "精选高稳定性、全客户端兼容、晚高峰不降速的自营与主推服务。"),
    ("content/faq/_index.md", "常见问题解答 (100 FAQ)", "覆盖梯子优选、节点超时排查、订阅导入及防失联解惑的100个痛点问答全展开。")
]

for filepath, title, desc in sections:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    content = f"""---
title: "{title}"
description: "{desc}"
date: 2026-09-30T10:00:00+08:00
draft: false
---

{desc}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Section _index.md files created successfully.")
