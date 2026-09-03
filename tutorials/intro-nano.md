# `nano`: An Introduction and Cheat Sheet

## What Is a Text Editor?

A text editor is a program for writing and changing plain text — no fonts, no bold, no bullet points, no invisible formatting codes. This is different from Word or Google Docs, which save documents full of formatting information you never see. Code has to be plain text, because the program reading it (the Python interpreter, in this course) only understands the characters themselves, not how they're styled.

`nano` is a text editor that lives entirely in the terminal, like `vim`, but with one big difference for a first-timer: **there's nothing extra to learn before you can type.** You open it, you type, your words appear. No modes, no surprises. It ships on nearly every Linux system and is a very reasonable choice if this is your first time editing a file from the command line.

If you'd rather learn `vim` instead — more to learn up front, but a much higher ceiling, and the editor most professional programmers who live in the terminal actually use — see `./intro-vim.md`. Either is fine for this course.

---

## The One Thing You Must Understand First: No Modes, and the `^` Symbol

Unlike some editors, `nano` has only one mode: whatever you type is inserted as text, immediately, wherever your cursor is. There's no separate "command mode" to get stuck in.

Commands are given with the **Control key**, held down together with a letter. `nano` shows these on screen using a caret:

| Symbol | Means |
|---|---|
| `^` | Hold **Ctrl** and press the letter shown next to it |
| `M-` | Hold **Alt** (sometimes labeled Meta) and press the letter shown |

So `^O` means "hold Ctrl, press O" — not "type a caret, then O." You'll see a row of these shortcuts listed along the bottom of the screen at all times, which is `nano`'s biggest advantage for beginners: you never have to memorize the whole command set to get started, because the most useful commands are always visible.

---

## Opening a File

```
$ nano filename.py
```

If the file exists, `nano` opens it. If it doesn't exist yet, `nano` creates it the first time you save.

---

## Your First Editing Session, Step by Step

**1. Open a new file:**
```
$ nano hello.py
```

**2. Just start typing — there's no mode to switch into:**
```python
print("Hello, World!")
```

**3. Save the file:**
```
Ctrl-O
```
`nano` asks you to confirm the file name at the bottom of the screen (it shows the name you opened, e.g. `hello.py`). Press **Enter** to confirm and write the file.

**4. Exit `nano`:**
```
Ctrl-X
```
If you've saved already, this exits immediately. If you have unsaved changes, `nano` asks `Save modified buffer?` — press **Y** to save and exit, **N** to discard changes and exit, or **Ctrl-C** to cancel and stay in the editor.

**5. Run what you wrote:**
```
$ python3 hello.py
Hello, World!
```

---

## Essential Commands

All of these use the Control key (`^`) unless noted otherwise.

### Saving and Exiting

| Command | Effect |
|---|---|
| `Ctrl-O` | Save (**O**ut — writes the file; confirm the name with Enter) |
| `Ctrl-X` | Exit; prompts to save first if there are unsaved changes |

### Moving Around

Arrow keys, `Home`, `End`, `Page Up`, and `Page Down` all work as you'd expect. A few extra shortcuts:

| Command | Movement |
|---|---|
| `Ctrl-A` | Beginning of the line |
| `Ctrl-E` | End of the line |
| `Ctrl-Y` | Page up |
| `Ctrl-V` | Page down |
| `Ctrl-_` then a number, Enter | Go to a specific line number |

### Editing

| Command | Effect |
|---|---|
| `Ctrl-K` | Cut the current line (stores it for pasting) |
| `Ctrl-U` | Paste (uncut) whatever was last cut |
| `Alt-U` | Undo the last change *(most modern versions of `nano`)* |
| `Alt-E` | Redo (undo the undo) *(most modern versions of `nano`)* |

### Searching

| Command | Effect |
|---|---|
| `Ctrl-W` | Search (**W**here is) — type your search text, press Enter |
| `Ctrl-W`, then Enter again | Repeat the last search |

### Getting Help

| Command | Effect |
|---|---|
| `Ctrl-G` | Open `nano`'s built-in help screen; `Ctrl-X` to close it |

---

## Recovering from Common Problems

**"I don't see my changes take effect after I typed something."**
That shouldn't happen in `nano` — typed characters always appear immediately. If the screen looks wrong, you may have pressed a Control shortcut by accident; press `Ctrl-G` for help, or `Ctrl-C` to cancel whatever prompt is showing.

**"I can't figure out how to save."**
`Ctrl-O`, then press **Enter** to confirm the filename shown at the bottom.

**"I can't exit."**
`Ctrl-X`. If it asks `Save modified buffer?`, press **Y** (save and exit), **N** (discard and exit), or **Ctrl-C** (cancel, stay in the editor).

**"I saved to the wrong file name."**
When `Ctrl-O` shows the filename prompt, you can edit it before pressing Enter — type a new name and confirm to save a copy under that name instead.

**"I cut a line by accident."**
`Ctrl-U` immediately after pastes it right back.

---

## A Minimal Workflow for This Course

For writing Python scripts in COMP 170, this loop is all you need:

```
nano script.py        ← open the file
(write your code)      ← just type, no mode switch needed
Ctrl-O, Enter          ← save
Ctrl-X                 ← exit
python3 script.py      ← run your program
```

Repeat until the program does what you want.

---

## What `nano` Looks Like in Practice

```
  GNU nano 6.2                    hello.py
name = "Leo"
print("Hello,", name)
print("Welcome to COMP 170.")




^G Help    ^O Write Out  ^W Where Is   ^K Cut       ^X Exit
^R Read File ^\ Replace   ^_ Go To Line ^U Paste
```

- The top line names the editor version and the file you're editing.
- The bottom two rows are the shortcut bar — always visible, so you never have to guess what's available.
- There's no `-- INSERT --` indicator, because there's no separate mode to indicate; you can always type.

---

## Cheat Sheet (One Page)

| Command | Effect |
|---|---|
| `nano file.py` | Open (or create) a file |
| *(just type)* | Insert text — no mode switch needed |
| `Ctrl-A` / `Ctrl-E` | Start / end of line |
| `Ctrl-Y` / `Ctrl-V` | Page up / page down |
| `Ctrl-_` | Go to line number |
| `Ctrl-K` | Cut line |
| `Ctrl-U` | Paste |
| `Alt-U` / `Alt-E` | Undo / redo |
| `Ctrl-W` | Search |
| `Ctrl-G` | Help |
| `Ctrl-O` | Save |
| `Ctrl-X` | Exit (prompts to save if needed) |

---

## Going Further (Optional)

You now know enough `nano` to do everything required in this course. If you want to go deeper:

- `Ctrl-G` inside `nano` opens the full built-in help.
- `man nano` at the shell prints the complete manual page.
- Once file editing feels comfortable, it's worth trying `./intro-vim.md` — `vim`'s modal design takes longer to learn but rewards you with speed once the muscle memory sets in.
