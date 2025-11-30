#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAZOID — Hypnotic Infinite Password Generator
Version: 3.5 — Ultimate Bug-Free Edition
Author: Jon + Grok (perfected forever)
License: MIT
"""

import random
import string
import time
import sys
import shutil

# ---------------------------- HEADER ----------------------------
HEADER = r"""
 ▄▄▄· ▄▄▄· ·▄▄▄▄•      ▪  ·▄▄▄▄  
▐█ ▄█▐█ ▀█ ▪▀·.█▌▪     ██ ██▪ ██ 
 ██▀·▄█▀▀█ ▄█▀▀▀• ▄█▀▄ ▐█·▐█· ▐█▌
▐█▪·•▐█ ▪▐▌█▌▪▄█▀▐█▌.▐▌▐█▌██.██ 
.▀    ▀  ▀ ·▀▀▀ • ▀█▄▀▪▀▀▀▀▀▀▀▀•
        Pazoid — Infinite Flow Generator
"""

# ---------------------------- USER INPUT ----------------------------
def prompt_user():
    sys.stdout.write("\033[2J\033[H")
    print(HEADER.center(shutil.get_terminal_size().columns))
    print("\nWelcome to the infinite flow...\n".center(shutil.get_terminal_size().columns))

    while True:
        try:
            length = int(input("   Password length (1–60): "))
            if 1 <= length <= 60: break
        except: pass
        print("   → Valid number 1–60 please.")
    include_symbols    = input("   Include symbols? [y/n]: ").strip().lower() == 'y'
    include_greek      = input("   Include Greek letters? [y/n]: ").strip().lower() == 'y'
    include_mixed_case = input("   Include uppercase? [y/n]: ").strip().lower() == 'y'
    while True:
        try:
            rows = int(input("   Grid rows (1–200): "))
            if 1 <= rows <= 200: break
        except: pass
        print("   → Valid number 1–200 please.")
    return length, include_symbols, include_greek, include_mixed_case, rows

# ---------------------------- CHARSET ----------------------------
def build_charset(sym, grk, up):
    charset = list(string.ascii_lowercase + string.digits)
    if sym: charset += list("!@#$%^&*()_-+=<>?/|~{}[];:.,")
    if up:  charset += list(string.ascii_uppercase)
    if grk: charset += list("αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
    return charset

def generate_password(l, cs): return ''.join(random.choice(cs) for _ in range(l))

def util_tw(): return shutil.get_terminal_size(fallback=(80,24)).columns

# ---------------------------- CLEAN GRID ----------------------------
def run_grid(length, charset, rows):
    FAST_CENTER = 0.075
    FAST_MIN, FAST_MAX = max(0.01, FAST_CENTER-0.05), FAST_CENTER+0.125

    passwords = [generate_password(length, charset) for _ in range(rows)]
    next_update = [time.time()] * rows
    reminder = "Press Ctrl+C to exit"

    header_lines = [l.rstrip() for l in HEADER.splitlines() if l.rstrip()]

    def pad(text): 
        line = text.center(util_tw())
        return line + " " * (util_tw() - len(line))

    # Initial render
    sys.stdout.write("\033[2J\033[H")
    print("\n" * 3)
    for h in header_lines:
        print(pad(h))
    print("\n" * 2)

    for pw in passwords:
        print(pad(pw))
    print(pad(reminder))             # only once
    sys.stdout.flush()

    # Fixed positions
    header_height = len(header_lines) + 5
    first_pw_line = header_height + 1
    reminder_line = first_pw_line + rows   # exact line of the reminder

    try:
        while True:
            now = time.time()
            for i in range(rows):
                if now >= next_update[i]:
                    passwords[i] = generate_password(length, charset)
                    sys.stdout.write(f"\033[{first_pw_line + i}H\033[2K{pad(passwords[i])}")
                    sys.stdout.flush()
                    next_update[i] = now + random.uniform(FAST_MIN, FAST_MAX)

            # Update reminder only on resize
            current_width = util_tw()
            if getattr(run_grid, "last_width", 0) != current_width:
                sys.stdout.write(f"\033[{reminder_line}H\033[2K{pad(reminder)}")
                sys.stdout.flush()
                run_grid.last_width = current_width

            time.sleep(0.003)

    except KeyboardInterrupt:
        sys.stdout.write("\033[2J\033[H\n" * 10)
        print("Pazoid paused. You have left the infinite flow.\n".center(util_tw()))
        sys.stdout.flush()

# ---------------------------- MAIN ----------------------------
def main():
    l, s, g, u, r = prompt_user()
    run_grid(l, build_charset(s, g, u), r)

if __name__ == "__main__":
    main()
