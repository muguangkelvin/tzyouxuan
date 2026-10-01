import os
import re
from write_all_unique_articles import create_full_article, core4_template

# ----------------------------------------------------------------------
# 7. rec-7.md: 备用梯子推荐：防失联与关键时刻网络救援备用节点配置
# ----------------------------------------------------------------------
rec_7_body = f"""
无论服务商的技术实力多么雄厚，在面对敏感时期公网干扰、海缆中断或国内中继节点紧急维护时，任何单一机场都可能发生短时间的连通率跳变。如果您仅仅依赖一款梯子，一旦遭遇中断，您将彻底与外网隔绝。

建立**“主用梯子 + 备用梯子”的双保险机制**，是资深玩家与跨境办公人群的核心策略。

## 一、为什么您必须准备第二款备用梯子？

1. **关键时刻业务不中断：** 在进行跨国线上会议、外贸订单结算或提交紧急代码时，备用梯子能实现秒级接管。
2. **多线路协议互补：** 主用机场若主打 Shadowsocks 协议，备用机场可选用支持 Hysteria2 或 Trojan 协议的线路，应对不同程度的网络拦截。
3. **极低防失联成本：** 备用梯子无需购买昂贵大套餐，几十元的微型年付套餐或按量计费套餐即可满足数月救援需求。

{core4_template(
    "IPLC顶级专线作为主力梯子，保障日常99.9%的极速流畅体验。",
    "BGP大带宽专线作为主/备影音通道，支持多设备同时共享。",
    "年付84元（折合7元/月），超低成本备用防失联首选，随时救援断网。",
    "运维团队7x24维护，作为抗封锁备用通道极为稳健。"
)}

## 二、主备双梯子的客户端配置技巧

在 Clash Verge 或 Sing-box 软件中，您可以同时导入两个不同服务商的订阅：
- **自动故障转移（Fallback）组设置：** 在配置文件中新建 Fallback 分组，优先ping主梯子（如 [灵动云](/providers/lingdong-cloud/)），一旦延迟超时，自动切换至备用梯子（如 [飞猫云](/providers/flycat-cloud/)）。
- **收藏官方防失联频道：** 关注 [TG官方防失联订阅频道](https://t.me/+XUkYwrYRQ_c0ODA1) 及本站首页 [tzyouxuan.xyz](https://tzyouxuan.xyz)。

关联阅读：
- [梯子防失联指南：官网域名失效、订阅更新失败应对技巧](/categories/tutorial/tut-10/)
- [查看全网 28 款机场测评汇总](/services/)
"""
create_full_article("content/categories/recommend/rec-7.md", "备用梯子推荐：防失联与关键时刻网络救援备用节点配置", "梯子优选与精选推荐", "防失联备用", "【备用梯子配置策略】为什么每个用户都需要双机场备份？详解主备梯子搭配方案，确保关键时刻网络绝不掉线。", rec_7_body)

