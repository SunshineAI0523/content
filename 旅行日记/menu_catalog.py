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
    # welcome_content = (
    #     "✨ 探索知识之旅 ✨\n"
    #     "这里是我的数字图书馆，包含了许多有趣的文章、教程和资源。\n"
    #     "祝您阅读愉快！\n\n"
    #     "以下是我为您整理的文档列表：\n\n"
    # )
    catalog_content += welcome_content
    
    # 获取所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # 排除.gitignore、index.md以及当前脚本
    filtered_files = [
        f for f in files
        if f not in {'.gitignore', 'index.md', 'menu_catalog.py'}
    ]
    
    # 按文件名排序
    filtered_files.sort()
    
    # 生成目录内容
    for idx, filename in enumerate(filtered_files, 1):
        # 去除文件扩展名
        name_without_ext = os.path.splitext(filename)[0]
        # 生成超链接
        catalog_content += f"{idx}. [{name_without_ext}](./旅行日记/{name_without_ext})\n"
    
    # 写入index.md文件
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(catalog_content)
    
    print("目录已生成：index.md")

if __name__ == "__main__":
    generate_catalog()