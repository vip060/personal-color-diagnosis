# 🎨 Personal Color Diagnosis · 个人色彩诊断

<div align="center">

**🧬 一张自拍，解锁你的天命色盘**

[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-8A2BE2?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMiA3bDEwIDUgMTAtNS0xMC01ek0yIDE3bDEwIDUgMTAtNU0yIDEybDEwIDUgMTAtNSIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+)](https://github.com/vip060/personal-color-diagnosis)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![12 Types](https://img.shields.io/badge/12_Types-Complete-FF6B9D?style=flat-square)](references/color-palettes.md)
[![96 Colors](https://img.shields.io/badge/96_Colors-HEX_Coded-FFB800?style=flat-square)](references/color-palettes.md)

</div>

---

## ✨ 这什么神仙 Skill？

> **还在纠结买什么颜色的衣服？口红试了八百支不知道哪支显白？衣柜全是黑白灰因为"安全"？**

别闹了。

这个 Skill 用 **AI + 计算机视觉** 把你的肤色拆成四个维度，精准定位你的 **Personal Color 12 型**，然后甩给你一份：
- 🎯 **属于你的天命色盘**（连 HEX 色码都标好了）
- 👔 **从衣柜到化妆台的全套穿搭指南**
- 💎 **该戴金还是戴银——再也不用猜了**

韩国人做一次个人色彩诊断要花 **30 万韩元（约 1,500 RMB）**。你只需要一张素颜自拍，剩下的事交给 AI。

---

## 🔬 怎么做到的？

```
📸 素颜自拍
    │
    ▼
┌─────────────────────────────┐
│  🧬 四维肤色分析             │
│  ┌───────────────────────┐  │
│  │ 🌡️ 色温  → 1.33 (暖调) │  │
│  │ ☀️ 明度  → 150 (中偏浅)│  │
│  │ 🎯 饱和度 → 0.25 (鲜艳) │  │
│  │ ⚡ 对比度 → 0.79 (高)   │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  🎯 12 型判定引擎            │
│  暖净型 / Spring Clear       │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  📋 智能报告生成              │
│  ✅ 8 个天命色 + HEX 码      │
│  ❌ 5 个避雷色               │
│  👔 穿搭 / 💄 妆容 /         │
│  💇 发色 / 💎 饰品           │
└─────────────────────────────┘
```

不是随便猜的——每个脸颊区域采样上万像素，**R/B 比值量化色温**，**LAB 空间计算对比度**。比韩国美容室的分析还细。

---

## 🗂️ 里面有什么？

```
personal-color-diagnosis/
│
├── 🧠 SKILL.md                          # 核心大脑：完整的五步诊断工作流
│
├── 📚 references/
│   ├── color-palettes.md                # 🔥 96 种颜色 + HEX 码，12 型全覆盖
│   └── style-guide.md                   # 👗 302 行：穿搭·妆容·发色·饰品
│                                          #    每型都是独立完整指南
│
├── 📋 templates/
│   └── report-template.md               # 诊断报告 Markdown 模板
│
├── 🐍 scripts/
│   └── skin_analyze.py                  # 🚀 Python 独立分析脚本
│                                          #    `python skin_analyze.py 照片.jpg`
│
└── 📖 README.md                         # 就你在看的这个
```

> 💡 `skin_analyze.py` 可以**独立运行**，不需要 Hermes！装个 `pip install pillow numpy` 就行。

---

## 🎯 12 型完整体系

| 调性 | 别称 | 类型 | 英文名 | 一句话 |
|:---:|------|------|--------|--------|
| 🔥 | 春 | **暖浅型** | Spring Light | 早春阳光，温柔不刺眼 |
| 🔥 | 春 | **暖艳型** | Spring Bright | 春天花园，明亮活泼 |
| 🔥 | 春 | **暖净型** | Spring Clear | 水晶般清澈明亮 ✨ |
| 🍂 | 秋 | **暖柔型** | Autumn Soft | 秋叶飘落，温暖沉稳 |
| 🍂 | 秋 | **暖深型** | Autumn Deep | 深秋森林，浓郁饱满 |
| 🍂 | 秋 | **暖浊型** | Autumn Muted | 古老油画，温润典雅 |
| ❄️ | 夏 | **冷浅型** | Summer Light | 夏日晨雾，朦胧清凉 |
| ❄️ | 夏 | **冷柔型** | Summer Soft | 盛夏绽放，清凉明丽 |
| ❄️ | 夏 | **冷酷型** | Summer Cool | 北极光般冷艳通透 |
| 💎 | 冬 | **冷艳型** | Winter Bright | 冬夜霓虹，鲜明有力 |
| 💎 | 冬 | **冷深型** | Winter Deep | 冬夜星空，深邃内敛 |
| 💎 | 冬 | **冷净型** | Winter Clear | 极致黑白，纯粹对比 |

> 每一型都有完整的 **8 个天命色 + HEX**、**4 个避雷色**、**穿搭/妆容/发色/饰品详细建议**。不是那种"你适合暖色系"的敷衍回答，是**具体到色号的精准推荐**。

---

## 🚀 三秒上手

### 方式一：Hermes Agent 一键安装

```bash
# 克隆
git clone https://github.com/vip060/personal-color-diagnosis.git

# 丢进 skills 目录
cp -r personal-color-diagnosis ~/.hermes/skills/creative/

# 验证一下
hermes skill view personal-color-diagnosis
```

然后对 AI 说 **"帮我测一下肤色"**，发张自拍，完事。

### 方式二：独立 Python 脚本

```bash
pip install pillow numpy
python scripts/skin_analyze.py 你的自拍.jpg
```

输出示例：
```
🎯 判定: 暖净型 (Spring Clear)
  R/B 比 (暖度): 1.325
  饱和度:        0.2451
  明度:          150
  对比度:        0.794
```

### 触发词

以下任意一句都能唤醒它：

| 中文 | English |
|------|---------|
| "个人色彩诊断" | "personal color" |
| "我是冷皮还是暖皮" | "what's my season" |
| "帮我测一下肤色" | "analyze my skin tone" |
| "四季色彩" | "color analysis" |

---

## 🆚 为什么比 YouMind 版强？

| 维度 | YouMind 官方版 | ☄️ 这个 |
|:---|:---:|:---:|
| **Prompt 可见？** | ❌ 私有黑盒 | ✅ 完全开源 |
| **分析原理** | 图片模型「猜测」 | 像素级 Python 色彩分析 |
| **色板数据** | 无 | 96 色 + HEX 精确色码 |
| **风格指南** | 无 | 302 行 12 型全覆盖 |
| **平台绑定** | 必须用 YouMind | 随便哪里都能跑 |
| **独立运行** | 不可能 | `python skin_analyze.py` |
| **你能改吗？** | 不行 | 随便 fork 随便改 |

> YouMind 版 Fork 1,069 次还什么都看不到。这个——**代码全在这儿，颜色都给你标好了**。

---

## 🌟 为什么你需要它？

- 👔 **买衣服**：不再纠结「这颜色显白吗」——看报告就完了
- 💄 **挑口红**：珊瑚橘还是玫红？色温说了算
- 💇 **染发**：亚麻灰还是暖棕？明度和饱和度决定一切
- 💍 **选首饰**：黄金还是白金？静脉颜色骗不了人
- 🎨 **做设计**：96 个 HEX 色码直接拿来用

> 韩国一次色彩诊断 30 万韩元。这玩意儿免费，还更准——因为算法不会累。

---

## 🤝 贡献

Fork → 改 → PR。或者直接提 Issue。

特别欢迎：
- 🎨 补充更多颜色搭配方案
- 📊 优化肤色分析算法
- 🌍 翻译成其他语言

---

## 📄 License

MIT — 随便用，随便改，顺便给个 ⭐ 就更好了。

---

<div align="center">

**🧬 一张自拍，解锁你的天命色盘**

⭐ [Star on GitHub](https://github.com/vip060/personal-color-diagnosis) · 🍴 [Fork it](https://github.com/vip060/personal-color-diagnosis/fork)

</div>
---

## 🤝 联动 `outfit-upgrade`

两个 skill 串联，打造完整形象升级流水线：

```
📸 用户发照片
    │
    ├─→ personal-color-diagnosis → 🎨 天命色盘
    │       "你是 Spring Clear 暖净型"
    │
    └─→ outfit-upgrade → 👔 三场景穿搭报告
            "配色已从你的色盘中自动选取"
```

> 💡 [outfit-upgrade →](https://github.com/vip060/outfit-upgrade) TikTok 竖屏衣品改造报告生成器