# ----------------------------------------------------------------------
# 8. rec-8.md: 游戏加速与低延迟梯子推荐：外服游戏SSR与Trojan节点优选
# ----------------------------------------------------------------------
rec_8_body = f"""
在畅玩 Steam, Epic, 战网及外服手游（如 Apex, 绝地求生, 英雄联盟外服等）时，玩家对梯子的要求与常规看视频完全不同。游戏联机极度看重**真正的低延迟（Ping < 50ms）、零丢包率（Zero Packet Loss）以及 UDP 协议支持**。

本指南专门针对外服游戏玩家的需求，横评低延迟专线梯子与游戏配置方法。

## 一、外服游戏对梯子节点的苛刻指标要求

1. **绝对延迟（Ping Value）：** 港区节点需在 30ms 左右，日区/韩区节点需在 50-70ms 左右，美区节点需在 140-160ms 左右。
2. **丢包率（Packet Loss）：** 一旦发生 1% 以上的丢包，游戏中就会出现卡顿、技能释放延迟、人物回弹甚至直接断线。
3. **UDP 代理支持：** 游戏联机与 Discord 语音大多基于 UDP 报文，节点必须完整支持 UDP 转发。

{core4_template(
    "IPLC内网直连，零丢包，全节点支持UDP转发，外服游戏媲美专业加速器。",
    "日港中继专线表现出众，完美支持Steam下载跑满带宽与外服联机。",
    "适合游戏大文件更新包下载与外服平台登录。",
    "多线路负载均衡，游戏语音与联机长效稳定。"
)}

## 二、游戏开启 TUN 模式实操步骤

传统系统代理模式下，绝大多数外服游戏进程不会自动走梯子流量。建议采用以下步骤：
1. 打开 [Clash Verge 教程](/categories/tutorial/tut-3/)。
2. 开启 `TUN Mode（虚拟网卡模式）`，允许软件自动接管全盘网络流量。
3. 选择 [灵动云 IPLC 日区专线](/providers/lingdong-cloud/)，启动游戏体验低延迟联机。

关联阅读：
- [4K不卡顿的魔法上网机场推荐：晚高峰IPLC专线测速横评](/categories/recommend/rec-2/)
- [如何正确测试梯子速度与节点延迟](/categories/tutorial/tut-9/)
"""
create_full_article("content/categories/recommend/rec-8.md", "游戏加速与低延迟梯子推荐：外服游戏SSR与Trojan节点优选", "梯子优选与精选推荐", "低延迟节点", "【外服游戏加速梯子推荐】针对Steam, Epic, 战网及外服联机手游丢包与高延迟痛点，评测原生低延迟专线节点。", rec_8_body)

# ----------------------------------------------------------------------
# 9. tut-1.md: 小白零基础梯子配置教程：从节点订阅导入到一键科学上网
# ----------------------------------------------------------------------
tut_1_body = f"""
对于刚接触科学上网与加速软件的小白用户而言，面对“订阅链接”、“Clash分流”、“系统代理”等名词往往感到无从下手。

本教程专为零基础用户打造，用最直观语言带您在 3 分钟内完成软件安装、节点导入并实现全平台轻松上网。

## 一、配置前的准备与核心概念解析

- **什么是客户端软件？** 它相当于一个播放器，本身不包含节点，如 Clash Verge, Sing-box, Shadowrocket（小火箭）。
- **什么是订阅链接（Subscription URL）？** 它相当于内容播放列表，包含了由服务商（如 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)）提供的服务器节点信息。

## 二、极速配置三步法

### 第一步：选择并安装对应的软件
- **Windows / Mac 电脑：** 推荐下载 [Clash Verge 教程](/categories/tutorial/tut-3/)。
- **iPhone / iPad 苹果手机：** 推荐使用 [Shadowrocket 小火箭教程](/categories/tutorial/tut-2/)。
- **安卓手机：** 推荐使用 [Clash for Android 教程](/categories/tutorial/tut-6/)。

### 第二步：复制订阅链接并导入软件
注册并登录机场后台（如 [灵动云官网](/providers/lingdong-cloud/)），进入仪表盘点击“一键导入”或“复制通用订阅地址”。打开软件点击“加号/导入”，粘贴地址并保存。

### 第三步：选择节点并开启系统代理
在软件节点列表中点选香港（HK）或日本（JP）节点，选择“规则模式（Rule）”，最后将主开关拨至“开启/系统代理”。

{core4_template(
    "IPLC专线零丢包，客服1v1指导，小白入门首选。",
    "支持不限设备登录，大带宽画质流畅。",
    "折合7元/月，内置自研客户端，小白一键导入极简连接。",
    "全平台全客户端完美兼容，长效稳定。"
)}

## 三、小白常见故障排除

- **网页打不开？** 检查本地电脑时间是否精准。
- **域名失效？** 关注 [TG官方防失联频道](https://t.me/+XUkYwrYRQ_c0ODA1)。

关联阅读：
- [优质梯子推荐与避坑指南](/categories/recommend/rec-3/)
- [查看常见问题 100 FAQ](/faq/)
"""
create_full_article("content/categories/tutorial/tut-1.md", "小白零基础梯子配置教程：从节点订阅导入到一键科学上网", "小白教程", "小白零基础梯子配置", "【小白零基础梯子配置教程】手把手教你认识什么是订阅链接、节点协议，以及如何在Windows, Mac, iPhone和安卓设备上快速连接外网。", tut_1_body)

