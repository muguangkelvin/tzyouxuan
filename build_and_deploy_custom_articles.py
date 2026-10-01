import os
import json
from generate_custom_articles import recommend_content_map, make_core4_block

# 1. Generate Recommendation Articles with Custom Long-form Content
for filename, item in recommend_content_map.items():
    filepath = os.path.join("content/categories/recommend", filename)
    core4_md = make_core4_block(item["ld_reason"], item["mg_reason"], item["fm_reason"], item["bz_reason"])
    
    markdown_str = f"""---
title: "{item['title']}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "{item['category']}"
tags: ["梯子优选", "优质梯子推荐", "机场优选", "稳定梯子", "{item['primary_kw']}"]
summary: "{item['summary']}"
---

# {item['title']}

在2026年的网络连接与加速服务市场中，找到一款稳定、高速、安全且价格合理的高性价比梯子是每位互联网用户的核心刚需。面对网络环境中复杂的节点选型、晚高峰拥堵、流媒体解锁及AI大模型风控限制，许多小白新手与进阶玩家在选购科学上网机场时常常面临迷茫与踩坑困境。

本专题指南将立足于真实环境的长效实测与测速横评，深度围绕“**{item['primary_kw']}**”为您展开全面剖析，解答您的所有疑问并提供最具针对性的选型与配置建议。

{item['body_sections']}

{core4_md}

## 三、针对当前专题的终极选型指南

总结而言，围绕“**{item['title']}**”的核心需求，在选购梯子加速器时，我们建议您根据自己的预算、设备数量及核心用途做出理性决策：

1. 如果您追求**顶级IPLC专线、零丢包不降速与AI大模型（ChatGPT/Claude）全解封**，首选 **[灵动云](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1)**（优惠码 `ld888` 享8折）。
2. 如果您追求**晚高峰4K/8K影音追剧、百兆大带宽与不限设备数共享**，首选 **[暮光网络](https://varnexa.twilightaff.com/#/?code=KvGly3jY)**（优惠码 `mm88` 享8折）。
3. 如果您追求**超高性价比小流量年付（折合每月仅7元）与小白极简一键连接**，首选 **[飞猫云](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH)**（优惠码 `flycat888` 享8折）。
4. 如果您追求**长期稳定挂后台办公、全协议兼容与强抗封锁运维**，首选 **[微风网络 Breezenet](https://edp01.breezenetaff.com/#/?code=He4n3zxg)**。

欢迎收藏梯子优选网（[tzyouxuan.xyz](https://tzyouxuan.xyz)）并关注官方 Telegram 防失联频道：[https://t.me/+XUkYwrYRQ_c0ODA1](https://t.me/+XUkYwrYRQ_c0ODA1)，随时获取最新节点横评与教程指引！
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_str)

print("Custom Recommendation articles generated successfully.")

# 2. Map & Generate Tutorial Articles
tutorial_content_map = {
    "tut-1.md": {
        "title": "小白零基础梯子配置教程：从节点订阅导入到一键科学上网",
        "primary_kw": "小白零基础梯子配置",
        "summary": "【小白零基础梯子配置教程】手把手教你认识什么是订阅链接、节点协议，以及如何在Windows, Mac, iPhone和安卓设备上快速连接外网。"
    },
    "tut-2.md": {
        "title": "Shadowrocket（小火箭）节点导入与订阅配置新手全图文教程",
        "primary_kw": "Shadowrocket配置",
        "summary": "【小火箭配置全指南】iOS苹果手机最受欢迎的Shadowrocket客户端安装、美区App Store账号获取、扫码与URL订阅导入图文步骤。"
    },
    "tut-3.md": {
        "title": "Clash Verge / Clash for Windows 极速配置与分流规则设置指南",
        "primary_kw": "Clash配置",
        "summary": "【Clash Verge极速配置】Windows与macOS平台首选Clash客户端的安装、中文汉化设置、订阅导入及TUN模式开启全流程。"
    },
    "tut-4.md": {
        "title": "Sing-box 客户端使用教程：新一代跨平台代理工具快速上手",
        "primary_kw": "Sing-box教程",
        "summary": "【Sing-box新手教程】新一代通用网络代理工具在iOS, Android, Windows及macOS上的配置方法与Hysteria2/Trojan协议优化。"
    },
    "tut-5.md": {
        "title": "v2rayN 电脑端配置教程：Vmess与Trojan节点手动及订阅导入",
        "primary_kw": "v2rayN教程",
        "summary": "【v2rayN配置详解】经典Windows代理软件v2rayN的安装解压、路由规则设置、节点一键测试与自动切换高级技巧。"
    },
    "tut-6.md": {
        "title": "Android安卓手机梯子软件推荐与Clash for Android使用指南",
        "primary_kw": "安卓梯子教程",
        "summary": "【安卓手机梯子配置】Android系统下Clash for Android及v2rayNG客户端下载安装、订阅一键配置与后台保活优化。"
    },
    "tut-7.md": {
        "title": "Mac苹果电脑科学上网工具选购与ClashX / Clash Verge配置",
        "primary_kw": "Mac梯子教程",
        "summary": "【Mac苹果电脑科学上网】macOS系统下顶级加速客户端选购对比，解决Apple Silicon M系列芯片兼容与系统代理开启问题。"
    },
    "tut-8.md": {
        "title": "梯子节点超时、连接失败与无法打开网页故障排查九步法",
        "primary_kw": "节点超时排查",
        "summary": "【梯子故障排查指南】系统梳理节点超时、显示-1ms、系统时间不同步、DNS污染及订阅更新失败的九大常用修复秘籍。"
    },
    "tut-9.md": {
        "title": "如何正确测试梯子速度与节点延迟？真实丢包率与测速避坑",
        "primary_kw": "节点测速技巧",
        "summary": "【梯子测速避坑秘籍】教你认清虚标延迟与假带宽，学会使用 Speedtest、YouTube 统计信息及 ping 批处理测量真实网络品质。"
    },
    "tut-10.md": {
        "title": "梯子防失联指南：官网域名失效、订阅更新失败应对技巧",
        "primary_kw": "梯子防失联",
        "summary": "【梯子防失联全攻略】掌握TG防失联频道关注、备用镜像域名收藏、本地配置文件备份及多机场协同的高效防失联策略。"
    }
}

for filename, item in tutorial_content_map.items():
    filepath = os.path.join("content/categories/tutorial", filename)
    
    tut_md = f"""---
