---
layout: post
title: "Code Style"
date: 2013-12-07 18:07:00 +0800
comments: true
categories: teamtoy
---
## 代码风格
* 代码是给人看的, 偶尔也在机器上跑一跑
* 代码应该越写越少: **Write Less Do More** !!!
* 所有源代码文件(包括 html/css/properties/readme 等)均为 utf-8 无 bom 格式, unix 换行
* **禁用tab**, 所有源代码文件一律使用 4 空格缩进

## Java
* [Java Code Conventions][java-code]
* [Java编码规范(中文版)][java-code-cn]
<!-- more -->

### 组内规范
* 除上述规范外, 还应该遵循下述组内规范
* 第三部分
  * 每行不超过 120 字符, 一个文件不超过 600 行
  * 愿意遵循每行不超过 72 或 80 字符的也可以, 但不超过 120 是必须的
* 第四部分
  * 再次强调每行不超过 120 字符, 一个文件不超过 600 行
  * **注意换行**
* 第六部分
  * 一行声明一个变量
* 第七部分
  * 语句块即使只有一行也要有括号
  * 尤其是 if 语句!
* 第九部分
  * 类名为首字母大写格式
  * 包名均为小写, 视觉上应为一个倒置的域名, 比如```com.domain.codename```
  * 常量为全大写, 下划线分隔
* 第十部分
  * 善用 TODO, XXX, FIXME
* 其它
  * 避免 magic number
  * 禁用 ```System.out.print```, 使用 logger
  * 如果可能, 避免使用 ```++```, 无论是前 ```++``` 还是后 ```++```, 而是用 ```+= 1```来替代
  * 包结构: 包内文件不超过 10 个, 接口的实现要放在对应的 impl 目录下

## Html/Css/Javascipt
* html 的 id 为驼峰格式, 形如 abcXyz
* html 的 class 为全小写, 形如 abc-xyz

 [java-code]: http://www.oracle.com/technetwork/java/codeconv-138413.html "Java 编码规范"
 [java-code-cn]: http://doc.javanb.com/code-conventions-for-the-java-programming-language-zh/ "Java 编码规范(中文版)"
