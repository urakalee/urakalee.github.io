---
layout: post
title: "Mac 图标缓存的二三事"
date: 2013-11-25 13:50:02 +0800
comments: true
categories: oshack
---
信息焦虑的第三个症状：随时需要“清理”自己的电脑，虽然完全不知道究竟“清理”了啥。

CleanMyMac 满足了我的这个愿望，但也给我带来了一些麻烦。首当其冲的就是图标缓存问题——每次清理完之后，缓存就会瘫痪，不仅 Launchpad 中有的图标显示不出来，Alfred 也难以幸免，最让人无法接受的是 Finder 会崩溃（Path Finder 貌似无碍）。好在重启之后一切如常。

今天终于不淡定了，因为重启也不能解决问题了！按照 [Apple 社区][community]上给出的解决办法，打开终端，运行命令，图标找回，分组消失。。。
<pre><code>rm ~/Library/Application\ Support/Dock/*.db
killall Dock
</code></pre>

好吧，本来分组这种东西也是我蛋疼搞的，消失就消失吧，有 Alfred 呢。。。

 [community]: https://discussions.apple.com/message/23541241#23541241 "Mavericks Launchpad, missing icons" 
