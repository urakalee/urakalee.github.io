---
layout: post
title: "Git 手册"
date: 2013-12-03 18:13:53 +0800
comments: true
categories: manual
---
## 反悔
 * 将两个 commit 合并成一个
``` sh
git reset --soft HEAD^1
git commit --amend
```
