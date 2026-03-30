# Caesar Cipher Tool

A command-line tool written in Python to encrypt, decrypt, and brute force Caesar cipher messages — with coloured terminal output.

---

##  What it looks like

```
╔══════════════════════════════════╗
║        CAESAR CIPHER TOOL        ║
╚══════════════════════════════════╝

  What do you want to do?
  1. Encrypt a message
  2. Decrypt a message
  3. Brute force a message
  4. Exit

  Enter choice (1-4): 1

  Enter message to encrypt: Hello World
  Enter shift key (1-25): 3

  ✓  Encrypted: Khoor Zruog
  Shift key used: 3
```

---

##  Features

- Encrypt any message with a shift key of your choice
- Decrypt a message if you know the shift key
- Brute force a message — tries all 25 possible keys to crack it without the key
- Input validation — handles invalid keys gracefully without crashing
- Colour-coded terminal output (red / green / cyan)

---

## How to run

**Requirements:** Python 3 — no external libraries needed.

```bash
python3 caesar_cipher.py
```

Then use the menu to encrypt, decrypt, or brute force a message.

---

## How it works

A Caesar cipher shifts every letter in a message by a fixed number of positions in the alphabet.

For example with a shift of 3:
```
A → D
B → E
H → K
HELLO → KHOOR
```

To decrypt, you just shift back by the same number. The shift value is the **key** — without it you would need to brute force all 25 possible shifts to find the original message.

The `ord()` and `chr()` Python functions handle the shifting:
```python
ord('A')        # returns 65 — the ASCII number for that letter
chr(65)         # returns 'A' — converts a number back to a letter
ord('A') + 3    # = 68 = 'D'
```

Wrapping around the alphabet is handled with `% 26`:
```python
# Without % 26:  Z(25) + 3 = 28  ❌ goes past the alphabet
# With % 26:     Z(25) + 3 = 2   ✅ wraps around to C
```

---

## Project structure

```
caesar-cipher/
│
├── caesar_cipher.py   
└── README.md          
```

---

## Built with

- Python 3
- ANSI escape codes for terminal colours
- No external libraries — fully standard library

---

## Notes

- Colours work in macOS Terminal, iTerm2, and any modern terminal
- Spaces, numbers, and symbols are left unchanged — only letters are shifted
- Brute force tries all 25 possible shifts and prints them all — just scan for the one that makes sense

---

*Mini project — built to practise Python functions, loops, and ASCII character manipulation.*
