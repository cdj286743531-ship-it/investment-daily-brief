# 配置示例 | Configuration Examples

## 基础配置（飞书推送）

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,
      "type": "webhook",
      "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/xxx",
      "secret": ""
    }
  },
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 18 * * 1-5",
      "timezone": "Asia/Shanghai",
      "output": {
        "channels": ["feishu"],
        "file_prefix": "投资日报"
      }
    }
  ]
}
```

---

## 多渠道推送

### 飞书 + 企业微信 + 邮件

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,
      "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
    },
    "wechatwork": {
      "enabled": true,
      "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"
    },
    "email": {
      "enabled": true,
      "smtp_host": "smtp.gmail.com",
      "smtp_port": 587,
      "smtp_user": "your@gmail.com",
      "smtp_password": "your_password",
      "from_addr": "your@gmail.com",
      "to_addrs": ["recipient@example.com"]
    }
  },
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 18 * * 1-5",
      "output": {
        "channels": ["feishu", "wechatwork", "email"],
        "file_prefix": "投资日报"
      }
    }
  ]
}
```

---

## 自定义关注行业

### 专注科技股

```json
{
  "customization": {
    "focus_areas": [
      "半导体", "人工智能", "消费电子",
      "云计算", "软件服务", "互联网"
    ],
    "stock_focus": {
      "indices": ["纳斯达克 100", "科创 50", "恒生科技"],
      "sectors": ["科技", "通信", "传媒"],
      "themes": ["AI 算力", "国产替代", "出海"]
    }
  }
}
```

### 专注消费股

```json
{
  "customization": {
    "focus_areas": [
      "食品饮料", "家电", "汽车",
      "医药生物", "零售", "旅游"
    ],
    "stock_focus": {
      "indices": ["沪深 300", "中证消费"],
      "sectors": ["消费", "医药", "汽车"],
      "themes": ["消费升级", "国货崛起", "老龄化"]
    }
  }
}
```

### 专注港股

```json
{
  "customization": {
    "focus_areas": [
      "港股市场", "港股通", "中概股"
    ],
    "stock_focus": {
      "indices": ["恒生指数", "恒生国企", "恒生科技"],
      "sectors": ["互联网", "房地产", "金融", "消费"],
      "themes": ["估值修复", "回购潮", "南下资金"]
    }
  }
}
```

---

## 修改推送时间

### 早上 9 点（开盘前）

```json
{
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 9 * * 1-5",
      "timezone": "Asia/Shanghai"
    }
  ]
}
```

### 中午 12 点（午间休息）

```json
{
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 12 * * 1-5",
      "timezone": "Asia/Shanghai"
    }
  ]
}
```

### 晚上 20 点（复盘）

```json
{
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 20 * * 1-5",
      "timezone": "Asia/Shanghai"
    }
  ]
}
```

---

## 环境变量配置（推荐）

### 使用环境变量存储敏感信息

```bash
# ~/.bashrc 或~/.zshrc
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
export FEISHU_SECRET="xxx"
export WECOM_WEBHOOK_URL="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"
export SMTP_PASSWORD="your_password"
```

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,
      "webhook_url": "${FEISHU_WEBHOOK_URL}",
      "secret": "${FEISHU_SECRET}"
    },
    "wechatwork": {
      "enabled": true,
      "webhook_url": "${WECOM_WEBHOOK_URL}"
    },
    "email": {
      "enabled": true,
      "smtp_password": "${SMTP_PASSWORD}"
    }
  }
}
```

---

## 完整配置示例

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,
      "type": "webhook",
      "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/xxx",
      "secret": ""
    },
    "wechatwork": {
      "enabled": false,
      "webhook_url": ""
    },
    "email": {
      "enabled": false,
      "smtp_host": "smtp.gmail.com",
      "smtp_port": 587,
      "smtp_user": "",
      "smtp_password": ""
    }
  },
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 18 * * 1-5",
      "timezone": "Asia/Shanghai",
      "output": {
        "channels": ["feishu"],
        "file_prefix": "投资日报"
      }
    }
  ],
  "customization": {
    "language": "zh-CN",
    "max_items": 12,
    "focus_areas": [
      "A 股市场", "港股市场", "美股市场",
      "宏观经济", "货币政策", "行业动态"
    ],
    "stock_focus": {
      "indices": ["上证指数", "恒生指数", "标普 500"],
      "sectors": ["科技", "金融", "消费", "医药"],
      "themes": ["AI 算力", "高股息", "国产替代"]
    },
    "search_keywords": {
      "cn": [
        "A 股 收盘 涨跌",
        "央行 逆回购 MLF",
        "财报 业绩 超预期"
      ],
      "en": [
        "S&P 500 NASDAQ close",
        "Fed interest rate",
        "earnings beat"
      ]
    }
  }
}
```

---

## 常见问题

### Q: 如何禁用某个推送渠道？

A: 设置 `"enabled": false`

```json
{
  "adapters": {
    "feishu": { "enabled": false }
  }
}
```

### Q: 如何增加推送频率？

A: 修改 cron 表达式

```json
{
  "cron": [
    {
      "schedule": "0 9 * * 1-5",
      "name": "早盘简报"
    },
    {
      "schedule": "0 18 * * 1-5",
      "name": "投资日报"
    }
  ]
}
```

### Q: 如何只关注特定股票？

A: 在 `stock_focus` 中添加

```json
{
  "stock_focus": {
    "stocks": ["腾讯控股", "阿里巴巴", "贵州茅台", "宁德时代"]
  }
}
```

---

## 更新日志

- **2026-03-12**：初始版本
