---
title: "全平台代理客户端零基础配置教程：Windows / Mac / iOS / Android"
description: "本文是一篇面向新手的全平台配置指南，带你从零开始在 Windows、macOS、iOS 和 Android 设备上安装并配置主流网络工具（Clash Verge Rev、Sing-box、Shadowrocket 等），实现快速稳定的网络分流。"
date: 2026-09-30T10:00:00+08:00
draft: false
---

<div class="guide-intro-card">
  <div class="intro-badge">🚀 教程导读 / 摘要</div>
  <p class="intro-text">
    本文是一篇面向新手的全平台配置指南，带你从零开始在 <strong>Windows、macOS、iOS 和 Android</strong> 设备上安装并配置主流网络工具（Clash Verge Rev、Sing-box、Shadowrocket 等），实现快速稳定的网络分流与高品质极速上网体验。
  </p>
</div>

<div class="guide-principles-card" style="margin-top: 25px;">
  <h2 class="section-heading">🔑 前置准备与核心概念</h2>
  <p class="section-desc">在开始配置前，请先准备好以下两样基础要素并了解核心机制：</p>
  <ul class="principles-list">
    <li><strong>订阅链接（URL）：</strong> 服务提供商后台提供的配置链接（通常支持 Clash 订阅、Sing-box 订阅或通用 V2Ray / Shadowsocks 订阅）。</li>
    <li><strong>路由分流模式认知：</strong>
      <ul style="margin-top: 8px; margin-left: 20px; list-style-type: disc;">
        <li><strong style="color: #2563eb;">规则模式（Rule）：</strong> <strong>推荐默认使用。</strong> 国内网站直连不消耗代理流量，海外受限网站自动走代理，兼顾访问速度与隐私安全。</li>
        <li><strong style="color: #ea580c;">全局模式（Global）：</strong> 所有网络流量强制通过代理节点转发，常用于排查特殊规则或网站无法打开等问题。</li>
        <li><strong style="color: #64748b;">直连模式（Direct）：</strong> 所有网络流量均不经过代理节点，直接与目标服务器通信。</li>
      </ul>
    </li>
  </ul>
</div>

<div class="platform-section-header">
  <h2>💻 1. 桌面端：Windows & macOS（推荐 Clash Verge Rev）</h2>
  <div class="platform-section-desc">Clash Verge Rev 是目前桌面端功能最完善、界面现代化且支持 Clash Meta（Mihomo）内核的主流代理客户端。</div>
</div>

<div class="tutorial-steps-grid">
  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge">STEP 01</span>
        <div class="step-card-title">下载与安装</div>
      </div>
      <div class="step-card-body">
        <ul>
          <li><strong>Windows：</strong>前往 GitHub Releases 下载 <code>.msi</code> 或 <code>_x64-setup.exe</code> 安装包（如提示缺少环境需配合安装微软 WebView2）。</li>
          <li><strong>macOS：</strong>Apple Silicon（M1/M2/M3/M4 系列）选 <code>aarch64.dmg</code>；Intel 芯片老款选 <code>x64.dmg</code>。若提示未验证开发者，在<em>系统设置 → 隐私与安全性</em>中点击“仍要打开”。</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge">STEP 02</span>
        <div class="step-card-title">导入订阅配置</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>打开 Clash Verge Rev，在左侧导航栏点击 <strong>订阅 (Subscription)</strong>。</li>
          <li>将复制好的机场订阅链接粘贴到顶部 URL 输入框，点击 <strong>导入 (Import)</strong>。</li>
          <li>导入成功后，列表显示该配置卡片，单击选中高亮生效。</li>
        </ol>
      </div>
      <div class="step-verify-tip">
        <strong>✅ 验证方法：</strong> 卡片上显示更新时间与节点数量即代表导入成功。
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge">STEP 03</span>
        <div class="step-card-title">选节点与开启代理</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>点击左侧 <strong>代理 (Proxy)</strong> 菜单，顶部模式保持为 <strong>Rule (规则)</strong>。</li>
          <li>点击右上角 Wi-Fi 测速图标，点选低延迟节点。</li>
          <li>在设置中将 <strong>系统代理 (System Proxy)</strong> 开关切换为开启。</li>
        </ol>
      </div>
      <div class="step-verify-tip">
        <strong>🚀 验证方法：</strong> 访问 Google/YouTube，页面顺畅秒开即配置成功。
      </div>
    </div>
  </div>
