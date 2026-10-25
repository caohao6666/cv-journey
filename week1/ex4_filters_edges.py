"""练习 4：滤波与边缘检测（从“像素”到“结构”的第一步）。

目标
- 卷积/滤波的直觉：高斯模糊让图像变“糊”，本质是邻域加权平均
- cv2.GaussianBlur(img, (5,5), 0)：核越大越糊
- 边缘检测前先转灰度：cv2.Canny(50, 150)，输出是“只含 0 和 255 的图”
- 试改阈值（30,90 / 100,200），观察边缘数量变化

任务
1. 对 bus.jpg 做高斯模糊（核 5x5），保存 outputs/ex4_blur.png
2. 转灰度后做 Canny(50,150)，保存 outputs/ex4_edges.png
3. 打印 edge_img 中“边缘像素”的占比（nonzero / 总数）

运行：python week1/ex4_filters_edges.py
验收：edges 是 uint8、且只包含 0/255；边缘占比在 0.5%~50% 之间
"""

from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "outputs"


def main():
    OUT.mkdir(exist_ok=True)
    img = cv2.imread(str(ASSETS / "bus.jpg"))
    assert img is not None, "读图失败"

    # TODO 1: 高斯模糊，保存为 ex4_blur.png
    blurred = None

    # TODO 2: 灰度 + Canny，保存为 ex4_edges.png
    edges = None

    assert blurred is not None and edges is not None, "TODO 1/2 未完成"
    assert edges.dtype == np.uint8, "Canny 输出应该是 uint8"
    assert set(np.unique(edges)).issubset({0, 255}), "Canny 输出只应有 0 和 255"

    cv2.imwrite(str(OUT / "ex4_blur.png"), blurred)
    cv2.imwrite(str(OUT / "ex4_edges.png"), edges)

    ratio = np.count_nonzero(edges) / edges.size
    print(f"边缘像素占比 = {ratio:.2%}")
    assert 0.005 < ratio < 0.5, f"边缘占比异常（{ratio:.2%}），检查 Canny 阈值"
    print("[PASS] 练习4 完成：模糊 + 边缘检测都正确")


if __name__ == "__main__":
    main()
