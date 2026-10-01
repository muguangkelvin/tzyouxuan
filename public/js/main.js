/* main.js - Comprehensive Site Search & Associated Terms Engine */

let searchIndexData = null;
let isIndexLoading = false;
let searchDebounceTimer = null;

// Built-in Airport Providers dataset for instant matching
const PROVIDERS_DATASET = [
  { name: '灵动云', price: '18.8元/月', tag: 'IPLC顶级专线', summary: '全网首推顶级IPLC专线梯子，晚高峰零丢包不降速，全节点解锁ChatGPT/Claude等AI服务及4K流媒体。', link: 'https://varnexa.lingdongaff.com/#/?code=JoIy7bO1' },
  { name: '暮光网络 (暮光加速)', price: '20元/月', tag: 'BGP中继4K', summary: 'BGP中继与原生IP高速专线，晚高峰跑满百兆，超强流媒体解锁。', link: 'https://varnexa.twilightaff.com/#/?code=KvGly3jY' },
  { name: '飞猫云', price: '84元/年', tag: '小流量超值年付', summary: '高性价比小流量年付梯子首选，自研极简客户端一键导入配置。', link: 'https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH' },
  { name: '微风网络 Breezenet', price: '137元/年', tag: '全能兼容口碑', summary: '口碑极佳的稳定梯子优选，完美适配Clash/Sing-box/小火箭等主流客户端。', link: 'https://edp01.breezenetaff.com/#/?code=He4n3zxg' },
  { name: '隐形人', price: '15元/月', tag: '隐蔽安全防护', summary: '主打隐蔽通信与安全防护的梯子服务商，多节点动态负载均衡。', link: 'https://varnexa.invisibleaff.com/#/?code=FlyoraeM' },
  { name: '浪网 WaveNet', price: '22元/月', tag: 'Hysteria2协议', summary: '采用新一代Hysteria2协议，大带宽抗丢包，适合恶劣网络。', link: 'https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ' },
  { name: '梯子云 LadderCloud', price: '18元/月', tag: '品牌多通道', summary: '简单直观的品牌梯子服务商，全平台客户端文档齐备。', link: 'https://varnexa.ladderaff.com/#/?code=bYVSMHMh' },
  { name: '飞V', price: '25元/月', tag: '高倍率大流量', summary: '专为大流量与稳定连接设计的优质梯子，高倍率与1X节点混合。', link: 'https://varnexa.flyvaff.com/#/?code=qaMgTyhY' },
  { name: 'Sogo云', price: '12元/月', tag: '入门推荐', summary: '界面简洁，新手一键导入方便，入门推荐。', link: 'https://wzjc.sogoyunaff.cc/#/?code=JpsSYPPG' },
  { name: '宇宙云 YuZhou', price: '16元/月', tag: '多速率等级', summary: '节点数量充沛，多速率等级可选。', link: 'https://wzjc.yuzoucloud.cc/#/?code=MQM25nhk' },
  { name: '二猫云 2mao', price: '15元/月', tag: '低延时调优', summary: '节点延时调优出色，适合网页浏览与办公。', link: 'https://waaa.2maoyunaff.cc/#/?code=b4qTK67Z' },
  { name: '一翻云 1fly', price: '14元/月', tag: '轻量稳定', summary: '强调轻量与稳定性，轻度翻墙用户优选。', link: 'https://wzjc.1flyunaff.cc/#/?code=twb00vnS' },
  { name: '唯兔云 V2云', price: '17元/月', tag: 'V2Ray优化', summary: '经典 V2Ray 协议优化，连接稳定，文档教程齐全。', link: 'https://fast.v2yunvipaff.com/#/?code=B9Mbez3V' },
  { name: 'U1S1 有一说一', price: '15元/月', tag: '老牌中转', summary: '性价比突出，套餐灵活，老牌中转线路。', link: 'https://pkdj7.vipaff.cc/#/?code=BgqW6VLS' },
  { name: '极连云', price: '19元/月', tag: '极速秒开冗余', summary: '极速秒开，多节点冗余备份，连接成功率高。', link: 'https://kdjhao.jlyvipaff.com/#/?code=lHO8G2Sy' },
  { name: '全球云', price: '21元/月', tag: '全球冷热门节点', summary: '全球冷门与热门节点丰富，适合跨境业务。', link: 'https://sswdh.gcvipaff.com/#/?code=WJFuG7Wm' },
  { name: '光年梯', price: '23元/月', tag: '大流量下载', summary: '专为大流量用户设计，下载速率表现亮眼。', link: 'https://ggmq.gntaff.com/#/?code=1SLG97Ch' },
  { name: '光速云', price: '25元/月', tag: '外服游戏低延迟', summary: '速度快，延迟低，适合外服游戏与实时交互。', link: 'https://mdlky.gsyaff.com/' },
  { name: '星岛梦', price: '22元/月', tag: '流媒体解锁', summary: '节点覆盖广，流媒体解锁能力强，适合追剧党。', link: 'https://kfccbb.xingdaomeng.com/#/?code=o2LVBz3A' }
];