</div>

<div class="tutorial-image-container" style="margin-bottom: 35px; text-align: center;">
  <img src="/images/tutorials/clash-verge-guide.svg" alt="Clash Verge Rev Windows & Mac 配置教程示意图" style="width: 100%; max-width: 850px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 1-1：Clash Verge Rev (Windows / macOS) 订阅导入与代理切换示意图</p>
</div>

<div class="platform-section-header" style="border-left-color: #d97706;">
  <h2>📱 2. 苹果移动端：iOS / iPadOS（推荐 Shadowrocket 小火箭）</h2>
  <div class="platform-section-desc">Shadowrocket（俗称“小火箭”）是 iOS 端功能强大、连接极其稳定的经典规则分流工具。</div>
</div>

<div class="tutorial-steps-grid">
  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 01</span>
        <div class="step-card-title">获取与下载</div>
      </div>
      <div class="step-card-body">
        <ul>
          <li>因区域限制，Shadowrocket 未在国区 App Store 上架。</li>
          <li>需使用美区或港区等非国区 Apple ID 登录 App Store 后搜索并购买下载。</li>
          <li><strong>认准开发者：</strong> <em>Shadow Launch Technology Limited</em>。</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 02</span>
        <div class="step-card-title">添加订阅</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>打开 Shadowrocket，点击右上角 <strong>「+」</strong> 号。</li>
          <li>点击第一行 <strong>类型 (Type)</strong>，修改为 <strong>Subscribe</strong>。</li>
          <li>在 <strong>URL</strong> 栏粘贴订阅地址，备注可自定义（如“我的节点”）。</li>
          <li>点击右上角 <strong>完成 (Done/Save)</strong> 保存。</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 03</span>
        <div class="step-card-title">连接与权限配置</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>首页 <strong>全局路由</strong> 确保勾选为 <strong>配置 (Config)</strong>（规则分流）。</li>
          <li>勾选点选任意低延迟节点。</li>
          <li>开启顶部 <strong>连接</strong> 开关，首次使用系统弹出 VPN 权限，点击 <strong>允许</strong> 并验证密码。</li>
        </ol>
      </div>
      <div class="step-verify-tip">
        <strong>🚀 验证方法：</strong> 连接显示已连接，状态栏出现 VPN 图标，网络顺畅访问。
      </div>
    </div>
  </div>
</div>

<div class="tutorial-image-container" style="margin-bottom: 35px; text-align: center;">
  <img src="/images/tutorials/shadowrocket-guide.svg" alt="Shadowrocket iOS 配置教程示意图" style="width: 100%; max-width: 850px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 2-1：Shadowrocket (iOS / iPadOS) 小火箭订阅添加与 VPN 权限设置示意图</p>
</div>

<div class="platform-section-header" style="border-left-color: #10b981;">
  <h2>🤖 3. 安卓端：Android（推荐 Sing-box / CMFA）</h2>
  <div class="platform-section-desc">Android 端以开源、跨平台的 Sing-box 和 Clash Meta for Android（CMFA）为常用高级分流工具。</div>
</div>

