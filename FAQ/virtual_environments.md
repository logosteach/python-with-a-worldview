---
title: "Python with a worldview"
author: "John C. Partridge"
edition: "2nd"
date: "03/30/2026"
chapter: FAQ
faq_topic: "All About Virtual Environments"
---

<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# All About Virtual Environments

- [All About Virtual Environments](#all-about-virtual-environments)
  - [Why they exist](#why-they-exist)
  - [Key Benefits for Beginners](#key-benefits-for-beginners)
  - [Windows: Step by Step](#windows-step-by-step)
    - [Creating the environment - Windows](#creating-the-environment---windows)
    - [Activating the environment - Windows](#activating-the-environment---windows)
    - [How to tell it worked - Windows](#how-to-tell-it-worked---windows)
    - [Deactivating - Windows](#deactivating---windows)
  - [macOS and Linux Step by Step](#macos-and-linux-step-by-step)
    - [Creating the environment - macOS and Linux](#creating-the-environment---macos-and-linux)
    - [Activating the environment - macOS and Linux](#activating-the-environment---macos-and-linux)
    - [How to tell it worked - maxOS and Linux](#how-to-tell-it-worked---maxos-and-linux)
    - [Deactivating - macOS and Linux](#deactivating---macos-and-linux)

A <mark>**virtual environment** is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.</mark>[^1]

* A virtual environment is created on top of an existing Python installation (called the "base" Python).
* It has its own independent set of Python packages installed in its own site directories.
* By default, it is isolated from the packages in the base Python installation and from other virtual environments. This means only the packages you explicitly install inside the virtual environment are available when you use it.

---

**Important Note:** Inside your virtual environment (venv) you should use the **`python`** command _instead of or in place of_ `py` or `python3`. The virtual environment ties into your system's current version of python. This makes group projects _universal_ across various operating system platforms.

---

## Why they exist

The main problem they solve is **dependency conflicts.** Different Python projects or applications may require different versions of the same package (for example, one project needs version 1.0 of a library while another needs version 2.0). Without virtual environments, installing packages globally can break one project when you update packages for another.

A virtual environment gives each project its own isolated space, so:

- You can install exactly the packages and versions your project needs.
- Changes (upgrades, removals) in one environment do not affect others or your system Python.
- It makes your projects more reproducible and easier to share with others.

Think of a virtual environment as a protective software bubble :bubbles:. Inside the bubble, your project has its own isolated Python interpreter and packages. Packages installed inside the bubble stay there — they don’t affect your global system Python. And packages from outside the bubble don’t interfere with what’s happening inside it.

## Key Benefits for Beginners

- Prevents _“it works on my machine”_ problems.
- Keeps your global Python installation clean.
- Allows you to work on multiple projects with conflicting requirements at the same time.

You create a virtual environment using the built-in venv module, typically with a command like:

## Windows: Step by Step

In order to create and activate a virtual environment on your Windows machine, you will need to follow each step carefully.

### Creating the environment - Windows

1. You must have Python 3.6 or greater installed on your computer. Microsoft prefers that Python be installed from the [Microsoft Store](https://apps.microsoft.com/home?hl=en-US&gl=US).
2. Press `Win + S`, type **Command Prompt** or **PowerShell**, and open it. (Note: If you open PowerShell then make sure to run it "As Administrator")
3. Navigate to your project folder: `cd path\to\your\project`. _Example: `cd C:\Users\YourName\Documents\my-project`._
4. Create the virtual environment using one of these two commands. (The first is the recommended way)
   - `py -m venv .venv`
   - `python -m venv .venv`

- `.venv` is the modern, popular name (t stays hidden in file explorers).
- You can also use `venv` or `myenv` -- whatever you prefer.
- This creates a new hidden folder named `.venv` with its own isolated Python and packages.

### Activating the environment - Windows

If using the command prompt:

`.venv\Scripts\activate`

- You do not need the `.bat` extension -- Windows finds it automatically.
- Your prompt will change to : `(.venv) C:\...>`

If using the PowerShell:

`.venv\Scripts\activate.ps1`

- If you get an error about **execution policy**, run this one-time first:

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Then try activating again.

### How to tell it worked - Windows

- Your prompt now shows (.venv) at the beginning.
- Run `python --version` -- it should match the Python you used to create the venv.
- Run `where python` (or `Get-Command python` in PowerShell) -- it should point inside your `.venv\Scripts\` folder.

### Deactivating - Windows

To deactivate the virtual environment, simply type: `deactivate` in the command prompt or PowerShell.

## macOS and Linux Step by Step

In order to create and activate a virtual environment on your Windows machine, you will need to follow each step carefully.

### Creating the environment - macOS and Linux

1. Make sure Python 3.6 or greater is installed on your system.
2. Open your terminal
   - macOS: Spotlight → Terminal
   - Linux: Open your favorite terminal (GNOME Terminal, Konsole, etc.)

3. Navigate to your project folder: `cd path/to/your/project`
   - Example: `cd ~/Documents/my-project`

4. Create the virtual environment with: `python3 -m venv .venv`
   - `.venv` is the recommended hidden folder name (keeps it out of sight and out of Git).
   - This creates a brand-new isolated "bubble" with its own Python and packages.

You will now see a new `.venv` folder in your project.

### Activating the environment - macOS and Linux

Use this single command in your terminal window: `source .venv/bin/activate`

- Your prompt will now change to show the environment is active: `(.venv) user@computer project %` (or something like that..)
- Now `python` and `pip` automatically point inside the bubble -- no more `python3` usage needed.

### How to tell it worked - maxOS and Linux

```console
python --version            # should show your venv's Python
which python                # should point to .venv/bin/python
```

### Deactivating - macOS and Linux

Simply type: `deactivate` in your terminal window.

[^1]: [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
