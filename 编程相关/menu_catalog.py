import os

# 设置目标目录
target_directory = './'  # 当前目录

# 创建Markdown目录页内容
catalog_content = "# 文章列表:\n\n"

# 排序并列出文件
sorted_files = sorted([f for f in os.listdir(target_directory) if f != 'index.md'], key=lambda x: os.path.getmtime(os.path.join(target_directory, x)))

for index, filename in enumerate(sorted_files, 0):
    if os.path.isfile(os.path.join(target_directory, filename)):
        # 排除当前脚本和Markdown文件
        if filename != os.path.basename(__file__) and filename != 'index.md' and filename != '.gitignore':
            # 生成带有序号的链接
            catalog_content += f"{index}. [{filename}](./{filename})\n"

# 写入Markdown文件
with open('index.md', 'w', encoding='utf-8') as f:
    f.write(catalog_content)

print("目录页已生成，文件名为 index.md。")