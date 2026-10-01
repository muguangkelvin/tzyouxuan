import os

tutorial_md_content = '''---
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

---

## 💻 1. 桌面端：Windows & macOS（推荐 Clash Verge Rev）

Clash Verge Rev 是目前桌面端功能最完善、界面现代化且支持 Clash Meta（Mihomo）内核的主流代理客户端。

### 步骤 1：下载与安装
* **Windows：** 前往 GitHub Releases 下载以 .msi 或 _x64-setup.exe 结尾的安装包（如提示缺少运行环境，需配合安装微软 WebView2）。
* **macOS：** Apple Silicon（M1/M2/M3/M4 系列芯片）请选择 aarch64.dmg；Intel 芯片老款 Mac 请选择 x64.dmg。安装后首次打开若提示“无法验证开发者”，请在 macOS *系统设置 → 隐私与安全性* 中点击“仍要打开”。

### 步骤 2：导入订阅配置
1. 打开 Clash Verge Rev，在左侧导航栏点击 **订阅（Subscription）**。
2. 将复制好的机场订阅链接粘贴到顶部的 URL 输入框中，点击 **导入（Import）**。
3. 导入成功后，列表会显示该配置卡片，单击选中让其高亮生效。

> **✅ 验证方法：** 卡片上显示更新时间与节点数量即代表导入成功。

### 步骤 3：选择节点并开启系统代理
1. 点击左侧 **代理（Proxy）** 菜单，顶部模式保持为 **Rule（规则）**。
2. 点击右上角的 Wi-Fi 测速图标，列表会显示各节点延迟（毫秒数），点击选中一个可用的低延迟节点。
3. 回到主界面或 **设置（Settings）**，将 **系统代理（System Proxy）** 开关切换为开启。

> **🚀 验证方法：** 打开浏览器访问常用海外网站（如 Google/YouTube），页面能顺畅秒开即表示配置成功。

<div class="tutorial-image-container" style="margin-top: 20px; text-align: center;">
  <img src="/images/tutorials/clash-verge-guide.svg" alt="Clash Verge Rev Windows & Mac 配置教程示意图" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 1-1：Clash Verge Rev (Windows / macOS) 订阅导入与代理切换示意图</p>
</div>

---

## 📱 2. 苹果移动端：iOS / iPadOS（推荐 Shadowrocket 小火箭）

Shadowrocket（俗称“小火箭”）是 iOS 端功能强大、连接极其稳定的经典规则分流工具。

### 步骤 1：获取与下载
由于区域限制，Shadowrocket 未在部分地区的 App Store 上架，需使用美区等非国区 Apple ID 登录 App Store 后搜索并购买下载（注意认准开发者：*Shadow Launch Technology Limited*）。

### 步骤 2：添加订阅
1. 打开 Shadowrocket，点击右上角的 **「+」** 号。
2. 点击第一行的 **类型（Type）**，修改为 **Subscribe**。
3. 在 **URL** 一栏粘贴订阅地址，备注（Remarks） 可自定义填写（如“我的节点”）。
4. 点击右上角 **完成（Done/Save）** 保存。首页会自动加载并列出所有可用节点。

### 步骤 3：连接与权限配置
1. 首页 **全局路由** 确保勾选为 **配置（Config）**（即规则分流模式）。
2. 勾选选中任意一个低延迟节点（节点左侧会出现选择标识）。
3. 打开首页最顶部的 **连接** 开关。首次使用系统会弹出 “添加 VPN 配置” 弹窗，点击 **允许（Allow）** 并验证锁屏密码或面容 ID。

> **🚀 验证方法：** 连接开关显示为已连接，手机状态栏顶部出现 VPN 图标，浏览器可正常访问外部网络。

<div class="tutorial-image-container" style="margin-top: 20px; text-align: center;">
  <img src="/images/tutorials/shadowrocket-guide.svg" alt="Shadowrocket iOS 配置教程示意图" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 2-1：Shadowrocket (iOS / iPadOS) 小火箭订阅添加与 VPN 权限设置示意图</p>
</div>

---

## 🤖 3. 安卓端：Android（推荐 Sing-box / Clash Meta for Android）

Android 端以开源、跨平台的 Sing-box 和 Clash Meta for Android（CMFA）为常用高级分流工具。

### 步骤 1：客户端选择与安装
* **Sing-box：** 可直接从 Google Play 商店安装，或在 GitHub Releases 下载对应架构的 .apk 文件。
* **CMFA：** 基于 Clash Meta 核心维护，界面交互与传统 Clash 保持一致。

### 步骤 2：以 Sing-box 为例导入配置
1. 打开 Sing-box，在底部点击 **Profiles（配置）**。
2. 点击右上角 **「+」** 创建新配置：
   * **Name：** 任意命名（如：机场订阅）。
   * **Type：** 选择 **Remote（远程 URL）**。
   * **URL：** 粘贴服务商提供的专用 Sing-box 订阅链接（若服务商仅提供 Clash 订阅，请先通过服务商面板转换或客户端转换工具）。
3. 点击右上角保存勾选，等待配置下载解析完成。

### 步骤 3：启动连接与授权
1. 回到首页 Dashboard，点击配置名称选中刚刚导入的 Profile。
2. 点击 Groups（节点组），点选可用地区的低延迟节点。
3. 点击大圆圈 **启动开关**。屏幕弹出系统级“网络连接请求 / VPN 权限”，点击 **确定**。

> **🚀 验证方法：** 状态栏出现 Key/VPN 钥匙图标，节点测速响应正常。

<div class="tutorial-image-container" style="margin-top: 20px; text-align: center;">
  <img src="/images/tutorials/singbox-guide.svg" alt="Sing-box Android 配置教程示意图" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
  <p class="img-caption" style="margin-top: 8px; font-size: 13px; color: #64748b; font-weight: 600;">📸 图 3-1：Sing-box / CMFA (Android 安卓端) Profiles 导入与启动加速示意图</p>
</div>

---

## 🛠️ 4. 常见问题排查与避坑指南

使用过程中遇到网络连不上或报错？请参考下方流程图与常见故障排错对策表快速定位并解决：

<div class="tutorial-image-container" style="margin-bottom: 25px; text-align: center;">
  <img src="/images/tutorials/troubleshoot-guide.svg" alt="常见故障排错流程图" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.06);">
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

<h2 class="section-heading text-center" style="font-size: 24px; font-weight: 800; margin-bottom: 25px;">📚 零基础客户端配置与使用教程文章合集</h2>
'''

with open("content/categories/tutorial/_index.md", "w", encoding="utf-8") as f:
    f.write(tutorial_md_content)

print("Tutorial markdown simplified update completed.")
