# Linux: An Introduction and Cheat Sheet

## What Is the Shell?

The shell is a program that reads commands you type and runs them — no icons, no windows to click, just text in and text out. This is the terminal you'll use throughout this course to move around your files, run Python scripts, and edit code with `vim` or `nano`.

It looks intimidating at first because it gives you almost no visual cues — no folder icons, no "you are here" arrow. But it takes only a handful of commands to work comfortably, and those commands are the same on every Linux machine and on macOS, which is exactly why this course uses them: the skills transfer everywhere.

If you haven't yet, see `./intro-vim.md` or `./intro-nano.md` for how to edit files once you can navigate to them.

---

## The One Thing You Must Understand First: Where You Are

Unlike a file browser, the shell doesn't show you a folder window — it just remembers a "current directory," and every command you type runs relative to that location unless you say otherwise. Almost every confusing shell moment comes down to not knowing where you currently are.

Two commands fix that instantly:

| Command | Effect |
|---|---|
| `pwd` | **P**rint **w**orking **d**irectory — shows where you are right now |
| `ls` | **L**ist the files and folders in the current directory |

Run these often. When in doubt, run `pwd`.

---

## Paths: Absolute vs. Relative

A path is just an address for a file or folder.

- **Absolute path** — starts from the very top (`/`) and gives the full address, e.g. `/home/leo/comp170/hello.py`. Works no matter where you currently are.
- **Relative path** — starts from wherever you currently are, e.g. `hello.py` or `scripts/hello.py`.

Two special shorthand names show up constantly:

| Symbol | Means |
|---|---|
| `.` | The current directory |
| `..` | The parent directory (one level up) |
| `~` | Your home directory |
| `-` | The previous directory you were in (used with `cd`) |

---

## Your First Terminal Session, Step by Step

**1. See where you are:**
```
$ pwd
/home/leo
```

**2. See what's there:**
```
$ ls
comp170  Documents  Downloads
```

**3. Move into a folder:**
```
$ cd comp170
```

**4. Confirm you moved:**
```
$ pwd
/home/leo/comp170
```

**5. Make a new folder for today's work:**
```
$ mkdir week01
```

**6. Move into it and create a file:**
```
$ cd week01
$ touch hello.py
```

**7. Confirm the file exists:**
```
$ ls
hello.py
```

From here, `vim hello.py` or `nano hello.py` opens it for editing.

---

## Essential Commands

### Finding Out Where You Are and What's There

| Command | Effect |
|---|---|
| `pwd` | Print the current directory |
| `ls` | List files and folders here |
| `ls -l` | List with details — permissions, size, date |
| `ls -a` | List everything, including hidden files (names starting with `.`) |
| `ls -la` | Combine both: details, including hidden files |

### Moving Around

| Command | Effect |
|---|---|
| `cd foldername` | Move into `foldername` (relative path) |
| `cd /full/path` | Move to an absolute path |
| `cd ..` | Move up one level, to the parent directory |
| `cd ~` or `cd` | Go straight to your home directory |
| `cd -` | Go back to the previous directory |

### Working with Folders

| Command | Effect |
|---|---|
| `mkdir name` | Make a new directory (**m**a**k**e **dir**ectory) |
| `mkdir -p a/b/c` | Make nested directories in one shot, creating parents as needed |
| `rmdir name` | Remove an **empty** directory |
| `rm -r name` | Remove a directory and everything inside it — irreversible, use with care |

### Working with Files

| Command | Effect |
|---|---|
| `touch file.py` | Create an empty file, or update its timestamp if it exists |
| `cp source dest` | **C**o**p**y a file |
| `cp -r source dest` | Copy a directory and its contents |
| `mv source dest` | **M**o**v**e a file — also how you rename, since renaming is just moving to a new name in the same place |
| `rm file.py` | Remove (delete) a file — irreversible, no trash bin, use with care |
| `cat file.py` | Print the entire contents of a file to the screen |
| `less file.py` | View a file one screen at a time — `q` to quit, arrow keys to scroll |

### Getting Information

| Command | Effect |
|---|---|
| `man command` | Open the manual page for `command` — `q` to quit |
| `command --help` | Print a short usage summary for most commands |
| `whoami` | Print your username |
| `history` | List recently run commands |
| `clear` | Clear the terminal screen |

---

## Recovering from Common Problems

**"I don't know where I am."**
Run `pwd`. Then `ls` to see what's around you.

**"`cd` says no such file or directory."**
You likely mistyped the name, or the folder is somewhere else. Run `ls` first to see the exact spelling of what's actually there — folder and file names are case-sensitive (`Week01` and `week01` are different).

**"I deleted something I needed."**
There is no undo for `rm` in the terminal — it does not go to a recycle bin. Always double-check the name before running `rm`, especially with `rm -r`.

**"My command seems stuck / frozen."**
Press `Ctrl-C` to cancel whatever is running and get your prompt back.

**"I want to redo a command I ran a minute ago."**
Press the **Up arrow** to cycle back through recent commands, or check `history`.

---

## A Minimal Workflow for This Course

For getting to your code and running it in COMP 170, this loop is all you need:

```
pwd                    ← confirm where you are
ls                      ← see what's here
cd foldername           ← move into your course folder
nano script.py          ← (or vim) write your code
python3 script.py       ← run your program
```

---

## What the Terminal Looks Like in Practice

```
leo@machine:~/comp170/week01$ ls
hello.py
leo@machine:~/comp170/week01$ cat hello.py
print("Hello, World!")
leo@machine:~/comp170/week01$ python3 hello.py
Hello, World!
```

- The text before `$` is the **prompt** — it typically shows your username, machine name, and current directory, so you can often tell where you are without even running `pwd`.
- Everything after `$` is what you typed; everything below is the output.

---

## Cheat Sheet (One Page)

| Command | Effect |
|---|---|
| `pwd` | Show current directory |
| `ls` / `ls -la` | List files / list all, with details |
| `cd folder` | Move into a folder |
| `cd ..` | Move up one level |
| `cd ~` | Go home |
| `cd -` | Go to previous directory |
| `mkdir name` | Make a directory |
| `mkdir -p a/b/c` | Make nested directories |
| `rmdir name` | Remove an empty directory |
| `rm -r name` | Remove a directory and its contents |
| `touch file` | Create an empty file |
| `cp a b` | Copy a file |
| `cp -r a b` | Copy a directory |
| `mv a b` | Move or rename |
| `rm file` | Delete a file |
| `cat file` | Print file contents |
| `less file` | View file one screen at a time |
| `man command` | Manual page for a command |
| `Ctrl-C` | Cancel the running command |

---

## Going Further (Optional)

You now know enough of the shell to do everything required in this course. If you want to go deeper:

- `man command` in front of any command name (e.g. `man ls`) opens its full manual — `q` to quit.
- Wildcards like `*` (e.g. `ls *.py`) match multiple files at once and are worth learning early.
- Once navigation feels comfortable, `./intro-vim.md` and `./intro-nano.md` cover editing the files you've just learned to find.