// Associated Terms & Synonyms Mapping
const SYNONYMS_MAP = {
  '梯子': ['机场', '翻墙', '科学上网', '加速器', '节点', 'IPLC', '专线', '订阅', '推荐', '优选', '梯子推荐'],
  '翻墙': ['梯子', '科学上网', '加速器', '节点', '机场', '魔法上网'],
  '科学上网': ['梯子', '翻墙', '加速器', '节点', '机场', '魔法上网'],
  '魔法上网': ['梯子', '翻墙', '科学上网', '机场', '节点'],
  '机场': ['梯子', '服务商', '节点', 'IPLC', '专线', '订阅', '28款', '测评', '机场推荐'],
  '苹果': ['iOS', 'iPhone', 'iPad', 'macOS', 'Mac', 'Shadowrocket', '小火箭', 'Clash'],
  'ios': ['苹果', 'iPhone', 'iPad', 'Shadowrocket', '小火箭', '配置', '订阅'],
  'mac': ['macOS', '苹果', 'Clash Verge', 'Sing-box', '桌面端'],
  '安卓': ['Android', 'Sing-box', 'CMFA', 'v2rayN', 'Clash Meta', '配置'],
  'android': ['安卓', 'Sing-box', 'CMFA', 'v2rayN'],
  'windows': ['Win', '电脑', '桌面端', 'Clash Verge', 'v2rayN'],
  '小火箭': ['Shadowrocket', 'iOS', '苹果', '规则模式', '节点导入', '小火箭配置'],
  'clash': ['Clash Verge', 'CMFA', '规则', 'Mihomo', '订阅', '小火箭'],
  'singbox': ['Sing-box', '安卓', 'Android', 'Remote', '配置'],
  '节点': ['专线', 'IPLC', 'BGP', '延迟', '超时', 'Timeout', '测速'],
  '超时': ['Timeout', '连不上', '0ms', '排错', 'DNS', '时间同步'],
  '连不上': ['Timeout', '无法连接', '排错', '全局模式', 'DNS'],
  '优惠': ['优惠码', '折扣', '年付', '8折', '试用', '便宜'],
  '推荐': ['优选', '榜单', '四大主推', '第一梯队', '性价比', '评测']
};

function toggleMobileMenu() {
  const modal = document.getElementById('mobileNavModal');
  if (modal) {
    modal.classList.toggle('active');
  }
}

// Lazy Load Site Search Index JSON
function handleSearchFocus() {
  if (!searchIndexData && !isIndexLoading) {
    isIndexLoading = true;
    fetch('/index.json')
      .then(response => response.json())
      .then(data => {
        searchIndexData = data;
        isIndexLoading = false;
      })
      .catch(err => {
        console.warn('Search index fetch notice:', err);
        isIndexLoading = false;
      });
  }
}

function handleSearchInput(event) {
  clearTimeout(searchDebounceTimer);
  searchDebounceTimer = setTimeout(() => {
    performLiveSearch();
  }, 150);
}

function handleSearch(event) {
  if (event.key === 'Enter') {
    executeSearch();
  } else if (event.key === 'Escape') {
    closeSearchDropdown();
  }
}

