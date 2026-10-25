"""练习 1：图像 = 一个 numpy 数组（读懂这句话就入门一半）。

目标
- 会用 cv2.imread 读图、cv2.imwrite 写图
- 用 img.shape 看 (高, 宽, 通道数)，用 img.dtype 看数据类型
- 记住 OpenCV 默认通道顺序是 **BGR**，不是 RGB
- 会用 cv2.resize 缩放

运行：python week1/ex1_read_image.py
验收：输出 [PASS]，且 week1/outputs/ex1_resized.jpg 生成（宽高各缩一半）
"""

from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "outputs"


def main():
    OUT.mkdir(exist_ok=True)
    img = cv2.imread(str(ASSETS / "bus.jpg"))
    assert img is not None, "读图失败：检查 week1/assets/bus.jpg 是否存在"

    h, w, c = img.shape  # 注意顺序是 (高, 宽, 通道)
    print(f"形状 shape = {img.shape}  ->  高 {h}, 宽 {w}, 通道 {c}")
    print(f"数据类型 dtype = {img.dtype}（0~255 的 uint8）")

    b, g, r = img[100, 100].tolist()  # 注意：img[y, x]，先 y 后 x
    print(f"像素 (y=100, x=100) 的 BGR = ({b}, {g}, {r}) —— 若按 RGB 理解就错了")

    half = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_AREA)
    out = OUT / "ex1_resized.jpg"
    cv2.imwrite(str(out), half)

    assert out.exists(), "保存失败"
    assert half.shape[:2] == (h // 2, w // 2), "缩放假失败"
    print(f"[PASS] 练习1 完成，输出：{out}")


if __name__ == "__main__":
    main()
