---
layout: post
title: "Octopress 新手小记"
date: 2013-11-24 21:10:28 +0800
comments: true
categories: selfengine
---
信息焦虑的第二个症状：换过好几个博客，但都因为配置复杂、格式不可控、备份麻烦等原因放弃了。

作为一个程序员，深深地为自己不能迅速地把博客搞定而惭愧。在构思许久之后，终于还是决定先偷懒，把习惯陪养起来再说。Octopress 还是非常符合我审美的，没有太多可配置的东西，所有格式都能自己掌控，更不用说备份——噢！又犯病了。。。

[唐大牛的博客][devtang]很容易搜到，但我还是建议第一次搞的同学看一下官网。如果你像我一样在使用最新版的 MacOS，那么 ruby 部分就会简化许多：
<pre><code>git clone git://github.com/imathis/octopress.git octopress 
cd octopress
sudo gem install bundler
sudo bundle install
rake install
</code></pre>

 [devtang]: http://beyondvincent.com/blog/2013/08/03/108-creating-a-github-blog-using-octopress/ "利用Octopress搭建一个Github博客"
