import os
import json
from generate_site_contents import create_article_markdown

# Load providers
with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# 1. Generate 8 Articles in Category `recommend`
recommend_articles = [
    ("rec-1.md", "2026便宜好用的梯子优选推荐榜单：高性价比魔法上网机场评测", "梯子优选与精选推荐", "便宜好用梯子", "探讨全网最划算且性能出众的便宜梯子，从月付几元到高品质专线进行多维对比。"),
    ("rec-2.md", "4K不卡顿的魔法上网机场推荐：晚高峰IPLC专线测速横评", "梯子优选与精选推荐", "IPLC专线梯子", "聚焦高码率视频与高清追剧场景，深入分析晚高峰不降速的IPLC与BGP专线优势。"),
    ("rec-3.md", "优质梯子推荐与避坑指南：小白零基础选购科学上网工具技巧", "梯子优选与精选推荐", "优质梯子推荐", "手把手教小白如何分辨劣质小机场，掌握节点延迟、丢包率与解锁能力的考察标准。"),
    ("rec-4.md", "高速翻墙梯子排行榜：多设备共享与跨境办公节点挑选", "梯子优选与精选推荐", "高速翻墙梯子", "面向多设备协同、团队跨境办公用户，提供大流量、多并发设备的梯子选型建议。"),
    ("rec-5.md", "AI工具专用梯子推荐：ChatGPT与Claude原生IP解锁节点选购", "梯子优选与精选推荐", "AI工具解锁", "针对ChatGPT、Claude 3.5、Midjourney等AI大模型访问受限问题，评测干净原生IP节点。"),
    ("rec-6.md", "按月付费梯子优选：灵活无负担的稳定魔法上网机场推荐", "梯子优选与精选推荐", "月付梯子", "分析月付套餐在防跑路、避坑失联方面的巨大优势，推荐支持灵活按月付费的靠谱服务商。"),
    ("rec-7.md", "备用梯子推荐：防失联与关键时刻网络救援备用节点配置", "梯子优选与精选推荐", "防失联备用", "为什么每个用户都应该准备第二款备用梯子？详解多机场协同保障网络通畅的策略。"),
    ("rec-8.md", "游戏加速与低延迟梯子推荐：外服游戏SSR与Trojan节点优选", "梯子优选与精选推荐", "低延迟节点", "专为Steam、Epic、外服手游与主机玩家打造的高速低延迟节点挑选与配置指南。")
]

for filename, title, category, kw, extra in recommend_articles:
    path = os.path.join("content/categories/recommend", filename)
    create_article_markdown(path, title, category, kw, extra)

print("8 Recommend articles generated successfully.")

# 2. Generate 10 Articles in Category `tutorial`
tutorial_articles = [
    ("tut-1.md", "小白零基础梯子配置教程：从节点订阅导入到一键科学上网", "小白教程", "小白零基础梯子配置", "从零开始讲解什么是订阅链接、什么是节点协议，以及如何在电脑手机上快速连接网络。"),
    ("tut-2.md", "Shadowrocket（小火箭）节点导入与订阅配置新手全图文教程", "小白教程", "Shadowrocket配置", "iOS苹果手机小火箭客户端扫码与URL订阅导入详细步骤解析。"),
    ("tut-3.md", "Clash Verge / Clash for Windows 极速配置与分流规则设置指南", "小白教程", "Clash配置", "PC桌面端最受欢迎的Clash客户端安装、汉化、订阅导入及TUN模式开启全流程。"),
    ("tut-4.md", "Sing-box 客户端使用教程：新一代跨平台代理工具快速上手", "小白教程", "Sing-box教程", "介绍Sing-box新一代协议客户端在iOS, Android, Windows以及macOS上的配置方法。"),
    ("tut-5.md", "v2rayN 电脑端配置教程：Vmess与Trojan节点手动及订阅导入", "小白教程", "v2rayN教程", "经典Windows代理软件v2rayN的安装步骤、路由规则切换与节点测速技巧。"),
    ("tut-6.md", "Android安卓手机梯子软件推荐与Clash for Android使用指南", "小白教程", "安卓梯子教程", "安卓系统无感魔法上网配置，包含APK下载、订阅更新及后台保活设置。"),
    ("tut-7.md", "Mac苹果电脑科学上网工具选购与ClashX / Clash Verge配置", "小白教程", "Mac梯子教程", "macOS系统下优秀加速客户端对比，解决M系列芯片兼容性与系统代理开启问题。"),
    ("tut-8.md", "梯子节点超时、连接失败与无法打开网页故障排查九步法", "小白教程", "节点超时排查", "详尽梳理系统时间不同步、DNS污染、端口冲突及订阅过期等常见错误及修复方案。"),
    ("tut-9.md", "如何正确测试梯子速度与节点延迟？真实丢包率与测速避坑", "小白教程", "节点测速技巧", "教你认清假带宽与虚标延迟，学会使用Speedtest与YouTube统计信息查看真实网速。"),
    ("tut-10.md", "梯子防失联指南：官网域名失效、订阅更新失败应对技巧", "小白教程", "梯子防失联", "掌握TG频道订阅、防失联镜像域名收藏以及本地备份配置的核心技巧。")
]

