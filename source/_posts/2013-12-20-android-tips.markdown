---
layout: post
title: "Android 开发点滴"
date: 2013-12-20 13:27:02 +0800
comments: true
categories: android
---
## Manifest

### 弹出键盘
* `android:windowSoftInputMode` 控制弹出键盘
  * stateHidden 为刚进入 activity 时不显示键盘

## 控件

### EditText 与弹出键盘
* 在 xml 中设置 `android:inputType`, 常用的有:
  * default, 中文手机会弹出中文输入法, 并切换到默认输入模式(通常是中文模式)
  * phone, 电话号码键盘, 不过我们通常还是会用 number 彻底限制只能输入数字
  * textEmailAddress, 虽然名字是 email, 但是也可以输入电话号码
* java 中可以 `setInputType`, 对应的 type 在 `InputType` 找到:
  * 比如 textEmailAddress 对应 TYPE_TEXT_VARIATION_EMAIL_ADDRESS
  * 注意 textPassword 对应 TYPE_CLASS_TEXT | TYPE_TEXT_VARIATION_PASSWORD
* 详见 [官方文档][official-edit-text]

## 工具

### sleep
* `SystemClock.sleep` 不会抛出 `InterruptedException`, 同时也无法 `thread.interrupt`
  * Thread.sleep 则正相反

## 线程

### UI 线程
* UI 控件不是线程安全的, 所以只能在 UI 线程上操作
  * Activity.runOnUiThread
  * View.post/postDelayed
  * Handler
* AsyncTask
  * doInBackground 在 worker 线程
  * onPre/PostExecute 和 onProgressUpdate 在 UI 线程

## WebView

### 使用 HttpClient 的 cookie
``` java
/**
 * @param url - 形如 http://xxx.domain.com/yyy/zzz.z?mmm=nnn
 * @param cookie - 从 HttpClient 取得的 cookie
 */
public static void synCookies(Context context, String url, Cookie cookie) {
    CookieSyncManager.createInstance(context);
    CookieManager cookieManager = CookieManager.getInstance();
    cookieManager.setAcceptCookie(true); // 这句可能可以不要
    String cookieString = cookie.getName() + "=" + cookie.getValue() + "; domain=" + cookie.getDomain();
    cookieManager.setCookie(url, cookieString);
    CookieSyncManager.getInstance().sync();
}
```

 [official-edit-text]: http://developer.android.com/guide/topics/ui/controls/text.html "Text Fields"
