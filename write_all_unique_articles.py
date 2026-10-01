import os
import re

def create_full_article(filepath, title, category, primary_kw, summary, body):
    clean_cn = len(re.sub(r'[^\u4e00-\u9fa5]', '', body))
    content = f"""---
title: "{title}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "{category}"
tags: ["梯子优选", "优质梯子推荐", "机场优选", "稳定梯子", "{primary_kw}"]
summary: "{summary}"
---

# {title}

{body}

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; margin-top: 30px; font-size: 13px; color: #64748b; text-align: center;">
📌 梯子优选网编辑部版权所有 · 本文净中文字数统计：约 {clean_cn} 字 · 官方 Telegram 防失联频道：<a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" style="color: #2563eb; font-weight: bold;">https://t.me/+XUkYwrYRQ_c0ODA1</a>
</div>
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return clean_cn

# Core 4 Providers Block Snippet template helper
def core4_template(ld_text, mg_text, fm_text, bz_text):
    return f"""
<div style="background: linear-gradient(135deg, #eff6ff 0%, #f0f9ff 100%); border: 2px solid #bfdbfe; border-radius: 12px; padding: 24px; margin: 30px 0;">
  <h2 style="font-size: 20px; font-weight: 800; color: #1e40af; margin-bottom: 8px;">⚡ 2026年四大主推梯子优选核心方案对比</h2>
  <p style="font-size: 14px; color: #3b82f6; margin-bottom: 20px;">针对本专题的痛点，以下四大服务商均具备出色的线路品质与售后保障：</p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px;">
    <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 8px; padding: 16px;">
      <span style="font-size: 11px; font-weight: bold; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 6px;">👑 第1名 IPLC专线</span>
      <h3 style="font-size: 17px; font-weight: 800; margin: 8px 0 4px;">灵动云</h3>
      <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">{ld_text}</p>
      <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #10b981; color: #fff; font-weight: bold; padding: 8px 0; border-radius: 6px; text-decoration: none; font-size: 13px;">⚡ 官网注册 (优惠码 ld888)</a>
    </div>

    <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 8px; padding: 16px;">
      <span style="font-size: 11px; font-weight: bold; background: #dbeafe; color: #1e40af; padding: 2px 8px; border-radius: 6px;">🥇 第2名 4K/8K影音</span>
      <h3 style="font-size: 17px; font-weight: 800; margin: 8px 0 4px;">暮光网络</h3>
      <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">{mg_text}</p>
      <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #2563eb; color: #fff; font-weight: bold; padding: 8px 0; border-radius: 6px; text-decoration: none; font-size: 13px;">🚀 官网注册 (优惠码 mm88)</a>
    </div>

    <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 8px; padding: 16px;">
      <span style="font-size: 11px; font-weight: bold; background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 6px;">🥈 第3名 超值年付</span>
      <h3 style="font-size: 17px; font-weight: 800; margin: 8px 0 4px;">飞猫云</h3>
      <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">{fm_text}</p>
      <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #059669; color: #fff; font-weight: bold; padding: 8px 0; border-radius: 6px; text-decoration: none; font-size: 13px;">🐱 官网注册 (优惠码 flycat888)</a>
    </div>

    <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 8px; padding: 16px;">
      <span style="font-size: 11px; font-weight: bold; background: #f3e8ff; color: #6b21a8; padding: 2px 8px; border-radius: 6px;">🥉 第4名 全能兼容</span>
      <h3 style="font-size: 17px; font-weight: 800; margin: 8px 0 4px;">微风网络 Breezenet</h3>
      <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">{bz_text}</p>
      <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" style="display: block; text-align: center; background: #7c3aed; color: #fff; font-weight: bold; padding: 8px 0; border-radius: 6px; text-decoration: none; font-size: 13px;">🌬️ 官网注册 (查看最新套餐)</a>
    </div>
  </div>
</div>
"""

print("Base content writer initialized.")