// Perform Live Keyword & Association Matching Search
function performLiveSearch() {
  const input = document.getElementById('searchInput');
  const dropdown = document.getElementById('searchResultsDropdown');
  if (!input || !dropdown) return;

  const rawQuery = input.value.trim();
  if (!rawQuery) {
    closeSearchDropdown();
    return;
  }

  const queryLower = rawQuery.toLowerCase();
  
  // Expand search terms with associated synonyms
  let expandedTerms = [queryLower];
  for (let key in SYNONYMS_MAP) {
    if (queryLower.includes(key) || key.includes(queryLower)) {
      expandedTerms = expandedTerms.concat(SYNONYMS_MAP[key].map(s => s.toLowerCase()));
    }
  }

  let matchedProviders = [];
  let matchedPages = [];

  // 1. Search Provider Cards
  PROVIDERS_DATASET.forEach(p => {
    let score = 0;
    const pText = (p.name + ' ' + p.tag + ' ' + p.summary + ' ' + (p.keywords || '')).toLowerCase();
    
    if (p.name.toLowerCase().includes(queryLower)) score += 100;
    else if (pText.includes(queryLower)) score += 70;
    
    expandedTerms.forEach(term => {
      if (pText.includes(term)) score += 30;
    });

    if (score > 0) {
      matchedProviders.push({ item: p, score });
    }
  });

  // 2. Search Hugo Articles & Tutorials Pages
  if (searchIndexData && Array.isArray(searchIndexData)) {
    searchIndexData.forEach(page => {
      let score = 0;
      const titleLower = (page.title || '').toLowerCase();
      const summaryLower = (page.summary || '').toLowerCase();
      const categoryLower = (page.category || '').toLowerCase();
      const keywordsLower = (page.keywords || '').toLowerCase();
      
      if (titleLower.includes(queryLower)) score += 100;
      else if (keywordsLower.includes(queryLower)) score += 80;
      else if (categoryLower.includes(queryLower)) score += 60;
      else if (summaryLower.includes(queryLower)) score += 40;

      expandedTerms.forEach(term => {
        if (titleLower.includes(term)) score += 30;
        else if (summaryLower.includes(term)) score += 15;
      });

      if (score > 0) {
        matchedPages.push({ item: page, score });
      }
    });
  }

  // Sort matched items by score
  matchedProviders.sort((a, b) => b.score - a.score);
  matchedPages.sort((a, b) => b.score - a.score);

  // Render Dropdown Results HTML
  let html = '';
  const totalMatches = matchedProviders.length + matchedPages.length;

  if (totalMatches === 0) {
    html = `<div class="search-no-results">🔍 未能定位到关键词 "<strong>${escapeHtml(rawQuery)}</strong>"，建议尝试搜索 <code>Clash</code>、<code>小火箭</code>、<code>灵动云</code> 或 <code>IPLC</code></div>`;
  } else {
    html += `<div class="search-header-bar"><span>🔍 相关检索结果 (${totalMatches})</span><span>按 Esc 退出</span></div>`;

    // Render Providers
    matchedProviders.slice(0, 3).forEach(res => {
      const p = res.item;
      html += `
        <a href="${p.link}" target="_blank" rel="sponsored nofollow noopener" class="search-result-item">
          <div class="search-result-title">⚡ ${escapeHtml(p.name)} <span style="font-size:12px;color:#d97706;font-weight:bold;">${p.price}</span></div>
          <div class="search-result-meta"><span class="search-cat-badge">机场服务</span> <span style="font-size:11px;color:#64748b;">${escapeHtml(p.tag)}</span></div>
          <div class="search-result-snippet">${escapeHtml(p.summary)}</div>
        </a>
      `;
    });

    // Render Pages & Tutorials
    matchedPages.slice(0, 5).forEach(res => {
      const page = res.item;
      html += `
        <a href="${page.permalink}" class="search-result-item">
          <div class="search-result-title">${escapeHtml(page.title)}</div>
          <div class="search-result-meta"><span class="search-cat-badge">${escapeHtml(page.category)}</span></div>
          <div class="search-result-snippet">${escapeHtml(page.summary)}</div>
        </a>
      `;
    });
  }

  dropdown.innerHTML = html;
  dropdown.classList.add('active');
}

function executeSearch() {
  const input = document.getElementById('searchInput');
  if (!input) return;
  const query = input.value.trim();
  if (!query) {
    alert('请输入搜索关键词');
    return;
  }
  performLiveSearch();
}

function closeSearchDropdown() {
  const dropdown = document.getElementById('searchResultsDropdown');
  if (dropdown) {
    dropdown.classList.remove('active');
  }
}

function escapeHtml(text) {
  if (!text) return '';
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Global click outside search listener
document.addEventListener('click', function(e) {
  const searchBox = document.querySelector('.search-box');
  if (searchBox && !searchBox.contains(e.target)) {
    closeSearchDropdown();
  }
});
