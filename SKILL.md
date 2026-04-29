---
name: personal-color-diagnosis
description: >
  个人色彩诊断 — 上传素颜自拍照，AI 完成面部色彩提取 +
  四维分析（色温/明度/饱和度/对比度）→ 判定 Personal Color
  12 型 → 生成诊断报告（SVG 看板）+ AI 穿搭形象建议。
tags: [personal-color, beauty, fashion, image-generation, style, korean]
triggers:
  - 个人色彩诊断
  - 色彩诊断
  - personal color
  - 我是冷皮还是暖皮
  - 看看我适合什么颜色
  - 帮我测一下肤色
  - 四季色彩
  - 12型色彩
---

# 个人色彩诊断 (Personal Color Diagnosis)

从素颜自拍照出发，通过 AI 视觉分析判定用户的 Personal Color 12 型，
生成专业诊断报告和穿搭建议。

---

## 工作流程

### 第 1 步：接收并验证照片

1. 请用户上传一张**素颜正面自拍照**。
2. 确认照片质量要求：
   - 自然光下拍摄（避免强光/暗光）
   - 无美颜滤镜
   - 面部清晰、无遮挡
   - 背景尽量简洁（白墙最佳）
3. 如果用户没有照片或照片不符合要求，友好提示重新上传。

---

### 第 2 步：面部色彩分析

**两种分析方式，按优先级尝试：**

#### 方式 A：vision_analyze（优先，当模型支持多模态时）

调用 `vision_analyze` 对照片进行分析，提取四维特征。

#### 方式 B：Python 像素级分析（备选，当模型不支持视觉时）

当模型不支持多模态（如 DeepSeek V4/V3 等纯文本模型），使用 Pillow + NumPy 进行像素级肤色分析：

```python
from PIL import Image
import numpy as np

img = Image.open(photo_path)
img_np = np.array(img)
h, w = img_np.shape[:2]

def analyze_skin(region, name):
    r, g, b = region[:,:,0].flatten(), region[:,:,1].flatten(), region[:,:,2].flatten()
    lum = 0.299*r + 0.587*g + 0.114*b
    mask = (lum > 50) & (lum < 235)  # 排除过曝/过暗像素
    r, g, b = r[mask], g[mask], b[mask]
    
    avg_r, avg_g, avg_b = np.mean(r), np.mean(g), np.mean(b)
    r_b_ratio = avg_r / max(avg_b, 0.1)  # 核心暖度指标
    max_c, min_c = np.maximum(np.maximum(r, g), b), np.minimum(np.minimum(r, g), b)
    sat = np.mean((max_c - min_c) / np.maximum(max_c, 1))
    bright = np.mean(max_c)
    return {'r_b_ratio': r_b_ratio, 'sat': sat, 'bright': bright}
```

**关键采样区域：** 取脸颊中部（避开额头镜框阴影、鼻梁高光、下巴过曝），多个采样点求平均。左右脸分别采样以平衡光照不均。

**判定阈值：**

| 指标 | 范围 | 判定 |
|------|------|------|
| R/B 比 | >1.15 / 1.08-1.15 / 1.03-1.08 / 0.98-1.03 / <0.98 | 明显暖调 / 暖调 / 微暖 / 中性 / 冷调 |
| 饱和度 | >0.25 / 0.15-0.25 / 0.08-0.15 / <0.08 | 鲜艳 / 中等偏艳 / 中等 / 柔和 |
| 明度 | >180 / 150-180 / 120-150 / <120 | 浅色 / 中等偏浅 / 中等 / 深色 |
| 对比度 | 肤色亮度与眉毛/发色亮度的归一化差 | >0.3 高 / 0.15-0.3 中 / <0.15 低 |

**常见陷阱：**
- 额头中央易受镜框/帽檐阴影影响，数值异常偏低
- 鼻梁和下巴中心易过曝，R/B 比虚高
- 左右脸光照不均：分别采样能发现差异

---

### 第 3 步：判定 Personal Color 12 型

根据四维分析结果，对照以下 12 型分类表判定用户类型：

```
                      暖调 (Warm)
                        |
          浅色 ──── 柔和 ──── 鲜艳
           |          |          |
    暖浅型(春 Light)  暖柔型(秋 Soft)  暖艳型(春 Bright)
           |          |          |
          深色 ──── 柔和 ──── 鲜艳
           |          |          |
    暖深型(秋 Deep)   暖柔深(秋 Soft Deep)  (已含)

                      冷调 (Cool)
                        |
          浅色 ──── 柔和 ──── 鲜艳
           |          |          |
    冷浅型(夏 Light)  冷柔型(夏 Soft)  冷艳型(冬 Bright)
           |          |          |
          深色 ──── 柔和 ──── 鲜艳
           |          |          |
    冷深型(冬 Deep)   冷柔深(夏 Soft Deep)  (已含)
```

