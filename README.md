<div align="center">

# Lava

A simple AUR helper for Arch Linux enthusiasts built in Python

![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)
![GitHub Forks](https://img.shields.io/github/forks/Syntaxspin/lava?&logo=github)
![Stars](https://img.shields.io/github/stars/Syntaxspin/lava?&logo=github)
![Contributors](https://img.shields.io/github/contributors/Syntaxspin/lava?color=green)
[![License](https://img.shields.io/badge/License-MIT-pink)](https://github.com/Syntaxspin/lava/blob/main/LICENSE)
</div>

---

## Description

**Lava** is a lightweight AUR helper written in Python for Arch Linux users.  
It simplifies installing and removing packages from the Arch User Repository using a minimal command-line interface.

The project focuses on simplicity, readability, and direct interaction with native Arch Linux tooling such as:

- `git`
- `makepkg`
- `pacman`

Unlike larger AUR helpers, `lava` keeps the workflow minimal and transparent.

---

## Features

- Search packages from the AUR
- Clone packages directly from AUR Git repositories
- Install packages using `makepkg`
- Remove installed packages using `pacman`
- Lightweight and beginner-friendly Python codebase
- Minimal dependencies

---

## Installation

#### 1. Clone the repository

```bash
git clone https://github.com/SyntaxSpin/lava.git
```

#### 2. Move into the project directory

```bash
cd lava/Lava
```

#### 3. Install required dependency

```bash
pip install requests
```

#### 4. Run the installer script

```bash
chmod +x install.sh
./install.sh
```

---

## Usage

### Install a package

```bash
lava -S <package-name>
```

Example:

```bash
lava -S visual-studio-code-bin
```

### Remove a package

```bash
lava -R <package-name>
```

Example:

```bash
lava -R visual-studio-code-bin
```

---

## File Structure

```bash
lava
├── LICENSE
├── README.md
└── Lava
    ├── install.sh
    └── main.py
```

### File Overview

| File | Purpose |
|------|----------|
| `main.py` | Core logic of the AUR helper |
| `install.sh` | Installation script |
| `LICENSE` | Project license |
| `README.md` | Documentation |

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.

---

## Bug Reports

Found a bug or issue?

Please open an issue on the GitHub repository with:

- Steps to reproduce
- Expected behavior
- Actual behavior
- System information

Contributions, fixes, and improvements are welcome.

---

<div align="center">

Made with 💌 by [Syntaxspin](https://github.com/Syntaxspin)

</div>
