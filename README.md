PAZOID — Infinite Terminal Password Generator
============================================

      ▄▄▄· ▄▄▄· ·▄▄▄▄•      ▪  ·▄▄▄▄  
     ▐█ ▄█▐█ ▀█ ▪▀·.█▌▪     ██ ██▪ ██ 
      ██▀·▄█▀▀█ ▄█▀▀▀• ▄█▀▄ ▐█·▐█· ▐█▌
     ▐█▪·•▐█ ▪▐▌█▌▪▄█▀▐█▌.▐▌▐█▌██. ██ 
      .▀    ▀  ▀ ·▀▀▀ • ▀█▄▀▪▀▀▀▀▀▀▀▀•
                  Pazoid — Password Generator

Version 1.0 — A fast, hypnotic, infinite password generator in your terminal.

----------------------------------------------------------
Features
----------------------------------------------------------

- ASCII CLI Header: Bold, stylized “PAZOID” banner for a retro hacker feel.
- Infinite Password Flow: Generates a grid of randomized passwords endlessly.
- Custom Settings:
    - Password length (1–60)
    - Include symbols, Greek letters, uppercase letters
    - Grid size (1–200 rows)
    - Fast, randomized independent refresh
- Smooth Terminal Display: Flicker-free updates using ANSI escape codes.
- Dynamic Iteration: Each row updates independently, creating a mesmerizing visual effect.
- Easy Exit: Press Ctrl+C to stop anytime.

----------------------------------------------------------
Demo
----------------------------------------------------------

Pg?BψγΖΑ{mcΜΤζr;XγΩ=43:χλWo+rJ
5-Παη6AqW@+3{)7λδrQNΦΟΝΨφχOμoΙ
AquL6Xη5πΚ<w{ΔvQoλ$/Υχ%I..o8Ε_
σWΞηΨδgMΝΜxwΡ:ζ=Vπφ\<ΟZ&QUΕ#2Θ
tpυc\Θ9zΑoBWlP$Ηα=ΖχΦdΛGE50eZΟ
Press Ctrl+C to exit

*Passwords continuously refresh at different speeds for a hypnotic effect.*

----------------------------------------------------------
Installation & Usage
----------------------------------------------------------

1. Clone the repository:

   git clone https://github.com/kron777/Pazoid.git
   cd Pazoid

2. Run Pazoid:

   python3 pazoid.py

3. Enter your desired settings when prompted:
   - Password length
   - Include symbols / Greek letters / uppercase letters
   - Grid rows

4. Watch the passwords flow! Press Ctrl+C to stop.

----------------------------------------------------------
Code Structure
----------------------------------------------------------

- pazoid.py — Main Python script
    - prompt_user(): Collects user preferences
    - build_charset(): Builds the character set based on choices
    - generate_password(): Generates a random password
    - run_grid(): Handles smooth infinite password grid updates

No external dependencies — works on Linux, Mac, Windows.

----------------------------------------------------------
Contributing
----------------------------------------------------------

Contributions are welcome! Feel free to:
- Suggest new features
- Improve ASCII art or visual effects
- Enhance charset options

Fork the repo, make your changes, and submit a pull request.

----------------------------------------------------------
License
----------------------------------------------------------

MIT License © Jon (kron777)

----------------------------------------------------------
Call to Action
----------------------------------------------------------

Star it, fork it, and get lost in the Pazoid flow!
