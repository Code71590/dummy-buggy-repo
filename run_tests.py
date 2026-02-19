"""Run pytest (with --continue-on-collection-errors) and flake8, save full output"""
import subprocess
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lines = []

lines.append("=" * 70)
lines.append("PYTEST RESULTS (--continue-on-collection-errors)")
lines.append("=" * 70)
result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short",
     "--continue-on-collection-errors"],
    capture_output=True, text=True
)
lines.append(result.stdout)
if result.stderr:
    lines.append("STDERR:" + result.stderr)

lines.append("\n" + "=" * 70)
lines.append("FLAKE8 RESULTS")
lines.append("=" * 70)
result2 = subprocess.run(
    [sys.executable, "-m", "flake8", "src/", "--max-line-length=100"],
    capture_output=True, text=True
)
lines.append(result2.stdout if result2.stdout else "(no flake8 warnings)")
if result2.stderr:
    lines.append("STDERR:" + result2.stderr)

output = "\n".join(lines)
with open("test_results.txt", "w", encoding="utf-8") as f:
    f.write(output)

print(output)
