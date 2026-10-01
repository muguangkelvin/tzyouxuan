import os
import json

def make_word_count(text):
    return len(text)

# Provider Data Reference
with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# Helper to generate the Core 4 Provider Block
def get_core4_md():
    return """
## ⚡ 2026年梯子优选四大主推服务评测与官网入口

无论你是需要极速4K追剧、大流量下载，还是AI工具解锁与小白极简配置，以下四大主推服务均经过本站长效实测，稳定性与售后保障极佳：

### 1. 灵动云（全网首推 IPLC顶级专线全能王）
- **核心特点：** IPLC原生专线，晚高峰零丢包不降速，全节点解锁ChatGPT/Claude等AI工具及4K/8K超清视频。
- **适用人群：** AI重度使用者、跨境办公、对延迟和稳定性要求极高的进阶用户。
- **参考价格：** 18.8元/月起（流量100GB/月起）。
- **专属优惠：** 使用优惠码 `ld888` 享8折优惠。
- 官网注册入口：[👉 点击访问灵动云官网注册领优惠](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1) *(rel="sponsored nofollow noopener")*

---

### 2. 暮光网络 (暮光加速 - 晚高峰4K/8K影音首选)
- **核心特点：** BGP中继与原生IP专线，晚高峰带宽跑满百兆，超强流媒体解锁与不限设备数支持。
- **适用人群：** 追剧影音派、大流量下载派、多设备共享家族。
- **参考价格：** 20元/月起（流量120GB/月起）。
- **专属优惠：** 使用优惠码 `mm88` 享8折优惠。
- 官网注册入口：[👉 点击访问暮光网络官网查看套餐](https://varnexa.twilightaff.com/#/?code=KvGly3jY) *(rel="sponsored nofollow noopener")*

---

### 3. 飞猫云（小流量超值年付首选）
- **核心特点：** 超高性价比小流量年付梯子，折合每月仅7元，自研极简客户端小白一键连接。
- **适用人群：** 学生党、轻量备用防失联、小白极简用户。
- **参考价格：** 84元/年起（流量50GB/月）。
- **专属优惠：** 使用优惠码 `flycat888` 季付及以上享8折。
- 官网注册入口：[👉 点击访问飞猫云官网查看低价套餐](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH) *(rel="sponsored nofollow noopener")*

---

### 4. 微风网络 Breezenet（全能客户端兼容口碑之选）
- **核心特点：** 口碑极佳的稳定梯子，完美适配Clash/Sing-box/v2rayN/小火箭等客户端，节点抗封锁力强。
- **适用人群：** 追求长效稳定挂后台、多端协同办公用户。
- **参考价格：** 137元/年起（流量100GB/月）。
- **专属优惠：** 最新优惠以官网结算页为准。
- 官网注册入口：[👉 点击访问微风网络官网立即连接](https://edp01.breezenetaff.com/#/?code=He4n3zxg) *(rel="sponsored nofollow noopener")*
"""

print("Helper script ready.")
