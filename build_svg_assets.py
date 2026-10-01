import os
import subprocess

# Ensure directory static/images/tutorials exists
os.makedirs("static/images/tutorials", exist_ok=True)

# 1. Generate SVG for Clash Verge Rev (Windows & macOS)
svg_clash = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="auto" style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); background: #ffffff;">
  <rect width="800" height="480" fill="#f8fafc" rx="12"/>
  
  <!-- Window Header -->
  <path d="M 0 12 C 0 5.37 5.37 0 12 0 L 788 0 C 794.63 0 800 5.37 800 12 L 800 44 L 0 44 Z" fill="#1e293b"/>
  <circle cx="24" cy="22" r="6" fill="#ef4444"/>
  <circle cx="44" cy="22" r="6" fill="#f59e0b"/>
  <circle cx="64" cy="22" r="6" fill="#10b981"/>
  <text x="400" y="27" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Clash Verge Rev (Windows / macOS) 配置与使用示意图</text>

  <!-- Sidebar -->
  <rect x="0" y="44" width="180" height="436" fill="#0f172a"/>
  
  <!-- Sidebar Nav Items -->
  <rect x="12" y="64" width="156" height="36" rx="6" fill="#2563eb"/>
  <text x="48" y="87" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">📥 订阅 (Sub)</text>
  
  <rect x="12" y="112" width="156" height="36" rx="6" fill="#1e293b"/>
  <text x="48" y="135" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="14">⚡ 代理 (Proxy)</text>
  
  <rect x="12" y="160" width="156" height="36" rx="6" fill="#1e293b"/>
  <text x="48" y="183" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="14">⚙️ 设置 (Settings)</text>

  <rect x="12" y="208" width="156" height="36" rx="6" fill="#1e293b"/>
  <text x="48" y="231" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="14">📋 日志 (Logs)</text>

  <!-- Main Content Area -->
  <!-- Step 1 Box: Subscription -->
  <rect x="204" y="64" width="572" height="120" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="204" y="64" width="572" height="32" fill="#eff6ff" rx="8"/>
  <text x="220" y="85" fill="#1e40af" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">步骤 1：导入订阅链接 (Import Subscription)</text>
  <rect x="220" y="108" width="420" height="36" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="232" y="131" fill="#64748b" font-family="system-ui, sans-serif" font-size="13">https://your-airport-domain.com/api/v1/client/subscribe?...</text>
  <rect x="650" y="108" width="110" height="36" rx="6" fill="#2563eb"/>
  <text x="705" y="131" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">导入 Import</text>
  
  <rect x="220" y="152" width="540" height="20" fill="none"/>
  <text x="220" y="166" fill="#059669" font-family="system-ui, sans-serif" font-size="12" font-weight="600">✓ 配置文件更新成功！列表已解析 28 个高速加速节点</text>

  <!-- Step 2 & Step 3 Box -->
  <rect x="204" y="200" width="572" height="260" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="204" y="200" width="572" height="32" fill="#f0fdf4" rx="8"/>
  <text x="220" y="221" fill="#166534" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">步骤 2 & 3：选择节点并开启系统代理 (Proxy & System Proxy)</text>
  
  <!-- Mode Buttons -->
  <text x="220" y="255" fill="#334155" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">分流模式 (Mode)：</text>
  <rect x="310" y="240" width="80" height="24" rx="12" fill="#2563eb"/>
  <text x="350" y="256" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Rule 规则</text>
  <rect x="400" y="240" width="80" height="24" rx="12" fill="#e2e8f0"/>
  <text x="440" y="256" fill="#64748b" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Global 全局</text>
  <rect x="490" y="240" width="80" height="24" rx="12" fill="#e2e8f0"/>
  <text x="530" y="256" fill="#64748b" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Direct 直连</text>

  <!-- Node List -->
  <text x="220" y="295" fill="#334155" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">节点选择 (Select Node)：</text>

  <!-- Node Item 1 Selected -->
  <rect x="220" y="308" width="540" height="34" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="235" y="330" fill="#1d4ed8" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">🇭🇰 香港 IPLC 01 | 4K 极速专线 [选定]</text>
  <rect x="680" y="315" width="68" height="20" rx="10" fill="#dcfce7"/>
  <text x="714" y="329" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">24 ms</text>

  <!-- Node Item 2 -->
  <rect x="220" y="348" width="540" height="34" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="235" y="370" fill="#475569" font-family="system-ui, sans-serif" font-size="13">🇸🇬 新加坡 BGP 02 | 流媒体原生解锁</text>
  <rect x="680" y="355" width="68" height="20" rx="10" fill="#dcfce7"/>
  <text x="714" y="369" fill="#15803d" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">42 ms</text>

  <!-- System Proxy Toggle Bar -->
  <rect x="220" y="396" width="540" height="48" rx="8" fill="#1e293b"/>
  <text x="240" y="425" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">💻 系统代理 (System Proxy)</text>
  <rect x="690" y="408" width="56" height="24" rx="12" fill="#10b981"/>
  <circle cx="734" cy="420" r="9" fill="#ffffff"/>
  <text x="645" y="424" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">已开启 ON</text>