<div class="tutorial-steps-grid">
  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-green">STEP 01</span>
        <div class="step-card-title">客户端选择与安装</div>
      </div>
      <div class="step-card-body">
        <ul>
          <li><strong>Sing-box：</strong> 可直接从 Google Play 商店安装，或从 GitHub Releases 下载对应架构 <code>.apk</code> 文件。</li>
          <li><strong>CMFA：</strong> 基于 Clash Meta 核心维护，界面交互与传统 Clash 保持一致。</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-green">STEP 02</span>
        <div class="step-card-title">导入 Sing-box 配置</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>打开 Sing-box，点击底部 <strong>Profiles (配置)</strong>。</li>
          <li>点击右上角 <strong>「+」</strong>：Type 选择 <strong>Remote (远程 URL)</strong>，粘贴服务商 Sing-box 订阅链接。</li>
          <li>点击右上角保存，等待配置下载解析完成。</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-green">STEP 03</span>
        <div class="step-card-title">启动连接与授权</div>
      </div>
      <div class="step-card-body">
        <ol>
          <li>回到 Dashboard 选中导入的 Profile。</li>
          <li>点击 Groups 选可用低延迟节点。</li>
          <li>点击大圆圈 <strong>启动开关</strong>，系统弹出 VPN 权限选择 <strong>确定</strong>。</li>
        </ol>
      </div>
      <div class="step-verify-tip">
        <strong>🚀 验证方法：</strong> 状态栏出现 Key/VPN 钥匙图标，节点测速正常。
      </div>
    </div>
  </div>
</div>

<div class="tutorial-image-container" style="margin-bottom: 35px; text-align: center;">
  <img src="/images/tutorials/singbox-guide.svg" alt="Sing-box Android 配置教程示意图" style="width: 100%; max-width: 850px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 3-1：Sing-box / CMFA (Android 安卓端) Profiles 导入与启动加速示意图</p>
</div>

<div class="platform-section-header" style="border-left-color: #7c3aed;">
  <h2>🛠️ 4. 常见问题排查与避坑指南</h2>
  <div class="platform-section-desc">使用过程中遇到网络连不上或报错？请参考下方流程图与常见故障排错对策表快速定位并解决：</div>
</div>

<div class="tutorial-image-container" style="margin-bottom: 25px; text-align: center;">
  <img src="/images/tutorials/troubleshoot-guide.svg" alt="常见故障排错流程图" style="width: 100%; max-width: 850px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 4-1：网络代理常见故障快速诊断与排错流程图</p>
</div>

<div class="table-responsive">
  <table class="custom-guide-table">
    <thead>
      <tr>
        <th style="width: 25%;">常见故障现象</th>
        <th style="width: 30%;">潜在触发原因</th>
        <th style="width: 45%;">针对性排查与解决方案</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="font-weight: bold; color: #dc2626;">节点全部 Timeout / 0ms / 连不上</td>
        <td>1. 本地系统时间不准<br>2. DNS 受到劫持污染<br>3. 节点域名或套餐已到期</td>
        <td>
          1. 前往系统设置勾选“自动同步时间”；<br>
          2. 在客户端中临时切换分流模式为“全局模式”测试；<br>
          3. 登录机场后台核查可用剩余流量与订阅有效状态。
        </td>
      </tr>
      <tr>
        <td style="font-weight: bold; color: #d97706;">订阅更新失败 (Download Error)</td>
        <td>1. 订阅 URL 前后包含空格<br>2. 本地 DNS 无法解析订阅域名<br>3. 运营商阻断了配置获取端口</td>
        <td>
          1. 将系统 DNS 更改为 1.1.1.1 或 8.8.8.8；<br>
          2. 重新登录机场后台复制完整订阅 URL；<br>
          3. 开启已有代理开关后，再次尝试更新订阅。
        </td>
      </tr>
      <tr>
        <td style="font-weight: bold; color: #2563eb;">国内网站打不开或访问极慢</td>
        <td>误将客户端分流模式开启成了“全局模式 (Global)”</td>
        <td>
          在客户端主界面将模式切换为<strong>“规则模式 (Rule / Config)”</strong>，即可恢复国内网站直连秒开。
        </td>
      </tr>
      <tr>
        <td style="font-weight: bold; color: #7c3aed;">App Store 搜不到 Shadowrocket</td>
        <td>使用了大陆国区 Apple ID 登录 App Store</td>
        <td>
          需要退出国区账号，登录美区或港区等非国区 Apple ID 后重新搜索下载，认准开发者 <em>Shadow Launch Technology Limited</em>。
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

