# cv-journey

机器视觉（Computer Vision）学习仓库，跟着 `机器视觉学习规划.md` 走 12 周。

## 目录

```
cv-journey/
├── week0/            # 第 0 周：环境与工具链
│   ├── check_env.py  # 一键自检：Python / CUDA / 依赖 / 网络
│   ├── yolo_demo.py  # 最小可跑推理：YOLO11n 检测一张图
│   └── bus.jpg       # 示例图片
├── week1/            # 第 1 周：图像基础 + OpenCV
│   ├── README.md     # 本周说明与做题顺序
│   ├── generate_assets.py  # 生成测试图（shapes.png）
│   ├── ex1_read_image.py   # 练习1：读图/属性/resize（完整示例）
│   ├── ex2_color_spaces.py # 练习2：灰度 + HSV
│   ├── ex3_pixel_roi.py    # 练习3：切片 ROI + 画框
│   ├── ex4_filters_edges.py# 练习4：高斯模糊 + Canny
│   ├── ex5_batch_tool.py   # 练习5：批量 resize 小工具
│   ├── check.py      # 一键验收：python week1\check.py
│   ├── assets/       # 练习用图
│   └── outputs/      # 练习输出（不提交 git）
├── yolo11n.pt        # YOLO11n 预训练权重（5.5 MB）
├── runs/             # 推理/训练输出（不提交 git）
└── requirements.txt  # 依赖版本记录
```

## 本机环境（2026-10-24 验收）

| 项目 | 版本 / 规格 |
| --- | --- |
| Python | 3.11.9（`D:\Python\python.exe`） |
| PyTorch | 2.14.1+cu130 |
| torchvision | 0.29.1+cu130 |
| CUDA runtime | 13.0（驱动 610.47） |
| cuDNN | 9.24 |
| GPU | NVIDIA GeForce RTX 4060 Laptop，8 GB，sm_89 |
| Ultralytics | 8.4.187 |
| OpenCV | 4.11.0 |
| NumPy | 1.26.4 |
| Git | 2.55.0 |

实测 fp16 矩阵乘 4096³：**22.5 TFLOP/s**；YOLO11n 单图推理约 **66 ms**（含前后处理首轮稍慢）。

## 快速开始

```powershell
python week0\check_env.py                 # 环境自检
python week0\yolo_demo.py week0\bus.jpg   # 跑一次检测，结果在 runs/

python week1\generate_assets.py           # 生成第 1 周测试图（只需一次）
python week1\check.py                     # 第 1 周验收：看还有哪几题没做完
```

## 进度

- [x] 第 0 周：环境搭建 + YOLO 跑通 + GitHub 仓库推送（2026-10-24）
- [ ] 第 1 周：图像基础 + OpenCV（练习 1~5，见 [week1/README.md](week1/README.md)）
- [ ] 第 2 周：传统机器视觉与几何