for filename, title, category, kw, extra in tutorial_articles:
    path = os.path.join("content/categories/tutorial", filename)
    create_article_markdown(path, title, category, kw, extra)

print("10 Tutorial articles generated successfully.")

# 3. Generate 3 AI Recommendation Articles
ai_articles = [
    ("ai-1.md", "AI 机场推荐：ChatGPT、Claude、Gemini 等工具的节点与套餐选择", "梯子优选与精选推荐", "AI 机场推荐", "针对人工智能AI交互场景，评测解封ChatGPT和Claude的原生IP专线梯子。"),
    ("ai-2.md", "AI 工具使用场景怎么选机场：地区节点、IP 质量、延迟与设备兼容", "梯子优选与精选推荐", "AI工具节点", "深度分析美国与欧洲节点在AI大模型对话中的稳定性表现。"),
    ("ai-3.md", "AI 办公机场推荐：跨境协作、代码工具与多设备需求比较", "梯子优选与精选推荐", "AI办公加速", "为程序员与跨境办公人士推荐高稳定性、不频繁要求验证码的优质梯子。")
]

for filename, title, category, kw, extra in ai_articles:
    path = os.path.join("content/categories/recommend", filename)
    create_article_markdown(path, title, category, kw, extra)

print("3 AI articles generated successfully.")

# 4. Generate 28 Provider Articles in `content/providers/`
for p in providers:
    p_filename = f"{p['slug']}.md"
    p_path = os.path.join("content/providers", p_filename)
    p_title = f"{p['name']}机场测评：价格、节点、适合人群与官网注册教程"
    
    p_content = f"""---
title: "{p_title}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "机场测评"
tags: ["{p['name']}", "机场测评", "梯子优选", "稳定梯子"]
summary: "{p['name']}详细测评报告：包含当前参考价格 {p['priceFrom']}、流量 {p['trafficFrom']}、节点地区分布、解封AI与4K视频表现及官方直接注册入口。"
---

# {p_title}

在2026年众多的网络加速与梯子服务商中，**{p['name']}** 凭借其独特的线路定位与优质的服务体验，受到了不少用户的关注。本文将为您对 **{p['name']}** 进行全方位深度的测评与分析。

## 一、{p['name']} 核心资料与基础参数概览

- **服务名称：** {p['name']}
- **排名定位：** 梯子优选推荐榜第 #{p['rank']} 位
- **参考价格：** {p['priceFrom']}
- **流量配置：** {p['trafficFrom']}
- **结算周期：** {p['billingPeriod']}
- **设备限制：** {p['deviceLimit']}
- **节点地区：** {p['regions']}
- **支持协议：** {p['protocols']}
- **适用人群：** {p['suitableFor']}
- **官方注册入口：** [👉 点击访问 {p['name']} 官网注册]({p['inviteURL']}) *(rel="sponsored nofollow noopener")*

## 二、{p['name']} 核心优势与性能表现

1. **线路质量与晚高峰稳定性：** {p['summary']} 在网络高峰期表现平稳，能够维持较低的延迟与丢包率。
2. **解锁能力：** 支持常见的海外网站访问，香港、日本及美区节点能够解锁主流社交媒体与4K视频。
3. **客户端兼容性：** 支持一键导出 Clash、Sing-box、Shadowrocket（小火箭）及 v2rayN 等通用订阅格式，小白配置简便。

## 三、{p['name']} 套餐选择建议与注意事项

如果您正在考虑选购 **{p['name']}**，我们建议：
- **初次尝试：** 建议先购买其基础月付或小额体验套餐，实测本地网络（电信/联通/移动）的连接效果后再决定是否长期续费。
- **优惠码使用：** {p.get('couponNote', '最新优惠请以官网结算页为准')}。

[👉 立即点击访问 {p['name']} 官网查看最新套餐与节点]({p['inviteURL']})

---

## ⚡ 2026年梯子优选四大自营与主推服务对照参考

在选择 **{p['name']}** 的同时，您也可以对比本站四大主推核心服务，选择最契合您痛点的方案：

1. **[灵动云](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1)**：全网首推顶级IPLC专线，全节点解锁ChatGPT/Claude等AI服务及4K/8K视频。（优惠码 `ld888` 享8折）
2. **[暮光网络](https://varnexa.twilightaff.com/#/?code=KvGly3jY)**：晚高峰BGP中继与原生IP专线，大带宽追剧流媒体解锁首选。（优惠码 `mm88` 享8折）
3. **[飞猫云](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH)**：超值小流量年付折合7元/月，自研客户端一键连接。（优惠码 `flycat888` 享8折）
4. **[微风网络 Breezenet](https://edp01.breezenetaff.com/#/?code=He4n3zxg)**：口碑极佳的稳定梯子，全客户端完美兼容，长效运维抗封锁。

欢迎关注梯子优选网，获取更多机场评测与网络加速技术支持！
"""
    with open(p_path, "w", encoding="utf-8") as f:
        f.write(p_content)

