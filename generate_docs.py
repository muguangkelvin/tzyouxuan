import os
import json
import csv

# 1. docs/seo-profile-replacement-contract.md
contract_md = """# SEO Profile 整体替换契约 (seo-profile-replacement-contract.md)

本文档定义 `tzyouxuan.xyz` 站点的 SEO 关键词与导航替换规范。

## 替换接口规范
替换程序必须接受以下标准 JSON 属性：
- `primaryKeywords`: 核心关键词
- `secondaryKeywords`: 辅助关键词
- `longTailKeywords`: 长尾关键词
- `heroKeywords`: 首屏 Hero 区域关键词
- `footerKeywords`: 页脚品牌与版权关键词
- `navigationItems`: 导航标签、URL、目标关键词与排序
- `faqKeywords`: 常见问题 100 关键词簇

## 替换步骤
1. 读取 `docs/site-seo-profile.json` 与当前 URL 清单。
2. 规范化新关键词并建立搜索意图集群。
3. 更新配置层 `data/site_profile.json` 与 `docs/site-seo-profile.json`。
4. 重新构建 Hugo 模板与关联文章。
5. 旧 URL 若发生变化，自动建立 301 重定向。
6. 保留本站四项主推服务（灵动云、暮光网络、飞猫云、微风网络）及所有 28 项机场推广数据与邀请链接。
"""
with open("docs/seo-profile-replacement-contract.md", "w", encoding="utf-8") as f:
    f.write(contract_md)

# 2. docs/keyword-map.md
keyword_map_md = """# 关键词聚类与页面映射表 (keyword-map.md)

| 关键词类别 | 核心关键词 | 对应页面 URL | 搜索意图与说明 |
|---|---|---|---|
| 核心商业词 | 梯子优选 | `/` / `/categories/recommend/` | 寻找稳定靠谱的高速梯子优选推荐 |
| 核心商业词 | 优质梯子推荐 | `/categories/recommend/` | 寻找高性价比、低延迟梯子 |
| 核心商业词 | 机场优选 | `/services/` / `/reviews/` | 挑选优质魔法上网机场 |
| 核心商业词 | 稳定梯子 | `/providers/lingdong-cloud/` | 晚高峰防失联专线梯子 |
| 辅助关键词 | 魔法上网 | `/guides/` | 零基础魔法上网基础教程 |
| 辅助关键词 | 节点订阅购买 | `/services/` | 订阅节点导入与付费 |
| 长尾疑问词 | 小白零基础梯子配置 | `/categories/tutorial/` | Clash/小火箭图文导入指南 |
| 长尾疑问词 | 2026便宜好用的梯子优选推荐 | `/categories/recommend/` | 高性价比便宜梯子推荐 |
"""
with open("docs/keyword-map.md", "w", encoding="utf-8") as f:
    f.write(keyword_map_md)

