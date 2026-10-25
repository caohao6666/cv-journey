# cv-journey

机器视觉（Computer Vision）学习仓库，跟着 `机器视觉学习规划.md` 走 12 周。

## 目录

```
cv-journey/
├── week0/            # 第 0 周：环境与工具链
│   ├── check_env.py  # 一键自检：Python / CUDA / 依赖 / 网络
│   ├── yolo_demo.py  # 最小可跑推理：YOLO11n 检测一张图
│   └── bus.jpg       # 示例图片
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
python week0\check_env.py          # 环境自检
python week0\yolo_demo.py week0\bus.jpg   # 跑一次检测，结果在 runs/
```

## 下一步

1. 配置 git 身份并做第一次提交（见《第0周-环境验收报告.md》）。
2. 在 GitHub 建远程仓库 `cv-journey` 并 push。
3. 进入第 1 周：图像基础 + OpenCV。
