# AI Watch Shop (Monorepo)

Repo chung cho hai mô-đun:
- `ai-recommend`: AI Recommendation Service (Python)
- `chatbot2`: Rasa Chatbot (Python)

## Cấu trúc thư mục
- `ai-recommend/`: Mã nguồn AI gợi ý đồng hồ (train, serve API)
- `chatbot2/`: Chatbot Rasa (NLU, stories, actions)

## Quick Start

### 1) AI Recommendation Service (`ai-recommend`)
```bash
cd ai-recommend
# (khuyến nghị) tạo venv
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements_ai_server.txt

# cấu hình môi trường (tuỳ chọn)
copy env_example.txt .env  # hoặc tự tạo .env

# chạy nhanh (Windows)
./setup_and_start.bat
# hoặc
python ai_server.py
```

### 2) Chatbot Rasa (`chatbot2`)
```bash
cd chatbot2
# (khuyến nghị) tạo venv riêng
python -m venv rasaenv
. rasaenv/Scripts/activate  # Windows PowerShell: rasaenv\Scripts\Activate.ps1
pip install -r requirements.txt

# chạy bot (Windows)
./start_actions.bat
./start_server.bat
```

## Khởi tạo Git repo mới (tại thư mục gốc)
```bash
cd C:\PHU\STUDY\DATN\ai-watch-shop

git init -b main  # nếu lỗi, dùng: git init && git branch -M main
git add .
git commit -m "Initial commit: combine ai-recommend and chatbot2 into one repo"
# thay URL bên dưới bằng repo của bạn
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Ghi chú
- Nên bổ sung `.gitignore` để bỏ `/.venv`, `/models`, `/.rasa`, các file tạm.
- Các script `.bat` đã sẵn cho Windows; trên Linux/macOS dùng script `.sh` tương ứng.
