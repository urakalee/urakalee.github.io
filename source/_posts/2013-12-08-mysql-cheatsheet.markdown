---
layout: post
title: "MySQL 手册"
date: 2013-12-08 16:22:54 +0800
comments: true
categories: cheatsheet
published: false
---
## SQL 语句

### mysql 时间
http://www.webasp.net/article/25/24538.htm

### 支持executeBatch
* jdbc:mysql://<host>/<db>?rewriteBatchedStatements=true
  * http://hidba.org/?p=369
  * http://lionbule.iteye.com/blog/1098537

## MySQL 客户端

### mysql 权限
``` sql
SHOW GRANTS FOR '<user>'@'<%|host>'; -- 注意单引号
GRANT ALL PRIVILEGES ON <database>.<*|table> to '<user>'@'<%|host>' [IDENTIFIED BY '<password>'];
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,ALTER,DROP ON ...;
```
* http://database.51cto.com/art/201006/203939.htm
* http://www.111cn.net/database/mysql/41034.htm

## 支持中文

### mysql 客户端
```set names utf8;```: 插入或查询中文出现乱码时使用

### my.cnf
* [mysqld] character-set-server=utf8
  * http://guichina.blog.51cto.com/2001125/724939
* 老版本可能还需要进行如下修改
  * [client] default-character-set=utf8
  * [mysqld] default-storage-engine=INNODB

## MyBatis
* 返回自增值
* 多参数映射/ list 映射
  * http://fengfan876.iteye.com/blog/1473863
* 如何annotation
  * http://huangmin001.iteye.com/blog/1185806
