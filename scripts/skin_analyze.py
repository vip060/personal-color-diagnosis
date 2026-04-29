#!/usr/bin/env python3
"""
Personal Color 肤色分析脚本
用法: python3 skin_analyze.py <图片路径>
输出: RGB 色温/明度/饱和度/对比度 + 12 型判定
"""

import sys
import numpy as np
from PIL import Image


def analyze_skin(region, name, verbose=True):
    """分析一个皮肤区域的颜色特征."""
    r = region[:, :, 0].flatten()
    g = region[:, :, 1].flatten()
    b = region[:, :, 2].flatten()
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    mask = (lum > 50) & (lum < 235)
    r, g, b = r[mask], g[mask], b[mask]

    if len(r) < 100:
        return None

    avg_r, avg_g, avg_b = np.mean(r), np.mean(g), np.mean(b)
    r_b_ratio = avg_r / max(avg_b, 0.1)

    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    sat = np.mean((max_c - min_c) / np.maximum(max_c, 1))
    bright = np.mean(max_c)

    if verbose:
        print(f"  {name}: RGB({avg_r:.0f},{avg_g:.0f},{avg_b:.0f}) "
              f"R/B={r_b_ratio:.3f} Sat={sat:.4f} Bright={bright:.0f}")

    return {"r_b_ratio": r_b_ratio, "sat": sat, "bright": bright}


def classify_personal_color(r_b_ratio, saturation, brightness, contrast):
    """根据四维分析结果判定 Personal Color 12 型."""
    # 色温
    if r_b_ratio > 1.12:
        warmth = "warm"
    elif r_b_ratio > 1.03:
        warmth = "neutral_warm"
    elif r_b_ratio > 0.98:
        warmth = "neutral"
    else:
        warmth = "cool"

    # 明度
    if brightness > 180:
        lightness = "light"
    elif brightness > 150:
        lightness = "medium_light"
    elif brightness > 120:
        lightness = "medium"
    else:
        lightness = "deep"

    # 饱和度
    if saturation > 0.22:
        saturation_level = "bright"
    elif saturation > 0.14:
        saturation_level = "medium_bright"
    elif saturation > 0.08:
        saturation_level = "medium"
    else:
        saturation_level = "soft"

    # 匹配 12 型
    mapping = {
        ("warm", "light", "soft"): ("暖浅型", "Spring Light"),
        ("warm", "light", "bright"): ("暖艳型", "Spring Bright"),
        ("warm", "deep", "soft"): ("暖柔型", "Autumn Soft"),
        ("warm", "deep", "bright"): ("暖深型", "Autumn Deep"),
        ("cool", "light", "soft"): ("冷浅型", "Summer Light"),
        ("cool", "light", "bright"): ("冷柔型", "Summer Soft"),
        ("cool", "deep", "bright"): ("冷艳型", "Winter Bright"),
        ("cool", "deep", "soft"): ("冷深型", "Winter Deep"),
    }

    for (w, l, s), (cn, en) in mapping.items():
        if (warmth.startswith(w) and lightness.startswith(l) and
                saturation_level.startswith(s)):
            return cn, en

    # 降级匹配
    if warmth in ("warm", "neutral_warm"):
        return "暖净型", "Spring Clear"
    else:
        return "冷净型", "Winter Clear"


def analyze_image(image_path):
    """分析一张照片的肤色."""
    img = Image.open(image_path)
    img_np = np.array(img)
    h, w = img_np.shape[:2]
    print(f"\n🎨 分析: {image_path} ({w}x{h})")
    print("=" * 50)

    # 采样脸颊区域
    samples = [
        (img_np[int(h * 0.23):int(h * 0.35), int(w * 0.22):int(w * 0.38)], "左颊"),
        (img_np[int(h * 0.23):int(h * 0.35), int(w * 0.62):int(w * 0.78)], "右颊"),
        (img_np[int(h * 0.35):int(h * 0.45), int(w * 0.24):int(w * 0.38)], "左下颊"),
        (img_np[int(h * 0.35):int(h * 0.45), int(w * 0.62):int(w * 0.76)], "右下颊"),
        (img_np[int(h * 0.06):int(h * 0.14), int(w * 0.35):int(w * 0.65)], "额头"),
    ]

    results = []
    for region, name in samples:
        r = analyze_skin(region, name)
        if r:
            results.append(r)

    if not results:
        print("❌ 无法提取有效肤色数据")
        return None

    avg_rb = np.mean([r["r_b_ratio"] for r in results])
    avg_sat = np.mean([r["sat"] for r in results])
    avg_bright = np.mean([r["bright"] for r in results])

    # 对比度
    brow_region = img_np[int(h * 0.15):int(h * 0.21), int(w * 0.25):int(w * 0.75)]
    brow_flat = brow_region.reshape(-1, 3)
    brow_lum = 0.299 * brow_flat[:, 0] + 0.587 * brow_flat[:, 1] + 0.114 * brow_flat[:, 2]
    brow_dark = brow_flat[brow_lum < 80]
    skin_region = img_np[int(h * 0.06):int(h * 0.14), int(w * 0.25):int(w * 0.75)]
    skin_flat = skin_region.reshape(-1, 3)
    skin_lum = 0.299 * skin_flat[:, 0] + 0.587 * skin_flat[:, 1] + 0.114 * skin_flat[:, 2]
    skin_valid = skin_flat[(skin_lum > 60) & (skin_lum < 230)]

    if len(brow_dark) > 0 and len(skin_valid) > 0:
        brow_avg = np.mean(0.299 * brow_dark[:, 0] + 0.587 * brow_dark[:, 1] + 0.114 * brow_dark[:, 2])
        skin_avg = np.mean(0.299 * skin_valid[:, 0] + 0.587 * skin_valid[:, 1] + 0.114 * skin_valid[:, 2])
        contrast = (skin_avg - brow_avg) / max(skin_avg, 1)
    else:
        contrast = 0.3

    cn, en = classify_personal_color(avg_rb, avg_sat, avg_bright, contrast)

    print(f"\n{'=' * 50}")
    print(f"📊 综合结果")
    print(f"  R/B 比 (暖度): {avg_rb:.3f}")
    print(f"  饱和度:        {avg_sat:.4f}")
    print(f"  明度:          {avg_bright:.0f}")
    print(f"  对比度:        {contrast:.3f}")
    print(f"\n🎯 判定: {cn} ({en})")
    print(f"{'=' * 50}")

    return {
        "type_cn": cn,
        "type_en": en,
        "r_b_ratio": avg_rb,
        "saturation": avg_sat,
        "brightness": avg_bright,
        "contrast": contrast,
    }


def main():
    if len(sys.argv) < 2:
        print("用法: python3 skin_analyze.py <图片路径> [图片路径2 ...]")
        print("依赖: pip install pillow numpy")
        sys.exit(1)

    for path in sys.argv[1:]:
        try:
            analyze_image(path)
        except Exception as e:
            print(f"❌ 分析 {path} 时出错: {e}")


if __name__ == "__main__":
    main()