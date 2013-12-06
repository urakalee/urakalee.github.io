---
layout: post
title: "Git 手册"
date: 2013-12-03 18:13:53 +0800
comments: true
categories: cheatsheet
---
## 基本操作
 * 创建版本库: ```git init```
 * 克隆版本库
   * ```git clone /path/to/repo```
   * ```git clone user@host:/path/to/repo```
   * 多版本库: ```git remote add <repo-name> <repo>```
   * 多版本库列表: ```git remote -v```
 * 更新版本库
   * ```git pull <repo-name>```
     * ```git pull --rebase``` 可以避免无意义的 pull-merge, 使版本树尽可能是一条直线
   * ```git fetch <repo-name>``` - ```git pull``` does a ```git fetch``` followed by a ```git merge```
     * 会把 origin 的更新都 fetch 到本地, 包括建立的新分枝, 但不会建立本地分枝
 * 提交到本地
   * stage: ```git add <file/dir>```
   * ```git commit -m "<comment>"```
     * 已经处于版本控制中的文件, 可以使用 ``` git commit -am "<comment>"``` 略过 stage
   * ```git commit --amend```
 * 提交到远程
   * ```git push origin master```
     * ```git push -u <repo-name> master``` 设置 push/pull 时默认使用的 repo-name
   * ```git push <repo-name> <branch>```
     * ```git push <repo-name> <branch>:<remote-branch>``` - 如果本地和远程分枝名字不同
 * 管理远程
   * ```git remote show <repo-name>```
<!-- more -->

## 反悔
 1. revert stage: ```git reset HEAD <file>```
 2. reset working: ```git checkout -- <file>```
 3. restore(1+2): ```git checkout HEAD <file>```
    * 如果改动, add, 再改动, 使用 ```1.``` 不会恢复到第一次改动的结果; 使用 ```2.``` 才行!
 4. checkout 上一个版本, 放在 stage/working 中: ```git checkout HEAD~ <file>```
 5. ```git checkout <rev> <file>```
    * ```<rev>``` 默认为 ```--``` 也就是 stage
    * 如果 ```<rev>``` 是 ```--``` 也就是 stage, 则从 stage checkout 到 working
    * 否则, 从 ```<rev>``` checkout 到 stage 再到 working
 6. ```git reset <rev>```
    * reset 把 HEAD 指向 ```<rev>```, 如果 ```--hard```, 那么 stage 和 working 都更新为 ```<rev>```; 如果 ```--soft```, 那么 stage 和 working 都不变(但 ```git status``` 会发现有文件 stage 了, 这是相对运动的结果); 如果 ```--mixed``` (默认), 那么只更新 stage (这时 ```git status``` 会发现 working 中有改动, 原因同上)
    * ```<rev>``` 默认为 HEAD, 也就是说, 如果 ```--hard```, 那么 stage 和 working 都更新为 HEAD (和 ```3.``` 效果一样); ```--soft``` 没意义; 如果 ```--mixed```, 那么只更新 stage (就是 ```1.``` 咯~)
    * ```--hard``` 类似于 checkout, 区别在于 ```reset <rev>``` 会移动 master 指针, ```checkout master``` 回不去, 而 ```checkout <rev>``` 再 ```checkout master``` 可以回去
    * 放弃所有本地改动(含本地提交): ```git reset --hard origin/master```
 7. ```git revert <rev>```: 类似于倒着merge, 产生一个新版本V+, 和V-完全一样 - 仅用于 revert 一个很久以前的错误改动!
 8. 将两个 commit 合并成一个(未提交到远程之前)
``` sh
git reset --soft HEAD^1
git commit --amend
```

## 分枝
 * 建立分枝:
   * ```git checkout -b <branch>``` 在当前 HEAD 上创建分枝并切换到新分枝
   * ```git checkout -b <branch> <repo-name>/<remote-branch>``` 跟踪远程分枝
 * 切换分枝: ```git checkout <branch>```
   * ```git checkout <rev>``` 会产生一个 detached HEAD (匿名分枝)
     * 如果不建立实名分枝, 该分枝可能会丢失
 * 删除分枝: ```git branch -d <branch>```
 * 分枝提交到远程(在远程建立新分枝): ```git push <repo-name> <branch>```
 * 查看所有分枝: ```git branch -av```
   * ```git branch``` 不显示远程分枝

