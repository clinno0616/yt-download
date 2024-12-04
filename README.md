# YouTube 下載器

這是一個使用 Streamlit 建立的 YouTube 影片下載工具，支援下載 MP3 和 MP4 格式。

## 功能特點

- 支援 YouTube 影片下載
- 可選擇 MP3 或 MP4 格式
- 顯示影片詳細資訊（標題、頻道、時長、觀看次數）
- 自動將檔案儲存在 videos 目錄
- 側邊欄顯示已下載檔案列表

## 安裝需求

### 1. Python 套件
```bash
pip install streamlit yt-dlp
```

### 2. FFmpeg 安裝

#### Windows
使用 Chocolatey：
```bash
choco install ffmpeg
```
或手動安裝：
1. 下載 [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)
2. 解壓縮到指定目錄（例如 C:\ffmpeg）
3. 將 bin 目錄加入環境變數 Path（例如 C:\ffmpeg\bin）

#### MacOS
使用 Homebrew：
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

## 使用方法

1. 啟動應用程式：
```bash
streamlit run app.py
```

2. 在瀏覽器中開啟顯示的網址（通常是 http://localhost:8501）

3. 貼上 YouTube 影片網址

4. 選擇下載格式（MP3 或 MP4）

5. 點擊下載按鈕

6. 下載完成後，檔案會自動儲存在 `videos` 目錄中

## 注意事項

- 請確保有足夠的硬碟空間
- 只支援公開的 YouTube 影片
- 下載速度取決於網路連線和影片大小
- 請遵守 YouTube 的服務條款和版權規定

## 目錄結構

```
.
├── app.py          # 主程式
├── videos/         # 下載檔案存放目錄
└── README.md       # 說明文件
```

## 故障排除

1. FFmpeg 相關錯誤：
   - 確認 FFmpeg 已正確安裝
   - 確認環境變數設定正確
   - 重新啟動終端機/命令提示字元

2. 下載錯誤：
   - 確認網址是否正確
   - 確認影片是否為公開影片
   - 確認網路連線狀態

## 更新紀錄

### v1.0.0
- 初始版本
- 支援 MP3 和 MP4 下載
- 新增檔案管理功能
- 新增下載狀態顯示