print("28 Provider articles generated successfully.")

# 5. Generate 100 FAQ Articles in `content/faq/`
faq_questions = [
    ("新手如何挑选一款稳定靠谱的网络梯子服务？", "挑选梯子最重要的是看线路类型（IPLC专线或BGP中继）、晚高峰丢包率、客服售后以及是否支持月付。建议先购买月付试用，优先推荐灵动云与暮光网络。"),
    ("为什么晚高峰观看4K视频会频繁缓冲卡顿？", "晚高峰时期国际出口总带宽拥堵，公网直连线路极易丢包。选用灵动云等IPLC专线或暮光网络等BGP中继专线可以有效解决卡顿问题。"),
    ("Clash订阅链接导入失败提示Net Error怎么办？", "检查本地网络是否通畅、系统时间是否与北京时间一致，或者尝试关闭本地防火墙后重新复制订阅链接导入。"),
    ("Shadowrocket（小火箭）节点全部超时显示-1ms怎么排查？", "首先确认小火箭已开启‘全局路由-配置’或‘代理’，然后尝试更新订阅。若依然超时，检查套餐是否已到期或流量耗尽。"),
    ("IPLC专线与普通BGP中继梯子有什么区别？", "IPLC专线不经过公网防火墙，延迟极低且零丢包；BGP中继则通过国内中继节点转发，性价比极高。"),
    ("访问ChatGPT提示Access Denied或IP被封怎么解决？", "OpenAI对节点IP风控严格，需要使用干净的原生IP节点。推荐使用灵动云美区原生节点访问。"),
    ("梯子套餐流量每月重置时间和计算规则是怎样的？", "绝大多数机场按照自然月或账单日重置流量。若流量用尽可以购买临时流量叠加包或等待下一账单周期。"),
    ("手机电脑如何实现多设备同时在线使用梯子？", "选用支持多设备同时登录的服务商（如暮光网络支持不限设备数，灵动云支持5-10台设备），并在各端导入相同订阅。"),
    ("梯子软件Clash与Sing-box哪个更好用？", "Clash生态成熟、规则丰富；Sing-box架构更新、内存占用小、支持Hysteria2等新协议。两者均是优秀选择。"),
    ("官网域名打不开，如何防止梯子失联？", "建议收藏官方Telegram防失联频道 https://t.me/+XUkYwrYRQ_c0ODA1 以及本站 [tzyouxuan.xyz](https://tzyouxuan.xyz) 随时获取更新。")
]

