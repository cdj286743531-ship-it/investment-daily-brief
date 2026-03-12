---
name: investment-daily-brief
description: |
  AI 驱动的投资日报自动生成器。自动搜集 A 股/港股/美股市场数据、宏观动态、公司公告、机构观点，
  生成结构化投资日报并推送到飞书/企业微信/钉钉等渠道。
  触发关键词：投资日报、股市日报、market daily brief、investment report、财经日报。
allowed-tools:
  - read_file
  - write_to_file
  - replace_in_file
  - execute_command
  - web_search
  - web_fetch
  - message
disable: false
---

# 投资日报生成器 | Investment Daily Brief Generator

一个 AI 驱动的投资日报自动生成技能，自动搜集、过滤、编写并推送高质量的投资日报。

## 🚀 快速开始

### 1. 安装技能

```bash
# 方式 1: 从 GitHub 克隆
git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief

# 方式 2: 使用 clawhub (如果已发布)
clawhub install investment-daily-brief
```

### 2. 初始化配置

```bash
cd ~/.openclaw/workspace/skills/investment-daily-brief
python scripts/init_config.py
```

### 3. 配置推送渠道

编辑 `daily-brief-config.json`，启用你需要的推送渠道：

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,
      "webhook_url": "你的飞书机器人 Webhook URL"
    }
  }
}
```

### 4. 设置定时任务

```bash
openclaw cron add --name "投资日报" --schedule "0 18 * * 1-5" --task "生成投资日报"
```

---

## 📋 功能特性

### 核心模块

| 模块 | 内容 | 信源 |
|------|------|------|
| 📈 市场概览 | 主要指数、涨跌、成交量 | Yahoo Finance、新浪财经、交易所 |
| 🔥 热点板块 | 当日领涨/领跌板块 | 同花顺、东方财富、财联社 |
| 💵 宏观动态 | 政策、利率、经济数据 | 央行、统计局、SEC、Fed |
| 🏢 公司动态 | 财报、并购、高管变动 | 公司公告、交易所、SEC filings |
| 📊 机构观点 | 投行评级、目标价调整 | 高盛、摩根、中金、中信 |
| ⚠️ 风险提示 | 黑天鹅、地缘风险 | 多方交叉验证 |
| 📅 未来一周事件 | 重要经济数据、财报 | 财经日历 |
| 💡 策略建议 | 短期和中期投资策略 | 综合研判 |

### 推送渠道

支持 9 大推送渠道：

| 渠道 | 配置难度 | 推荐度 |
|------|---------|--------|
| 飞书 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| 企业微信 | ⭐⭐ | ⭐⭐⭐⭐ |
| 钉钉 | ⭐⭐ | ⭐⭐⭐⭐ |
| 邮件 | ⭐⭐⭐ | ⭐⭐⭐ |
| Slack | ⭐⭐ | ⭐⭐⭐ |
| Discord | ⭐⭐ | ⭐⭐⭐ |
| Telegram | ⭐⭐⭐ | ⭐⭐ |
| Teams | ⭐⭐⭐ | ⭐⭐ |
| GitHub Pages | ⭐⭐⭐⭐ | ⭐⭐ |

---

## 📁 文件结构

```
investment-daily-brief/
├── SKILL.md                      # 技能定义文件
├── README.md                     # 英文文档
├── README_zh.md                  # 中文文档
├── CHANGELOG.md                  # 更新日志
├── LICENSE                       # MIT 许可证
├── daily-brief-config.json       # 配置文件（运行后生成）
├── scripts/
│   ├── init_config.py            # 配置初始化脚本
│   ├── send_feishu.py            # 飞书推送脚本
│   ├── send_wecom.py             # 企业微信推送脚本
│   ├── send_dingtalk.py          # 钉钉推送脚本
│   ├── send_email.py             # 邮件推送脚本
│   └── ...                       # 其他渠道脚本
├── assets/
│   └── report-template.html      # HTML 报告模板
└── references/
    ├── source-guide.md           # 信源使用指南
    └── config-examples.md        # 配置示例
