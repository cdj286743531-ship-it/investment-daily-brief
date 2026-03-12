# 投资日报技能 - 安装指南

## 📦 打包发布

### 方式 1: GitHub 发布（推荐）

1. **创建 GitHub 仓库**
   ```bash
   cd ~/.openclaw/workspace/skills/investment-daily-brief
   git init
   git add .
   git commit -m "Initial release: investment daily brief skill"
   ```

2. **推送到 GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/investment-daily-brief.git
   git push -u origin main
   ```

3. **分享安装命令**
   ```bash
   git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief
   ```

### 方式 2: clawhub 发布

1. **安装 clawhub**
   ```bash
   pnpm install -g clawhub
   ```

2. **发布技能**
   ```bash
   cd ~/.openclaw/workspace/skills/investment-daily-brief
   clawhub publish
   ```

3. **分享安装命令**
   ```bash
   clawhub install investment-daily-brief
   ```

### 方式 3: 直接分享文件

1. **打包技能**
   ```bash
   cd ~/.openclaw/workspace/skills/
   tar -czf investment-daily-brief.tar.gz investment-daily-brief/
   ```

2. **分享压缩包**
   - 通过邮件、微信、飞书等方式发送
   - 接收方解压到 `~/.openclaw/workspace/skills/`

---

## 📋 给用户的安装说明

### 安装步骤

```bash
# 1. 克隆技能
git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief

# 2. 初始化配置
cd ~/.openclaw/workspace/skills/investment-daily-brief
python scripts/init_config.py

# 3. 配置飞书机器人
# 编辑 daily-brief-config.json，填入你的 Webhook URL

# 4. 设置定时任务（可选）
openclaw cron add --name "投资日报" --schedule "0 18 * * 1-5"

# 5. 测试
# 告诉 AI：「生成投资日报」
```

### 配置飞书机器人

1. 打开飞书群 → 群设置 → 群机器人
2. 添加机器人 → 自定义机器人
3. 复制 Webhook URL
4. 编辑 `daily-brief-config.json`，填入 URL：
   ```json
   {
     "adapters": {
       "feishu": {
         "enabled": true,
         "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
       }
     }
   }
   ```

---

## 🔧 自定义配置

### 修改推送时间

编辑 `daily-brief-config.json`：

```json
"cron": [
  {
    "name": "投资日报",
    "schedule": "0 9 * * 1-5"  // 改为早上 9 点
  }
]
```

### 增加关注行业

```json
"customization": {
  "focus_areas": [
    "A 股市场", "港股市场", "美股市场",
    "新能源", "半导体", "人工智能"  // 添加你关注的行业
  ]
}
```

### 增加推送渠道

```json
"adapters": {
  "feishu": { "enabled": true, ... },
  "wechatwork": { "enabled": true, "webhook_url": "..." },
  "email": { "enabled": true, ... }
}
```

---

## ❓ 常见问题

### Q: 收不到推送？

A: 检查：
1. Webhook URL 是否正确
2. 机器人是否添加到群聊
3. Gateway 是否运行：`openclaw gateway status`

### Q: 数据不完整？

A: 检查网络连接，部分财经网站有反爬限制。

### Q: 如何禁用定时任务？

A: 编辑 `daily-brief-config.json`，设置 `"enabled": false`

---

## 📞 技术支持

- GitHub Issues: https://github.com/YOUR_USERNAME/investment-daily-brief/issues
- 文档：SKILL.md
