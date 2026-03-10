---
title: "自定义 OpenClaw 定时任务的模型"
date: 2026-03-10
draft: false
tags: ["openclaw"]
---

不是所有定时任务都需要高级模型，改个配置就能省不少费用。

<!--more-->

手改 `~/.openclaw/cron/jobs.json` 实现配置：

```json
"payload": {
    "kind": "agentTurn",
    "message": "{定时任务内容}",
    "model": "google/gemini-3.1-flash-lite-preview",
    "thinking": "low"
},
```

另外，大部分定时任务可以选择 isolate 模式，这样请求时就不带主 agent 的上下文（减少 token）：

```json
"sessionTarget": "isolated",
```

在 web 管理页面上也可以修改模型和 sessionTarget，但列表里只有官方支持的模型可选，像 `gemini-3.1-flash-lite-preview` 就只能手改了。
