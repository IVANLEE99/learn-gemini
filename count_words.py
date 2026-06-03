import os
import re
from pathlib import Path

def count_content(text):
    # 统计中文字符数
    chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', text))
    # 统计英文单词数
    english_words = len(re.findall(r'[a-zA-Z0-9]+', text))
    return chinese_chars + english_words

def main():
    current_dir = Path(".")
    md_files = list(current_dir.glob("*.md"))
    
    if not md_files:
        print("❌ 未找到任何 .md 文件")
        return

    print("=" * 45)
    print(f" {'Markdown 文件字数统计工具':^35}")
    print("=" * 45)
    
    total_words = 0
    for file_path in md_files:
        try:
            content = file_path.read_text(encoding="utf-8")
            words = count_content(content)
            total_words += words
            print(f"📄 {file_path.name:<20} : {words:>6} 字")
        except Exception as e:
            print(f"❌ 读取 {file_path.name} 失败: {e}")
            
    print("-" * 45)
    print(f"📊 汇总: 共 {len(md_files)} 个文件 | 总计 {total_words} 字")
    print("=" * 45)

if __name__ == "__main__":
    main()