```

---

## 🔧 配置说明

### 配置文件位置

`~/.openclaw/workspace/daily-brief-config.json`

### 完整配置示例

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
      "type": "webhook",
      "webhook_url": ""
    },
    "email": {
      "enabled": false,
      "type": "smtp",
      "smtp_host": "smtp.gmail.com",
      "smtp_port": 587,
      "smtp_user": "",
      "smtp_password": "",
      "from_addr": "",
      "to_addrs": []
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
    }
  }
}
```

### 环境变量（推荐）

敏感信息建议使用环境变量：

```bash
export FEISHU_WEBHOOK_URL="https://..."
export FEISHU_SECRET=""
export SMTP_PASSWORD=""
```

---

## 📊 输出示例

### Markdown 格式

```markdown
## 💰 投资日报 | 2026-03-12

### 📈 市场概览
| 指数 | 收盘 | 涨跌 |
|------|------|------|
| 上证指数 | 3xxx | +x.xx% |
| 标普 500 | 6xxx | -x.xx% |

### 🔥 热点板块
- 🟢 AI 算力 (+x.xx%)
- 🔴 房地产 (-x.xx%)

### 💵 宏观动态
- 【央行】今日开展 xxx 亿元逆回购【来源】

### 🏢 公司动态
- 【财报】腾讯发布 Q4 业绩，超预期【来源】

### 📊 机构观点
- 高盛：上调目标价至 xxx【来源】

### ⚠️ 风险提示
- xxx【来源】
```

---

## 🤖 使用方式

### 手动触发

告诉 AI：
- "生成投资日报"
- "投资日报"
- "market daily brief"
- "今日股市总结"

### 自动执行

配置 cron 任务后，每个交易日自动发送：
- 默认时间：18:00（A 股收盘后）
- 可自定义：`"schedule": "0 9 * * 1-5"`（早上 9 点）

---

## 📝 自定义配置

### 修改关注行业

编辑 `daily-brief-config.json`：

```json
"customization": {
  "focus_areas": [
    "新能源", "半导体", "人工智能",
    "生物医药", "消费电子"
  ]
}
```

### 修改推送时间

```json
"cron": [
  {
    "name": "投资日报",
    "schedule": "0 9 * * 1-5"  // 改为早上 9 点
  }
]
```

### 增加推送渠道

```json
"adapters": {
  "feishu": { "enabled": true, ... },
  "wechatwork": { "enabled": true, ... },
  "email": { "enabled": true, ... }
}
```

---

## 🔍 信源说明

### 第一优先级（官方）

- 中国证监会、中国人民银行、国家统计局
- SEC、Federal Reserve、Bloomberg、Reuters
- 交易所公告（上交所、深交所、港交所、NYSE、NASDAQ）
- 财联社、Wind

### 第二优先级（机构）

- 投行研报：高盛、摩根士丹利、摩根大通、中金、中信
- 券商：华泰、国泰君安、招商、申万
- 财经媒体：华尔街见闻、新浪财经、东方财富

### 严格排除

- 自媒体、搬运号、标题党
- 无来源转述、财经谣言

---

## ⚠️ 注意事项

1. **数据延迟**：免费行情数据可能延迟 15 分钟
2. **推送限制**：各渠道有频率限制（飞书：5 条/分钟）
3. **API Key**：部分渠道需要配置 Webhook 或 API Key
4. **定时任务**：需要 OpenClaw Gateway 运行中

---

## 🐛 故障排查

### 问题 1：收不到推送

检查：
1. Webhook URL 是否正确
2. 机器人是否添加到群聊
3. Gateway 是否运行：`openclaw gateway status`

### 问题 2：数据不完整

检查：
1. 网络连接是否正常
2. 信源网站是否可访问
3. 增加搜索关键词：`customization.search_keywords`

### 问题 3：定时任务未执行

检查：
1. cron 配置是否正确：`openclaw cron list`
2. Gateway 日志：`journalctl -u openclaw-gateway`

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发环境设置

```bash
git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git
cd investment-daily-brief
pip install -r requirements.txt
```

### 提交规范

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `config:` 配置变更

---

## 📞 支持

- GitHub Issues: https://github.com/YOUR_USERNAME/investment-daily-brief/issues
- 文档：https://github.com/YOUR_USERNAME/investment-daily-brief/wiki

---

**投资有风险，入市需谨慎。本技能提供的信息仅供参考，不构成投资建议。**
