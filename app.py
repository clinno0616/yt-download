#pip install streamlit yt-dlp
import streamlit as st
import yt_dlp
import re
import os
from urllib.parse import urlparse, parse_qs

# 建立 videos 目錄
DOWNLOAD_DIR = "videos"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def is_valid_youtube_url(url):
    """檢查是否為有效的YouTube URL"""
    try:
        parsed_url = urlparse(url)
        if 'youtube.com' in parsed_url.netloc or 'youtu.be' in parsed_url.netloc:
            return True
        return False
    except:
        return False

def get_video_info(url):
    """獲取影片資訊"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Unknown'),
                'duration': f"{int(info.get('duration', 0)) // 60}分{int(info.get('duration', 0)) % 60}秒",
                'thumbnail': info.get('thumbnail', ''),
                'channel': info.get('channel', 'Unknown'),
                'view_count': f"{info.get('view_count', 0):,}"
            }
    except Exception as e:
        st.error(f"獲取影片資訊時發生錯誤: {str(e)}")
        return None

def download_video(url, download_type):
    """下載影片"""
    try:
        output_template = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
        
        if download_type == "MP3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': output_template,
            }
        else:  # MP4
            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': output_template,
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if download_type == "MP3":
                return f"{ydl.prepare_filename(info)[:-4]}.mp3"
            else:
                return ydl.prepare_filename(info)
                
    except Exception as e:
        st.error(f"下載時發生錯誤: {str(e)}")
        return None

def list_downloaded_files():
    """列出已下載的檔案"""
    try:
        files = os.listdir(DOWNLOAD_DIR)
        files = [f for f in files if f.endswith(('.mp3', '.mp4'))]
        return files
    except Exception as e:
        st.error(f"讀取檔案列表時發生錯誤: {str(e)}")
        return []

def main():
    st.title("YouTube 影片下載器")
    st.write("請輸入YouTube影片網址，選擇下載格式")
    
    # 顯示已下載檔案列表
    st.sidebar.title("已下載檔案")
    downloaded_files = list_downloaded_files()
    if downloaded_files:
        st.sidebar.write(f"共 {len(downloaded_files)} 個檔案在 videos 目錄中:")
        for file in downloaded_files:
            st.sidebar.write(f"- {file}")
    else:
        st.sidebar.write("目前沒有已下載的檔案")
    
    # 輸入URL
    url = st.text_input("YouTube URL")
    
    if url:
        if not is_valid_youtube_url(url):
            st.error("請輸入有效的YouTube URL")
            return
        
        # 獲取影片資訊
        video_info = get_video_info(url)
        if video_info:
            if video_info['thumbnail']:
                st.image(video_info['thumbnail'], use_container_width=True)
            st.write(f"標題: {video_info['title']}")
            st.write(f"頻道: {video_info['channel']}")
            st.write(f"影片長度: {video_info['duration']}")
            st.write(f"觀看次數: {video_info['view_count']}")
            
            # 選擇下載格式
            download_type = st.radio("選擇下載格式:", ("MP4", "MP3"))
            
            if st.button("下載"):
                with st.spinner("下載中...請稍候"):
                    output_file = download_video(url, download_type)
                    if output_file and os.path.exists(output_file):
                        st.success(f"下載完成！檔案已儲存在 videos 目錄: {os.path.basename(output_file)}")
                        # 提供下載連結
                        with open(output_file, 'rb') as file:
                            st.download_button(
                                label=f"下載 {download_type} 檔案",
                                data=file,
                                file_name=os.path.basename(output_file),
                                mime="audio/mp3" if download_type == "MP3" else "video/mp4"
                            )

if __name__ == "__main__":
    main()