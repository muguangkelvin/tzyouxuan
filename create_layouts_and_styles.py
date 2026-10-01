import os

# 1. layouts/partials/head.html
head_html = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ if .IsHome }}{{ .Site.Title }}{{ else }}{{ .Title }} - {{ .Site.Params.brandName }}{{ end }}</title>
<meta name="description" content="{{ if .Description }}{{ .Description }}{{ else }}{{ .Site.Params.siteDescription }}{{ end }}">
<meta name="keywords" content="{{ .Site.Params.heroKeywords }}">
<link rel="canonical" href="{{ .Permalink }}">
<link rel="stylesheet" href="/css/style.css">
<!-- Open Graph -->
<meta property="og:title" content="{{ .Title }}">
<meta property="og:description" content="{{ if .Description }}{{ .Description }}{{ else }}{{ .Site.Params.siteDescription }}{{ end }}">
<meta property="og:type" content="{{ if .IsPage }}article{{ else }}website{{ end }}">
<meta property="og:url" content="{{ .Permalink }}">
<meta property="og:site_name" content="{{ .Site.Params.brandName }}">
"""

with open("layouts/partials/head.html", "w", encoding="utf-8") as f:
    f.write(head_html)

# 2. layouts/partials/header.html
header_html = """<header class="site-header">
  <div class="container header-inner">
    <div class="logo-area">
      <a href="/" class="brand-logo">
        <span class="logo-icon">⚡</span>
        <div class="logo-text-wrap">
          <span class="brand-name">梯子优选</span>
          <span class="brand-domain">tzyouxuan.xyz</span>
        </div>
      </a>
    </div>

    <nav class="main-nav">
      <ul class="nav-list">
        <li><a href="/" class="nav-item">首页</a></li>
        <li><a href="/categories/recommend/" class="nav-item">梯子优选与精选推荐</a></li>
        <li><a href="/categories/tutorial/" class="nav-item">小白教程</a></li>
        <li><a href="/services/" class="nav-item">自营与优选专区</a></li>
        <li><a href="/faq/" class="nav-item">常见问题</a></li>
        <li><a href="/reviews/" class="nav-item">机场测评</a></li>
      </ul>
    </nav>

    <div class="header-actions">
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="搜索文章/教程/节点..." onkeyup="handleSearch(event)">
        <button class="search-btn" onclick="executeSearch()">🔍 搜索</button>
      </div>
      <a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" rel="noopener noreferrer" class="tg-btn">
        <span class="tg-icon">✈️</span> TG防失联频道
      </a>
      <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">☰</button>
    </div>
  </div>
  <div id="mobileNavModal" class="mobile-nav-modal">
    <ul class="mobile-nav-list">
      <li><a href="/" onclick="toggleMobileMenu()">首页</a></li>
      <li><a href="/categories/recommend/" onclick="toggleMobileMenu()">梯子优选与精选推荐</a></li>
      <li><a href="/categories/tutorial/" onclick="toggleMobileMenu()">小白教程</a></li>
      <li><a href="/services/" onclick="toggleMobileMenu()">自营与优选专区</a></li>
      <li><a href="/faq/" onclick="toggleMobileMenu()">常见问题</a></li>
      <li><a href="/reviews/" onclick="toggleMobileMenu()">机场测评</a></li>
      <li><a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" rel="noopener noreferrer" style="color:#229ED9;font-weight:bold;">✈️ Telegram 防失联频道</a></li>
    </ul>
  </div>
</header>
"""

with open("layouts/partials/header.html", "w", encoding="utf-8") as f:
    f.write(header_html)

# 3. layouts/partials/footer.html
footer_html = """<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-col brand-col">
      <h3 class="footer-title">梯子优选网 (tzyouxuan.xyz)</h3>
      <p class="footer-desc">
        专注为小白新手与进阶用户提供2026稳定高速梯子推荐、高性价比机场评测横评、主流客户端配置教程（Clash/Sing-box/v2rayN/小火箭等）及避坑防失联技巧。本站自营与精选服务优先推荐转化，全网节点延迟稳定性实测保障。
      </p>
      <div class="footer-tg">
        <a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" rel="noopener noreferrer" class="footer-tg-link">
          ✈️ 官方Telegram防失联订阅频道: https://t.me/+XUkYwrYRQ_c0ODA1
        </a>
      </div>
    </div>

    <div class="footer-col">
      <h4 class="footer-subtitle">快速导航</h4>
      <ul class="footer-links">
        <li><a href="/categories/recommend/">梯子优选与精选推荐</a></li>
        <li><a href="/categories/tutorial/">小白教程与配置指南</a></li>
        <li><a href="/services/">自营与优选专区</a></li>
        <li><a href="/faq/">常见问题 (100FAQ)</a></li>
        <li><a href="/reviews/">全网机场测评横评</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4 class="footer-subtitle">热门关键词</h4>
      <div class="tag-cloud">
        <span class="foot-tag">梯子优选</span>
        <span class="foot-tag">优质梯子推荐</span>
        <span class="foot-tag">机场优选</span>
        <span class="foot-tag">稳定梯子</span>
        <span class="foot-tag">高速翻墙梯子</span>
        <span class="foot-tag">魔法上网</span>
        <span class="foot-tag">IPLC专线梯子</span>
        <span class="foot-tag">便宜好用梯子</span>
        <span class="foot-tag">Clash配置</span>
        <span class="foot-tag">小火箭节点导入</span>
      </div>
    </div>
  </div>

  <div class="footer-bottom">
    <div class="container">
      <p>&copy; 2026 梯子优选网 (tzyouxuan.xyz) 官方版权所有 · 全网节点延迟稳定性实测 · 科学上网常见问题答疑与防失联备用入口</p>
      <p class="disclosure">本站包含推广合作链接，点击跳转将通过 <code>rel="sponsored nofollow noopener"</code> 安全保障访问。价格与流量请以第三方服务商当前页面为准。</p>
    </div>
  </div>
</footer>
<script src="/js/main.js"></script>
"""

with open("layouts/partials/footer.html", "w", encoding="utf-8") as f:
    f.write(footer_html)

# 4. layouts/_default/baseof.html
baseof_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  {{ partial "head.html" . }}
</head>
<body>
  {{ partial "header.html" . }}
  <main class="main-content">
    {{ block "main" . }}{{ end }}
  </main>
  {{ partial "footer.html" . }}
</body>
</html>
"""

with open("layouts/_default/baseof.html", "w", encoding="utf-8") as f:
    f.write(baseof_html)

print("Base layouts created successfully.")
