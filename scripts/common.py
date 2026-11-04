"""脚本共用的路径与小工具"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE = os.path.join(ROOT, "course")
EXTRACTED = os.path.join(COURSE, "extracted")
FRAMES = os.path.join(COURSE, "frames")
LEVELS = os.path.join(COURSE, "levels")


def stem(path):
    return os.path.splitext(os.path.basename(path))[0]


def hms(sec):
    sec = int(sec)
    return "%02d:%02d:%02d" % (sec // 3600, sec % 3600 // 60, sec % 60)


def parse_hms(s):
    parts = [float(x) for x in s.strip().replace(",", ".").split(":")]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def ffmpeg_exe():
    """优先系统 ffmpeg，其次 venv 里 imageio-ffmpeg 自带的"""
    import shutil
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        raise SystemExit("找不到 ffmpeg：先运行 bash scripts/setup.sh 并 source .venv/bin/activate")