title: "{item['title']}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "小白教程"
tags: ["小白教程", "客户端配置", "梯子优选", "科学上网教程", "{item['primary_kw']}"]
summary: "{item['summary']}"
---

# {item['title']}

对于刚刚接触网络加速与翻墙客户端的小白新手而言，面对“订阅链接”、“Clash分流”、“TUN模式”、“节点超时”等专业术语时，往往会感到不知所措。本篇指南将以最直观、通俗易懂的文字，手把手带您完成“**{item['primary_kw']}**”的全部操作流程，助您轻松实现全平台快速科学上网。

## 一、开始前的准备工作

在配置客户端之前，您需要准备好以下两项基础条件：
1. **安装对应的软件客户端：** 根据您的操作系统（Windows, macOS, iOS 或 Android），提前下载好官方正版客户端软件（如 Clash Verge, Sing-box, v2rayN 或 Shadowrocket）。
2. **获取有效的梯子订阅链接（Subscription URL）：** 注册并登录高品质机场后台，在“订阅中心”复制专属于您账号的通用订阅 URL。

## 二、{item['title']} - 详细步骤分解

### 第一步：打开客户端并进入订阅管理
启动客户端软件后，在主界面侧边栏找到“Profiles（配置）”或“订阅”选项。

### 第二步：粘贴订阅 URL 并点击 Download（下载）
将您从服务商后台复制的订阅链接粘贴至 URL 输入框中，点击下载。客户端将自动拉取服务器节点列表并生成智能分流规则。

### 第三步：选择节点并开启系统代理（System Proxy）
在“Proxy（代理）”界面选择合适的节点（如香港或日本节点），将开关切换至“规则模式（Rule）”或“全局模式”，最后勾选“系统代理（System Proxy）”或“开启连接”。

## 三、配合高品质专线梯子提升配置体验

再好的客户端软件，也需要底层优质的节点线路支撑。如果在配置过程中遇到节点频繁超时，建议配合本站四大主推优质服务商使用：

- **👑 [灵动云 IPLC专线](/providers/lingdong-cloud/)**：全节点IPLC内网专线，延迟极低，零丢包，全节点解封ChatGPT/Claude及4K流媒体。（优惠码 `ld888` 享8折）
- **🥇 [暮光网络 BGP专线](/providers/twilight-net/)**：晚高峰大带宽影音首选，不限设备数。（优惠码 `mm88` 享8折）
- **🥈 [飞猫云 超值年付](/providers/flycat-cloud/)**：折合每月7元，内置自研极简客户端，小白一键连接。（优惠码 `flycat888` 享8折）
- **🥉 [微风网络 Breezenet](/providers/breezenet/)**：全平台全客户端完美兼容，长效运维抗封锁。

## 四、常见故障与快捷解决办法

- **问：节点列表导入成功，但无法打开外网网页？**
  答：请检查系统时间是否精准与北京时间一致；或者尝试勾选开启“TUN 模式（虚拟网卡）”。
- **问：如何防止订阅失效或官网被打不开？**
  答：建议立刻关注官方 Telegram 防失联订阅频道：[https://t.me/+XUkYwrYRQ_c0ODA1](https://t.me/+XUkYwrYRQ_c0ODA1) 以及本站首页 [tzyouxuan.xyz](https://tzyouxuan.xyz)。

关联阅读：
- [2026便宜好用的梯子优选推荐榜单](/categories/recommend/rec-1/)
- [查看常见问题 100 FAQ 全解答](/faq/)
- [查看全网28款机场测评列表](/services/)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tut_md)

print("Custom Tutorial articles generated successfully.")
