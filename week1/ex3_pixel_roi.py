"""练习 3：像素、切片（ROI）、在图上画东西。

目标
- 图像切片 img[y1:y2, x1:x2] 就是 numpy 切片：得到一块 ROI（Region of Interest）
- 切片得到的是“视图”还是“拷贝”？改 ROI 会不会改原图？（动手验证）
- cv2.rectangle 画框，参数是 (图, 左上角, 右下角, 颜色BGR, 线宽)
- 用 mean(axis=(0,1)) 求区域平均颜色

任务
1. 从 shapes.png 里切出红圆区域：img[60:180, 100:220]
2. 保存到 outputs/ex3_circle.png
3. 复制原图（img.copy()），在上面用绿色框住这块区域，保存 outputs/ex3_rect.png
4. 计算 ROI 的平均 BGR 并打印，解释为什么 R 最大

运行：python week1/ex3_pixel_roi.py
验收：crop 形状 (120,120,3)；平均颜色的 R 通道最大；两张图都保存成功
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

    # TODO 1: 切出红圆区域（提示：先 y 后 x）
    crop = None

    # TODO 2: 在 img.copy() 上画绿框，框住同样的区域
    canvas = None

    # TODO 3: 计算 crop 的平均 BGR：mean_b, mean_g, mean_r = crop.mean(axis=(0,1))
    # 并打印

    assert crop is not None and canvas is not None, "TODO 1/2 未完成"
    assert crop.shape == (120, 120, 3), f"crop 形状应为 (120,120,3)，现在是 {crop.shape}"

    cv2.imwrite(str(OUT / "ex3_circle.png"), crop)
    cv2.imwrite(str(OUT / "ex3_rect.png"), canvas)

    mean_b, mean_g, mean_r = crop.mean(axis=(0, 1))
    print(f"ROI 平均 BGR = ({mean_b:.1f}, {mean_g:.1f}, {mean_r:.1f})")
    assert mean_r > mean_b and mean_r > mean_g, "红圆的区域 R 通道应该最大"
    print("[PASS] 练习3 完成：切片、画框、求均值都正确")


if __name__ == "__main__":
    main()
