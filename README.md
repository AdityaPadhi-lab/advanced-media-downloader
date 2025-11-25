# 🎥 Advanced Media Downloader

A powerful Python-based media downloader built to download videos and audio from multiple platforms with clean workflow, modular architecture, and batch processing support.

---

## 🚀 Features

- Download **video/audio** from multiple platforms  
- **Batch downloading** using text files  
- Choose **output format** (mp4, mp3, wav, etc.)  
- Custom **output directory**  
- **Naming templates** for organized files  
- Error-handled and stable pipeline  
- Modular code for easy maintenance and future upgrades  

---

## 🧠 Project Workflow (How the System Works)

Below is the complete workflow to help others understand the system clearly.

### 1️⃣ Input Handling
- Accepts:
  - A **single URL**
  - A **batch file** (`urls.txt`)
- Arguments parsed via `argparse`.

### 2️⃣ URL Validation
- Checks for:
  - Empty URLs  
  - Invalid links  
  - Unsupported platforms  
- Invalid links are skipped but logged.

### 3️⃣ Downloader Engine
- Uses `yt-dlp` or custom logic.
- Supports:
  - Video quality selection  
  - Audio-only extraction  
  - Format selection  
  - Metadata extraction  

### 4️⃣ Processing Pipeline
After the download starts:
- Metadata fetched  
- Name formatted  
- File saved  
- Conversion (if selected)  
- Progress displayed  

### 5️⃣ Output Handling

Downloads stored in:


File name format:


### 6️⃣ Logging & Error Management
- Logs each download with:
  - URL
  - Timestamp
  - Output file path
  - Failure messages (if any)
- Batch mode continues even when a link fails.

### 7️⃣ Directory Structure


---

## 🖥️ Usage

### ▶️ Download a Single URL
```bash
python cli.py --url "https://youtube.com/..."
python cli.py --batch urls.txt
python cli.py --url <URL> --output-dir ./downloads
python cli.py --help
git clone https://github.com/AdityaPadhi-lab/advanced-media-downloader.git
cd advanced-media-downloader
pip install -r requirements.txt
pytest
