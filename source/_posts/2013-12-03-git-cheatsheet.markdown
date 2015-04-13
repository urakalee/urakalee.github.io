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
  * ```git pull [repo-name]```
    * repo-name 默认为 origin
    * ```git pull --rebase``` 可以避免无意义的 pull-merge, 使版本树尽可能是一条直线
  * ```git fetch [repo-name]``` - ```git pull``` does a ```git fetch``` followed by a ```git merge```
    * repo-name 默认为 origin
    * 会把 repo-name 的更新都 fetch 到本地, 包括新分枝和新标签, 但不会建立本地分枝
* 提交到本地
  * stage: ```git add <file/dir>```
  * ```git commit -m "<comment>"```
    * 对于已经处于版本控制中的文件, 可以使用 ``` git commit -am "<comment>"``` 略过 stage
    * 有时需要构造空提交: ```git commit --allow-empty -m "EMPTY"```
* 提交到远程
  * ```git push [repo-name] [branch] ```
    * repo-name 默认为 origin, branch 默认为当前分枝
    * ```git push -u <repo-name> <branch>``` 设置 push/pull 时默认使用的 repo-name
    * ```git push <repo-name> <branch>:<remote-branch>``` - 如果本地和远程分枝名字不同
<!-- more -->

## 反悔
1. revert stage: ```git reset HEAD <file>```
2. reset working: ```git checkout -- <file>```
3. restore(1+2): ```git checkout HEAD <file>```
   * checkout 上一个版本, 放在 stage/working 中: ```git checkout HEAD~ <file>```
   * 如果改动, add, 再改动, 使用 ```1.``` 不会恢复到第一次改动的结果; 使用 ```2.``` 才行!
4. ```git reset <rev> [file]```
   * 没有 file 把 HEAD/branch 指向 rev
   * 有 file 把 rev 版本的 file checkout 出来
   * 如果 ```--hard```, 那么 stage 和 working 都更新为 rev; 如果 ```--soft```, 那么 stage 和 working 都不变(但 ```git status``` 会发现有文件 stage 了, 这是相对运动的结果); 如果 ```--mixed``` (默认), 那么只更新 stage (这时 ```git status``` 会发现 working 中有改动, 原因同上)
   * rev 默认为 HEAD: 如果 ```--hard```, 那么 stage 和 working 都更新为 HEAD (和 ```3.``` 效果一样); ```--soft``` 没意义; 如果 ```--mixed```, 那么只更新 stage (就是 ```1.``` 咯~)
   * 没有 file 时 ```--hard``` 类似于 checkout, 区别在于 ```reset <rev>``` 会移动 branch 指针, ```checkout <branch>``` 回不去, 而 ```checkout <rev>``` 再 ```checkout <branch>``` 可以回去
   * 放弃所有本地改动(含本地提交): ```git reset --hard <repo-name>/<remote-branch>```
5. ```git checkout <rev> [file]```
   * 没有 file 会建立一个 detached HEAD (匿名分枝) - 最好别用!
   * 有 file 把 rev 版本的 file checkout 出来
   * rev 默认为 ```--``` 即 stage, 从 stage checkout 到 working
   * 其它 rev 从 rev checkout 到 stage 再到 working
6. ```git revert <rev>```: 类似 svn 中的倒着 merge, 生成一个新版本 V+, 和 V-完全一样 - 仅用于 revert 一个很久以前的错误改动!
1. 修改已经 push 到远程的提交
   1. 使用下面的方法修改已经 push 到远程的提交
   1. ```git push <repo-name> +<branch>:<remote-branch>```
8. 修改上一个提交: ```git commit --amend```
9. 修改多个提交(交互式)
   1. ```git rebase -i <rev>```, 编辑 rev 之后的提交, rev 默认为 repo-name/remote-branch
   1. 对于想合并到前一个的提交, 选择 fixup
   1. 对于想删除的提交, 直接删除对应的行
10. 将上 N 个提交合并成一个
``` sh
git reset --soft HEAD^(N-1)
git commit --amend
```

## 分枝
* 建立分枝:
  * ```git checkout -b <branch>``` 在当前 HEAD 上创建分枝并切换到新分枝
  * ```git checkout -b <branch> <repo-name>/<remote-branch>``` 跟踪远程分枝
* 切换分枝: ```git checkout <branch>```
* 删除分枝: ```git branch -d <branch>```
  * 对于没有合并或提交到远程的分枝, 删除时会提示用 ```-D``` 强制删除
* 将分枝提交到远程(在远程建立新分枝): ```git push <repo-name> <branch>```
  * 提交到远程之后, 如果希望能够 pull 该分枝, 需要 ```git push -u```
* 删除远程分枝: ```git push <repo-name> :<remote-branch>```
* 查看所有分枝: ```git branch -av```
  * ```git branch``` 不显示远程分枝

## diff
* 分枝 diff: ```git diff <src-branch> <tgt-branch>``` (tgt 默认为当前分枝)
  * 如果是和 master 比较, src-branch 应该是master
* 版本 diff: ```git diff <src-rev> <tgt-rev>``` (tgt 默认为当前版本)
  * src-rev 应该是比 tgt-rev 更老的版本(祖先版本)
  * ```git merge-base <src-branch> <tgt-branch>``` 可能可以得到你需要的 src-rev
* 其它 diff
  * working 和 stage 的 diff: ```git diff```
  * stage 和 HEAD 的 diff: ```git diff --cached```
  * working 和 HEAD 的 diff: ```git diff HEAD```
  * **注意** 上述 3 种方式都不会 diff 新文件(未处于版本控制中的文件)

## 合并
* 合并 branch 到当前分枝: ```git merge <branch>```
  * fetch 后用 ```git merge <repo-name>/<remote-branch>``` merge
  * 如果 ```merge <branch>```, 修改 branch, 再 merge, 只 merge 修改的部分
  * 合并冲突时, 不 merge 而是指定某个版本: ```git checkout --ours/--theirs <file>```
  * "复制" 一次提交(比如某个分枝只有一次提交需要保留): ```git cherry-pick <rev>```
    * 停止 "复制": ```git cherry-pick --abort```
* 将当前分枝 rebase 到 tgt-branch: ```git rebase <tgt-branch>```
* merge 与 rebase 的区别
  * merge 建立了一个新版本, 而 rebase 是分枝上有多少新版本, 就会建立多少新版本
  * rebase 后需要再做一次快速 merge, 才能使 tgt-branch 的指针正确(两者指针移动方式不同)

## 查看状态信息
* ```git status```
* ```git log```
* ```git reflog```: 查看 HEAD 指针的移动历史
* ```git branch --merge```: 查看哪些分枝已被合并到当前分枝
* ```git branch --no-merged```: 查看尚未合并的分枝
* ```git remote show <repo-name>```: 查看远程信息

## 暂存
``` sh
git stash
git stash pop
git stash list
git stash clear
git stash apply stash@{x}
git stash drop stash@{x}
git stash branch <branch>
```

## 标签
``` sh
git tag # 标签列表
git tag <tag> # 在当前版本上打标签
git show <tag> # 查看标签
git tag -d <tag> # 删除标签
git push <repo-name> <tag> # 提交标签
git push <repo-name> :<tag> # 删除远程标签
```

## submodule @2015.04.13
``` sh
git submodule add <remote-path> [<local-path>] # 添加 remote-path 为当前项目的 submodule
```
``` sh 删除 local-path 下的子项目
git rm -r <local-path> # 如果有问题, 试试 git rm --cached <local-path>
vim .gitmodules # 通常会在 git rm 时自动执行
vim .git/config
git commit
```
