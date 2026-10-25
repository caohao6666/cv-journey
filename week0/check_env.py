"""第 0 周环境自检：Python / PyTorch CUDA / 关键依赖 / Git 代理 / 网络。

用法：python week0/check_env.py
提示：若终端中文显示乱码，先执行 chcp 65001 再运行。
"""

import importlib.metadata
import shutil
import socket
import sys
import time
import urllib.request

OK = "[OK]  "
WARN = "[WARN]"
BAD = "[BAD] "

issues = []


def check_packages():
    print("\n== 依赖版本 ==")
    for name in [
        "torch", "torchvision", "ultralytics", "opencv-python",
        "numpy", "matplotlib", "pillow", "ipykernel",
    ]:
        try:
            print(f"  {name:16s} {importlib.metadata.version(name)}")
        except importlib.metadata.PackageNotFoundError:
            print(f"  {name:16s} 未安装")
            if name in ("torch", "torchvision", "ultralytics"):
                issues.append(f"{name} 未安装")


def check_cuda():
    print("\n== PyTorch / CUDA ==")
    try:
        import torch
    except ImportError:
        print(BAD, "无法 import torch")
        issues.append("torch 不可用")
        return
    print(f"  torch      : {torch.__version__}")
    print(f"  torch cuda : {torch.version.cuda}")
    print(f"  cudnn      : {torch.backends.cudnn.version()}")
    print(f"  cuda avail : {torch.cuda.is_available()}")
    if not torch.cuda.is_available():
        print(BAD, "CUDA 不可用：检查是否装了 CPU 版 torch / 显卡驱动")
        issues.append("torch.cuda.is_available() == False")
        return
    for i in range(torch.cuda.device_count()):
        p = torch.cuda.get_device_properties(i)
        print(f"  GPU[{i}]     : {p.name} | sm_{p.major}{p.minor} | {p.total_memory / 1024**3:.1f} GiB")
    a = torch.randn(2048, 2048, device="cuda", dtype=torch.float16)
    b = torch.randn(2048, 2048, device="cuda", dtype=torch.float16)
    for _ in range(3):
        a @ b
    torch.cuda.synchronize()
    t0 = time.time()
    for _ in range(10):
        a @ b
    torch.cuda.synchronize()
    dt = (time.time() - t0) / 10
    print(f"  fp16 2048^3 单次 {dt * 1000:.1f} ms -> {2 * 2048**3 / dt / 1e12:.1f} TFLOP/s")


def check_git():
    print("\n== Git ==")
    git = shutil.which("git")
    if not git:
        print(BAD, "git 不在 PATH")
        issues.append("git 未安装")
        return
    import subprocess

    ver = subprocess.run([git, "--version"], capture_output=True, text=True).stdout.strip()
    print(f"  {ver}")
    cfg = subprocess.run(
        [git, "config", "--global", "--get", "http.proxy"], capture_output=True, text=True
    ).stdout.strip()
    if cfg:
        print(f"  全局 http.proxy = {cfg}")
        try:
            host_port = cfg.split("://")[-1].split("/")[0]
            host, port = host_port.rsplit(":", 1)
            with socket.create_connection((host, int(port)), timeout=2):
                print(OK, "代理端口可连接")
        except OSError:
            print(BAD, "代理端口连不上！git clone/push 会失败。")
            print("        解决：启动你的代理软件，或执行")
            print("        git config --global --unset http.proxy")
            print("        git config --global --unset https.proxy")
            issues.append("git 配置了不可用的代理")
    else:
        print("  未配置代理（直连）")


def _speed(url, seconds=6.0):
    t0 = time.time()
    n = 0
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            while time.time() - t0 < seconds:
                chunk = r.read(1 << 16)
                if not chunk:
                    break
                n += len(chunk)
    except Exception as e:  # noqa: BLE001
        return None, str(e)
    return n / (time.time() - t0) / 1024, ""


def check_network():
    print("\n== 网络（GitHub 相关） ==")
    asset = "https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo11n.pt"
    for label, url in [
        ("PyPI", "https://pypi.org/simple/"),
        ("GitHub", asset),
        ("ghfast 镜像", "https://ghfast.top/" + asset),
    ]:
        kbs, err = _speed(url)
        if kbs is None:
            print(f"  {label:12s} 连不上：{err[:60]}")
            if label != "PyPI":
                issues.append(f"{label} 不可达")
        else:
            print(f"  {label:12s} ~{kbs:8.1f} KB/s")
            if label == "GitHub" and kbs < 100:
                print("        直连 GitHub 很慢：下载 release 用 https://ghfast.top/ 前缀")


def check_disk():
    print("\n== 磁盘 ==")
    for drive in ("C:\\", "D:\\"):
        try:
            usage = shutil.disk_usage(drive)
            print(f"  {drive} 总 {usage.total / 1024**3:6.1f} GB  剩余 {usage.free / 1024**3:6.1f} GB")
        except OSError:
            pass


def main():
    print(f"Python : {sys.version.split()[0]}  ({sys.executable})")
    check_packages()
    check_cuda()
    check_git()
    check_network()
    check_disk()

    print("\n== 结论 ==")
    if issues:
        print(BAD, "发现问题：")
        for it in issues:
            print("   -", it)
        sys.exit(1)
    print(OK, "全部通过，可以开始第 1 周。")


if __name__ == "__main__":
    main()
