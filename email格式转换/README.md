# Email格式转换工具

这个工具用于从文本中提取电子邮件地址。

## 功能说明

购买的mail账号复制到email.txt文件中，自己改完相同的密码后，或者使用相同密码注册项目，整理格式并将它们保存到accounts.js文件中。修改固定密码位置。
```bash
 password = "1234567898."
```

## 使用方法

### 基本用法

将包含电子邮件地址的文本保存在脚本同目录下的 `email.txt` 文件中，然后运行：

```bash
python extract_emails.py
```

提取的电子邮件地址将保存在 `emails.txt` 文件中。


## 输入文件格式

输入文件可以是任何包含电子邮件地址的文本文件。工具会自动识别并提取符合电子邮件格式的字符串。