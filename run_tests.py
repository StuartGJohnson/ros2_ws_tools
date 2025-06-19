#!/usr/bin/env python3
# GPT4o-authored (after strong constraints by SGJ). 
# This script finds and used subprocess to run unit tests in all or
# any of the ROS2 packages in the current workspace. The python test
# API is a little more fidgety than running as a process.

import os
import subprocess
import argparse
from pathlib import Path

def find_test_files(package_dir):
    test_dir = package_dir / "test"
    if not test_dir.exists():
        return []
    return sorted(f for f in test_dir.glob("test_*.py") if f.is_file())

def run_tests(package=None):
    workspace = Path.cwd()
    src_dir = workspace / "src"

    packages = [package] if package else [p.name for p in src_dir.iterdir() if p.is_dir()]

    for pkg_name in packages:
        package_path = src_dir / pkg_name
        test_files = find_test_files(package_path)
        if not test_files:
            print(f"⚠️  No test files found for {pkg_name}")
            continue

        env = os.environ.copy()
        env["PYTHONPATH"] = str(package_path) + ":" + env.get("PYTHONPATH", "")

        for test_file in test_files:
            print(f"\n▶ Running {test_file.relative_to(workspace)}")
            result = subprocess.run(["python3", str(test_file)], env=env)
            if result.returncode != 0:
                print(f"❌ Test {test_file.name} failed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", help="Run tests for a specific ROS2 package")
    args = parser.parse_args()
    run_tests(package=args.package)