<h2 class="section-heading text-center" style="font-size: 24px; font-weight: 800; margin-top: 35px; margin-bottom: 25px;">📚 零基础客户端配置与使用教程文章合集</h2>

<div class="collection-intro-banner" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #ffffff; padding: 24px 28px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
  <p style="font-size: 15px; line-height: 1.8; margin-bottom: 12px; color: #f1f5f9;">
    对于刚接触跨境网络与代理工具的新手来说，面对各种专有名词——订阅链接、内核、TUN 模式、分流规则、节点延迟，常常会感到无从下手；更有不少用户在配置好之后，出现“国内网页打不开”、“软件报错闪退”或“节点全红超时”等问题。
  </p>
  <p style="font-size: 15px; line-height: 1.8; margin: 0; color: #cbd5e1;">
    工欲善其事，必先利其器。为了让大家少走弯路，本文梳理了主流跨平台代理工具的零基础配置与使用文章合集。无论你使用的是 Windows 办公电脑、MacBook，还是 iPhone、安卓手机，都能在这里找到清晰直观的保姆级入门指南。
  </p>
</div>

<div class="platform-section-header" style="border-left-color: #f59e0b;">
  <h2>🚀 零、 新手必读：三步通用配置逻辑</h2>
  <div class="platform-section-desc">无论你使用哪个平台、哪款客户端，核心逻辑永远只有三步，理解了这个流程，换用任何软件都能轻松上手：</div>
</div>

<div class="tutorial-steps-grid">
  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 01</span>
        <div class="step-card-title">1. 获取订阅</div>
      </div>
      <div class="step-card-body">
        在你的服务商后台复制专属的“订阅链接”（Sub URL）或使用客户端直接扫描二维码导入节点。
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 02</span>
        <div class="step-card-title">2. 导入与更新</div>
      </div>
      <div class="step-card-body">
        将链接粘贴到客户端的订阅/配置管理框中，点击“导入”或“更新”拉取最新可用节点列表。
      </div>
    </div>
  </div>

  <div class="step-card-item">
    <div>
      <div class="step-card-header">
        <span class="step-badge step-badge-amber">STEP 03</span>
        <div class="step-card-title">3. 选节点与开启代理</div>
      </div>
      <div class="step-card-body">
        在节点列表中挑一个延迟较低的节点选中，最后打开软件的主开关（System Proxy / 启动代理）。
      </div>
    </div>
  </div>
</div>

<div class="platform-section-header" style="border-left-color: #2563eb;">
  <h2>💻 一、 Windows 桌面端配置指南</h2>
  <div class="platform-section-desc">Windows 平台客户端生态成熟，目前最推荐兼具现代化 UI 与新协议支持的工具：</div>
</div>

<div class="custom-card-grid">
  <div class="custom-card card-blue">
    <div>
      <span class="card-badge badge-amber">桌面神器</span>
      <h4>1. 《Clash Verge Rev 零基础实操图文教程》</h4>
      <p class="card-desc"><strong>工具定位：</strong>新一代基于 Clash Meta (Mihomo) 内核的桌面神器，界面美观，功能完善。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>软件下载与安装注意事项（避免中文路径报错）。</li>
          <li>订阅配置导入、一键定时自动更新设置。</li>
          <li>开启 TUN 虚拟网卡模式：完美解决游戏、Steam、某些专用开发软件不走系统代理的问题。</li>
          <li>规则模式（Rule）与全局模式（Global）的区别与正确用法。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-4/" class="rec-btn">查看实操教程 →</a>
  </div>

  <div class="custom-card card-sky">
    <div>
      <span class="card-badge badge-green">老牌经典</span>
      <h4>2. 《v2rayN 新版极简上手指南》</h4>
      <p class="card-desc"><strong>工具定位：</strong>老牌经典、轻量高效，适合对新版复杂的图形化界面不习惯的传统用户。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>Xray / Sing-box 双内核切换与组件下载。</li>
          <li>剪贴板快速批量导入节点与订阅分组管理。</li>
          <li>开启“绕过大陆”分流，保持国内直连低延迟。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-6/" class="rec-btn btn-sky">查看极简指南 →</a>
  </div>
