"""第 0 周最小可跑推理：用 YOLO11n 在 GPU 上检测一张图。

用法：
    python week0/yolo_demo.py week0/bus.jpg
    python week0/yolo_demo.py https://ultralytics.com/images/bus.jpg
"""

import os
import sys
import time

from ultralytics import YOLO

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEIGHT = os.path.join(ROOT, "yolo11n.pt")


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "week0", "bus.jpg")
    if not os.path.exists(WEIGHT):
        print("找不到权重 yolo11n.pt，开始下载（GitHub 慢的话见 README 的 ghfast.top 用法）")
    model = YOLO(WEIGHT)
    device = 0 if _cuda_ok() else "cpu"
    t0 = time.time()
    results = model.predict(src, device=device, imgsz=640, verbose=False,
                            save=True, project=os.path.join(ROOT, "runs"), name="week0_demo")
    r = results[0]
    print(f"设备        : {'cuda:0' if device == 0 else 'cpu'}")
    print(f"耗时        : {(time.time() - t0) * 1000:.1f} ms (含首轮预热)")
    print(f"各阶段 ms   : {r.speed}")
    print(f"检测到 {len(r.boxes)} 个目标:")
    for box in r.boxes:
        cls = r.names[int(box.cls)]
        print(f"  - {cls:10s} conf={float(box.conf):.2f}  xyxy={[round(v, 1) for v in box.xyxy[0].tolist()]}")
    print(f"结果图片    : {r.save_dir}")


def _cuda_ok():
    try:
        import torch

        return torch.cuda.is_available()
    except Exception:  # noqa: BLE001
        return False


if __name__ == "__main__":
    main()