## diff
  * 分枝 diff: ```git diff <src-branch> <tgt-branch>``` (tgt默认为当前分枝)
    * 如果是和 master 比较, src-branch 应该是master
  * 版本 diff: ```git diff <src-rev> <tgt-rev>``` (tgt默认为当前版本)
    * src-rev 应该是比 tgt-rev 更老的版本(祖先版本)
    * ```git merge-base <src-branch> <tgt-branch>``` 可能可以得到你需要的 src-rev
  * 其它 diff
    * working 和 stage 的 diff: ```git diff```
    * stage 和 HEAD 的 diff: ```git diff --cached```
    * working 和 HEAD的 diff: ```git diff HEAD```
    * **注意** 上述 3 种方式都不会 diff 新文件(未处于版本控制中的文件)
 * 合并
  * 合并branch到当前分枝: git merge <branch>
   * merge <branch>之后, 修改<branch>, 再次merge, 会只merge修改的部分
  * 合并冲突, 不merge而是指定某个版本: git checkout --ours/--theirs <file>
  * "复制"一次提交(比如某个分枝只有一次提交需要保留): git cherry-pick <rev>
 * rebase
  * git rebase --onto <tgt-branch> <rev> <src-branch>
   * <rev>默认为<tgt-branch>和<src-branch>的共同祖先节点
    * rev可能是一个branch, 如git rebase --onto master server client
    * --onto用于控制<rev>, 但是却放在<tgt-branch>前面, 挺奇怪 [???]
   * <src-branch>默认为当前分枝
  * 与merge的区别
   * merge建立了一个新版本, 而rebase是分枝上有多少新版本, 就会建立多少新版本
   * rebase后需要再做一次快速merge, 才能使tgt的指针正确(两者指针移动方式不同)
  * 交互式rebase: git rebase -i origin/master
 * 协同
  * daemon
```
cd /path/to/project.git
touch git-daemon-export-ok
git daemon --reuseaddr --base-path=/opt/git/
git checkout git://your_ip_address/project
```
  * [[http://git-scm.com/book/zh/%E5%88%86%E5%B8%83%E5%BC%8F-Git|项目管理]]
   * 冲突解决: git fetch + git merge <remote-branch>
 * 标签
  * git tag: 标签列表
  * git tag <tag>: 在当前分枝当前版本上打标签
  * git push origin <tag>: 分享标签
  * git tag -d <tag>: 删除标签
 * 其它
  * git status
  * git reflog: 查看HEAD指针的移动历史
  * git log
  * 查看上次push的版本?
   * git branch -av: 显示所有分枝(含远程)的最后提交版本 -> 多人协同时不够用
   * git log origin/master: 显示远程分枝的log -> 能找到, 但还是很麻烦
   * git log origin/master..origin [√]
   * git log origin/master..HEAD [√]
   * git log origin/master.. [√]
   * 多点语法
```
$ git log refA..refB
$ git log ^refA refB
$ git log refB --not refA
$ git log refA refB ^refC
$ git log refA refB --not refC
```
   * 三点语法: git log origin/master...origin --left-right
  * git branch --merge: 查看哪些分枝已被并入当前分枝
   * git branch --no-merged: 查看尚未合并的分枝
  * 删除远程分枝: git push <name> :<remote-branch>
  * 合并提交(squashing): git rebase -i <rev>, 编辑<rev>之后的提交, 选择squashing
  * 拆分提交/filter-branch
 * [[http://git-scm.com/book/zh/Git-%E5%B7%A5%E5%85%B7-%E4%BA%A4%E4%BA%92%E5%BC%8F%E6%9A%82%E5%AD%98|交互式stage]]
  * git add --patch: [[http://nuclearsquid.com/writings/git-add/|将一个文件的改动分成多次提交]]
 * [[http://git-scm.com/book/zh/Git-%E5%B7%A5%E5%85%B7-%E5%82%A8%E8%97%8F%EF%BC%88Stashing%EF%BC%89|stash]]
  * git stash/git stash list/git stash apply/git stash apply stash@{x}/git stash apply --index
  * git stash drop stash@{x}/git stash pop/gis stash branch <branch>


## 反悔
