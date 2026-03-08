---
title: "避坑指南：Parallels 虚拟机 Chrome 连不上内网代理"
date: 2026-03-08
draft: false
tags: ["openclaw"]
---

我的 OpenClaw 是部署在 Parallels 虚拟机里的，最近想让它通过浏览器帮我收集一些信息，结果遇到了一个非常“玄学”的问题：明明能 ping 通内网代理，但 Chrome 插件（ZeroOmega）死活连不上。和 Gemini 联手排查了半天，终于搞定了。

<!--more-->

## 必杀技：关闭 Chrome 的"安全 DNS" (DoH)

**操作步骤：**

1. 打开 Chrome，访问 `chrome://settings/security`
2. 找到 **"使用安全 DNS" (Use secure DNS)** 选项
3. 关掉

## 其它检查

- **Ping：** 先确保能 ping 通
- **Allow LAN：** 内网代理软件必须"允许局域网连接"
- **Bridged Network：** 使用"桥接模式"，手动指定正确的网卡

断断续续折腾了好几天，终于搞定了，应该早问 AI。
