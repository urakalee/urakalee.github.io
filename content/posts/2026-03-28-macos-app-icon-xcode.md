---
title: "macOS 应用图标：去背景 + 导入 Xcode"
date: 2026-03-28
draft: false
tags: ["design", "cheatsheet"]
---

两步搞定：用"预览"去掉图标背景，再把透明 PNG 拖进 Xcode 的 AppIcon。

<!--more-->

## 第一步：用"预览"去背景

> 如果图标本身已是透明 PNG，跳过此步。

1. 用**预览**打开图片（需为 PNG 格式）
2. `View > Show Markup Toolbar`，点击**即时 Alpha**（魔法棒图标）
3. 在背景区域点击并缓慢向外拖动，直到红色覆盖全部背景但不碰到主体
4. 松开鼠标，按 `Delete` 删除选区
5. `File > Save` 保存

有多块不连续背景时，重复步骤 3-4。

---

## 第二步：导入 Xcode

### 生成所需尺寸

用以下脚本从一张 1024×1024 PNG 生成全部尺寸：

```bash
#!/bin/bash
SRC=$1
OUT="icons"
mkdir -p "$OUT"

for SIZE in 16 32 64 128 256 512 1024; do
    sips -z $SIZE $SIZE "$SRC" --out "$OUT/icon_${SIZE}.png" > /dev/null
done

echo "Done → $OUT/"
```

用法：`sh gen_icons.sh {path-to-original}.png`

### 在 Xcode 中配置

1. 打开项目，点击左侧 `Assets.xcassets`
2. 选中 `AppIcon`（没有则右键 > macOS > New macOS App Icon）
3. 将 `icons/` 目录里的 PNG 按尺寸拖放到对应槽位
4. 点击项目 > Target > **General** > App Icons and Launch Images，确认 "App Icon Source" 指向 `AppIcon`
