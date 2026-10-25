# 第 1 周：图像基础 + OpenCV（走完这一周，你才算“会看图”）

> 目标不是背函数，而是建立三个直觉：
> **图像 = 数组**、**坐标是 (y, x)**、**颜色能拆成不同空间（BGR/灰度/HSV）**。

## 0. 开始前

```powershell
cd D:\cv\cv-journey
D:\Python\python.exe week1\generate_assets.py   # 生成测试图（只需一次）
D:\Python\python.exe week1\check.py             # 看当前进度：只有练习1会 PASS
```

预期：`通过 1/5`。之后每做完一题，再跑一次 `check.py`，PASS 数会涨。

## 1. 练习顺序与要求

| 题号 | 文件 | 内容 | 要不要自己写 | 产物 |
| --- | --- | --- | --- | --- |
| 1 | `ex1_read_image.py` | 读图、shape/dtype、BGR、resize | ❌ 已写好，通读并运行，弄懂每行 | `outputs/ex1_resized.jpg` |
| 2 | `ex2_color_spaces.py` | BGR→灰度/HSV，看 H 描述颜色 | ✅ 补 3 个 TODO | `outputs/ex2_gray.png`、`ex2_hsv.png` |
| 3 | `ex3_pixel_roi.py` | 切片抠 ROI、画矩形、求区域均值 | ✅ 补 3 个 TODO | `outputs/ex3_circle.png`、`ex3_rect.png` |
| 4 | `ex4_filters_edges.py` | 高斯模糊、Canny 边缘 | ✅ 补 2 个 TODO | `outputs/ex4_blur.png`、`ex4_edges.png` |
| 5 | `ex5_batch_tool.py` | argparse + 批量 resize 小工具 | ✅ 补 3 个 TODO | `outputs/batch/*_224.png` |

**规则**：每题跑通 `[PASS]` 才算完成；卡住超过 20 分钟再看参考答案思路（问我），别硬扛。

## 2. 每题考察的关键点

**练习 1（示范）**：`img.shape` 返回 `(高, 宽, 通道)`；`img[y, x]` 先 y 后 x；`cv2.imread` 读出来是 BGR。
**练习 2**：灰度图 `ndim == 2`（丢了通道维）；HSV 里 H 管颜色（红≈0/180）、S 管鲜艳度、V 管亮度；红色在 HSV 里 H 接近 0，和深浅无关。
**练习 3**：切片是 numpy 切片，`crop = img[60:180, 100:220]`；`img.copy()` 后画框不影响原图，不 copy 直接画会改原图——这是新手最常踩的坑之一。
**练习 4**：滤波 = 邻域加权平均；Canny 输出只有 0/255；阈值越小边缘越多，用 `np.count_nonzero` 量化边缘占比。
**练习 5**：`Path.glob` 逐个匹配；缩小用 `INTER_AREA` 才不糊；命令行参数让脚本可复用（这就是“工具”和“作业”的区别）。

## 3. 自检命令

```powershell
D:\Python\python.exe week1\check.py          # 全部
D:\Python\python.exe week1\check.py 3 4      # 只跑第 3、4 题
```

`check.py` 会显示每题 PASS/未通过 和最后一行输出（哪个 assert 挂了，就回去看那个 TODO）。

## 4. 查文档（英文别怕，直接 Ctrl+F 函数名）

- OpenCV-Python 教程总目录：https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- 图像基础（读/写/显示/像素）：https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html
- 色彩空间（含 HSV 阈值表）：https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
- Canny 边缘：https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
- 中文补充：learnopencv 的 OpenCV Basics 系列 https://github.com/spmallick/learnopencv

## 5. 完成后要做的三件事

1. 跑 `check.py` 到 `通过 5/5`
2. 截图或保存 `outputs/` 里的结果图（建议新建 `week1/notes.md` 记录：每题学到什么、踩了什么坑）
3. 提交：

```powershell
cd D:\cv\cv-journey
git add -A
git commit -m "week1: 完成 5 个 OpenCV 基础练习"
git push
```

> 注意：PS 5.1 里不要用 `&&` 连接命令，一行一行敲。
