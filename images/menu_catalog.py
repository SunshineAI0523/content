import os

def generate_catalog():
    # 当前目录
    directory = './'
    
    # 初始化目录内容
    catalog_content = "# 目录页\n\n"
    
    # 添加欢迎语和简介
    welcome_content = (
        "欢迎来到我的文档中心！\n"
        "在这里，您可以找到各种文档和资源，每个文件都经过精心整理，便于查阅和学习。\n"
        "以下为您列出的可用文档：\n\n"
    )
    catalog_content += welcome_content
    
    # 获取所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # 排除.gitignore、catalog.md以及当前脚本
    filtered_files = [
        f for f in files
        if f not in {'.gitignore', 'catalog.md', 'generate_catalog.py'}
    ]
    
    # 按文件名排序
    filtered_files.sort()
    
    # 生成目录内容
    for idx, filename in enumerate(filtered_files, 1):
        # 去除文件扩展名
        name_without_ext = os.path.splitext(filename)[0]
        # 生成超链接
        catalog_content += f"{idx}. [{name_without_ext}]({filename})\n"
    
    # 写入catalog.md文件
    with open('catalog.md', 'w', encoding='utf-8') as f:
        f.write(catalog_content)
    
    print("目录已生成：catalog.md")

if __name__ == "__main__":
    generate_catalog()