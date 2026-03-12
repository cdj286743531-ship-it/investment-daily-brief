# Investment Daily Brief Generator

🤖 AI-powered investment daily brief generator for OpenClaw.

## Features

- 📈 Multi-market coverage (A-shares, HK stocks, US stocks)
- 🔥 Hot sectors and themes tracking
- 💵 Macro economic news and policy updates
- 🏢 Company announcements and earnings
- 📊 Institutional ratings and price targets
- ⚠️ Risk alerts and black swan events
- 📅 Weekly event calendar
- 💡 Investment strategy suggestions

## Quick Start

### 1. Install

```bash
git clone https://github.com/YOUR_USERNAME/investment-daily-brief.git ~/.openclaw/workspace/skills/investment-daily-brief
```

### 2. Initialize Config

```bash
cd ~/.openclaw/workspace/skills/investment-daily-brief
python scripts/init_config.py
```

### 3. Configure

Edit `daily-brief-config.json` to enable your preferred channels.

### 4. Set Cron

```bash
openclaw cron add --name "Investment Daily" --schedule "0 18 * * 1-5"
```

## Usage

**Manual Trigger:**
- "生成投资日报"
- "investment daily brief"
- "market summary"

**Auto Execution:**
- Configured cron job runs at 18:00 on trading days

## Documentation

See [README_zh.md](README_zh.md) for Chinese documentation.

## License

MIT
