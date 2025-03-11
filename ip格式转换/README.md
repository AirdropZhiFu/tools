# IP格式转换工具

这个工具用于将IP地址从标准格式转换为socks5代理格式。

## 功能说明

将格式为 `ip:port:username:password` 的代理地址转换为 `socks5://username:password@ip:port` 格式。将ip存放在ip.txt文件中的ip地址转换为socks5代理格式。

## 使用方法

### 基本用法

将IP地址列表保存在脚本同目录下的 `ip.txt` 文件中，然后运行：

```bash
python ip_converter.py
```

转换后的结果将保存在 `socks5_proxies.txt` 文件中。

### 指定输入文件

```bash
python ip_converter.py 路径/到/你的/ip.txt
```

### 指定输入和输出文件

```bash
python ip_converter.py 路径/到/你的/ip.txt 路径/到/输出/文件.txt
```

## 输入文件格式

输入文件中的每一行应该是以下格式：

```
ip:port:username:password
```

例如：
```
192.168.1.1:1080:user:pass
10.0.0.1:8080:admin:123456
```

## 输出文件格式

输出文件中的每一行将是以下格式：

```
socks5://username:password@ip:port
```

例如：
```
socks5://user:pass@192.168.1.1:1080
socks5://admin:123456@10.0.0.1:8080
```

## 错误处理

如果找不到输入文件，程序会显示当前工作目录并提示用户检查文件路径。
```
