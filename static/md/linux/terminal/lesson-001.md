# Lesson 1: Using the Terminal on Debian Linux

**Theme:** Ayu Light  
**Font:** Consolas, `monospace`  
**Audience:** beginners

> Type commands in **lowercase**. Linux is case-sensitive.

---

## 1. What is a terminal?

The **terminal** is a text window where you type commands and the computer replies with text. The desktop (windows, icons, mouse) is one way to use Debian. The terminal is another.

The program inside the window is usually **Bash**. The window is the terminal; Bash reads your commands.

Why use it?

- Many tasks are one command instead of many clicks
- You can repeat and automate work
- Servers and admin tools expect the command line

---

## 2. Open the terminal with the keyboard

Try this first:

```text
Ctrl + Alt + T
```

Hold **Ctrl** and **Alt**, then tap **T**.

**Debian note:** Ubuntu often has this shortcut already. Stock Debian GNOME sometimes does not. If nothing happens, use the GUI method below, then add a shortcut:

1. **Settings → Keyboard → Keyboard Shortcuts**
2. **Custom Shortcuts → +**
3. Name: `Terminal`  
   Command: `gnome-terminal`  
   Keys: `Ctrl+Alt+T`

Another keyboard method:

```text
Alt + F2
```

Type `gnome-terminal` and press Enter.

On XFCE use `xfce4-terminal`. On KDE use `konsole`.

---

## 3. Open the terminal with the GUI

**GNOME (common Debian desktop):**

1. Click **Activities** or press the **Super** (Windows) key
2. Type `terminal`
3. Click **Terminal**

Or: **Activities → Show Applications → Terminal**

**XFCE:** Applications menu → Terminal Emulator  
**KDE:** Application launcher → Konsole

---

## 4. What is the prompt?

When the terminal is ready, it prints a short line and waits. That line is the **prompt**.

```text
student@debian:~$
```

| Piece | Meaning |
|---|---|
| `student` | your username |
| `@debian` | the computer name |
| `~` | current folder (`~` means **home**) |
| `$` | you are a normal user |

If you see `#` instead of `$`, you are **root**. Be extra careful.

After you move into Documents the prompt often looks like:

```text
student@debian:~/Documents$
```

Type **after** the prompt, then press **Enter**.

Leave later with `exit` or by closing the window.

---

## 5. The `echo` command

`echo` prints text. It is the simplest way to see that the shell is listening.

```bash
echo Hello
```

```text
Hello
```

```bash
echo "Hello, Debian terminal"
```

```text
Hello, Debian terminal
```

Quotes keep a phrase together when there are spaces.

```bash
echo one two three
```

```text
one two three
```

Show built-in values:

```bash
echo $HOME
```

```text
/home/student
```

```bash
echo $USER
```

```text
student
```

`$HOME` is your home folder path. `$USER` is your username.

**Try it**

1. Print your name with `echo`
2. Print `I am learning the terminal`
3. Run `echo $HOME` and read the path

---

## 6. The `ls` command

`ls` means **list**. It shows what is in the current folder.

```bash
ls
```

```text
Desktop  Documents  Downloads  Music  Pictures  Videos
```

Useful options (a space, then a dash, then letters):

```bash
ls -l
```

**Long** listing: permissions, owner, size, date, name.

```bash
ls -a
```

**All** items, including hidden names that start with a dot (`.bashrc`, and also `.` and `..`).

```bash
ls -la
```

Both together.

```bash
ls -lh
```

Long list with human-readable sizes (K, M, G).

List a folder without going into it:

```bash
ls /etc
```

```bash
ls Documents
```

If a name has a space:

```bash
ls "My Folder"
```

**Try it**

1. Run `ls`
2. Run `ls -l` and compare
3. Run `ls -a` and look for names starting with `.`

---

## 7. The `cd` command — down and up

`cd` means **change directory**. It moves you into another folder.

Folders nest like a tree:

```text
/                      ← root (top of the whole system)
├── home
│   └── student        ← your home (also called ~)
│       ├── Documents
│       ├── Downloads
│       └── Pictures
├── etc
└── usr
```

### Go down (into a folder)

```bash
cd Documents
```

Then check with `ls`.

Several levels in one step:

```bash
cd Documents/Work
```

(Only works if that path exists from where you are.)

### Climb up (to the parent)

```bash
cd ..
```

Two levels up:

```bash
cd ../..
```

### Shortcuts

| Command | Where it takes you |
|---|---|
| `cd` | your home folder |
| `cd ~` | your home folder |
| `cd /` | the system **root** |
| `cd ..` | one folder up |
| `cd -` | the folder you were in just before |

If the name does not exist, Bash says `No such file or directory`. Check spelling and capitals.

Press **Tab** after a few letters to auto-complete a folder name.

---

## 8. Absolute path vs relative path

A **path** is the address of a file or folder.

### Absolute path

Starts at the top of the system with `/`. It works from *any* current folder.