</svg>'''

with open("static/images/tutorials/clash-verge-guide.svg", "w", encoding="utf-8") as f:
    f.write(svg_clash)

# 2. Generate SVG for Shadowrocket (iOS)
svg_shadowrocket = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="auto" style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); background: #ffffff;">
  <rect width="800" height="480" fill="#f8fafc" rx="12"/>
  
  <!-- Card Header -->
  <path d="M 0 12 C 0 5.37 5.37 0 12 0 L 788 0 C 794.63 0 800 5.37 800 12 L 800 44 L 0 44 Z" fill="#0284c7"/>
  <text x="400" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">📱 Shadowrocket 小火箭 (iOS / iPadOS) 配置流程示意图</text>

  <!-- Left: Phone UI Mockup -->
  <rect x="40" y="60" width="260" height="400" rx="24" fill="#000000" stroke="#334155" stroke-width="4"/>
  <rect x="48" y="68" width="244" height="384" rx="18" fill="#f1f5f9"/>
  
  <!-- iOS Notch / Island -->
  <rect x="120" y="74" width="100" height="14" rx="7" fill="#000000"/>
  <circle cx="210" cy="81" r="3" fill="#1e293b"/>
  <!-- Status bar VPN icon -->
  <rect x="60" y="74" width="28" height="12" rx="3" fill="#0284c7"/>
  <text x="74" y="83" fill="#ffffff" font-family="system-ui, sans-serif" font-size="8" font-weight="bold" text-anchor="middle">VPN</text>

  <!-- Shadowrocket App Header -->
  <rect x="48" y="96" width="244" height="40" fill="#0284c7"/>
  <text x="64" y="121" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Shadowrocket</text>
  <text x="270" y="121" fill="#ffffff" font-family="system-ui, sans-serif" font-size="20" font-weight="bold" text-anchor="middle">+</text>

  <!-- Connection Switch Bar -->
  <rect x="60" y="146" width="220" height="44" rx="8" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="172" fill="#0f172a" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">未连接 / 已连接</text>
  <rect x="220" y="156" width="48" height="24" rx="12" fill="#10b981"/>
  <circle cx="256" cy="168" r="9" fill="#ffffff"/>

  <!-- Global Routing -->
  <rect x="60" y="198" width="220" height="36" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="221" fill="#64748b" font-family="system-ui, sans-serif" font-size="12">全局路由</text>
  <text x="250" y="221" fill="#0284c7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="end">配置 (Config) ✓</text>

  <!-- Node Section -->
  <rect x="60" y="242" width="220" height="190" rx="8" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="262" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">订阅服务器列表</text>
  
  <rect x="68" y="272" width="204" height="32" rx="4" fill="#e0f2fe"/>
  <text x="78" y="293" fill="#0369a1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">✓ 🇭🇰 香港 IPLC 01 (26ms)</text>

  <rect x="68" y="310" width="204" height="32" rx="4" fill="#f8fafc"/>
  <text x="78" y="331" fill="#475569" font-family="system-ui, sans-serif" font-size="11">🇸🇬 新加坡 01 (38ms)</text>

  <rect x="68" y="348" width="204" height="32" rx="4" fill="#f8fafc"/>
  <text x="78" y="369" fill="#475569" font-family="system-ui, sans-serif" font-size="11">🇺🇸 美国 4K 专线 (120ms)</text>

  <!-- Right: 3 Step Guide Cards -->
  <!-- Step 1 Card -->
  <rect x="330" y="60" width="430" height="120" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="88" r="14" fill="#0284c7"/>
  <text x="360" y="93" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1</text>
  <text x="388" y="93" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">获取与下载客户端</text>
  <text x="350" y="125" fill="#475569" font-family="system-ui, sans-serif" font-size="13">使用非国区 Apple ID（如美区）登录 App Store 搜索并下载。</text>
  <text x="350" y="148" fill="#64748b" font-family="system-ui, sans-serif" font-size="12" font-style="italic">注意认准开发者：Shadow Launch Technology Limited</text>

  <!-- Step 2 Card -->
  <rect x="330" y="195" width="430" height="130" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="223" r="14" fill="#0284c7"/>
  <text x="360" y="228" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2</text>
  <text x="388" y="228" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">添加订阅 (Subscribe)</text>
  <text x="350" y="258" fill="#475569" font-family="system-ui, sans-serif" font-size="13">点击右上角「+」→ 类型选择 Subscribe → 粘贴 URL。</text>
  <text x="350" y="280" fill="#475569" font-family="system-ui, sans-serif" font-size="13">点击右上角完成 (Done) 保存，首页自动生成节点列表。</text>

  <!-- Step 3 Card -->
  <rect x="330" y="340" width="430" height="120" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="368" r="14" fill="#10b981"/>
  <text x="360" y="373" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3</text>
  <text x="388" y="373" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">启动连接与 VPN 授权</text>
  <text x="350" y="403" fill="#475569" font-family="system-ui, sans-serif" font-size="13">选定低延迟节点，开启顶部 [未连接] 按钮。</text>
  <text x="350" y="425" fill="#475569" font-family="system-ui, sans-serif" font-size="13">系统弹窗提示“添加 VPN 配置”时点击“允许”并解锁。</text>
</svg>'''

