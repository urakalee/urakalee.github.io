---
title: "在 OpenClaw 中使用 Gemini 3.1 Flash Lite"
date: 2026-03-08
draft: false
tags: ["openclaw"]
---

Gemini 3.1 Flash Lite 跑的飞快。

<!--more-->

官方好像还没有支持，或者不想立刻升级的同学，可以手改 `openclaw.json`：

```json
"google": {
    "baseUrl": "https://generativelanguage.googleapis.com/v1beta",
    "api": "google-generative-ai",
    "models": [
        {
            "id": "gemini-3.1-flash-lite-preview",
            "name": "Gemini 3.1 Flash Lite",
            "reasoning": true,
            "input": [
                "text"
            ],
            "contextWindow": 400000,
            "maxTokens": 8192
        }
    ]
}
```

加好之后重启 OpenClaw 就能在模型列表里看到了。
