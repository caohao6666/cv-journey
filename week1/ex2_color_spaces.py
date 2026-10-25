"""练习 2：色彩空间转换（BGR → 灰度 / HSV）。

目标
- cv2.cvtColor 的用法：cv2.COLOR_BGR2GRAY、cv2.COLOR_BGR2HSV
- 理解灰度图是 2 维数组（没有通道维），HSV 图仍是 3 通道
- 理解“颜色”可以用色相 H 来描述：红色在 H≈0（或 180）附近，和亮度 V 无关

任务（在下面 TODO 处补代码）
1. 把 img 转成灰度图，保存到 outputs/ex2_gray.png
2. 把 img 转成 HSV 图，保存到 outputs/ex2_hsv.png
3. 打印红圆圆心像素 (y=120, x=160) 的 H/S/V，并解释为什么 H 接近 0

运行：python week1/ex2_color_spaces.py
验收：灰图 ndim==2；HSV 是 3 通道；圆心像素 H<10 或 H>170 且 S>200
"""

from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "outputs"


def main():
    OUT.mkdir(exist_ok=True)
    img = cv2.imread(str(ASSETS / "shapes.png"))
    assert img is not None, "读图失败：先运行 python week1/generate_assets.py"

    # TODO 1: 转灰度图，保存到 outputs/ex2_gray.png
    gray = None

    # TODO 2: 转 HSV 图，保存到 outputs/ex2_hsv.png
    hsv = None

    # TODO 3: 读取圆心像素 hsv[120, 160]，拆出 h, s, v 并打印
    # 提示：h, s, v = hsv[120, 160]

    assert gray is not None, "TODO 1 未完成：gray 还是 None"
    assert hsv is not None, "TODO 2 未完成：hsv 还是 None"
    assert gray.ndim == 2, f"灰度图应该是 2 维数组，现在是 {gray.ndim} 维"
    assert hsv.shape[2] == 3, "HSV 图应该是 3 通道"

    cv2.imwrite(str(OUT / "ex2_gray.png"), gray)
    cv2.imwrite(str(OUT / "ex2_hsv.png"), hsv)

    h, s, v = hsv[120, 160]
    print(f"圆心像素 HSV = (H={h}, S={s}, V={v})")
    assert (h < 10 or h > 170) and s > 200, f"圆心应该是红色（H≈0，S 很高），现在是 {h}, {s}"
    print("[PASS] 练习2 完成：灰图 2 维、HSV 3 通道、红色 H≈0，都验证通过")


if __name__ == "__main__":
    main()
