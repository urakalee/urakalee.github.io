#!/usr/bin/env python3
"""
图片压缩脚本
用法: python compress_image.py <文件名>
      文件默认从 ~/Downloads 目录读取
      压缩后保存到原目录，文件名加 _compressed 后缀
"""

import sys
import os
from pathlib import Path
from PIL import Image

MAX_WIDTH = 512
MAX_SIZE_KB = 500
MAX_SIZE_BYTES = MAX_SIZE_KB * 1024


def compress_image(filename: str) -> None:
    downloads = Path.home() / "Downloads"
    input_path = downloads / filename

    if not input_path.exists():
        print(f"错误：找不到文件 {input_path}")
        sys.exit(1)

    img = Image.open(input_path).convert("RGBA")

    # 等比缩放，最大宽度 512
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_size = (MAX_WIDTH, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
        print(f"缩放至 {img.width}x{img.height}")
    else:
        print(f"尺寸无需缩放（{img.width}x{img.height}）")

    stem = input_path.stem
    output_dir = downloads

    # 优先尝试 PNG
    png_path = output_dir / f"{stem}_compressed.png"
    img.save(png_path, format="PNG", optimize=True)
    if png_path.stat().st_size <= MAX_SIZE_BYTES:
        print(f"已保存为 PNG：{png_path}（{png_path.stat().st_size // 1024} KB）")
        return

    # PNG 超限，改用 JPEG（不支持透明通道，转 RGB）
    print(f"PNG 超过 {MAX_SIZE_KB} KB，改用 JPEG 压缩...")
    png_path.unlink()

    rgb_img = img.convert("RGB")
    jpg_path = output_dir / f"{stem}_compressed.jpg"

    quality = 85
    while quality >= 10:
        rgb_img.save(jpg_path, format="JPEG", quality=quality, optimize=True)
        size = jpg_path.stat().st_size
        if size <= MAX_SIZE_BYTES:
            print(f"已保存为 JPEG（quality={quality}）：{jpg_path}（{size // 1024} KB）")
            return
        quality -= 5

    # quality 降到最低仍超限，按当前结果保存并提示
    size = jpg_path.stat().st_size
    print(f"警告：已尽力压缩，最终大小 {size // 1024} KB（仍超过 {MAX_SIZE_KB} KB）")
    print(f"已保存：{jpg_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python compress_image.py <文件名>")
        print("示例: python compress_image.py screenshot.png")
        sys.exit(1)

    compress_image(sys.argv[1])
