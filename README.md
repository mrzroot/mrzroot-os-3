# MRZROOT OS 3: System Snapshot

Read OS, architecture, logical core count and Python version as text or JSON.

<div dir="rtl" lang="fa">

**گزارش لحظه‌ای سیستم** · مشخصات سیستم و نسخهٔ پایتون را در قالب متن یا JSON ببینید. نام دستگاه به‌صورت پیش‌فرض نمایش داده نمی‌شود.

</div>

- [Project page source](docs/index.html) · open it locally in a browser.
- Python 3.9+; no third-party runtime dependencies.

## Quick start

```sh
git clone https://github.com/mrzroot/mrzroot-os-3.git
cd mrzroot-os-3
python main.py --json
python main.py --help
```

This is a one-time snapshot, not a monitoring daemon. The monotonic clock is a counter, not a wall-clock timestamp.

## Features

- Text output for people, JSON for scripts.
- Hostname, interpreter path, and PID are opt-in.
- No network calls or background process.

## Tests

```sh
python -m unittest discover -v
```

## MRZROOT OS series

- [OS 1: Async Task Runner](https://github.com/mrzroot/mrzroot-os-1)
- [OS 2: Terminal Microbenchmark](https://github.com/mrzroot/mrzroot-os-2)
- [OS 3: System Snapshot](https://github.com/mrzroot/mrzroot-os-3)
