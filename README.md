<div align="center">

<!-- Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,25,45&height=200&section=header&text=MRZROOT-OS-3&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=%E2%9A%A1%20Simple%2C%20Fast%20System%20%26%20Hardware%20Info%20Tool%20for%20Python&descFontSize=16&descAlignY=58&descAlign=50" alt="MRZROOT OS 3 Banner" width="100%" />

<!-- Animated Typist -->
<a href="https://github.com/mrzroot/mrzroot-os-3">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=2800&pause=1000&color=00D2FF&center=true&vCenter=true&width=650&lines=Quick+System+%26+Hardware+Diagnostics+in+Python;Clean%2C+Lightweight+%26+Zero+Extra+Packages;Beginner-Friendly+Open+Source+Utility" alt="Typing SVG" />
</a>

<br />

<!-- Live Status Badges -->
<p align="center">
  <a href="https://github.com/mrzroot/mrzroot-os-3/stargazers">
    <img src="https://img.shields.io/github/stars/mrzroot/mrzroot-os-3?style=for-the-badge&logo=github&color=00D2FF" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/mrzroot/mrzroot-os-3/network/members">
    <img src="https://img.shields.io/github/forks/mrzroot/mrzroot-os-3?style=for-the-badge&logo=github&color=38BDF8" alt="GitHub Forks" />
  </a>
  <a href="https://github.com/mrzroot/mrzroot-os-3/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge" alt="License" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome" />
</p>

<p align="center">
  <strong>⭐ If you find this project useful, please consider starring the repository to support development! ⭐</strong>
</p>

</div>

---

### 📖 Overview

**MRZROOT-OS-3** is a simple, lightweight system and hardware information tool written in pure Python. It quickly inspects your OS, CPU, memory, and environment details without requiring any third-party packages or complex setup.

```
┌─────────────────────────────────────────────────────────────┐
│  ⚡ MRZROOT-OS-3 System & Hardware Inspector               │
│  [Core] Simple • Fast • Lightweight • Zero Dependencies     │
└─────────────────────────────────────────────────────────────┘
```

---

### ✨ Key Features

- ⚡ **Zero Dependencies**: Works out-of-the-box using only Python standard library.
- 🔍 **Instant System Diagnostics**: Quickly view OS, CPU cores, Python version, and execution stats.
- 💻 **Cross-Platform**: Works smoothly on Windows, Linux, and macOS.
- 📖 **Clean & Beginner-Friendly Code**: Easy to read, modify, and learn from.

---

### 🚀 Quick Start & Installation

```bash
# Clone the repository
git clone https://github.com/mrzroot/mrzroot-os-3.git
cd mrzroot-os-3

# Run the telemetry daemon
python main.py
```

---

### 💻 Architecture Flow

```mermaid
graph LR
    classDef input fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef engine fill:#0284c7,stroke:#00D2FF,stroke-width:2px,color:#fff;
    classDef output fill:#0f766e,stroke:#2dd4bf,stroke-width:2px,color:#fff;

    Probe["🔍 Hardware / OS Probes"]:::input
    Engine["⚡ Telemetry Stream Aggregator"]:::engine
    Storage["📦 Structured Metric Snapshots"]:::engine
    Dashboard["📊 Terminal Dashboard / JSON Stream"]:::output

    Probe --> Engine
    Engine --> Storage
    Storage --> Dashboard
```

---

### 🌟 Star History & Community Support

Support our open-source journey! If you like what we're building, leave a star ⭐:

<div align="center">
  <a href="https://star-history.com/#mrzroot/mrzroot-os-3&Date">
    <img src="https://api.star-history.com/svg?repos=mrzroot/mrzroot-os-3&type=Date" alt="Star History Chart" width="70%" />
  </a>
</div>

---

### 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mrzroot/mrzroot-os-3/issues).

### 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
