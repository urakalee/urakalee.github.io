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
``` sh
find . -name "*.xyz"
find . -name "*abc*" -delete
```

### wc
``` sh
wc -l find -name "*.java" # 统计 java 代码行数
```

### 权限
```sh
chmod u+x <file> # 设为可执行文件
chown <name> <file>
chown -R <name> <dir>
chgrp ... # 格式同 chown
```

## 系统工具

### ssh
* ssh-add -D删除所有记住的key
  * 解决 Mac 下所有使用过的 key 都会被记住，删除 key 文件没用的问题

### 链接库
* 查看链接库是否缺失: `ldd <可执行文件>`
* 修改系统加载库
``` sh
vim /etc/ld.so.conf
/sbin/ldconfig
```
