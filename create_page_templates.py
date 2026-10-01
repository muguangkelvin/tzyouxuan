import os

# 1. layouts/index.html
index_html = """{{ define "main" }}
<section class="hero-section">
  <div class="container">
    <div class="hero-content">
      <span class="hero-badge">🔥 2026年最新梯子优选与高性价比网络加速指南</span>
      <h1 class="hero-title">梯子优选 (tzyouxuan.xyz) - 2026稳定高速梯子推荐与小白魔法上网配置教程指南</h1>
      <p class="hero-desc">
        面向小白新手与进阶用户的梯子优选指南！专注提供2026便宜好用的梯子优选推荐、优质梯子推荐、高性价比机场评测横评、主流客户端配置教程（Clash/Sing-box/v2rayN/小火箭等）及防失联备用入口。汇聚IPLC专线梯子、4K不卡顿魔法上网机场，助你极速安全冲浪！
      </p>
      <div class="hero-buttons">
        <a href="#top4-services" class="btn btn-primary btn-lg">⚡ 查看2026梯子优选四大主推服务</a>
        <a href="/categories/tutorial/" class="btn btn-secondary btn-lg">📖 查看小白零基础配置教程</a>
        <a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" rel="noopener noreferrer" class="btn btn-tg btn-lg">✈️ 加入TG防失联频道</a>
      </div>
    </div>
  </div>
</section>

<!-- Core 4 Featured Recommendation Section -->
<section id="top4-services" class="section featured-section">
  <div class="container">
    <div class="section-header text-center">
      <h2 class="section-title">🏆 2026年四大自营与主推梯子优选（重磅推荐）</h2>
      <p class="section-sub">全网实测表现卓越，涵盖IPLC专线、晚高峰4K影音大带宽、小流量超值年付及全客户端稳定兼容方案</p>
    </div>

    <div class="provider-grid primary-grid">
      <!-- 1. 灵动云 -->
      <div class="provider-card primary-card rank-1">
        <div class="rank-tag">👑 第1名 · IPLC顶级专线全能首选</div>
        <div class="card-header">
          <h3 class="provider-name">灵动云</h3>
          <span class="price-badge">18.8元/月起</span>
        </div>
        <p class="provider-summary">全网首推顶级IPLC专线梯子，晚高峰零丢包不降速，全节点解锁ChatGPT/Claude等AI服务及4K/8K全网流媒体。</p>
        <ul class="provider-features">
          <li><strong>节点线路：</strong> 香港、日本、新加坡、美国IPLC原生专线</li>
          <li><strong>主要特点：</strong> 低延迟过检测、全节点AI解锁、专属1v1客服</li>
          <li><strong>适用人群：</strong> AI重度用户、跨境办公、4K/8K视频画质派</li>
          <li><strong>专属优惠：</strong> 使用优惠码 <code>ld888</code> 享8折优惠</li>
        </ul>
        <div class="card-actions">
          <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="btn btn-register">⚡ 访问灵动云官网注册领优惠</a>
          <a href="/providers/lingdong-cloud/" class="btn btn-detail">查看灵动云详细测评</a>
        </div>
      </div>

      <!-- 2. 暮光网络 -->
      <div class="provider-card primary-card rank-2">
        <div class="rank-tag">🥇 第2名 · 晚高峰4K/8K影音首选</div>
        <div class="card-header">
          <h3 class="provider-name">暮光网络 (暮光加速)</h3>
          <span class="price-badge">20元/月起</span>
        </div>
        <p class="provider-summary">BGP中继与原生IP高速专线，晚高峰测速稳定跑满百兆，超强流媒体解锁体验，大流量派最爱。</p>
        <ul class="provider-features">
          <li><strong>节点线路：</strong> 香港、日本、新加坡、美国BGP中继专线</li>
          <li><strong>主要特点：</strong> 晚高峰大带宽不降速、不限设备数、流媒体全解锁</li>
          <li><strong>适用人群：</strong> 追剧影音派、大流量下载、多设备共享家族用户</li>
          <li><strong>专属优惠：</strong> 使用优惠码 <code>mm88</code> 享全站8折优惠</li>
        </ul>
        <div class="card-actions">
          <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" class="btn btn-register">🚀 访问暮光网络官网查看套餐</a>
          <a href="/providers/twilight-net/" class="btn btn-detail">查看暮光网络详细测评</a>
        </div>
      </div>

      <!-- 3. 飞猫云 -->
      <div class="provider-card primary-card rank-3">
        <div class="rank-tag">🥈 第3名 · 小流量超值年付首选</div>
        <div class="card-header">
          <h3 class="provider-name">飞猫云</h3>
          <span class="price-badge">84元/年起 (折合7元/月)</span>
        </div>
        <p class="provider-summary">高性价比小流量年付梯子首选，自研极简客户端一键导入配置，适合轻度上网与备用防失联。</p>
        <ul class="provider-features">
          <li><strong>节点线路：</strong> 香港、日本、新加坡高速优化线路</li>
          <li><strong>主要特点：</strong> 超低门槛年付、自研客户端小白一键连接、稳定不掉线</li>
          <li><strong>适用人群：</strong> 学生党、轻量备用梯子、注重低成本的小白用户</li>
          <li><strong>专属优惠：</strong> 使用优惠码 <code>flycat888</code> 季付以上享8折</li>
        </ul>
        <div class="card-actions">
          <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" class="btn btn-register">🐱 访问飞猫云官网查看低价套餐</a>
          <a href="/providers/flycat-cloud/" class="btn btn-detail">查看飞猫云详细测评</a>
        </div>
      </div>

      <!-- 4. 微风网络 Breezenet -->
      <div class="provider-card primary-card rank-4">
        <div class="rank-tag">🥉 第4名 · 客户端全能兼容口碑之选</div>
        <div class="card-header">
          <h3 class="provider-name">微风网络 Breezenet</h3>
          <span class="price-badge">137元/年起</span>
        </div>
        <p class="provider-summary">口碑极佳的稳定梯子优选服务，完美适配Clash/Sing-box/小火箭等主流客户端，节点稳定延迟低。</p>
        <ul class="provider-features">
          <li><strong>节点线路：</strong> 香港、日本、新加坡、美国高品质专线</li>
          <li><strong>主要特点：</strong> 全协议全客户端兼容、7x24运维防护、抗封锁力强</li>
          <li><strong>适用人群：</strong> 追求长期稳定挂后台、跨平台多设备办公用户</li>
          <li><strong>专属优惠：</strong> 最新优惠以官网结算页为准</li>
        </ul>
        <div class="card-actions">
          <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" class="btn btn-register">🌬️ 访问微风网络官网立即连接</a>
          <a href="/providers/breezenet/" class="btn btn-detail">查看微风网络详细测评</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Ranking 5 to 8 Section -->
<section class="section secondary-section bg-light">
  <div class="container">
    <div class="section-header text-center">
      <h2 class="section-title">⭐ 第5名至第8名优质梯子推荐榜</h2>
      <p class="section-sub">精选高性价比、多场景契合的优质梯子服务商</p>
    </div>

    <div class="provider-grid secondary-grid">
      <!-- 5. 隐形人 -->
      <div class="provider-card mini-card">
        <div class="mini-rank">#5</div>
        <h4>隐形人</h4>
        <p>主打隐蔽通信与安全防护的梯子服务商，多节点动态负载均衡。</p>
        <div class="mini-price">15元/月起</div>
        <a href="https://varnexa.invisibleaff.com/#/?code=FlyoraeM" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">🥷 官网注册</a>
      </div>

      <!-- 6. 浪网 WaveNet -->
      <div class="provider-card mini-card">
        <div class="mini-rank">#6</div>
        <h4>浪网 WaveNet</h4>
        <p>采用新一代Hysteria2协议，大带宽抗丢包，适合恶劣网络。</p>
        <div class="mini-price">22元/月起</div>
        <a href="https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">🌊 官网注册</a>
      </div>

      <!-- 7. 梯子云 LadderCloud -->
      <div class="provider-card mini-card">
        <div class="mini-rank">#7</div>
        <h4>梯子云 LadderCloud</h4>
        <p>简单直观的品牌梯子服务商，全平台客户端文档齐备，小白秒上手。</p>
        <div class="mini-price">18元/月起</div>
        <a href="https://varnexa.ladderaff.com/#/?code=bYVSMHMh" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">🪜 官网注册</a>
      </div>

      <!-- 8. 飞V -->
      <div class="provider-card mini-card">
        <div class="mini-rank">#8</div>
        <h4>飞V</h4>
        <p>专为大流量与稳定连接设计的优质梯子，高倍率与1X节点混合。</p>
        <div class="mini-price">25元/月起</div>
        <a href="https://varnexa.flyvaff.com/#/?code=qaMgTyhY" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">✈️ 官网注册</a>
      </div>
    </div>
    <div class="text-center margin-top-lg">
      <a href="/services/" class="btn btn-outline btn-lg">🔍 查看全部28个机场服务测评与链接汇总</a>
    </div>
  </div>
</section>

<!-- Latest Articles Section -->
<section class="section articles-section">
  <div class="container">
    <div class="section-header">
      <h2 class="section-title">📚 最新梯子优选推荐与小白教程文章</h2>
      <a href="/categories/recommend/" class="view-all">查看全部文章 &rarr;</a>
    </div>

    <div class="article-grid">
      {{ range first 6 (where .Site.RegularPages "Type" "in" (slice "categories" "recommend" "tutorial" "posts")) }}
      <article class="article-card">
        <div class="article-body">
          <span class="article-cat">{{ .Params.category | default "梯子优选" }}</span>
          <h3 class="article-title"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
          <p class="article-excerpt">{{ .Summary | truncate 100 }}</p>
          <div class="article-meta">
            <span>📅 {{ .Date.Format "2006-01-02" }}</span>
            <span>⏱️ {{ .ReadingTime }} 分钟阅读</span>
          </div>
        </div>
      </article>
      {{ end }}
    </div>
  </div>
</section>
{{ end }}
"""

