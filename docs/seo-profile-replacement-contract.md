# SEO Profile 整体替换契约 (seo-profile-replacement-contract.md)

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