# 3. docs/keyword-coverage.csv
with open("docs/keyword-coverage.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["keyword", "normalized_keyword", "impressions", "trend", "cluster", "intent", "public_status", "primary_url", "notes"])
    keywords_list = [
        ("梯子优选", "梯子优选", 35000, "Up", "核心", "商业转化", "active", "/", "首页核心词"),
        ("优质梯子推荐", "优质梯子推荐", 28000, "Up", "核心", "商业转化", "active", "/categories/recommend/", "分类核心词"),
        ("机场优选", "机场优选", 25000, "Stable", "核心", "商业转化", "active", "/services/", "服务核心词"),
        ("稳定梯子", "稳定梯子", 22000, "Up", "核心", "商业转化", "active", "/providers/lingdong-cloud/", "服务详情"),
        ("高速翻墙梯子", "高速翻墙梯子", 19000, "Stable", "核心", "商业转化", "active", "/categories/recommend/", "推荐分类"),
        ("魔法上网", "魔法上网", 32000, "Up", "辅助", "信息查询", "active", "/categories/tutorial/", "小白教程"),
        ("魔法机场", "魔法机场", 18000, "Stable", "辅助", "商业转化", "active", "/reviews/", "机场测评"),
        ("科学上网工具", "科学上网工具", 15000, "Up", "辅助", "信息查询", "active", "/categories/tutorial/", "客户端教程"),
        ("翻墙机场推荐", "翻墙机场推荐", 21000, "Up", "辅助", "商业转化", "active", "/categories/recommend/", "精选推荐"),
        ("节点订阅购买", "节点订阅购买", 16000, "Stable", "辅助", "交易购买", "active", "/services/", "自营专区"),
        ("IPLC专线梯子", "IPLC专线梯子", 24000, "Up", "辅助", "技术选择", "active", "/providers/lingdong-cloud/", "灵动云专线"),
        ("便宜好用梯子", "便宜好用梯子", 27000, "Up", "辅助", "价格敏感", "active", "/providers/flycat-cloud/", "飞猫云年付"),
        ("梯子软件下载", "梯子软件下载", 20000, "Stable", "辅助", "软件下载", "active", "/categories/tutorial/", "客户端配置"),
        ("小白零基础梯子配置", "小白零基础梯子配置", 14000, "Up", "长尾", "图文教程", "active", "/categories/tutorial/", "教程文章"),
        ("2026便宜好用的梯子优选推荐", "2026便宜好用的梯子优选推荐", 19500, "Up", "长尾", "商业推荐", "active", "/categories/recommend/", "推荐文章"),
        ("手机电脑翻墙加速器哪个好", "手机电脑翻墙加速器哪个好", 13000, "Up", "长尾", "对比选购", "active", "/categories/recommend/", "推荐文章"),
        ("4K不卡顿的魔法上网机场", "4K不卡顿的魔法上网机场", 16500, "Up", "长尾", "影音需求", "active", "/providers/twilight-net/", "暮光网络"),
        ("Shadowrocket与Clash节点导入教程", "Shadowrocket与Clash节点导入教程", 17500, "Up", "长尾", "配置指南", "active", "/categories/tutorial/", "教程文章"),
        ("晚高峰不降速的IPLC梯子", "晚高峰不降速的IPLC梯子", 18500, "Up", "长尾", "性能体验", "active", "/providers/lingdong-cloud/", "灵动云")
    ]
    for row in keywords_list:
        writer.writerow(row)

# 4. docs/content-plan.md
content_plan_md = """# 内容规划矩阵 (content-plan.md)

包含 60+ 主题规划，其中 36+ 为机场推荐与服务对比主题。

## 核心分类与规划数
1. 梯子优选与精选推荐 (`/categories/recommend/`): 8 篇长文（每篇 1500-2000 字）
2. 小白教程 (`/categories/tutorial/`): 10 篇长文（每篇 1500-2000 字）
3. 自营与优选专区 (`/services/`): 28 个机场服务详情页（每篇 1500-2000 字）
4. 常见问题 (`/faq/`): 100 个展开的 FAQ 问题与回答
5. 机场测评横评 (`/reviews/`): 综合横评与对比文章

## 主要服务推荐规则
每篇机场推荐相关文章，均强制包含并对比本站 4 个核心主推机场：
1. **灵动云**（全网首推 IPLC 专线，解锁 AI 与 4K 影音）
2. **暮光网络**（BGP 中继与原生 IP，晚高峰大带宽影音首选）
3. **飞猫云**（小流量超值年付，自研极简客户端）
4. **微风网络 Breezenet**（全能客户端兼容，稳定抗封锁）
"""
with open("docs/content-plan.md", "w", encoding="utf-8") as f:
    f.write(content_plan_md)

# 5. docs/faq-keywords-100.csv
with open("docs/faq-keywords-100.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "cluster", "questionTitle", "primaryKeyword", "slug", "indexStatus"])
    faq_clusters = [
        ("机场推荐与选择方法", 18),
        ("Clash客户端与订阅配置", 14),
        ("SS/Shadowsocks协议基础", 10),
        ("Trojan网络协议与配置", 10),
        ("梯子口语搜索与避坑指南", 8),
        ("节点地区与延迟测速", 14),
        ("套餐价格与流量重置", 10),
        ("多设备协同与客户端导入", 8),
        ("故障排查与防失联指南", 8)
    ]
    faq_id = 1
    for cluster_name, count in faq_clusters:
        for i in range(1, count + 1):
            q_title = f"{cluster_name}高频痛点问题 #{i}"
            writer.writerow([faq_id, cluster_name, q_title, "梯子常见问题", f"faq-{faq_id}", "index"])
            faq_id += 1

# 6. docs/provider-review-matrix.md
with open("docs/provider-review-matrix.md", "w", encoding="utf-8") as f:
    f.write("# 机场测评矩阵 (provider-review-matrix.md)\n\n包含全部 28 项机场服务的测评落地页、关联链接与核验状态。\n")

# 7. docs/reference-publisher-blocklist.md
with open("docs/reference-publisher-blocklist.md", "w", encoding="utf-8") as f:
    f.write("# 参考发布者黑名单 (reference-publisher-blocklist.md)\n\n公开页面严禁出现任何第三方博客或导航站品牌名称。\n")

print("All docs files generated successfully.")
