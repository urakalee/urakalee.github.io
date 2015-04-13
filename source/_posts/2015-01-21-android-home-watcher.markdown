---
layout: post
title: "Android: 捕获 Home 键"
date: 2015-01-21 17:12:00 +0800
comments: true
categories: android
---
在[猿题库][yuantiku]工作一年多, 新功能做了不少, bug 也改了许多, 近期开始做更多的优化工作. 本篇博客的内容来自"错题锁屏"功能的优化.

我们 2014 年 9 月开始做"错题锁屏"功能, 希望增加曝光, 提高存留. 开发该功能的同学现在已经结束实习出国工作了, 但做这个功能的时候我就知道坑很多, 而且上线前为了避免风险留了一些坑没改. 上线后, 发现该功能比较受欢迎, 所以又有了多次拉锯式的修改, 不过对于锁屏本身的坑并没有填.

关于如何防止锁屏进程被杀, 我可能会开另外一篇博客来说明, 不过其实你也可以逆向工程我们的 apk 自己去看. 还有就是错题锁屏变成一个独立进程之后, 进程间共享数据变成了一个新的大坑...

由于我们一开始就不想把错题锁屏做得很暴力, 所以虽然禁用了 Back 键(按 Back 键不能退出锁屏), 却还是保留了按 Home 键退出的可能性, 避免用户因为答不对题而无法解锁(我们可能低估用户了).

于是有一个问题, 按 Home 键退出锁屏之后, 用户可以在"最近使用"中重新打开锁屏界面, 而我们只想让用户在"最近使用"中看到猿题库本身. 我开始寻找如何在用户按 Home 键时让锁屏界面自己把自己 finish 掉的方法.

首先查到的方法是 onUserLeaveHint, 按 Home 键时确实会调用这个函数. 不过遇到的问题也很坑: 当有其它锁屏, 甚至 QQ 弹窗(实际上也是用类似锁屏的方法实现的)出现时, 我们的锁屏可能被挤掉(onUserLeaveHint 被调用).

然后开始寻找能够捕获 Home 键的方法:

1. [override onKeyDown][detect-home-button-press-in-android], 不过 no longer works as of 4.0, [这里][override-hardware-home-button-android-listen-home-button-click-android]给出了完整的代码
1. [这篇 vote 比较少的文章][home-button-listener]其实离最终答案很近了, 不过因为 vote 太少, 我一开始没有相信它...
1. 中文网络上看起来有更多人搞过这个问题: 文章 [A][art-a] [B][art-b] [C][art-c] 大同小异, [这里][art-detail]分析得更详细一些. 其中 [B][art-b] 的代码更漂亮一些, 我试过可行 (Android4.+)

可行之后, 我发现又掉到了坑里: **即使 finish 掉了, 用户还是可以在最近使用中重新打开锁屏界面!!!**

最后, 我解决这个问题的方法与捕获 Home 键没有任何关系, 只能把锁屏的 activity 设为最近不可见 (excludeFromRecents="true"). 这充分体现了坚持做一个 SB 程序员的必要性: 过于相信一知半解的既有信息是错误的根源.

 [yuantiku]: http://yuantiku.com
 [detect-home-button-press-in-android]: http://stackoverflow.com/questions/8881951/detect-home-button-press-in-android
 [override-hardware-home-button-android-listen-home-button-click-android]: http://www.coderzheaven.com/2012/06/02/override-hardware-home-button-android-listen-home-button-click-android/
 [home-button-listener]: http://stackoverflow.com/questions/5907102/home-button-listener
 [art-a]: http://blog.csdn.net/way_ping_li/article/details/8953622
 [art-b]: http://blog.csdn.net/watt520/article/details/18959897
 [art-c]: http://blog.csdn.net/ekeuy/article/details/39400939
 [art-detail]: http://862123204-qq-com.iteye.com/blog/1888532
