import os
import re

def create_docs_from_readme(readme_path, docs_dir):
    # 确保docs目录存在
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配所有文档链接
    pattern = r'\d+\. \[(.+?)\]\(\./(.+?)\)'
    matches = re.findall(pattern, content)

    for item_title, item_path in matches:
        # 创建文档文件
        file_path = os.path.join(docs_dir, item_path)
        
        # 检查文件是否已存在
        if os.path.exists(file_path):
            print(f"文件已存在，跳过生成：{file_path}")
            continue
            
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {item_title}\n\n")
            f.write("## 内容概述\n\n")
            f.write("请在此处添加详细内容...\n")

if __name__ == "__main__":
    readme_path = "/Users/yuanjing/Desktop/KeyboardHandling/README.md"
    docs_dir = "/Users/yuanjing/Desktop/KeyboardHandling"
    create_docs_from_readme(readme_path, docs_dir)
    print("文档生成完成！")