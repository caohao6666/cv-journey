"""练习 5：写一个“小工具”——批量把图片缩放成统一尺寸。

这是本周唯一一个带命令行参数的工具，做完你就有了第一个“能复用”的脚本。

用法
    python week1/ex5_batch_tool.py --input week1/assets --output week1/outputs/batch --size 224

目标
- argparse 的用法：--input / --output / --size
- 遍历目录：Path.glob("*.jpg") + Path.glob("*.png")
- 批量读 → 缩放 → 写，养成“写文件、留产物”的习惯
- 体会 INTER_AREA（缩小用）和 INTER_CUBIC（放大用）的区别

任务（在 TODO 处补代码）
1. 遍历 input 目录下所有 .jpg/.png（两种后缀都要）
2. 每张图 cv2.resize 成 (size, size)，缩小用 cv2.INTER_AREA
3. 保存到 output 目录，文件名改为“原名_size.png”
4. 打印处理了哪些文件

运行：按上面的用法跑一遍
验收：output 目录下至少 2 张图，且每张都是 size×size
"""

import argparse
from pathlib import Path

import cv2


def parse_args():
    p = argparse.ArgumentParser(description="批量把图片缩放成统一尺寸")
    p.add_argument("--input", default="week1/assets", help="输入目录")
    p.add_argument("--output", default="week1/outputs/batch", help="输出目录")
    p.add_argument("--size", type=int, default=224, help="目标边长（正方形）")
    return p.parse_args()


def main():
    args = parse_args()
    in_dir = Path(args.input)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = []
    # TODO 1: 把 in_dir 里的 *.jpg 和 *.png 都收集进 files（提示：list(glob) + list(glob)）

    assert files, f"在 {in_dir} 里没找到图片，检查 --input 参数"

    for f in files:
        img = cv2.imread(str(f))
        if img is None:
            print(f"跳过（读不了）: {f.name}")
            continue
        # TODO 2: 缩放成 (args.size, args.size)
        resized = None
        # TODO 3: 保存为 out_dir / f"{f.stem}_{args.size}.png"
        out_path = None
        assert resized is not None and out_path is not None, f"TODO 2/3 未完成: {f.name}"
        cv2.imwrite(str(out_path), resized)
        print(f"已完成: {f.name} -> {out_path.name}")

    outs = sorted(out_dir.glob("*.png"))
    assert len(outs) >= 2, f"输出目录只有 {len(outs)} 张图，至少要 2 张"
    for o in outs:
        im = cv2.imread(str(o))
        assert im.shape[0] == args.size and im.shape[1] == args.size, f"{o.name} 尺寸不对: {im.shape}"
    print(f"[PASS] 练习5 完成：共处理 {len(outs)} 张图，全部为 {args.size}x{args.size}")


if __name__ == "__main__":
    main()
