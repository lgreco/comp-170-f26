# `vim`: An Introduction and Cheat Sheet

## What Is a Text Editor?

A text editor is a program for writing and changing plain text — no fonts, no bold, no bullet points, no invisible formatting codes. This is different from Word or Google Docs, which save documents full of formatting information you never see. Code has to be plain text, because the program reading it (the Python interpreter, in this course) only understands the characters themselves, not how they're styled.

Every programmer needs a text editor. `vim` is one of the oldest and most widely available — it ships on nearly every Unix-like system (Linux, macOS), which is exactly why this course uses it: the skills transfer everywhere.

If `vim`'s design below feels like more than you want to take on right now, `./intro-nano.md` covers a simpler editor with no modes to learn — a perfectly fine substitute for this course. Come back to `vim` later if you're curious; it has a much higher ceiling once you know it.

---

## The One Thing You Must Understand First: Modes

Most editors have one mode: open the file, type, text appears. `vim` has multiple modes, and the two that matter today are:

| Mode | What it does |
|---|---|
| **Normal mode** | Navigate, delete, copy, save, quit. Keystrokes are *commands*, not text. |
| **Insert mode** | Type text. Keystrokes appear as characters in the file. |

**`vim` always starts in Normal mode.**

This is why new users get stuck: they open a file, start typing, and letters vanish or the cursor jumps around instead of text appearing. That's Normal mode treating your keystrokes as commands, not as text to insert.

The golden rule:
- Press `i` to enter Insert mode and start typing.
- Press `Esc` to return to Normal mode.

When in doubt, press `Esc`. It never hurts to go back to Normal mode.

---

## Opening a File

```
$ vim filename.py
```

If the file exists, `vim` opens it. If it doesn't exist yet, `vim` creates it the first time you save.

---

## Your First Editing Session, Step by Step

**1. Open a new file:**
```
$ vim hello.py
```

**2. Enter Insert mode:**
```
i
```
You'll see `-- INSERT --` at the bottom of the screen. You can now type.

**3. Type a short program:**
```python
print("Hello, World!")
```

**4. Return to Normal mode:**
```
Esc
```
`-- INSERT --` disappears. You're back in Normal mode.

**5. Save the file:**
```
:w
```
The `:` opens a command prompt at the bottom of the screen. `w` stands for *write*.

**6. Quit `vim`:**
```
:q
```

Steps 5 and 6 can be combined into one command:
```
:wq
```

**7. Run what you wrote:**
```
$ python3 hello.py
Hello, World!
```

---

## Essential Commands

### Switching Modes

| Key | Effect |
|---|---|
| `i` | Enter Insert mode, before the cursor |
| `a` | Enter Insert mode, after the cursor |
| `o` | Open a new line below and enter Insert mode |
| `Esc` | Return to Normal mode |

### Saving and Quitting (type `:` first, in Normal mode)

| Command | Effect |
|---|---|
| `:w` | Save (write) |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit without saving — discard all changes |

### Moving Around (Normal mode, no `:` needed)

Arrow keys work. Once you're comfortable, these are faster because your hands never leave the home row:

| Key | Movement |
|---|---|
| `h` | Left |
| `l` | Right |
| `j` | Down |
| `k` | Up |
| `0` | Beginning of the line |
| `$` | End of the line |
| `gg` | Top of the file |
| `G` | Bottom of the file |

### Editing (Normal mode)

| Key | Effect |
|---|---|
| `x` | Delete the character under the cursor |
| `dd` | Delete (cut) the entire line |
| `u` | Undo the last change |
| `Ctrl-r` | Redo (undo the undo) |

---

## Recovering from Common Problems

**"I can't type anything — the letters aren't appearing."**
You're in Normal mode. Press `i` to enter Insert mode.

**"I pressed some keys and now the screen looks strange."**
Press `Esc` a few times to make sure you're back in Normal mode, then press `u` to undo. If that doesn't help, `:q!` quits without saving so you can start fresh.

**"I can't quit."**
Press `Esc` to make sure you're in Normal mode, then type `:q!` and press Enter.

**"I saved to the wrong file name."**
`:w newname.py` saves a copy under a new name.

---

## A Minimal Workflow for This Course

For writing Python scripts in COMP 170, this loop is all you need:

```
vim script.py       ← open the file
i                    ← enter Insert mode
(write your code)
Esc                  ← return to Normal mode
:wq                  ← save and quit
python3 script.py    ← run your program
```

Repeat until the program does what you want.

---

## What `vim` Looks Like in Practice

```
  1 name = "Leo"
  2 print("Hello,", name)
  3 print("Welcome to COMP 170.")
~
~
~
-- INSERT --
```

- The numbers on the left are line numbers.
- The `~` lines are empty — they aren't part of the file.
- `-- INSERT --` at the bottom confirms you're in Insert mode; it disappears in Normal mode.

---

## Cheat Sheet (One Page)

| Command | Effect |
|---|---|
| `vim file.py` | Open (or create) a file |
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `o` | New line below, then insert |
| `Esc` | Back to Normal mode |
| `h` `j` `k` `l` | Left, down, up, right |
| `0` / `$` | Start / end of line |
| `gg` / `G` | Top / bottom of file |
| `x` | Delete character |
| `dd` | Delete line |
| `u` / `Ctrl-r` | Undo / redo |
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit, discard changes |

---

## Going Further (Optional)

You now know enough `vim` to do everything required in this course. If you want to go deeper:

- `:help` opens `vim`'s built-in manual (`:q` to close it).
- `vimtutor` is an interactive 30-minute tutorial built into most systems — run it in the terminal.
- `vim` has a steep learning curve but a very high ceiling; many professional programmers use nothing else.