with open("static/images/tutorials/shadowrocket-guide.svg", "w", encoding="utf-8") as f:
    f.write(svg_shadowrocket)

# 3. Generate SVG for Sing-box / CMFA (Android)
svg_singbox = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="auto" style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); background: #ffffff;">
  <rect width="800" height="480" fill="#f8fafc" rx="12"/>
  
  <!-- Card Header -->
  <path d="M 0 12 C 0 5.37 5.37 0 12 0 L 788 0 C 794.63 0 800 5.37 800 12 L 800 44 L 0 44 Z" fill="#7c3aed"/>
  <text x="400" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🤖 Sing-box / CMFA (Android 安卓端) 配置流程示意图</text>

  <!-- Left Side: Android UI Mockup -->
  <rect x="40" y="60" width="260" height="400" rx="20" fill="#18181b" stroke="#3f3f46" stroke-width="4"/>
  <rect x="48" y="68" width="244" height="384" rx="14" fill="#09090b"/>

  <!-- Android Notification Bar with Key Icon -->
  <rect x="48" y="68" width="244" height="24" fill="#18181b"/>
  <text x="60" y="84" fill="#a1a1aa" font-family="system-ui, sans-serif" font-size="10">10:24</text>
  <text x="240" y="84" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="11">🔑 🔑 85%</text>

  <!-- App Header -->
  <text x="64" y="118" fill="#ffffff" font-family="system-ui, sans-serif" font-size="16" font-weight="bold">Sing-box</text>

  <!-- Big Connect Button Ring -->
  <circle cx="170" cy="200" r="50" fill="none" stroke="#7c3aed" stroke-width="6"/>
  <circle cx="170" cy="200" r="42" fill="#7c3aed"/>
  <text x="170" y="206" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">已连接</text>

  <!-- Profile Active Box -->
  <rect x="64" y="270" width="212" height="48" rx="8" fill="#27272a"/>
  <text x="76" y="291" fill="#e4e4e7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">配置文件 Profile</text>
  <text x="76" y="308" fill="#a1a1aa" font-family="system-ui, sans-serif" font-size="11">我的专属机场订阅 (Remote)</text>

  <!-- Group / Node Select -->
  <rect x="64" y="328" width="212" height="48" rx="8" fill="#27272a"/>
  <text x="76" y="349" fill="#e4e4e7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">节点组 (Groups)</text>
  <text x="76" y="366" fill="#a855f7" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">🇭🇰 香港 01 - 22ms</text>

  <!-- Bottom Navigation -->
  <rect x="48" y="412" width="244" height="40" fill="#18181b"/>
  <text x="85" y="436" fill="#a855f7" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">主页</text>
  <text x="170" y="436" fill="#71717a" font-family="system-ui, sans-serif" font-size="12">配置</text>
  <text x="240" y="436" fill="#71717a" font-family="system-ui, sans-serif" font-size="12">设置</text>

  <!-- Right Side: Instructions Cards -->
  <rect x="330" y="60" width="430" height="120" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="88" r="14" fill="#7c3aed"/>
  <text x="360" y="93" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1</text>
  <text x="388" y="93" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">安装客户端 (Sing-box / CMFA)</text>
  <text x="350" y="125" fill="#475569" font-family="system-ui, sans-serif" font-size="13">Google Play 商店搜索安装，或在 GitHub Releases</text>
  <text x="350" y="148" fill="#475569" font-family="system-ui, sans-serif" font-size="13">下载对应的 .apk 安装包文件。</text>

  <rect x="330" y="195" width="430" height="130" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="223" r="14" fill="#7c3aed"/>
  <text x="360" y="228" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2</text>
  <text x="388" y="228" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">导入 Remote 订阅地址</text>
  <text x="350" y="258" fill="#475569" font-family="system-ui, sans-serif" font-size="13">点击 Profiles → 右上角「+」→ 选择 Remote (远程 URL)。</text>
  <text x="350" y="280" fill="#475569" font-family="system-ui, sans-serif" font-size="13">粘贴 Sing-box / Clash 订阅链接后保存并解析。</text>

  <rect x="330" y="340" width="430" height="120" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
  <circle cx="360" cy="368" r="14" fill="#10b981"/>
  <text x="360" y="373" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3</text>
  <text x="388" y="373" fill="#0f172a" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">启动加速与授权</text>
  <text x="350" y="403" fill="#475569" font-family="system-ui, sans-serif" font-size="13">返回 Dashboard 选中配置，点击中心圆圈启动。</text>
  <text x="350" y="425" fill="#475569" font-family="system-ui, sans-serif" font-size="13">允许系统的“网络连接请求 / VPN 权限”即可完成连接。</text>