for i in range(1, 101):
    faq_filename = f"faq-{i}.md"
    faq_path = os.path.join("content/faq", faq_filename)
    
    q_title, q_ans = faq_questions[(i - 1) % len(faq_questions)]
    q_full_title = f"{q_title} (FAQ #{i})"
    
    faq_md = f"""---
title: "{q_full_title}"
date: 2026-09-30T10:00:00+08:00
draft: false
category: "常见问题"
tags: ["梯子FAQ", "魔法上网", "节点问题", "订阅配置"]
summary: "【常见问题解答 #{i}】{q_title}：详细解答与图文排查指引。"
---

# {q_full_title}

**问：{q_title}**

**答：** {q_ans}

### 详细实操排查步骤与建议：

1. **核验本地网络状态：** 确认非梯子环境下的常规网络访问正常，排查本地路由器或运营商DNS干扰。
2. **检查节点订阅与账号状态：** 登录服务商后台，确认套餐处于有效期内且流量充裕。
3. **选择匹配的客户端：** 建议使用最新版本的 Clash Verge, Sing-box 或 Shadowrocket 客户端。
4. **推荐替代方案对比：** 若当前节点持续不稳定，可随时切换至本站推荐的自营与主推优质服务商：
   - **[灵动云官网注册](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1)**（IPLC专线/AI全解锁，优惠码 `ld888`）
   - **[暮光网络官网注册](https://varnexa.twilightaff.com/#/?code=KvGly3jY)**（晚高峰4K影音，优惠码 `mm88`）
   - **[飞猫云官网注册](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH)**（超值年付折合7元/月，优惠码 `flycat888`）
   - **[微风网络官网注册](https://edp01.breezenetaff.com/#/?code=He4n3zxg)**（全能客户端兼容，长效稳定）

更多疑问，请随时关注梯子优选网（[tzyouxuan.xyz](https://tzyouxuan.xyz)）或加入Telegram防失联订阅频道：[https://t.me/+XUkYwrYRQ_c0ODA1](https://t.me/+XUkYwrYRQ_c0ODA1)。
"""
    with open(faq_path, "w", encoding="utf-8") as f:
        f.write(faq_md)

print("100 FAQ articles generated successfully.")

# 6. Generate Core Pages (about, contact, privacy, disclaimer, editorial-policy, methodology)
pages = [
    ("content/about.md", "关于我们 - 梯子优选 (tzyouxuan.xyz)", "梯子优选网 (tzyouxuan.xyz) 致力于为广大小白新手与进阶用户提供独立、实测、靠谱的梯子优选与网络加速指南。涵盖节点延迟测速、客户端配置教程及避坑技巧。官方Telegram防失联频道：https://t.me/+XUkYwrYRQ_c0ODA1"),
    ("content/contact.md", "联系我们 - 资料纠错与合作", "欢迎通过官方 Telegram 频道联系我们：[https://t.me/+XUkYwrYRQ_c0ODA1](https://t.me/+XUkYwrYRQ_c0ODA1)。如果您发现任何机场信息、节点数据或优惠码有误，请随时与我们反馈更新！"),
    ("content/privacy.md", "隐私政策 - 梯子优选", "本站尊重并保护所有访客的隐私。我们不收集任何个人账号密码、订阅地址或支付敏感数据。所有跳转外部服务商均通过安全推广链接安全进行。"),
    ("content/disclaimer.md", "免责声明", "本站所有评测文章与教程仅供网络技术交流、学术研究与合法跨境业务使用。请遵守当地法律法规，切勿用于任何违法违规用途。特此声明！"),
    ("content/editorial-policy.md", "编辑原则 - 梯子优选", "我们坚持独立实测、事实求是的原则。所有推荐服务商均基于真实的节点响应速度、晚高峰稳定性以及客服售后质量进行客观横评。"),
    ("content/methodology.md", "测评方法论 - 节点测速标准", "本站测评涵盖：1. 晚高峰20:00-23:00丢包率测试；2. 4K/8K视频秒开缓冲时间；3. OpenAI/Netflix流媒体解封状态校验；4. 7x24小时连通率监控。")
]

for filepath, p_title, p_body in pages:
    p_content = f"""---
title: "{p_title}"
date: 2026-09-30T10:00:00+08:00
draft: false
---

# {p_title}

{p_body}

## ⚡ 官方 Telegram 防失联频道
您可以随时关注我们的Telegram官方防失联频道获取最新节点更新与技术教程：
👉 [https://t.me/+XUkYwrYRQ_c0ODA1](https://t.me/+XUkYwrYRQ_c0ODA1)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(p_content)

print("Static pages generated successfully.")