**12 型完整列表：**

| # | 类型 | 英文名 | 别称 | 色温 | 明度 | 饱和度 | 对比度 |
|---|------|--------|------|------|------|--------|--------|
| 1 | 暖浅型 | Spring Light | 春季浅色型 | Warm | Light | Soft | Low |
| 2 | 暖艳型 | Spring Bright | 春季鲜艳型 | Warm | Light | Bright | High |
| 3 | 暖柔型 | Autumn Soft | 秋季柔和型 | Warm | Deep | Soft | Low |
| 4 | 暖深型 | Autumn Deep | 秋季深色型 | Warm | Deep | Bright | High |
| 5 | 冷浅型 | Summer Light | 夏季浅色型 | Cool | Light | Soft | Low |
| 6 | 冷柔型 | Summer Soft | 夏季柔和型 | Cool | Light | Bright | Low |
| 7 | 冷艳型 | Winter Bright | 冬季鲜艳型 | Cool | Deep | Bright | High |
| 8 | 冷深型 | Winter Deep | 冬季深色型 | Cool | Deep | Soft | Low |
| 9 | 暖净型 | Spring Clear | 春季净色型 | Warm | Light | Bright | High |
| 10 | 暖浊型 | Autumn Muted | 秋季浊色型 | Warm | Deep | Soft | Low |
| 11 | 冷酷型 | Summer Cool | 夏季冷色型 | Cool | Light | Bright | High |
| 12 | 冷净型 | Winter Clear | 冬季净色型 | Cool | Deep | Bright | High |

*详细色彩推荐见 `references/color-palettes.md`*

---

### 第 4 步：生成诊断报告

生成两份输出：

#### A. 诊断摘要（markdown 格式，直接回复用户）

```markdown
## 🎨 个人色彩诊断报告

**判定类型：{类型名}（{英文名}）**

### 四维分析结果
- 🌡️ 色温：{暖调/冷调}
- ☀️ 明度：{浅色/深色}
- 🎯 饱和度：{柔和/鲜艳}
- ⚡ 对比度：{高/低}

### 色彩推荐
- ✅ **适合色系**：{列出 5-8 个具体颜色}
- ❌ **避雷色系**：{列出 3-5 个不适合的颜色}

### 穿搭建议
- 👔 **上衣推荐**：...
- 💄 **妆容建议**：...
- 💇 **发色推荐**：...
- 💎 **饰品材质**：...
```

#### B. 视觉诊断看板（使用 image_generate）

调用 `image_generate` 生成两张韩式诊断看板风格图片：

**看板 1 — 色彩诊断卡 (Drape Test)：**
```
Prompt: Korean personal color diagnosis drape test board. Split layout showing the user's face
in the center, surrounded by fabric color swatches. Left side shows "Best Colors" with [适合色系列表],
right side shows "Avoid" with [避雷色系]. Clean white background, elegant Korean aesthetic,
professional beauty consultation style. Chinese + English bilingual labels.
Text on image: "{类型名} / {英文名}" at top center.
```

**看板 2 — 综合形象报告：**
```
Prompt: Korean personal color comprehensive style report board. The user's face as main visual,
with 5 sections around it showing: 1) outfit recommendation 2) hair color swatches
3) makeup palette 4) accessory suggestions (gold vs silver) 5) best color palette swatches.
Professional Korean beauty consultation aesthetic, clean layout, bilingual Chinese/English labels.
Text: "综合形象报告 / Style Report - {类型名}" at top.
```

---

### 第 5 步：穿搭建议细化

根据判定的类型，从 `references/style-guide.md` 中提取对应的详细建议，
以清晰易读的列表形式呈现给用户。

---

## 注意事项

1. **光线判断**：如果照片光线明显偏色（如黄色灯光），应先提醒用户这可能影响判断，建议在自然光下重拍。
2. **不够确定时**：如果四维分析中有维度难以确定，可给出"最可能类型 + 次可能类型"，让用户参考。
3. **中性肤色**：如果色温接近中性，可告知用户属于"中性调"，既可以走暖调路线也可以走冷调路线。
4. **避免绝对化**：强调这只是 AI 辅助参考，最准确的诊断仍需专业色彩顾问面诊。

---

## 引用文件

- `references/color-palettes.md` — 12 型详细色板对照
- `references/style-guide.md` — 各类型穿搭/妆容/发色详细建议
- `templates/report-template.md` — 诊断报告 Markdown 模板

## 依赖

- **Python 包：** `Pillow`、`numpy`（像素级分析备选方案）
- 安装：`python3 -m pip install pillow numpy`