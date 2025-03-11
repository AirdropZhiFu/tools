#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # 读取email.txt文件
    try:
        with open('email.txt', 'r') as file:
            emails = file.readlines()
    except FileNotFoundError:
        try:
            with open('email格式转换/email.txt', 'r') as file:
                emails = file.readlines()
        except FileNotFoundError:
            print("错误：找不到email.txt文件。请确保该文件存在于当前目录或email格式目录中。")
            return

    # 清理邮箱地址（去除空白字符并只保留冒号前的部分）
    cleaned_emails = []
    for email in emails:
        email = email.strip()
        if email:
            # 如果邮箱包含冒号，只保留冒号前的部分
            if ':' in email:
                email = email.split(':', 1)[0]
            cleaned_emails.append(email)
    
    # 固定密码
    password = "1234567898."
    
    # 生成JavaScript格式的输出
    js_output = "export const accounts = [\n"
    
    for email in cleaned_emails:
        js_output += f'  {{ username: "{email}", password: "{password}" }},\n'
    
    # 移除最后一个逗号并添加结束括号
    if cleaned_emails:
        js_output = js_output.rstrip(',\n') + '\n'
    js_output += "];\n"
    
    # 将结果保存到accounts.js文件
    with open('email格式转换/accounts.js', 'w') as output_file:
        output_file.write(js_output)
    
    print(f"成功提取了{len(cleaned_emails)}个邮箱地址，并保存到accounts.js文件中。")

if __name__ == "__main__":
    main() 