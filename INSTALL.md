# 🚀 EmoStream Installation Guide

**Super simple setup - just copy and paste!**

## 📋 What You Need

- **Docker** installed on your computer
- **Terminal/Command Prompt** (comes with your computer)
- **5 minutes** of your time

## 🔧 Step 1: Install Docker

### Windows/Mac
1. Go to [https://docker.com](https://docker.com)
2. Click "Download for Windows" or "Download for Mac"
3. Install the downloaded file
4. Restart your computer

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
# Logout and login again
```

### Linux (Arch/Manjaro)
```bash
sudo pacman -S docker docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
# Logout and login again
```

## 📥 Step 2: Get the Code

### Option A: Download ZIP (Easiest)
1. Click the green "Code" button on GitHub
2. Click "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

### Option B: Use Git
```bash
git clone https://github.com/yourusername/EmoStream.git
cd EmoStream
```

## 🚀 Step 3: Start Everything

**Copy and paste this command:**
```bash
docker-compose up --build -d
```

**What happens:**
- Docker downloads some images (first time only)
- Builds your application
- Starts all services

**Wait until you see:**
- "Started" messages
- No more progress bars
- Your terminal prompt returns

## ✅ Step 4: Test It Works

**Copy and paste this command:**
```bash
curl http://localhost:5000/
```

**You should see:**
```json
{
  "status": "healthy",
  "service": "EmoStream API"
}
```

🎉 **Success! Your EmoStream is running!**

## 🎯 Step 5: Try It Out

**Send your first emoji:**
```bash
curl -X POST http://localhost:5000/emoji \
  -H "Content-Type: application/json" \
  -d '{"emoji_type": "😊", "timestamp": "2025-08-13T20:45:00Z"}'
```

**Expected response:**
```json
{
  "message": "Emoji sent successfully"
}
```

## 🛑 When You're Done

**Stop everything:**
```bash
docker-compose down
```

## 🆘 Need Help?

**Check if services are running:**
```bash
docker-compose ps
```

**View logs:**
```bash
docker-compose logs app
```

**Common issues:**
- **"Docker not found"** → Install Docker first
- **"Port in use"** → Run `docker-compose down` first
- **"Permission denied"** → Add your user to docker group (Linux)

## 🎮 What Next?

- Try different emojis: 😂 ❤️ 👍 🎉 🚀 🌟
- Register clients and see how they get assigned
- Check out the full README for more features
- Explore the code to understand how it works

**Happy emoji streaming! 🎉**
