@echo off
REM 🎉 EmoStream Demo Script for Windows
REM Run this to test your system!

echo 🚀 Starting EmoStream Demo...
echo ================================

REM Wait for services to be ready
echo ⏳ Waiting for services to start...
timeout /t 5 /nobreak >nul

REM Test health endpoint
echo ✅ Testing health endpoint...
curl -s http://localhost:5000/

echo.
echo 🎯 Testing emoji submission...
curl -s -X POST http://localhost:5000/emoji -H "Content-Type: application/json" -d "{\"emoji_type\": \"😊\", \"timestamp\": \"%date:~-4%-%date:~3,2%-%date:~0,2%T%time:~0,2%:%time:~3,2%:%time:~6,2%Z\"}"

echo.
echo 👤 Testing client registration...
curl -s -X POST http://localhost:5000/register_client -H "Content-Type: application/json" -d "{\"client_id\": \"demo_user\"}"

echo.
echo 📋 Listing clients...
curl -s http://localhost:5000/list_clients

echo.
echo 🎉 Demo complete! Your EmoStream is working!
echo.
echo 💡 Try these commands:
echo    curl http://localhost:5000/
echo    curl -X POST http://localhost:5000/emoji -H "Content-Type: application/json" -d "{\"emoji_type\": \"🚀\", \"timestamp\": \"%date:~-4%-%date:~3,2%-%date:~0,2%T%time:~0,2%:%time:~3,2%:%time:~6,2%Z\"}"
echo.
echo 🛑 To stop everything: docker-compose down

pause
