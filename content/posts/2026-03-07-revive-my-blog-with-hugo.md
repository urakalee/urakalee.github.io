---
title: "重启十年前的博客"
date: 2026-03-07
draft: false
tags: ["selfengine"]
---

距离上一次更新这个博客，已经过去了整整十年。

当年用 Octopress 搭的，最后一篇是 2016 年；这次跟 Cursor 聊，换成了 Hugo。

<!--more-->

## 为什么选 Hugo

- 上面说了是跟 Cursor 聊的
- **零依赖**：主要考虑这个，Ruby 太烦了，这个 `brew install hugo` 就搞定了
- **部署简单**：配合 GitHub Actions，push 即发布

## 迁移过程

- 完全在 Cursor 里完成的
- Cursor 自己写了脚本，做了格式转换
- 大致看了一下没啥问题

转换好的文章放到 `content/posts/`，配置 `hugo.toml`，本地 `hugo server` 预览。

## 部署到 GitHub Pages

- GitHub 也比 10 年前更自动化了

在 `.github/workflows/deploy.yml` 里配置了 GitHub Actions，push 到 `main` 分支就会自动构建和部署。原来的 `master` 分支（旧的静态 HTML）和 `source` 分支（Octopress 源码）都保留着，作为历史备份。

## 如何写新文章和发布

### 创建文章

```bash
cd /path/to/blog
hugo new content posts/YYYY-MM-DD-my-post-title.md
```

会在 `content/posts/` 下生成一个带 front matter 模板的 Markdown 文件。

```yaml
---
title: "文章标题"
date: YYYY-MM-DD
draft: false
tags: ["tag1", "tag2"]
---
```

`draft: true` 的文章不会被发布，改成 `false` 才会出现在线上。

### 本地预览

```bash
hugo server -D
pkill hugo
```

`-D` 表示包含草稿。打开 `http://localhost:1313/` 就能看到效果。

### 发布

```bash
git add -A
git commit -m "新文章: xxx"
git push
```

push 到 `main` 分支后，GitHub Actions 会自动构建并部署。

## 样式

- 默认样式有点丑，让 Cursor 帮忙改了一下
- 但不知道是我的审美有问题，还是 Cursor 有问题，Opus 和 Gemini 3.1 都改不好
- 去掉了深色模式之后（大概还好改一点了），就还行

## 附件

### 链接

- 费了半天劲，最终还是 Opus 搞定了，不知道为什么 Sonnet 不行（位置搞不对）
- 公众号链接没搞定（感觉现在微信已经不支持了，但 AI 搜到的还都是过时消息），最后放了二维码

### 留言

- Cursor 提供了一些方案，先保存了一下没有实施

### 打赏

- 未调研，目前需求不大

### 发布到其它平台

- Wechatsync：Chrome 插件；试了一下发布到公众号时代码格式有点问题