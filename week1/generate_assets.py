"""生成第 1 周练习用的合成测试图（可重复生成，颜色/位置固定）。

运行：python week1/generate_assets.py
生成：week1/assets/shapes.png（640x480，白底，红圆 + 蓝方块 + 绿三角）
"""

from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def main():
    ASSETS.mkdir(exist_ok=True)
    img = np.full((480, 640, 3), 255, dtype=np.uint8)  # 白底

    # 红圆：圆心 (160,120)，半径 60
    cv2.circle(img, (160, 120), 60, (0, 0, 255), -1)
    # 蓝方块：(360,100)-(560,260)
    cv2.rectangle(img, (360, 100), (560, 260), (255, 0, 0), -1)
    # 绿三角：三个顶点
    tri = np.array([[320, 440], [180, 300], [460, 300]], np.int32)
    cv2.fillPoly(img, [tri], (0, 200, 0))

    out = ASSETS / "shapes.png"
    cv2.imwrite(str(out), img)
    print("已生成:", out)


if __name__ == "__main__":
    main()