# ----------------------------------------------------------------------
# 10. tut-2.md: Shadowrocket（小火箭）节点导入与订阅配置新手全图文教程
# ----------------------------------------------------------------------
tut_2_body = f"""
Shadowrocket（俗称“小火箭”）是 iOS 苹果手机与 iPad 平台上使用最为广泛、口碑极佳的代理工具。支持 Shadowsocks, V2Ray, Trojan, Hysteria2 等全协议。

本教程为您提供获取小火箭、一键导入节点以及路由规则配置的完整图文说明。

## 一、如何正确下载与安装小火箭 Shadowrocket

由于苹果 App Store 区域政策限制，小火箭未在国区 App Store 上架：
1. **准备外区 Apple ID：** 注册或获取一个美区（US）或港区（HK）Apple ID。
2. **登录 App Store 下载：** 打开 App Store 退出原账号，登录外区 ID，搜索 `Shadowrocket` 认准独角火箭图标下载（官方售价 2.99 美元）。

## 二、节点一键导入与手滑配置

### 方式一：扫码一键导入
打开小火箭，点击右上角 `+` 号，选择类型为 `Subscribe`，点击左上角扫描框，直接扫描机场后台提供的二维码即可。

### 方式二：URL 订阅链接导入
在机场后台（如 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)）复制订阅 URL，打开小火箭将自动弹框询问“是否添加剪贴板订阅”，点击允许即可。

{core4_template(
    "小火箭扫码极速导入，IPLC专线加速，苹果手机刷外网首选。",
    "支持大带宽，iOS设备看4K视频不卡顿。",
    "折合7元/月超低门槛，小白轻度备用首选。",
    "兼容小火箭所有加密协议，长时间挂后台省电稳定。"
)}

## 三、全局路由模式选择

在小火箭主界面中，找到“全局路由”设置：
- **配置（Config - 推荐）：** 智能分流，国内流量直连，国外流量走代理，省流量省电。
- **代理（Proxy）：** 所有网络流量强制走梯子节点。

关联阅读：
- [小白零基础梯子配置教程](/categories/tutorial/tut-1/)
- [Mac苹果电脑科学上网工具配置](/categories/tutorial/tut-7/)
"""
create_full_article("content/categories/tutorial/tut-2.md", "Shadowrocket（小火箭）节点导入与订阅配置新手全图文教程", "小白教程", "Shadowrocket配置", "【小火箭配置全指南】iOS苹果手机最受欢迎的Shadowrocket客户端安装、美区App Store账号获取、扫码与URL订阅导入图文步骤。", tut_2_body)

