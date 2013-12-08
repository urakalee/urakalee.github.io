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

### 内部规范
* 第三部分
  * 每行不超过 120 字符, 一个文件不超过 600 行
  * 愿意遵循每行不超过 72 或 80 字符的也可以, 但不超过 120 是必须的
* 第四部分
  * 再次强调每行不超过 120 字符, 一个文件不超过 600 行
  * ***换行是检验代码可读性的重要标准***
* 第六部分
  * 一行声明一个变量
* 第七部分
  * 语句块即使只有一行也要有括号
  * 尤其是 if 语句!
* 第九部分
  * 类名为首字母大写格式
  * 包名均为小写, 视觉上应为一个倒置的域名, 比如 ```com.domain.codename```
  * 常量为全大写, 下划线分隔
* 第十部分
  * 善用 TODO, XXX, FIXME
* 其它
  * 避免 magic number
  * 禁用 ```System.out.print```, 使用 logger
  * 如果可能, 避免使用 ```++```, 无论是前 ```++``` 还是后 ```++```, 而是用 ```+= 1```来替代
  * 文件结构: 将功能和方法分为命令和查询两类, 并将两者分别放在一起
    * 也可以分成更多类, 比如 override/implement/public/private/getter/setter 等
    * 定义 code template 是个好办法, 但关键还是在于所有人都能坚持遵循
  * 包结构: 包内文件不超过 10 个, 接口的实现要放在对应的 impl 目录下
  * Singleton (helper): 需要初始化
  * 静态函数集合 (utils): 不需要初始化, 或者有瞬间又无异常的static初始化

### 防御
* 警告就是错误!
* 报告所有的异常, 传播不能处理的异常, 禁止空 catch, 即使是临时这样做也不行!
* 在异常发生之前使用断言, 可以避免更严重的问题(比如数据不一致)

### 测试
* 单元测试就是最可信的文档
* 刚刚开始 TDD 时要用最简单的方式编写 TestCase, 而不是不断引入新的类, 否则你会强迫自己保留和使用它们
* 像重构代码一样重构测试
* 测试用例以 Test 开头, 测试一个类用 Test + 类名, 测试一个包用 Test + 包名(为了遵循类命名规范, 包名需要首字母大写)

### 调试
* 善用 debug 模式, 而不是 log, 更不是 print
* 但是, 在运行着的系统中 log 还是很有用的, 所以 log 中要展示有用的信息
* 实验用例以Run开头, 后面同测试用例, 通常每个实验用例都只有一个main函数, 主要用来做实验

## Html/Css/Javascipt
* html 的 id 为驼峰格式, 形如 abcXyz
* html 的 class 为全小写, 形如 abc-xyz

 [java-code]: http://www.oracle.com/technetwork/java/codeconv-138413.html "Java 编码规范"
 [java-code-cn]: http://doc.javanb.com/code-conventions-for-the-java-programming-language-zh/ "Java 编码规范(中文版)"