</div>

<div class="platform-section-header" style="border-left-color: #7c3aed;">
  <h2>🍎 二、 macOS 苹果电脑端配置指南</h2>
  <div class="platform-section-desc">Mac 系统对网络权限管理较为严格，针对不同系统版本，我们整理了最佳方案：</div>
</div>

<div class="custom-card-grid">
  <div class="custom-card card-purple">
    <div>
      <span class="card-badge badge-purple">Mac 推荐</span>
      <h4>1. 《Clash Verge Rev for Mac 保姆级指南》</h4>
      <p class="card-desc"><strong>工具定位：</strong>跨平台统一体验，完美原生支持 Apple Silicon (M1/M2/M3/M4) 系列芯片。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>初次运行权限赋予（授权 Helper 安装与系统网络扩展许可）。</li>
          <li>状态栏图标快捷切换节点与分流策略。</li>
          <li>解决“已连接但 Safari 无法加载海外页面”的常见 DNS 污染问题。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-8/" class="rec-btn btn-purple">查看 Mac 指南 →</a>
  </div>

  <div class="custom-card card-blue">
    <div>
      <span class="card-badge badge-amber">极客玩家</span>
      <h4>2. 《Sing-box / Loon for Mac 轻量进阶教程》</h4>
      <p class="card-desc"><strong>工具定位：</strong>极低内存占用、响应极快，适合追求原生系统质感与高阶分流控制的极客玩家。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>Sing-box / Loon 引擎原生规则转换与加载。</li>
          <li>Mac 端的全局 TUN 抓包与自定义域名黑名单拦截。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-5/" class="rec-btn">查看进阶教程 →</a>
  </div>
</div>

<div class="platform-section-header" style="border-left-color: #d97706;">
  <h2>📱 三、 iOS / iPadOS 移动端配置指南</h2>
  <div class="platform-section-desc">苹果手机由于 App Store 区域限制，需使用美区或海外 Apple ID 获取对应软件：</div>
</div>

<div class="custom-card-grid">
  <div class="custom-card card-green">
    <div>
      <span class="card-badge badge-green">iOS 必备</span>
      <h4>1. 《Shadowrocket（小火箭）从下载到日用配置全解》</h4>
      <p class="card-desc"><strong>工具定位：</strong>iOS 平台装机必备、功能全面的大众级网络工具。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>美区 Apple ID 获取与购买注意事项。</li>
          <li>扫码导入与一键订阅链接解析。</li>
          <li>底部“配置”策略选择：默认推荐开启“配置（按规则分流）”，实现无感切换。</li>
          <li>常用节点测速与自动选择最优节点设置。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-3/" class="rec-btn btn-green">查看小火箭教程 →</a>
  </div>

  <div class="custom-card card-amber">
    <div>
      <span class="card-badge badge-amber">高阶神器</span>
      <h4>2. 《Quantumult X（圈 X）与 Loon 新手快速入门》</h4>
      <p class="card-desc"><strong>工具定位：</strong>UI 优雅精细，支持丰富脚本与自定义重写的高阶网络工具。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>预设懒人分流规则的导入与定期自动更新。</li>
          <li>解决节点延迟测速成功但打开应用依然超时的排查步骤。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-1/" class="rec-btn btn-amber">查看圈 X 入门 →</a>
  </div>
</div>

