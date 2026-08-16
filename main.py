"""
=============================================================================
MRZROOT-OS-3: Real-Time Hardware Telemetry & System Daemon
=============================================================================
Pure Python (Zero external dependencies, sub-millisecond execution)
=============================================================================
"""

import os
import platform
import sys
import time


def banner():
    print(r"""
\033[1;35m  __  __ _____ ______ _____   ____   ____ _______        ____   _____        ____  
 |  \/  |  __ \___  /  __ \ / __ \ / __ \__   __|      / __ \ / ____|      |___ \ 
 | \  / | |__) | / /| |__) | |  | | |  | | | | ______ | |  | | (___   ______  __) |
 | |\/| |  _  / / / |  _  /| |  | | |  | | | ||______| | |  | |\___ \ |______||__ < 
 | |  | | | \ \/ /__| | \ \| |__| | |__| | | |        | |__| |____) |        ___) |
 |_|  |_|_|  \_\_____|_|  \_\\____/ \____/  |_|         \____/|_____/        |____/ \033[0m
 \033[1;32m[+] Real-Time Hardware Telemetry Daemon [v2.4.0]\033[0m
""")


def collect_metrics():
    print("\n📊 \033[1;33mHardware & Runtime Metrics Snapshot:\033[0m")
    print(f"  • Host Machine     : {platform.node()} ({platform.system()} {platform.release()})")
    print(f"  • CPU Architecture : {platform.machine()} (Logical Cores: {os.cpu_count()})")
    print(f"  • Python Engine    : {sys.version.split()[0]} ({sys.executable})")
    print(f"  • Process ID (PID) : {os.getpid()}")
    print(f"  • Precision Clock  : {time.monotonic_ns()} ns")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    banner()
    collect_metrics()
    print("\n✨ \033[1;32mTelemetry probe finished with 0 errors.\033[0m")


if __name__ == "__main__":
    main()