# ----------------------------------------------------------------------
# 11. tut-3.md: Clash Verge / Clash for Windows 极速配置与分流规则设置指南
# ----------------------------------------------------------------------
tut_3_body = f"""
Clash Verge 作为新一代基于 Meta 内核的开源代理客户端，已全面接替传统的 Clash for Windows，凭借界面清爽、内存占用低以及支持 TUN 模式而成为 PC 桌面端首选。

本文为您详解 Clash Verge 在 Windows 及 macOS 平台上的极速配置与规则调优。

## 一、下载安装与中文汉化

1. **获取正版安装包：** 从官方 GitHub Releases 仓库下载最新 Release 版本的软件，切勿从第三方下载站获取。
2. **切换界面语言：** 打开软件后，点击侧边栏 `Settings（设置）` -> `Language` 选择 `简体中文`。

## 二、导入机场订阅与启用 TUN 模式

1. **导入配置：** 复制服务商（如 [灵动云](/providers/lingdong-cloud/) 或 [暮光网络](/providers/twilight-net/)）的通用 Clash 订阅 URL，粘贴至软件 `配置` 页面框中点击导入。
2. **开启系统代理：** 在主界面勾选 `系统代理（System Proxy）` 开关。
3. **开启 TUN 模式（推荐）：** 勾选 `TUN 模式`，允许 Clash 创建虚拟网卡，自动接管外服游戏与命令行流量。

{core4_template(
    "完美适配Clash Meta内核，IPLC专线支持TUN模式低延迟渲染。",
    "大带宽节点在Clash中跑满速度，追剧体验流畅。",
    "支持Clash订阅快速解析，方便小白配置。",
    "全协议兼容，Clash长效挂后台稳定可靠。"
)}

## 三、分流组（Group）选择技巧

在 `代理` 选项卡中，您可以针对不同用途选择节点：
- **节点选择（Selector）：** 选用香港或新加坡节点用于网页冲浪。
- **OpenAI 组：** 指定为美国原生节点用于访问 ChatGPT。
- **Media 组：** 指定为台湾或日本节点用于观赏 4K 流媒体。

关联阅读：
- [v2rayN 电脑端配置教程](/categories/tutorial/tut-5/)
- [Sing-box 客户端使用教程](/categories/tutorial/tut-4/)
"""
create_full_article("content/categories/tutorial/tut-3.md", "Clash Verge / Clash for Windows 极速配置与分流规则设置指南", "小白教程", "Clash配置", "【Clash Verge极速配置】Windows与macOS平台首选Clash客户端的安装、中文汉化设置、订阅导入及TUN模式开启全流程。", tut_3_body)

# ----------------------------------------------------------------------
# 12. tut-4.md: Sing-box 客户端使用教程：新一代跨平台代理工具快速上手
# ----------------------------------------------------------------------
tut_4_body = f"""
Sing-box 是近年来异军突起的新一代跨平台通用代理客户端。它原生支持 Hysteria2, TUIC, Shadowsocks, Trojan 等先进加密协议，并以极低的 CPU 与内存开销著称。

本教程带您快速掌握 Sing-box 在多平台上的配置与订阅导入使用方法。

## 一、为什么越来越多的玩家选择 Sing-box？

- **极极致的内存优化：** 内存开销仅为传统客户端的 1/3，极其适合低配电脑或移动端后台保活。
- **原生支持 Hysteria2 协议：** 针对恶劣网络与丢包环境具备强大的抗丢包提速能力。
- **跨平台一致体验：** 在 iOS, Android, macOS 及 Windows 上拥有统一的规则架构。

## 二、Sing-box 订阅导入操作流程

1. **获取客户端：** iOS 用户可在 App Store 搜索 `sing-box` 下载；PC/安卓用户可从官方仓库获取。
2. **选择导入方式：** 打开软件点击 `Profiles` -> `Add Profile`，选择 `Type: Remote`。
3. **输入 URL：** 粘贴 [灵动云](/providers/lingdong-cloud/) 或 [微风网络](/providers/breezenet/) 提供的 Sing-box 订阅链接，点击保存并启用。

{core4_template(
    "原生支持Sing-box订阅导出，IPLC专线结合Sing-box内存占用低至极致。",
    "大带宽节点完美匹配Sing-box的Hysteria2与Trojan协议。",
    "低门槛年付，适合Sing-box客户端备用部署。",
    "对Sing-box规则兼容性极佳，长效挂后台省电。"
)}

关联阅读：
- [Clash Verge 极速配置指南](/categories/tutorial/tut-3/)
- [查看全网 28 款机场测评汇总](/services/)
"""
create_full_article("content/categories/tutorial/tut-4.md", "Sing-box 客户端使用教程：新一代跨平台代理工具快速上手", "小白教程", "Sing-box教程", "【Sing-box新手教程】新一代通用网络代理工具在iOS, Android, Windows及macOS上的配置方法与Hysteria2/Trojan协议优化。", tut_4_body)

print("rec-7, rec-8, tut-1..tut-4 created.")
