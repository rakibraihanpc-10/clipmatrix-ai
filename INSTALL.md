"""
Installation and setup guide
"""

# ClipMatrix AI - Installation Guide

## System Requirements

- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB+ recommended)
- **GPU**: NVIDIA GPU with CUDA support (optional, for acceleration)
- **Disk Space**: 2GB free space for temporary files

## Step-by-Step Installation

### 1. Install Python

Download Python 3.9+ from [python.org](https://www.python.org/downloads/)

Verify installation:
```bash
python --version
```

### 2. Install FFmpeg

**Windows (using Chocolatey):**
```bash
choco install ffmpeg
```

**Windows (manual):**
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\FFmpeg`
3. Add to PATH environment variable

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

### 3. Clone Repository

```bash
git clone https://github.com/rakibraihanpc-10/clipmatrix-ai.git
cd clipmatrix-ai
```

### 4. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. (Optional) Install CUDA for GPU Acceleration

For NVIDIA GPU support:
1. Download CUDA from https://developer.nvidia.com/cuda-downloads
2. Install CUDA Toolkit
3. FFmpeg will automatically detect and use GPU

### 7. Run Application

```bash
python main.py
```

## Troubleshooting

### FFmpeg not found
- Ensure FFmpeg is installed and added to PATH
- Restart terminal/IDE after installation
- Verify: `ffmpeg -version`

### PyQt6 import errors
```bash
pip install --upgrade PyQt6 PyQt6-Qt6
```

### GPU not detected
- Ensure NVIDIA drivers are up to date
- Install CUDA Toolkit
- Test with: `ffmpeg -codecs | grep nvenc`

### Memory errors during processing
- Close other applications
- Reduce video quality setting (higher CRF value)
- Process smaller video files

### Permission denied (Linux/macOS)
```bash
chmod +x main.py
```

## Performance Tips

1. **GPU Acceleration**: Install CUDA for 5-10x faster processing
2. **Quality vs Speed**: Higher CRF = smaller files but faster encoding
3. **Batch Processing**: Process multiple videos sequentially
4. **Disk Space**: Ensure 2GB+ free space for temporary files

## Next Steps

1. Open the application: `python main.py`
2. Drag & drop a video file
3. Configure processing options
4. Click "PROCESS VIDEO"
5. Monitor progress in the terminal log

Enjoy using ClipMatrix AI!
