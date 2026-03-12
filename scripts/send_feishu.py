# -*- coding: utf-8 -*-
"""
Investment Daily Brief — 飞书推送脚本

用法:
  python send_feishu.py --webhook "YOUR_WEBHOOK_URL" --content "消息内容"
  python send_feishu.py --config ../daily-brief-config.json --content "消息内容"
"""
import json
import argparse
import requests
import hashlib
import base64
import time

def generate_sign(secret, timestamp):
    """生成飞书签名"""
    string_to_sign = f'{timestamp}\n{secret}'
    hmac_code = base64.b64encode(
        hashlib.sha256(string_to_sign.encode('utf-8')).digest()
    ).decode('utf-8')
    return hmac_code

def send_feishu(webhook_url, content, secret=None):
    """发送飞书消息"""
    headers = {'Content-Type': 'application/json'}
    
    # 如果有签名，添加时间戳和签名
    if secret:
        timestamp = str(int(time.time()))
        sign = generate_sign(secret, timestamp)
        data = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "💰 投资日报",
                        "content": [
                            [{"tag": "text", "text": content}],
                            [{"tag": "text", "text": f"\n发送时间：{time.strftime('%Y-%m-%d %H:%M:%S')}"}]
                        ]
                    }
                }
            },
            "timestamp": timestamp,
            "sign": sign
        }
    else:
        data = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "💰 投资日报",
                        "content": [
                            [{"tag": "text", "text": content}]
                        ]
                    }
                }
            }
        }
    
    response = requests.post(webhook_url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        if result.get('StatusCode') == 0 or result.get('code') == 0:
            print("✅ 飞书消息发送成功")
            return True
        else:
            print(f"❌ 飞书消息发送失败：{result}")
            return False
    else:
        print(f"❌ HTTP 错误：{response.status_code}")
        print(response.text)
        return False

def main():
    parser = argparse.ArgumentParser(description='飞书推送脚本')
    parser.add_argument('--webhook', type=str, help='飞书 Webhook URL')
    parser.add_argument('--secret', type=str, help='飞书签名密钥')
    parser.add_argument('--config', type=str, help='配置文件路径')
    parser.add_argument('--content', type=str, required=True, help='消息内容')
    
    args = parser.parse_args()
    
    # 从配置文件读取
    if args.config and not args.webhook:
        with open(args.config, 'r', encoding='utf-8') as f:
            config = json.load(f)
        feishu_config = config.get('adapters', {}).get('feishu', {})
        webhook_url = feishu_config.get('webhook_url')
        secret = feishu_config.get('secret')
    else:
        webhook_url = args.webhook
        secret = args.secret
    
    if not webhook_url:
        print("❌ 错误：请提供 Webhook URL 或配置文件")
        sys.exit(1)
    
    success = send_feishu(webhook_url, args.content, secret)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
