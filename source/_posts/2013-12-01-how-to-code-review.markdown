---
layout: post
title: "How to code review"
date: 2013-12-01 21:17:33 +0800
comments: true
categories: teamtoy
---
## 引
 * 版本控制工具：Git
 * 代码 review 工具：[ReviewBoard][reviewboard]
 * 代码 review 需要积极评估代码的设计和清晰程度，项目 owner 还要确保被review 代码的逻辑正确性，而不仅限于命名和格式
 
## 准备工作
 * 用 ldap 账号登录
 * 确保参与 review 的人都需要登录过，否则会找不到人
 * 确保你要 review 的代码的 git 已经加入 reviewboard
 * 确保你要 review 的代码基点已经 push 到 git 服务器
   * 代码基点: `git diff <src-rev> <tgt-rev>` 中的 `<src-rev>`

## 提交一个 review
<!-- more -->
 1. 生成diff
    * `git diff <src-rev> <tgt-rev> > d1.diff`
      * 一般来说src是tgt的父节点
    * 如何得到 `<src-rev>`
      * 对于开分枝 / 开发 / merge 的工作模式而言
        * `<src-rev>` 就是你开分枝时分枝点的版本
        * 可以用 `git merge-base <src-branch> <tgt-branch>` 得到 `<src-rev>`
          * 比如你要从 work 分枝 merge 回 master，则执行 `git merge-base master work` 得到 `<src-rev>`，前提是你没有 merge 过
          * 但如果你已经 merge 过，这样得到的 `<src-rev>` 是从最后一次 merge 的版本
      * 对于在一个分枝上持续开发的工作模式
        * 查看git log 找到需要的 `<src-rev>`
      * 应该尽量在代码稳定时再 merge：勤开分枝，慎重 merge
      * 应该尽量使用 amend，减少 commit，git log 才好找
 1. 访问 reviewboard，点击 New Review Request
 1. 选择 Repository，选择 diff 文件，点击 Create Review Request
 1. 点击 View Diff，查看上传结果是否和预期一致
 1. 填写 Summary / People / Description，注意 people 是 ldap 账号名，用 tab 补全，别按回车
 1. 确认提交，系统会发邮件给 people，通知他们来 review
                                            
## 更新一个 review
 1. 修改代码提交之后生成新 diff
    * `git diff <src-rev> <tgt-rev2> > d2.diff`
    * **注意** 确保在一次 review 中，所有 diff 的 `<src-rev>` 都是同一个
 1. 访问 reviewboard，打开要更新的 review
    * 只能更新自己提交的 review
 1. 点击 Update 下拉菜单中的 Update Diff，选择 diff 文件，点击 Upload
 1. 点击 View Diff，查看上传结果是否和预期一致
 1. 填写本次更新的内容，确认提交
                                                        
## review 别人的代码
 1. 点击邮件通知中的链接，登录 reviewboard
 1. 点击 View Diff，查看被修改的代码
 1. 点击有问题的行，填写有什么问题
 1. 继续 review，直到所有代码都 review 完毕
 1. 点击页面上方悬浮条中的 Edit Review，预览所有你填写的内容
 1. 如果没有问题，点击 Publish Review
    * 如果需要修改，可以直接在预览页面上修改
    * 如果需要增加，点击 Cancel，增加，再 Edit Review
 1. 如果代码较多，可以 review 一页提交一页
                                                             
## 根据别人的 review 修改代码
 1. 别人提出的每个问题都会生成一个 issue
 1. 对照这些 issue 修改代码；如果 fix 了，就点 fixed；如果有异议，可以回复讨论；如果确认不需要改，就点 drop
 1. 修改完成后，提交代码，生成新的 diff
 1. 更新 review，继续，直到所有 issue 都 fixed 或 drop

 [reviewboard]: http://www.reviewboard.org/ "Review Board"
