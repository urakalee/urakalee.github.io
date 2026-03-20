---
title: "通过跳板机 SSH 一键登录"
date: 2026-03-20
draft: false
tags: ["cheatsheet"]
---

两步搞定 SSH 跳板机：配置 `~/.ssh/config`，再分发公钥，之后就能一条命令直连目标机器。

<!--more-->

## 第一步：配置 `~/.ssh/config`

```
# 配置跳板机
Host jump
    HostName <跳板机IP>
    User <跳板机用户名>

# 配置目标机器
Host target
    HostName <目标机IP>
    User <目标机用户名>
    ProxyJump jump
    ForwardAgent yes
```

`ProxyJump` 让 SSH 自动通过跳板机中转；`ForwardAgent yes` 把本地的 SSH Agent 转发过去，这样在跳板机上也能用本地的私钥继续往里跳。

## 第二步：分发公钥

在本地生成密钥（如果还没有的话）：

```bash
ssh-keygen
```

将公钥分别拷贝到跳板机和目标机（首次需要输密码）：

```bash
ssh-copy-id jump
ssh-copy-id target # 经由 config 中配置好的跳板机完成
```

完成后，直接 `ssh target` 一键登录。
