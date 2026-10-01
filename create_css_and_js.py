import os

css_content = """/* CSS Stylesheet for tzyouxuan.xyz */
:root {
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --accent-color: #f59e0b;
  --accent-hover: #d97706;
  --tg-color: #229ed9;
  --tg-hover: #1c8adb;
  --bg-color: #f8fafc;
  --card-bg: #ffffff;
  --text-main: #0f172a;
  --text-muted: #475569;
  --border-color: #e2e8f0;
  --radius: 12px;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  background-color: var(--bg-color);
  color: var(--text-main);
  line-height: 1.7;
}

a {
  color: var(--primary-color);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
  border-bottom: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  font-size: 28px;
}

.logo-text-wrap {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-size: 20px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.2;
}

.brand-domain {
  font-size: 12px;
  color: var(--primary-color);
  font-weight: 600;
}

.main-nav .nav-list {
  display: flex;
  list-style: none;
  gap: 20px;
}

.nav-item {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-muted);
  transition: color 0.2s;
}

.nav-item:hover {
  color: var(--primary-color);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-box {
  display: flex;
  align-items: center;
  background-color: #f1f5f9;
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 4px 8px;
}

.search-box input {
  border: none;
  background: transparent;
  padding: 6px 10px;
  font-size: 13px;
  outline: none;
  width: 160px;
}

.search-btn {
  border: none;
  background: var(--primary-color);
  color: #fff;
  padding: 6px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: bold;
  cursor: pointer;
}

.tg-btn {
  background-color: var(--tg-color);
  color: #ffffff;
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: background-color 0.2s;
}

.tg-btn:hover {
  background-color: var(--tg-hover);
  text-decoration: none;
}

.mobile-menu-toggle {
  display: none;
  font-size: 24px;
  background: none;
  border: none;
  cursor: pointer;
}

.mobile-nav-modal {
  display: none;
  position: absolute;
  top: 70px;
  left: 0;
  width: 100%;
  background: #ffffff;
  border-bottom: 1px solid var(--border-color);
  padding: 20px;
  box-shadow: var(--shadow-md);
}

.mobile-nav-modal.active {
  display: block;
}

.mobile-nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: #ffffff;
  padding: 60px 0;
  text-align: center;
}

.hero-badge {
  display: inline-block;
  background: rgba(37, 99, 235, 0.2);
  border: 1px solid var(--primary-color);
  color: #60a5fa;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 16px;
}

.hero-title {
  font-size: 32px;
  font-weight: 900;
  line-height: 1.3;
  margin-bottom: 16px;
  color: #ffffff;
}

.hero-desc {
  max-width: 850px;
  margin: 0 auto 28px;
  font-size: 16px;
  color: #94a3b8;
  line-height: 1.8;
}

.hero-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  flex-wrap: wrap;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 22px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-primary {
  background-color: var(--primary-color);
  color: #ffffff;
}

.btn-primary:hover {
  background-color: var(--primary-hover);
  text-decoration: none;
}

.btn-secondary {
  background-color: #334155;
  color: #ffffff;
}

.btn-secondary:hover {
  background-color: #475569;
  text-decoration: none;
}

.btn-tg {
  background-color: var(--tg-color);
  color: #ffffff;
}

.btn-tg:hover {
  background-color: var(--tg-hover);
  text-decoration: none;
}

.btn-register {
  background-color: #10b981;
  color: #ffffff;
  width: 100%;
  padding: 12px 18px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: bold;
}

.btn-register:hover {
  background-color: #059669;
  text-decoration: none;
}

.btn-detail {
  background-color: #f1f5f9;
  color: var(--text-main);
  width: 100%;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;

}

.btn-detail:hover {
  background-color: #e2e8f0;
  text-decoration: none;
}

.btn-sm {
  padding: 6px 12px;
  font-size: 13px;
}

/* Sections */
.section {
  padding: 50px 0;
}

.bg-light {
  background-color: #f1f5f9;
}

.section-header {
  margin-bottom: 35px;
}

.section-title {
  font-size: 26px;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 8px;
}

.section-sub {
  font-size: 15px;
  color: var(--text-muted);
}

.text-center {
  text-align: center;
}

/* Provider Grid */
.provider-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 20px;
}

.primary-grid {
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
}

.provider-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 24px;
  position: relative;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s, box-shadow 0.2s;
}

.provider-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.rank-tag {
  position: absolute;
  top: -12px;
  left: 20px;
  background: #1e293b;
  color: #ffffff;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
}

.rank-1 .rank-tag { background: #d97706; }
.rank-2 .rank-tag { background: #2563eb; }
.rank-3 .rank-tag { background: #059669; }
.rank-4 .rank-tag { background: #7c3aed; }

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 8px;
  margin-bottom: 12px;
}

.provider-name {
  font-size: 20px;
  font-weight: 800;
  color: var(--text-main);
}

.price-badge {
  background: #fef3c7;
  color: #92400e;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 13px;
  font-weight: bold;
}

.provider-summary {
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 16px;
  line-height: 1.6;
}

.provider-features {
  list-style: none;
  font-size: 13px;
  color: #334155;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.provider-features li {
  line-height: 1.5;
}

.card-actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: auto;
}

/* Mini Card */
.mini-card {
  padding: 16px;
}

.mini-rank {
  font-size: 16px;
  font-weight: 900;
  color: var(--primary-color);
  margin-bottom: 4px;
}

.mini-price {
  font-size: 13px;
  font-weight: bold;
  color: #d97706;
  margin: 8px 0;
}

/* Article Cards */
.article-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.article-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s;
}

.article-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.article-body {
  padding: 20px;
}

.article-cat {
  display: inline-block;
  background: #e0f2fe;
  color: #0369a1;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 10px;
}

.article-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 10px;
  line-height: 1.4;
}

.article-title a {
  color: var(--text-main);
}

.article-title a:hover {
  color: var(--primary-color);
}

.article-excerpt {
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 15px;
  line-height: 1.6;
}

.article-meta {
  font-size: 12px;
  color: #94a3b8;
  display: flex;
  justify-content: space-between;
}

/* Article Detail */
.page-layout {
  padding-top: 30px;
  padding-bottom: 60px;
}

.article-detail {
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 35px;
  box-shadow: var(--shadow-sm);
}

.breadcrumb {
  font-size: 13px;
  color: #64748b;
  margin-bottom: 15px;
}

.post-title {
  font-size: 28px;
  font-weight: 900;
  line-height: 1.3;
  margin-bottom: 15px;
}

.post-meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  font-size: 13px;
  color: #64748b;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 25px;
}

.tag-pill {
  background: #f1f5f9;
  padding: 2px 8px;
  border-radius: 10px;
}

/* Injected Recommendation Box */
.injected-recommendation-box {
  background: linear-gradient(135deg, #eff6ff 0%, #f0f9ff 100%);
  border: 2px solid #bfdbfe;
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 35px;
}

.box-title {
  font-size: 18px;
  font-weight: 800;
  color: #1e40af;
  margin-bottom: 6px;
}

.box-desc {
  font-size: 14px;
  color: #3b82f6;
  margin-bottom: 16px;
}

.injected-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 15px;
}

.inj-card {
  background: #ffffff;
  border: 1px solid #dbeafe;
  border-radius: 8px;
  padding: 14px;
  box-shadow: var(--shadow-sm);
}

.inj-badge {
  font-size: 11px;
  font-weight: bold;
  background: #dbeafe;
  color: #1e40af;
  padding: 2px 6px;
  border-radius: 6px;
}

.inj-card h4 {
  font-size: 16px;
  margin: 6px 0;
  color: var(--text-main);
}

.inj-card p {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 10px;
  line-height: 1.4;
}

/* Content Styling */
.post-content h2 {
  font-size: 22px;
  font-weight: 800;
  margin: 30px 0 15px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--primary-color);
}

.post-content h3 {
  font-size: 18px;
  font-weight: 700;
  margin: 22px 0 12px;
}

.post-content p {
  margin-bottom: 18px;
  font-size: 16px;
  color: #334155;
  line-height: 1.8;
}

.post-content ul, .post-content ol {
  margin: 0 0 20px 25px;
  color: #334155;
}

.post-content li {
  margin-bottom: 8px;
}

.post-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
}

.post-content th, .post-content td {
  border: 1px solid var(--border-color);
  padding: 12px;
  text-align: left;
  font-size: 14px;
}

.post-content th {
  background: #f8fafc;
  font-weight: bold;
}

/* FAQ Styles */
.faq-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.faq-item-card {
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow-sm);
}

.faq-question {
  font-size: 18px;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 12px;
}

.q-num {
  color: var(--primary-color);
}

.faq-answer {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 15px;
}

.faq-cta-bar {
  background: #f8fafc;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 13px;
  color: #64748b;
}

.btn-link {
  font-weight: bold;
  color: var(--primary-color);
}

/* Footer */
.site-footer {
  background: #0f172a;
  color: #94a3b8;
  padding: 50px 0 25px;
  margin-top: 60px;
}

.footer-inner {
  display: grid;
  grid-template-columns: 2fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-title {
  color: #ffffff;
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 12px;
}

.footer-desc {
  font-size: 13px;
  line-height: 1.7;
  margin-bottom: 15px;
}

.footer-subtitle {
  color: #ffffff;
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 15px;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 14px;
}

.footer-links a {
  color: #cbd5e1;
}

.footer-links a:hover {
  color: #ffffff;
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.foot-tag {
  background: #1e293b;
  color: #94a3b8;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
}

.footer-bottom {
  border-top: 1px solid #1e293b;
  padding-top: 20px;
  text-align: center;
  font-size: 13px;
}

.disclosure {
  font-size: 12px;
  color: #64748b;
  margin-top: 8px;
}

/* Media Queries */
@media (max-width: 900px) {
  .main-nav { display: none; }
  .mobile-menu-toggle { display: block; }
  .footer-inner { grid-template-columns: 1fr; }
  .hero-title { font-size: 24px; }
  .search-box input { width: 110px; }
}
"""

with open("static/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

js_content = """/* main.js */
function toggleMobileMenu() {
  const modal = document.getElementById('mobileNavModal');
  if (modal) {
    modal.classList.toggle('active');
  }
}

function handleSearch(event) {
  if (event.key === 'Enter') {
    executeSearch();
  }
}

function executeSearch() {
  const input = document.getElementById('searchInput');
  if (!input) return;
  const query = input.value.trim().toLowerCase();
  if (!query) {
    alert('请输入有效的搜索关键词');
    return;
  }
  // Simple in-page search redirect to categories with query
  window.location.href = '/categories/recommend/?q=' + encodeURIComponent(query);
}
"""

with open("static/js/main.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("CSS and JS created successfully.")
