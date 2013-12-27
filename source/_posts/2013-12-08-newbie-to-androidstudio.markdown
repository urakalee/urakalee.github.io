---
layout: post
title: "AndroidStudio 新手小记"
date: 2013-12-08 18:13:10 +0800
comments: true
categories: android
---
## 安装
* 下载安装后, 需要更新到最新版本
  * 不更新可能会遇到一些奇葩问题
  * 如果能直接更新或者翻墙更新的, 请直接更新
  * 不能更新的, 请参考下列文章手动更新
    * http://www.cnsecer.com/842.html
    * http://blog.csdn.net/hil2000/article/details/11395485
    * 关键命令
``` sh
java -classpath AI-<old-edition>-<new-edition>-patch-<os>.jar com.intellij.updater.Runner install .
```

## 新建项目
* 新建一个项目时, 视选择的 SDK 版本, 可能会失败, 原因是包不全
  * 打开 SDK Manager, 勾选需要的包, 点击 Install X package[s]...
  * 注意: 接受协议时可能需要在弹出的对话框里逐个接受, 才能一并下载

## 模拟器
* 以下问题仅限于 windows, Mac 用户可以直接放弃模拟器...
* 运行模拟器失败, 需要把 ```X盘/.android/avd``` 拷贝到 ```C盘/用户目录/.android``` 下
* 运行模拟器慢, 需要下载和安装 intel x86 emulator, 创建 avd 时也要选这个
  * 用 SDK Manager 下载 intel x86 emulator 和对应的 rom
  * 注意: 下载 emulator 后需要安装, 可执行文件在 ```sdk/extras/intel``` 中

## 数据目录
* AndroidStudio 目前还不太稳定, 偶尔折腾, 甚至需要把数据目录清空
* 下面的内容摘自 [Intellij 官网][jetbrain], 只要把路径换成 AndroidStudioPreview 即可
<pre><code>Mac
~/Library/Application Support/IntelliJIdeaXX contains the catalog with plugins.
~/Library/Preferences/IntelliJIdeaXX contains the rest of the configuration settings.
~/Library/Caches/IntelliJIdeaXX contains data caches, logs, local history, etc. These files can be quite significant in size.
9.0+ ~/Library/Logs/IntelliJIdeaXX contains logs
Windows
~\.IntelliJIdeaXX\config that contains user-specific settings.
~\.IntelliJIdeaXX\system that stores IntelliJ IDEA data caches.
</code></pre>

 [jetbrain]: http://www.jetbrains.com/idea/webhelp/project-and-ide-settings.html "Project and IDE Settings"
