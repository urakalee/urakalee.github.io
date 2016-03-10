---
layout: post
title: "Mac Chrome 升级"
date: 2013-12-25 14:05:13 +0800
comments: true
categories: oshack
---
1. 直接升级失败, Error 12
1. 找到[官方解决方案][google]
```sh
~/Library/Google/GoogleSoftwareUpdate/GoogleSoftwareUpdate.bundle/Contents/Resources/GoogleSoftwareUpdateAgent.app/Contents/Resources/install.py --uninstall # Mac 10.9 上无此文件
sudo /Library/Google/GoogleSoftwareUpdate/GoogleSoftwareUpdate.bundle/Contents/Resources/GoogleSoftwareUpdateAgent.app/Contents/Resources/install.py --uninstall
```
* 折腾半天还是不行, 最后从官网下载了最新版的 Chrome, 覆盖安装

 [google]: https://support.google.com/chrome/answer/1367288?hl=zh-Hans "无法在苹果机上更新 Google Chrome 浏览器"

****
 * Update@2016.03.10: 使用 Homebrew Cask
``` sh
brew install caskroom/cask/brew-cask
brew cask search chrome
brew cask install google-chrome
```