<div class="platform-section-header" style="border-left-color: #10b981;">
  <h2>🤖 四、 Android 安卓端配置指南</h2>
  <div class="platform-section-desc">安卓端开放度高，选择丰富且安装便捷，直接下载 APK 即可体验：</div>
</div>

<div class="custom-card-grid">
  <div class="custom-card card-green">
    <div>
      <span class="card-badge badge-green">安卓强推</span>
      <h4>1. 《Flclash / Clash Meta for Android 极简配置手册》</h4>
      <p class="card-desc"><strong>工具定位：</strong>界面简洁大方，完美适配安卓 Material You 设计语言。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>允许常驻后台与忽略电池优化设置（防止后台被系统杀进程）。</li>
          <li>开启“分应用代理”：仅让指定应用走代理，国内日常软件直连，省电又省流量。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-7/" class="rec-btn btn-green">查看安卓手册 →</a>
  </div>

  <div class="custom-card card-sky">
    <div>
      <span class="card-badge badge-amber">轻量稳定</span>
      <h4>2. 《v2rayNG 移动端极简上手指南》</h4>
      <p class="card-desc"><strong>工具定位：</strong>极致简洁稳定，低配备用机与平板的首选。</p>
      <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">
        <strong>教程核心涵盖：</strong>
        <ul class="card-list">
          <li>自定义规则集导入与 DNS 防泄漏设置。</li>
          <li>节点测试与路由模式快速选择。</li>
        </ul>
      </div>
    </div>
    <a href="/categories/tutorial/tut-7/" class="rec-btn btn-sky">查看 v2rayNG 教程 →</a>
  </div>
</div>

<div class="platform-section-header" style="border-left-color: #dc2626;">
  <h2>⚠️ 五、 常见新手翻车排错速查表</h2>
  <div class="platform-section-desc">在开始阅读具体教程前，若遇到突发故障，请对照以下四条黄金排错原则：</div>
</div>

<div class="avoid-card" style="margin-bottom: 30px;">
  <div class="avoid-list-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
    <div style="background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #fca5a5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
      <h5 style="color: #dc2626; font-size: 14px; font-weight: 700; margin-bottom: 6px;">1. 软件闪退或更新失败</h5>
      <p style="font-size: 13px; color: #7f1d1d; line-height: 1.6; margin: 0;">
        检查电脑本地时间是否准确。如果系统时间与网络标准时间偏差超过 90 秒，TLS 加密握手会直接失败。
      </p>
    </div>

    <div style="background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #fca5a5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
      <h5 style="color: #dc2626; font-size: 14px; font-weight: 700; margin-bottom: 6px;">2. 国内软件打不开/微信断连</h5>
      <p style="font-size: 13px; color: #7f1d1d; line-height: 1.6; margin: 0;">
        检查是否误开了“全局代理（Global）”；切换为“规则分流（Rule / 绕过大陆）”即可解决。
      </p>
    </div>

    <div style="background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #fca5a5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
      <h5 style="color: #dc2626; font-size: 14px; font-weight: 700; margin-bottom: 6px;">3. 关闭软件后整台电脑断网</h5>
      <p style="font-size: 13px; color: #7f1d1d; line-height: 1.6; margin: 0;">
        这是因为软件退出时没有正确清理系统代理设置。重新打开软件，先关闭“系统代理”开关，然后再退出程序即可恢复正常。
      </p>
    </div>

    <div style="background: #ffffff; padding: 16px; border-radius: 8px; border: 1px solid #fca5a5; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
      <h5 style="color: #dc2626; font-size: 14px; font-weight: 700; margin-bottom: 6px;">4. 延迟全部显示 Timeout / 超时</h5>
      <p style="font-size: 13px; color: #7f1d1d; line-height: 1.6; margin: 0;">
        多为节点服务器网络波动或本地网络防火墙拦截，尝试更换不同地区的节点测试，或更新订阅。
      </p>
    </div>
  </div>
</div>

