# -*- coding: utf-8 -*-
"""
Investment Daily Brief — 配置初始化脚本
生成默认的 daily-brief-config.json 配置文件。

用法:
  python init_config.py                       # 在 Skill 根目录生成配置
  python init_config.py /path/to/output       # 在指定目录生成配置
"""
import json
import sys
from pathlib import Path

# 读取模板配置
TEMPLATE_PATH = Path(__file__).parent.parent / "daily-brief-config.template.json"
DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent.parent / "daily-brief-config.json"

def main():
    # 确定输出路径
    if len(sys.argv) > 1:
        output_path = Path(sys.argv[1])
    else:
        output_path = DEFAULT_CONFIG_PATH
    
    # 读取模板
    if TEMPLATE_PATH.exists():
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        print(f"错误：模板文件不存在 {TEMPLATE_PATH}")
        sys.exit(1)
    
    # 写入配置
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 配置文件已生成：{output_path}")
    print()
    print("📝 下一步:")
    print("1. 编辑配置文件，填入你的 Webhook URL 或其他渠道配置")
    print("2. 运行：openclaw cron add --name \"投资日报\" --schedule \"0 18 * * 1-5\"")
    print("3. 测试：告诉 AI「生成投资日报」")
    print()
    print("📚 详细文档：SKILL.md")

if __name__ == "__main__":
    main()