with open("layouts/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

# 2. layouts/_default/single.html
single_html = """{{ define "main" }}
<div class="container page-layout">
  <article class="article-detail">
    <header class="article-header">
      <div class="breadcrumb">
        <a href="/">首页</a> &gt; <a href="/categories/recommend/">文章指南</a> &gt; <span>{{ .Title }}</span>
      </div>
      <h1 class="post-title">{{ .Title }}</h1>
      <div class="post-meta">
        <span>✍️ 发布者: 梯子优选编辑部</span>
        <span>📅 更新时间: {{ .Date.Format "2006-01-02" }}</span>
        <span>⏱️ 阅读时长: {{ .ReadingTime }} 分钟</span>
        <span>🏷️ 标签: {{ range .Params.tags }}<span class="tag-pill">{{ . }}</span> {{ end }}</span>
      </div>
    </header>

    <!-- Core 4 Featured Recommendation Banner Injected in Articles -->
    <div class="injected-recommendation-box">
      <h3 class="box-title">⚡ 2026年梯子优选四大自营与主推服务推荐（官网直达）</h3>
      <p class="box-desc">本文推荐优先选用以下四大高稳定性梯子，防失联避坑选型首选：</p>
      <div class="injected-grid">
        <div class="inj-card">
          <span class="inj-badge">第1名 IPLC专线</span>
          <h4>灵动云</h4>
          <p>全节点解AI与4K流媒体，晚高峰零丢包不降速。</p>
          <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">官网注册(优惠码ld888)</a>
        </div>

        <div class="inj-card">
          <span class="inj-badge">第2名 4K/8K影音</span>
          <h4>暮光网络</h4>
          <p>BGP中继原生IP，晚高峰大带宽影音追剧首选。</p>
          <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">官网注册(优惠码mm88)</a>
        </div>

        <div class="inj-card">
          <span class="inj-badge">第3名 超值年付</span>
          <h4>飞猫云</h4>
          <p>折合7元/月，自研极简客户端小白一键连接。</p>
          <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">官网注册(优惠码flycat888)</a>
        </div>

        <div class="inj-card">
          <span class="inj-badge">第4名 全能兼容</span>
          <h4>微风网络</h4>
          <p>适配Clash/Sing-box/小火箭，7x24稳定运维。</p>
          <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" class="btn btn-sm btn-register">官网注册(查看套餐)</a>
        </div>
      </div>
    </div>

    <!-- Article Content -->
    <div class="post-content">
      {{ .Content }}
    </div>

    <footer class="post-footer">
      <div class="tg-banner">
        <span>✈️ 担心网址失效防失联？请加入官方 Telegram 频道：</span>
        <a href="https://t.me/+XUkYwrYRQ_c0ODA1" target="_blank" rel="noopener noreferrer" class="btn btn-tg-sm">加入TG订阅频道</a>
      </div>
    </footer>
  </article>
</div>
{{ end }}
"""

with open("layouts/_default/single.html", "w", encoding="utf-8") as f:
    f.write(single_html)

# 3. layouts/_default/list.html
list_html = """{{ define "main" }}
<div class="container page-layout">
  <div class="list-header text-center">
    <h1 class="page-title">{{ .Title }}</h1>
    <p class="page-desc">{{ .Description | default "梯子优选与高性价比网络加速文章列表指南" }}</p>
  </div>

  <div class="article-grid margin-top-lg">
    {{ range .Pages }}
    <article class="article-card">
      <div class="article-body">
        <h3 class="article-title"><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3>
        <p class="article-excerpt">{{ .Summary | truncate 120 }}</p>
        <div class="article-meta">
          <span>📅 {{ .Date.Format "2006-01-02" }}</span>
          <span>⏱️ {{ .ReadingTime }} 分钟阅读</span>
        </div>
      </div>
    </article>
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open("layouts/_default/list.html", "w", encoding="utf-8") as f:
    f.write(list_html)

# 4. layouts/faq/list.html (100 FAQs fully expanded!)
faq_list_html = """{{ define "main" }}
<div class="container page-layout">
  <div class="list-header text-center">
    <h1 class="page-title">❓ 梯子优选常见问题解答 (100 FAQ 痛点全解答)</h1>
    <p class="page-desc">覆盖梯子优选、魔法上网新手教学、节点超时排查、Clash/Sing-box订阅配置、IPLC专线与BGP中继区别及防失联备用入口。</p>
  </div>

  <div class="faq-container margin-top-lg">
    {{ range $index, $element := .Pages }}
    <div class="faq-item-card expanded">
      <h3 class="faq-question"><span class="q-num">Q{{ add $index 1 }}:</span> {{ .Title }}</h3>
      <div class="faq-answer">
        {{ .Content }}
      </div>
      <div class="faq-cta-bar">
        <span>💡 首推梯子推荐：</span>
        <a href="https://varnexa.lingdongaff.com/#/?code=JoIy7bO1" target="_blank" rel="sponsored nofollow noopener" class="btn-link">灵动云(IPLC专线)</a> | 
        <a href="https://varnexa.twilightaff.com/#/?code=KvGly3jY" target="_blank" rel="sponsored nofollow noopener" class="btn-link">暮光网络(4K影音)</a> | 
        <a href="https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH" target="_blank" rel="sponsored nofollow noopener" class="btn-link">飞猫云(超值年付)</a> | 
        <a href="https://edp01.breezenetaff.com/#/?code=He4n3zxg" target="_blank" rel="sponsored nofollow noopener" class="btn-link">微风网络(全能兼容)</a>
      </div>
    </div>
    {{ end }}
  </div>
</div>
{{ end }}
"""

with open("layouts/faq/list.html", "w", encoding="utf-8") as f:
    f.write(faq_list_html)

# 5. layouts/services/list.html (28 Providers page)
services_list_html = """{{ define "main" }}
<div class="container page-layout">
  <div class="list-header text-center">
    <h1 class="page-title">🛒 2026全网梯子优选与机场服务商汇总 (28款机场测评)</h1>
    <p class="page-desc">本站收录并测试的所有机场服务商概览，包含详细资料、节点情况、适用场景、价格以及对应官网直接注册入口。</p>
  </div>

  <div class="services-full-list margin-top-lg">
    <div class="provider-grid">
      {{ range .Site.Data.providers }}
      <div class="provider-card {{ if .isPrimary }}primary-card{{ end }}">
        <div class="rank-tag">#{{ .rank }} {{ .name }}</div>
        <div class="card-header">
          <h3 class="provider-name">{{ .name }}</h3>
          <span class="price-badge">{{ .priceFrom }}</span>
        </div>
        <p class="provider-summary">{{ .summary }}</p>
        <ul class="provider-features">
          <li><strong>流量参考：</strong> {{ .trafficFrom }}</li>
          <li><strong>节点地区：</strong> {{ .regions }}</li>
          <li><strong>支持协议：</strong> {{ .protocols }}</li>
          <li><strong>适用场景：</strong> {{ .suitableFor }}</li>
        </ul>
        <div class="card-actions">
          <a href="{{ .inviteURL }}" target="_blank" rel="sponsored nofollow noopener" class="btn btn-register">{{ .ctaText }}</a>
        </div>
      </div>
      {{ end }}
    </div>
  </div>
</div>
{{ end }}
"""

with open("layouts/services/list.html", "w", encoding="utf-8") as f:
    f.write(services_list_html)

print("Page templates created successfully.")
