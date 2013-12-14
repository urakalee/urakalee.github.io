---
layout: post
title: "SSH 配置解析"
date: 2013-12-14 14:09:00 +0800
comments: true
categories: teamtoy
---
* 使用 git (ssh 模式)和 scp 等 ssh 相关命令时也遵从该配置
<pre><code>vim ~/.ssh/config

Host github.com
    User git # 使用 github 时的默认用户名
    IdentityFile ~/.ssh/id_rsa.github # 为不同的 host 配置不同的 key

Host gerrit.work-host.com
    User work-name # 使用公司 gerrit 服务时的默认用户名
    IdentityFile ~/.ssh/id_rsa.work-host # 为不同的 host 配置不同的 key

# ssh mctx => ssh urakalee@192.168.1.1
# 不需要配系统 host, 不过除 ssh 相关命令外, 该 host 不起作用
Host mctx
    HostName 192.168.1.1
    User urakalee # ssh 到私人服务器时的默认用户名
    IdentityFile ~/.ssh/id_rsa.urakalee # 为不同的 host 配置不同的 key
</code></pre>

<pre><code>vim ~/.ssh/known_hosts

# 通过用户认证的主机列表, 一行一个
<主机名>,ip1[,ip2]...[,ipN] ssh-<加密方式> <主机指纹>
</code></pre>

<pre><code>vim ~/.ssh/authorized_keys

# 设置本机允许那些用户登录, 一行一个
ssh-<加密方式> <公钥> [user@host]
</code></pre>
