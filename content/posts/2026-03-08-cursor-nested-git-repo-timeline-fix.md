---
title: "修复嵌套 Git 仓库 Cursor Timeline 为空问题"
date: 2026-03-08
draft: false
tags: ["ai-tool"]
---

主目录是 Git 仓库，子目录也是 Git 仓库时，用 Cursor 查看子目录文件的 Git 历史时，Timeline 面板显示为空。

<!--more-->

## 配置修改

`Cmd + ,` 打开设置，修改两项：

- `git.autoRepositoryDetection` → `true`
- `git.repositoryScanMaxDepth` → `3`

> [!NOTE]
> 不确定是否需要同时修改 User 和 Workspace 级别的配置，保险起见两个我都改了。

## 生效

`Cmd + Shift + P` → `Developer: Reload Window` 即可。

> [!NOTE]
> 我用的方式是完全关闭 Cursor 再打开，Gemini 说这个也可以。