```text
/home/student
/home/student/Documents
/etc
/
```

```bash
cd /home/student/Documents
```

### Relative path

Starts from **where you are now**. It does not begin with `/`.

If you are in `/home/student`:

```bash
cd Documents
```

is the same as:

```bash
cd /home/student/Documents
```

**Rule**

- Path starts with `/` → absolute (from the root)
- Path starts with `~` → from your home
- Anything else → relative to the current folder

---

## 9. Guided navigation

Do this sequence. After each `cd`, look at the prompt or run `pwd`.

**A. Go to the root**

```bash
cd /
```

```bash
ls
```

You should see system folders such as `bin`, `etc`, `home`, `usr`, `var`.  
Do not delete anything here.

**B. Go home**

Any of these:

```bash
cd
```

```bash
cd ~
```

```bash
cd /home/YOURUSERNAME
```

Replace `YOURUSERNAME` with the name before `@` in your prompt.

```bash
ls
```

**C. Enter a subfolder you choose**

Pick a real folder from `ls`:

```bash
cd Documents
```

```bash
cd Downloads
```

```bash
cd Pictures
```

Then:

```bash
ls
```

**D. Climb back toward home**

```bash
cd ..
```

**Challenge:** from home, go to root with an **absolute** path, return home with `cd`, then enter a subfolder with a **relative** path.

---

## 10. The `pwd` command

`pwd` means **print working directory**. It shows the **absolute path** of the folder you are in.

```bash
pwd
```

```text
/home/student/Documents
```

The prompt often shows a short version (`~` or `~/Documents`). `pwd` shows the full address.

Use `pwd` whenever you feel lost.

**Walk-through**

```bash
cd /
pwd

cd ~
pwd

cd Documents
pwd

cd ..
pwd
```

Watch the printed path change each time.

---

## 11. What `.` and `..` mean

These special names exist in **every** folder.

| Name | Meaning |
|---|---|
| `.` | **this** directory (where you are now) |
| `..` | the **parent** directory (one level up) |

See them with:

```bash
ls -a
```

```text
.  ..  .bashrc  Desktop  Documents  Downloads
```

`.` in practice:

```bash
ls .
```

Lists the current folder (same idea as plain `ls`).

```bash
cd .
```

Stays put. Not useful day to day, but it proves `.` means “here.”

`..` in practice:

```bash
cd ..
```

```bash
ls ..
```

`ls ..` lists the parent **without** leaving the current folder.

Combined relative paths:

```bash
cd ../Downloads
```

Go up one, then into Downloads.

```bash
cd ./Documents
```

Documents inside the current folder. The `./` is optional but explicit.

**Do not confuse**

- `.` = current folder
- `..` = parent folder
- `.bashrc` is a **hidden file**, not “current directory”

---

## Quick reference

| Command | What it does |
|---|---|
| `echo text` | print text |
| `ls` | list current folder |
| `ls -l` | detailed list |
| `ls -a` | include hidden items |
| `cd folder` | go into a folder |
| `cd ..` | go up one folder |
| `cd` or `cd ~` | go home |
| `cd /` | go to system root |
| `pwd` | show full path of current folder |
| `.` | current folder |
| `..` | parent folder |

---

## Practice

Complete these without using the file manager:

1. Open the terminal (keyboard or menu).
2. Read your prompt. Who are you, and which folder does `~` stand for?
3. `echo` a full sentence in quotes.
4. `ls` then `ls -la`. What extra names appear with `-a`?
5. `pwd`. Write down the path.
6. `cd /` then `pwd` then `ls`.
7. Return home (`cd` or `cd ~`) and `pwd` again.
8. `cd` into one subfolder you choose, `ls`, `pwd`.
9. `cd ..` and confirm with `pwd` that you went up.
10. Explain in one sentence each: absolute path, relative path, `.`, `..`.

---

## Common mistakes

- **Wrong capitals:** `Documents` and `documents` are different
- **Forgot Enter:** the command does not run until you press Enter
- **Spaces in names:** use quotes: `cd "My Folder"`
- **`cd` to a file:** `cd` only works on folders
- **Lost?** Run `pwd`, then `cd` to go home and start over

---

## Instructor notes (Ayu Light)

Use these colors when rendering terminal examples:

| Role | Hex |
|---|---|
| Background | `#f8f9fa` |
| Foreground | `#5c6166` |
| Title bar | `#ebeef0` |
| Border | `#d8d8d7` |
| User in prompt | `#6cbf43` |
| Host in prompt | `#3199e1` |
| Path in prompt | `#9e75c7` |
| Flags (`-l`, `-a`) | `#eca944` |
| Arguments / paths | `#46ba94` |
| Directories | `#3199e1` |
| Hidden / comments | `#686868` |
| Errors | `#ea6c6d` |
| Cursor / accent | `#ffaa33` |

Font stack:

```css
font-family: Consolas, monospace;
```
