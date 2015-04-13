---
layout: post
title: "Octopress 新手小记"
date: 2013-11-24 21:10:28 +0800
comments: true
categories: selfengine
---
信息焦虑的第二个症状：换过好几个博客，但都因为配置复杂、格式不可控、备份麻烦等原因放弃了。

作为一个程序员，深深地为自己不能迅速地把博客搞定而惭愧。在构思许久之后，终于还是决定先偷懒，把习惯陪养起来再说。Octopress 还是非常符合我审美的，没有太多可配置的东西，所有格式都能自己掌控，更不用说备份——噢！又犯病了。。。

[唐巧的博客][devtang]很容易搜到，但我还是建议第一次搞的同学看一下官网。如果你像我一样在使用最新版的 MacOS，那么 ruby 部分就会简化许多：
``` sh
git clone git://github.com/imathis/octopress.git octopress
cd octopress
sudo gem install bundler
sudo bundle install
rake install
```
<!-- more -->

写作就是 MarkDown 了, 虽然和 wiki 的写法有些差异, 容易记混. 通常我都会使用 Sublime Text + MarkDown 插件, 同时运行 `rake preview` 进行调试(-___-b). Preview 模式下, published:false 的文章会是可见的; 可能由于 bug, 如果你开着 preview 运行 deploy, published:false 的文章也会是可见的... ***`rake deploy` 前务必退出 preview, 并运行 `rake generate`***.

`rake deploy` 之前，要 `git add` 和 `git push origin source`, git 新手（像我）往往都习惯于顺手来个 `git pull`。唔，然后就悲剧了。因为这个时候 git 已经很傻地把你的 source 分枝和远程的 master 分枝关联在一起了，所以 pull 的时候会没头没脑地要 merge 这两个分枝。已经 merge 的怎么回退我就不说了，还没 pull 的，先修改一下 config 文件。
<pre><code>vim .git/config

...
[branch "source"]
    remote = origin
    merge = refs/heads/source
</code></pre>

如果你像我一样，公司用 git，但博客是私人的，那么最好配置一个 local 的 user，这样博客的提交会好看些。知道格式的也可以直接修改 config 文件。
``` sh
git config user.name <your-name>
git config user.email <your-email>
```

最后，在多台机器上部署。同样要先搞定 ruby 部分，但不需要运行 `rake install` 和 `rake setup_github_pages` 了。
``` sh
git clone <your-blog-repo>
cd <your-blog-name>.github.io
checkout source
git branch -D master # 不 checkout master
git clone <your-blog-repo> _deploy # 模拟 rake setup_github_pages
```

### 更多设置
 * 设置导航栏和增加文章分类的方法可以参考[冯威的博客][fengwei]
   * 文中 category_list.html 的代码有点小问题，应该是 <code>{&#37; category_list &#37;}</code>，估计是作者没有找到转义的方法，我用的是 ```<code>{&#37; category_list &#37;}</code>```
 * 输入和显示表格的方法可以参考 [@samwize 的博客][samwize]
 * 增加 disqus 的评论只需要申请 disqus 账号并修改 _config.yml @2013.12.14

 [devtang]: http://blog.devtang.com/blog/2012/02/10/setup-blog-based-on-github/ "象写程序一样写博客：搭建基于github的博客"
 [fengwei]: http://oec2003.github.io/blog/2013/06/26/octopress-blog-setting/ "Octopress博客设置"
 [samwize]: http://samwize.com/2012/09/24/octopress-table-stylesheet/ "Octopress Table Stylesheet"

****
 * PS: 由于可以使用 `rake preview` 进行调试，master 分枝仅用于发布，所以完全没有必要 checkout master；不 checkout 还避免了 pull 和 push 时会捎上 master 的问题
 * TODO: 更新 Octopress
