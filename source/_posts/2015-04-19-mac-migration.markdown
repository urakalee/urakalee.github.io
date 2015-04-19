---
layout: post
title: "Mac 重装/数据迁移"
date: 2015-04-19 10:14:44 +0800
comments: true
categories: oshack
---
* transfer 出来的 Mac 系统, 有一些地方需要重新设置
  1. 关闭 guest: Pref - User - Unlock - Guest User - Uncheck
  1. 修改机器名1: Pref - Share - Computer Name
  1. 修改机器名2: `sudo scutil --set HostName <name>`
  1. 修改 Terminal 提示符
```sh
vim ~/.bash_profile

export PS1="[\u@\h \W]\$ " # 增加这一行

source ~/.bash_profile
```
* 开启 TRIM
  * 方法 1: 使用 [Terminal 命令][weiphone]
  * 方法 2: 使用 [Chameleon SSD Optimizer][chameleon]
    * 我是在使用过方法 1 之后才找到方法 2 的, 不过以后再有需要会先用方法 2
* 检查安装的软件
  * ~~Dropbox~~
  * ~~CloudStation~~ -> 家用 ONLY
  * ~~GoAgentX: 升个级吧~~ -> 买个 VPN 吧
  * Alfred: [设置 Spotlight 索引][spotlight], 重建 Alfred 索引
* 配置 hosts/ssh-config/known_hosts/vimrc/gitconfig/SwitchySharp
* 各种清理
  * 清理个人的 Login Items: Pref - User - Login Items
  * 使用 CleanMyMac 清理全局的 Login Items
  * 使用 CleanMyMac 删除没用的软件
  * 到 `~/` 下删除没用的目录和没用软件的残留
  * 到 `~/Library/Application Support/` 和 `Preferences`, `Caches`, `Logs` 目录下删除没用软件的残留
* 运行 Disk Utility
* 修复 HomeBrew
  * 按照 `brew doctor` 的提示做即可

 [spotlight]: /blog/2013/11/25/confused-alfred-and-spotlight/ "Alfred & Spotlight"
 [weiphone]: http://bbs.weiphone.com/read-htm-tid-7173782.html "[求助] 10.9 怎么开启TRIM"
 [chameleon]: http://chameleon.alessandroboschini.it/index.php "Chameleon SSD Optimizer"

****
Update@2015.04.13: 修改"检查安装的软件"部分
