# ⚡ EmoStream Quick Start

**3 commands to get running!**

## 🚀 Start Everything
```bash
docker-compose up --build -d
```

## ✅ Test It Works
```bash
curl http://localhost:5000/
```

## 🎯 Send Your First Emoji
```bash
curl -X POST http://localhost:5000/emoji \
  -H "Content-Type: application/json" \
  -d '{"emoji_type": "😊", "timestamp": "2025-08-13T20:45:00Z"}'
```

## 🛑 Stop Everything
```bash
docker-compose down
```

---

**That's it!** 🎉

**Need more details?** Check `INSTALL.md` for step-by-step instructions.
**Want to explore?** Check `README.md` for full features and examples.
