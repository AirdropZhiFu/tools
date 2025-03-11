import os
import sys

def convert_to_socks5(input_file, output_file):
    """
    将IP文件中的内容转换为socks5://username:password@ip:port格式
    """
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        socks5_proxies = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split(':')
            if len(parts) == 4:
                ip, port, username, password = parts
                socks5_proxy = f"socks5://{username}:{password}@{ip}:{port}"
                socks5_proxies.append(socks5_proxy)
        
        with open(output_file, 'w') as f:
            f.write('\n'.join(socks5_proxies))
        
        print(f"转换完成！已将结果保存到 {output_file}")
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file}'")
        print(f"当前工作目录: {os.getcwd()}")
        print("请确保文件路径正确或使用绝对路径")
        sys.exit(1)
    except Exception as e:
        print(f"发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 默认文件路径设置在脚本所在目录
    default_input = os.path.join(script_dir, 'ip.txt')
    default_output = os.path.join(script_dir, 'socks5_proxies.txt')
    
    # 允许通过命令行参数指定文件
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = default_input
        
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = default_output
    
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")
    
    convert_to_socks5(input_file, output_file) 