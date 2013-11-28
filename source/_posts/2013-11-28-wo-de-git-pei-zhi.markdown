---
layout: post
title: "我的 Git 配置"
date: 2013-11-28 20:35:55 +0800
comments: true
categories: teamtoy
---
<pre><code>vim ~/.gitconfig

[color]
    ui = true
    diff = true
    status = true
    branch = true
    interactive = true
[alias]
    st = status
    ss = status -s
    ci = commit
    ca = commit --amend
    co = checkout
    ll = log --graph --color --format=format:'%C(bold)%h%C(reset) -%C(bold)%d%C(reset) %C(white)%s%C(reset) %C(bold red)- %an' --abbrev-commit
    ft = fetch
    pl = pull --rebase
    br = branch
    cp = cherry-pick
    mg = merge
    rb = rebase
    dci = dcommit
    sbi = submodule init
    sbu = submodule update
    sbp = submodule foreach git pull
    sbc = submodule foreach git co master
</code></pre>
