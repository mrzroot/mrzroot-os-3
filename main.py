"""Take one local system snapshot. Nothing is collected continuously or sent out."""
import argparse
import json
import os
import platform
import sys
import time


def collect_metrics(include_local_details=False):
    snapshot = {
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "logical_cores": os.cpu_count(),
        "python": platform.python_version(),
        "monotonic_ns": time.monotonic_ns(),
    }
    if include_local_details:
        snapshot.update(hostname=platform.node(), executable=sys.executable, pid=os.getpid())
    return snapshot


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="output a JSON object")
    parser.add_argument("--include-local-details", action="store_true", help="also include hostname, executable, and PID")
    args = parser.parse_args(argv)
    snapshot = collect_metrics(args.include_local_details)
    if args.json:
        print(json.dumps(snapshot, sort_keys=True))
    else:
        for key, value in snapshot.items():
            print(f"{key}: {value if value is not None else 'unknown'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
