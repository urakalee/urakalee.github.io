---
layout: post
title: "Linux 手册"
date: 2013-12-08 12:13:45 +0800
comments: true
categories: cheatsheet
published: false
---
## 常用命令

### find
* find -name "*.xyz"

### wc
* wc -l find -name "*.java"

## 系统工具

### ssh
* ssh-add -D删除所有记住的key
  * 解决mac下所有使用过的key都被记住，即使删除key也不起作用的问题

### 链接库
* 查看链接库是否缺失: ```ldd <可执行文件>```
* 修改系统加载库
``` sh
vim /etc/ld.so.conf
/sbin/ldconfig
```
