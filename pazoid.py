#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAZOID — Hypnotic Infinite Password Generator
Version: 2.9 (Ctrl+C Reminder Aligned to Grid)
Author: Jon
License: MIT
"""

import random
import string
import time
import sys

# ---------------------------- HEADER ----------------------------
HEADER = r"""
 ▄▄▄· ▄▄▄· ·▄▄▄▄•      ▪  ·▄▄▄▄  
▐█ ▄█▐█ ▀█ ▪▀·.█▌▪     ██ ██▪ ██ 
 ██▀·▄█▀▀█ ▄█▀▀▀• ▄█▀▄ ▐█·▐█· ▐█▌
▐█▪·•▐█ ▪▐▌█▌▪▄█▀▐█▌.▐▌▐█▌██. ██ 
.▀    ▀  ▀ ·▀▀▀ • ▀█▄▀▪▀▀▀▀▀▀▀▀•
            Pazoid — Password Generator
"""

# ---------------------------- USER INPUT ----------------------------

def prompt_user():
    print(HEADER)
    while True:
        try:
            length = int(input("Password length (1–60): "))
            if 1 <= length <= 60:
                break
        except ValueError:
            pass
        print("⚠️ Enter a valid number between 1 and 60.")

    include_symbols = input("Include symbols (!@#$%^&*)? [y/n]: ").strip().lower() == 'y'
    include_greek = input("Include Greek letters (αβγδε...)? [y/n]: ").strip().lower() == 'y'
    include_mixed_case = input("Include uppercase letters? [y/n]: ").strip().lower() == 'y'

    while True:
        try:
            rows = int(input("Grid rows (1–200): "))
            if 1 <= rows <= 200:
                break
        except ValueError:
            pass
        print("⚠️ Enter a valid number between 1 and 200.")

    return length, include_symbols, include_greek, include_mixed_case, rows

# ---------------------------- CHARSET ----------------------------

def build_charset(include_symbols, include_greek, include_mixed_case):
    charset = list(string.ascii_lowercase + string.digits)
    if include_symbols:
        charset += list("!@#$%^&*()_-+=<>?/|~{}[];:.,")
    if include_mixed_case:
        charset += list(string.ascii_uppercase)
    if include_greek:
        charset += list("αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
    return charset

# ---------------------------- PASSWORD GENERATOR ----------------------------

def generate_password(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

# ---------------------------- GRID UPDATER ----------------------------

def run_grid(length, charset, rows):
    """
    Each row updates independently with randomized intervals.
    Bottom Ctrl+C reminder aligned to grid right edge.
    """
    FAST_CENTER = 0.075
    FAST_MIN = max(0.01, FAST_CENTER - 0.05)
    FAST_MAX = FAST_CENTER + 0.125

    passwords = [generate_password(length, charset) for _ in range(rows)]
    next_update = [time.time() for _ in range(rows)]  # immediate first update

    max_len = max(len(pw) for pw in passwords)
    reminder = "Press Ctrl+C to exit"
    reminder_line = " " * max(0, max_len - len(reminder)) + reminder

    # Print header + grid + reminder
    sys.stdout.write(HEADER + "\n\n")
    for pw in passwords:
        sys.stdout.write(pw + "\n")
    sys.stdout.write(reminder_line + "\n")
    sys.stdout.flush()

    try:
        while True:
            now = time.time()
            for i in range(rows):
                if now >= next_update[i]:
                    # Move cursor to line
                    sys.stdout.write(f"\033[{rows - i + 1}A")  # +1 for reminder line
                    sys.stdout.write("\033[2K")               # clear line
                    pw = generate_password(length, charset)
                    sys.stdout.write(pw + "\n")
                    sys.stdout.write(f"\033[{rows - i + 1}B")  # move back down
                    sys.stdout.flush()
                    passwords[i] = pw
                    next_update[i] = now + random.uniform(FAST_MIN, FAST_MAX)

            # Update reminder alignment in case max password length changes
            new_max_len = max(len(pw) for pw in passwords)
            if new_max_len != max_len:
                max_len = new_max_len
                reminder_line = " " * max(0, max_len - len(reminder)) + reminder
                sys.stdout.write(f"\033[1A\033[2K{reminder_line}\n")  # update reminder line
                sys.stdout.flush()

            time.sleep(0.003)

    except KeyboardInterrupt:
        sys.stdout.write("\033[0m\n\nPazoid paused. Thanks for drifting through the flow.\n")
        sys.stdout.flush()

# ---------------------------- MAIN ----------------------------

def main():
    length, include_symbols, include_greek, include_mixed_case, rows = prompt_user()
    charset = build_charset(include_symbols, include_greek, include_mixed_case)
    run_grid(length, charset, rows)

if __name__ == "__main__":
    main()
