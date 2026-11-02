"""Run every figure script in sequence."""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent
scripts = sorted(HERE.glob("fig*.py"))
for s in scripts:
    print(f"=== {s.name} ===")
    r = subprocess.run([sys.executable, str(s)])
    if r.returncode != 0:
        print(f"FAILED: {s.name}"); sys.exit(r.returncode)
print("all figures generated")
