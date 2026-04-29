# 🎨 Personal Color Diagnosis (个人色彩诊断)

> A Hermes Agent Skill for AI-powered personal color analysis.

## 功能

上传素颜自拍照 → AI 面部色彩提取 + 四维分析（色温/明度/饱和度/对比度）→ 判定 Personal Color 12 型 → 生成诊断报告 + 穿搭建议。

## 文件结构

```
personal-color-diagnosis/
├── SKILL.md                     # 主 skill 文件（含完整工作流）
├── README.md                    # 本文件
├── references/
│   ├── color-palettes.md        # 12 型 × 每型 8 色 + HEX 色码（96 色）
│   └── style-guide.md           # 穿搭/妆容/发色/饰品详细建议（302 行）
├── templates/
│   └── report-template.md       # 诊断报告 Markdown 模板
└── scripts/
    └── skin_analyze.py          # Python 肤色分析脚本（独立可用）
```

## 安装

```bash
# 1. 克隆仓库
git clone https://github.com/YOUR_USERNAME/personal-color-diagnosis.git

# 2. 复制到 Hermes skills 目录
cp -r personal-color-diagnosis ~/.hermes/skills/creative/

# 3. 验证
hermes skill view personal-color-diagnosis
```

## 触发词

说以下任意一个即可触发：
- "个人色彩诊断" / "色彩诊断"
- "personal color"
- "我是冷皮还是暖皮"
- "帮我测一下肤色"
- "四季色彩" / "12型色彩"

## 12 型色彩体系

| 调性 | 类型 | 英文 |
|------|------|------|
| 暖调 | 暖浅型 / 暖艳型 / 暖柔型 / 暖深型 / 暖净型 / 暖浊型 | Spring Light / Bright · Autumn Soft / Deep · Spring Clear · Autumn Muted |
| 冷调 | 冷浅型 / 冷柔型 / 冷艳型 / 冷深型 / 冷酷型 / 冷净型 | Summer Light / Soft · Winter Bright / Deep · Summer Cool · Winter Clear |

## 对比 YouMind 版本

| 维度 | YouMind | Hermes 版 |
|------|---------|-----------|
| Prompt 可见 | ❌ 私有 | ✅ 完全开源 |
| 分析方式 | 图片生成模型猜测 | Python 色彩分析 + AI 视觉 |
| 色彩数据 | 无 | 96 色 + HEX 码 |
| 风格指南 | 无 | 302 行 12 型全覆盖 |
| 平台依赖 | YouMind 独占 | 完全本地化 |

## License

MIT
