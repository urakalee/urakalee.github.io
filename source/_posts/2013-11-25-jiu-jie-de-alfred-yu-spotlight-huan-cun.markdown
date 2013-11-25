---
layout: post
title: "纠结的 Alfred 与 Spotlight"
date: 2013-11-25 12:59:02 +0800
comments: true
categories: oshack
---
既然已经不用 Spotlight 了，就打算把它的索引彻底关掉。Google 到若干相关文章，操作也都很简单，[Apple 官网也有][apple]，于是就照着做了。

然后 Alfred 就挂了。新安装的 app 在 Alfred 中找不到，清了 cache 之后更是啥都没有了。

继续搞！没有找到确切的答案，但也能根据现有知识猜个差不离。无非是 Alfred 要调用 Spotlight 的结果，所以 Spotlight 关得不对 Alfred 也就不 work了。

于是还得打开 Spotlight，但是怎么打开还要考虑一下。目标是：Application 索引，而其它不索引。所以先把 HD 加到 privacy 中，再把 HD 下面 Application 之外的都加到 privacy 中；重启；查看一下索引大小，大概 12K；最后把 HD 从 privacy 中移除，DONE！

 [apple]: http://support.apple.com/kb/HT2409?viewlocale=zh_CN "Spotlight：如何重建文件夹或宗卷的索引"

****
 * PS1: Spotlight 索引文件的位置（from [Apple 社区][community]）在磁盘根目录 `/`
 * PS2: 查看其大小需要 root 权限 `:/ $ sudo du -sh .Spotlight-V100`
 * PS3: Path Finder 居然也要调用 Spotlight 的结果
 * PS4: Spotlight 真应该搞白名单机制，黑名单太纠结了

 [community]: https://discussions.apple.com/thread/2429947 "backup Spotlight index file - where is it?"