</svg>'''

with open("static/images/tutorials/singbox-guide.svg", "w", encoding="utf-8") as f:
    f.write(svg_singbox)

# 4. Generate SVG for Troubleshooting flowchart
svg_troubleshoot = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="100%" height="auto" style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); background: #ffffff;">
  <rect width="800" height="360" fill="#f8fafc" rx="12"/>
  
  <path d="M 0 12 C 0 5.37 5.37 0 12 0 L 788 0 C 794.63 0 800 5.37 800 12 L 800 44 L 0 44 Z" fill="#dc2626"/>
  <text x="400" y="27" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🛠️ 常见故障快速诊断与排错流程图</text>

  <!-- Box 1: Node Timeout -->
  <rect x="40" y="70" width="210" height="250" rx="8" fill="#ffffff" stroke="#fca5a5" stroke-width="1.5"/>
  <rect x="40" y="70" width="210" height="36" fill="#fef2f2" rx="8"/>
  <text x="145" y="93" fill="#991b1b" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">⚠️ 节点全部 Timeout / 0ms</text>
  <text x="55" y="130" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 1：本地系统时间未同步</text>
  <text x="55" y="150" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 前往系统设置自动同步时间</text>
  <text x="55" y="180" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 2：订阅规则被污染</text>
  <text x="55" y="200" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 尝试切换全局模式测试</text>
  <text x="55" y="230" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 3：套餐流量已耗尽</text>
  <text x="55" y="250" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 登录机场后台核查可用流量</text>

  <!-- Box 2: Subscription Download Failed -->
  <rect x="295" y="70" width="210" height="250" rx="8" fill="#ffffff" stroke="#fde68a" stroke-width="1.5"/>
  <rect x="295" y="70" width="210" height="36" fill="#fffbe6" rx="8"/>
  <text x="400" y="93" fill="#92400e" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">❌ 订阅更新失败/无法下载</text>
  <text x="310" y="130" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 1：DNS 被运营商劫持</text>
  <text x="310" y="150" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 修改系统 DNS 为 1.1.1.1</text>
  <text x="310" y="180" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 2：链接拷贝多出空格</text>
  <text x="310" y="200" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 重新复制官网完整 URL 链接</text>
  <text x="310" y="230" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因 3：机场节点域名变更</text>
  <text x="310" y="250" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 尝试开启已有代理后更新</text>

  <!-- Box 3: Local Site Slow -->
  <rect x="550" y="70" width="210" height="250" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.5"/>
  <rect x="550" y="70" width="210" height="36" fill="#eff6ff" rx="8"/>
  <text x="655" y="93" fill="#1e40af" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">🐢 国内网站打不开/速度慢</text>
  <text x="565" y="130" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">原因：误开启了“全局模式”</text>
  <text x="565" y="150" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 将模式调回“规则模式 / Rule”</text>
  <text x="565" y="180" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">优化：开启 TUN 模式</text>
  <text x="565" y="200" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 在设置中开启虚拟网卡 TUN</text>
  <text x="565" y="230" fill="#475569" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">检查：第三方防护软件冲突</text>
  <text x="565" y="250" fill="#64748b" font-family="system-ui, sans-serif" font-size="11">👉 允许 Clash/Singbox 穿透防火墙</text>
</svg>'''

with open("static/images/tutorials/troubleshoot-guide.svg", "w", encoding="utf-8") as f:
    f.write(svg_troubleshoot)

print("SVG files generated successfully.")
