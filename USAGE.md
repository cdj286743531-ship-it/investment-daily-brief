# OpenClaw 投资日报技能 - 使用说明

## 📋 技能定位

这是一个 **OpenClaw Skill 配置包**，核心功能由 OpenClaw AI 引擎提供：

| 组件 | 负责内容 |
|------|---------|
| **OpenClaw AI** | 抓取财经信息、AI 分析总结、生成日报内容 |
| **本技能** | 推送渠道配置、定时任务配置、辅助脚本 |

---

## 🚀 使用方式

### 方式 1：OpenClaw AI 自动生成（推荐）

**适用场景**：想让 AI 自动搜集信息并生成日报

**步骤**：

1. **安装技能**
   ```bash
   git clone https://github.com/cdj286743531-ship-it/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief
   ```

2. **初始化配置**
   ```bash
   cd ~/.openclaw/workspace/skills/investment-daily-brief
   python scripts/init_config.py
   ```

3. **配置飞书 Webhook**
   编辑 `~/.openclaw/workspace/daily-brief-config.json`：
   ```json
   {
     "adapters": {
       "feishu": {
         "enabled": true,
         "webhook_url": "你的飞书机器人 URL"
       }
     }
   }
   ```

4. **设置定时任务**
   ```bash
   openclaw cron add --name "投资日报" --schedule "0 18 * * 1-5"
   ```

5. **AI 会自动执行**：
   - 每天 18:00 自动触发
   - AI 搜集 A 股/港股/美股数据
   - AI 分析宏观动态、机构观点
   - AI 生成日报并发送到飞书

**手动触发**：
```
告诉 AI：「生成投资日报」
```

---

### 方式 2：独立脚本推送

**适用场景**：已有日报内容，只需要推送功能

**步骤**：

1. **准备内容**
   ```bash
   CONTENT="## 💰 投资日报\n\n### 📈 市场概览\n..."
   ```

2. **推送**
   ```bash
   cd ~/.openclaw/workspace/skills/investment-daily-brief
   python scripts/send_feishu.py \
     --webhook "你的飞书 Webhook URL" \
     --content "$CONTENT"
   ```

---

## 🔧 核心配置说明

### daily-brief-config.json

```json
{
  "adapters": {
    "feishu": {
      "enabled": true,      // 是否启用
      "webhook_url": "",    // 飞书机器人 URL
      "secret": ""          // 签名密钥（可选）
    }
  },
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 18 * * 1-5",  // 工作日 18:00
      "timezone": "Asia/Shanghai"
    }
  ],
  "customization": {
    "focus_areas": ["A 股市场", "港股市场", "美股市场"],  // 关注领域
    "stock_focus": {
      "indices": ["上证指数", "恒生指数", "标普 500"],  // 关注指数
      "sectors": ["科技", "金融", "消费"]  // 关注行业
    }
  }
}
```

---

## 📊 AI 生成逻辑

当 AI 执行「生成投资日报」任务时，会自动：

1. **搜集信息**
   - 使用 `web_search` 搜索关键词（A 股收盘、港股收盘、美股收盘等）
   - 使用 `web_fetch` 抓取财经网站（财联社、新浪财经、Reuters 等）

2. **分析整理**
   - 过滤低质信息（自媒体、标题党）
   - 交叉验证重要新闻
   - 按模块整理（市场概览、热点板块、宏观动态等）

3. **生成日报**
   - 输出 Markdown 格式
   - 标注数据来源
   - 提供策略建议

4. **发送推送**
   - 调用 `message` 工具发送到飞书
   - 或调用 `send_feishu.py` 脚本

---

## ⚠️ 注意事项

### 1. 数据源限制

- 免费行情数据可能延迟 15 分钟
- 部分财经网站有反爬限制
- 建议配合专业交易软件使用

### 2. 推送渠道限制

| 渠道 | 频率限制 | 配置难度 |
|------|---------|---------|
| 飞书 | 5 条/分钟 | ⭐⭐ |
| 企业微信 | 20 条/分钟 | ⭐⭐ |
| 钉钉 | 20 条/分钟 | ⭐⭐ |
| 邮件 | 取决于 SMTP | ⭐⭐⭐ |

### 3. 定时任务依赖

- 需要 OpenClaw Gateway 运行中
- 检查状态：`openclaw gateway status`
- 查看日志：`journalctl -u openclaw-gateway`

---

## 🐛 故障排查

### 问题 1：收不到推送

**检查**：
1. Webhook URL 是否正确
2. 机器人是否添加到群聊
3. Gateway 是否运行

**解决**：
```bash
openclaw gateway status
openclaw cron list
```

### 问题 2：AI 生成内容不完整

**检查**：
1. 网络连接是否正常
2. 信源网站是否可访问
3. 搜索关键词是否合适

**解决**：
编辑 `daily-brief-config.json`，增加搜索关键词：
```json
"search_keywords": {
  "cn": ["A 股 收盘 涨跌", "央行 逆回购", ...]
}
```

### 问题 3：定时任务未执行

**检查**：
```bash
openclaw cron list  # 查看任务状态
journalctl -u openclaw-gateway -n 50  # 查看日志
```

---

## 📝 自定义示例

### 只关注科技股

```json
{
  "customization": {
    "focus_areas": ["半导体", "人工智能", "消费电子"],
    "stock_focus": {
      "indices": ["纳斯达克 100", "科创 50", "恒生科技"],
      "sectors": ["科技", "通信", "传媒"]
    }
  }
}
```

### 早上 9 点推送（开盘前）

```json
{
  "cron": [
    {
      "name": "投资日报",
      "schedule": "0 9 * * 1-5"
    }
  ]
}
```

### 增加邮件推送

```json
{
  "adapters": {
    "feishu": { "enabled": true, ... },
    "email": {
      "enabled": true,
      "smtp_host": "smtp.gmail.com",
      "smtp_user": "your@gmail.com",
      "smtp_password": "your_password",
      "to_addrs": ["recipient@example.com"]
    }
  }
}
```

---

## 📞 技术支持

- GitHub Issues: https://github.com/cdj286743531-ship-it/investment-daily-brief/issues
- OpenClaw 文档：https://docs.openclaw.ai

---

**投资有风险，入市需谨慎。本技能提供的信息仅供参考，不构成投资建议。**
