# 投资日报生成器

🤖 AI 驱动的投资日报自动生成技能

## 功能特性

- 📈 多市场覆盖（A 股/港股/美股）
- 🔥 热点板块追踪
- 💵 宏观经济与政策
- 🏢 公司公告与财报
- 📊 机构评级与目标价
- ⚠️ 风险提示
- 📅 周度事件日历
- 💡 投资策略建议

## 快速开始

### 1. 安装

```bash
git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief
```

### 2. 初始化配置

```bash
cd ~/.openclaw/workspace/skills/investment-daily-brief
python scripts/init_config.py
```

### 3. 配置推送渠道

编辑 `daily-brief-config.json`

### 4. 设置定时任务

```bash
openclaw cron add --name "投资日报" --schedule "0 18 * * 1-5"
```

## 使用方法

**手动触发：**
- "生成投资日报"
- "investment daily brief"
- "今日股市总结"

**自动执行：**
- 配置 cron 后，交易日 18:00 自动发送

## 支持渠道

- ✅ 飞书
- ✅ 企业微信
- ✅ 钉钉
- ✅ 邮件
- ✅ Slack
- ✅ Discord
- ✅ Telegram
- ✅ Teams

## 配置示例

详见 [SKILL.md](SKILL.md)

## 许可证

MIT
