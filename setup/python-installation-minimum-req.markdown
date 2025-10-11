# Minimum Requirements for Python

## Computer Specifications
Python is lightweight and runs on most modern systems. Below are the minimum and recommended specifications for installing and using Python effectively:

- **Operating System**:
  - **Minimum**: Windows 10 (64-bit), macOS 10.15 (Catalina), or Linux (e.g., Ubuntu 20.04 or other major distributions)
  - **Recommended**: Latest version of Windows 11, macOS Ventura or later, or a recent Linux distribution
- **Processor**:
  - **Minimum**: 1 GHz processor (e.g., Intel Core i3 or equivalent)
  - **Recommended**: Multi-core processor (e.g., Intel Core i5/i7 or AMD Ryzen)
- **RAM**:
  - **Minimum**: 4 GB
  - **Recommended**: 8 GB or more for smoother performance, especially for data-heavy tasks
- **Storage**:
  - **Minimum**: 500 MB free disk space for Python installation
  - **Recommended**: 5 GB or more free space for Python, libraries, and projects
- **Internet Connection**:
  - Required for downloading Python and additional packages
- **Display**:
  - 1024x768 resolution or higher for coding environments/IDEs
- **Optional**:
  - A dedicated graphics card is not required unless working with GPU-intensive tasks (e.g., machine learning with libraries like TensorFlow).

## Installation Steps
Follow these steps to install and start using Python on your computer:

### Step 1: Download Python
1. Visit [python.org](https://www.python.org/downloads/) and download the latest stable version (e.g., Python 3.13 as of October 2025).
2. Select the appropriate installer for your operating system:
   - **Windows**: Download the executable installer (e.g., `python-3.13.x.exe`).
   - **macOS**: Download the macOS installer (e.g., `python-3.13.x-macos.pkg`).
   - **Linux**: Python is often pre-installed; if not, use your package manager (e.g., `sudo apt install python3` on Ubuntu).

### Step 2: Install Python
1. **Run the Installer**:
   - **Windows**:
     - Double-click the `.exe` file.
     - Check **"Add Python to PATH"** (critical for command-line access).
     - Select **"Install Now"** or customize as needed.
   - **macOS**:
     - Open the `.pkg` file and follow the prompts.
   - **Linux**:
     - If not pre-installed, run `sudo apt update && sudo apt install python3 python3-pip` (Ubuntu/Debian) or equivalent (e.g., `sudo dnf install python3` for Fedora).
2. **Verify Installation**:
   - Open a terminal/command prompt:
     - Windows: Press `Win + R`, type `cmd`, and press Enter.
     - macOS: Open Terminal from Applications > Utilities.
     - Linux: Open your terminal.
   - Type `python3 --version` or `python --version` to confirm the installed version (e.g., `Python 3.13.x`).
   - Check `pip --version` to verify the package manager.

### Step 3: Set Up a Development Environment
1. **Choose a Code Editor or IDE**:
   - **IDLE**: Included with Python; simple for beginners.
   - **Visual Studio Code (VS Code)**: Free, lightweight, with Python extension.
2. **Install and Configure**:
   - Download VS Code from [code.visualstudio.com](https://code.visualstudio.com).
   - For VS Code, install the Python extension and select the Python interpreter.

### Step 4: Write and Run Your First Program
1. Create a file (e.g., `hello.py`) in your editor with:
   ```python
   print("Hello, Python!")
   ```
2. Save the file with a `.py` extension.
3. Run it in the terminal with `python3 hello.py` (or `python hello.py` on Windows) or use the IDE’s "Run" button.

### Step 5: Install Additional Libraries
1. Use `pip` to install packages, e.g.:
   ```bash
   pip3 install requests
   ```
2. Verify with `pip3 list` and test libraries in your code.

## Troubleshooting Tips
- **Windows PATH Issues**: If `python` or `pip` commands fail, ensure "Add Python to PATH" was selected or manually add Python to your system PATH.
- **Linux/macOS Permissions**: Use `sudo` for system-wide installations or `pip3 install --user <package>` for user-specific installations.
- **Version Conflicts**: Use `python3` or `python3.x` (e.g., `python3.13`) to specify the correct version if multiple are installed.