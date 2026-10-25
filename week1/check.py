"""第 1 周总验收：一键跑 5 个练习，看哪些通过、哪些还没做完。

用法
    python week1/check.py            # 跑全部
    python week1/check.py 3 4        # 只跑第 3、4 题

每道题都是独立脚本，靠脚本末尾的 assert 自检；你改完代码再跑这里即可。
只有 ex1 一开始就是完整的（示范用），ex2~ex5 需要你按 TODO 补完才会 PASS。
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY = sys.executable

EXERCISES = {
    1: ("ex1_read_image.py", []),
    2: ("ex2_color_spaces.py", []),
    3: ("ex3_pixel_roi.py", []),
    4: ("ex4_filters_edges.py", []),
    5: ("ex5_batch_tool.py", [
        "--input", str(ROOT / "assets"),
        "--output", str(ROOT / "outputs" / "batch"),
        "--size", "224",
    ]),
}


def run_one(num):
    script, extra = EXERCISES[num]
    proc = subprocess.run(
        [PY, str(ROOT / script), *extra],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=180,
    )
    tail = (proc.stdout.strip().splitlines() or [""])[-1]
    if proc.returncode == 0 and "[PASS]" in proc.stdout:
        return True, tail
    err = (proc.stderr.strip().splitlines() or [""])[-1]
    return False, tail or err


def main():
    todo = [int(x) for x in sys.argv[1:]] or sorted(EXERCISES)
    print(f"运行第 1 周验收：{todo}\n")
    results = {}
    for num in todo:
        ok, line = run_one(num)
        results[num] = ok
        print(f"  练习{num}: {'PASS' if ok else '未通过'}  {line}")

    passed = sum(results.values())
    print(f"\n通过 {passed}/{len(results)}")
    if passed < len(results):
        print("提示：先看脚本里的 TODO 注释，对照 README 里的 OpenCV 文档链接。")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
