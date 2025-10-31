@echo off
chcp 65001 >nul

echo =======================
echo  STOP ALL SERVERS TOOL
echo =======================
echo.
echo File này sẽ dừng tất cả tiến trình liên quan đến:
echo - python.exe chạy ai_server.py/scheduler.py
echo - rasa.exe, rasa run, rasa actions
echo.
set /p CONFIRM="Bạn có muốn tiếp tục? (YES/NO): "
if /I NOT "%CONFIRM%"=="YES" (
    echo Hủy thao tác!
    timeout /t 1 >nul
    exit /b
)

echo Đang tìm và dừng các server liên quan...

REM --- Kill AI Recommendation Server
taskkill /F /IM python.exe /FI "WINDOWTITLE eq AI Server*" >nul 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Scheduler*" >nul 2>nul

REM --- Kill Rasa (tìm tiến trình có từ 'rasa' hoặc tên cửa sổ Rasa...)
taskkill /F /IM rasa.exe >nul 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Rasa Server*" >nul 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Rasa Action Server*" >nul 2>nul

REM --- Đóng tất cả cmd windows mở bởi launcher (cẩn thận không đóng shell chính)
REM (Chỉ nên dùng với các CMD mà bạn xác định là server, tránh kill nhầm shell chính)
REM Nếu cần gọn gàng hơn dùng: taskkill /F /FI "WINDOWTITLE eq *Server*"

echo Đã gửi tín hiệu dừng các tiến trình server!
echo (Nếu còn sót, hãy tự đóng những cửa sổ cmd còn lại hoặc đóng bằng Task Manager.)
echo Xong.
pause
exit /b
