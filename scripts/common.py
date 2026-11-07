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


# ---------- 跨平台：UTF-8 输出、gh、设备名 ----------

def utf8_stdio():
    """Windows PowerShell 默认非 UTF-8，中文会乱码或报错"""
    import sys
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def find_gh():
    """gh 可执行文件路径；没有返回 None"""
    import shutil
    exe = shutil.which("gh")
    if exe:
        return exe
    local = os.path.expanduser("~/.local/bin/gh")
    return local if os.path.exists(local) else None


def run(cmd, input=None):
    """跑命令，返回 (退出码, stdout, stderr)；命令不存在时退出码 127"""
    import subprocess
    try:
        p = subprocess.run(cmd, cwd=ROOT, input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           encoding="utf-8", errors="replace")
    except OSError as e:
        return 127, "", str(e)
    return p.returncode, p.stdout, p.stderr


DEVICE_FILE = os.path.join(ROOT, ".learn-device")


def device_name():
    """本设备的名字：.learn-device 第一行，缺省 hostname"""
    import socket
    try:
        with open(DEVICE_FILE, encoding="utf-8") as f:
            name = f.readline().strip()
        if name:
            return name
    except OSError:
        pass
    return socket.gethostname()
