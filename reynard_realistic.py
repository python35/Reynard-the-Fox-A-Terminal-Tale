#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys
import random

def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Display text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_ascii(frames, repeat=1, delay=0.2):
    """Show an animation of ASCII frames."""
    for _ in range(repeat):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(delay)

# More realistic ASCII art for the fox (Reynard)
fox = """
⠀⠀⠀⠀⠀⠀⠀⣀⡈⢯⡉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣉⠹⠷⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠹⠝⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠀⣀⣠⣤⣤⠄⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠚⠢⠼⠿⠟⢛⣾⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣻⠃⠀⠀⠀⠀⢸⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⢻⡷⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⢽⡟⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢧⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣷⣱⡀⠀⠀⠀⠀⣸⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣷⡙⣆⠀⠀⣾⠃⠀⠀⠀⠀⠈⢽⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡇⢷⡏⠃⢠⠇⠀⠀⣀⠄⠀⠀⠀⣿⡖⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡇⢨⠇⠀⡼⢀⠔⠊⠀⠀⠀⠀⠀⠘⣯⣄⢀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡇⣼⡀⣰⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⣇⢻⣧⡄
⠀⠀⠀⠀⣀⣮⣿⣿⣿⣿⡭⢉⠟⠛⠳⢤⣄⣀⣀⣀⣀⡴⢠⠨⢻⣿
⠀⠀⢀⣾⣿⣿⣿⣿⢏⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢨⣿
⠀⣰⣿⣿⣿⣿⣿⣿⡱⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢭⣾⠏
⣰⡿⠟⠋⠛⢿⣿⣿⣊⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⡿⠋⠀
⠋⠁⠀⠀⠀⠀⠈⠑⠿⢶⣄⣀⣀⣀⣀⣀⣄⣤⡶⠿⠟⠋⠁⠀⠀⠀

"""

fox_sneaky = """
⠀⠀⠀⠀⠀⠀⠀⣀⡈⢯⡉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣉⠹⠷⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠹⠝⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠀⣀⣠⣤⣤⠄⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠚⠢⠼⠿⠟⢛⣾⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣻⠃⠀⠀⠀⠀⢸⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⢻⡷⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⢽⡟⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢧⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣷⣱⡀⠀⠀⠀⠀⣸⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣷⡙⣆⠀⠀⣾⠃⠀⠀⠀⠀⠈⢽⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡇⢷⡏⠃⢠⠇⠀⠀⣀⠄⠀⠀⠀⣿⡖⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡇⢨⠇⠀⡼⢀⠔⠊⠀⠀⠀⠀⠀⠘⣯⣄⢀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡇⣼⡀⣰⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⣇⢻⣧⡄
⠀⠀⠀⠀⣀⣮⣿⣿⣿⣿⡭⢉⠟⠛⠳⢤⣄⣀⣀⣀⣀⡴⢠⠨⢻⣿
⠀⠀⢀⣾⣿⣿⣿⣿⢏⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢨⣿
⠀⣰⣿⣿⣿⣿⣿⣿⡱⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢭⣾⠏
⣰⡿⠟⠋⠛⢿⣿⣿⣊⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⡿⠋⠀
⠋⠁⠀⠀⠀⠀⠈⠑⠿⢶⣄⣀⣀⣀⣀⣀⣄⣤⡶⠿⠟⠋⠁⠀⠀⠀

"""

fox_laughing = """
⠀⠀⠀⠀⠀⠀⠀⣀⡈⢯⡉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣉⠹⠷⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠹⠝⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠀⣀⣠⣤⣤⠄⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠚⠢⠼⠿⠟⢛⣾⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⣻⠃⠀⠀⠀⠀⢸⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⢻⡷⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⢽⡟⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢧⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣷⣱⡀⠀⠀⠀⠀⣸⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣷⡙⣆⠀⠀⣾⠃⠀⠀⠀⠀⠈⢽⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡇⢷⡏⠃⢠⠇⠀⠀⣀⠄⠀⠀⠀⣿⡖⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡇⢨⠇⠀⡼⢀⠔⠊⠀⠀⠀⠀⠀⠘⣯⣄⢀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡇⣼⡀⣰⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⣇⢻⣧⡄
⠀⠀⠀⠀⣀⣮⣿⣿⣿⣿⡭⢉⠟⠛⠳⢤⣄⣀⣀⣀⣀⡴⢠⠨⢻⣿
⠀⠀⢀⣾⣿⣿⣿⣿⢏⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢨⣿
⠀⣰⣿⣿⣿⣿⣿⣿⡱⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢭⣾⠏
⣰⡿⠟⠋⠛⢿⣿⣿⣊⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⡿⠋⠀
⠋⠁⠀⠀⠀⠀⠈⠑⠿⢶⣄⣀⣀⣀⣀⣀⣄⣤⡶⠿⠟⠋⠁⠀⠀⠀

"""

# More realistic ASCII art for the lion (King Noble)
lion = """
           ,  ,, ,
      , ,; ; ;;  ; ;  ;
   , ; ';  ;  ;; .-''\ ; ;
, ;  ;`  ; ,; . / /8b \ ; ;
`; ; .;'         ;,\8 |  ;  ;
 ` ;/   / `_      ; ;;    ;  ; ;
    |/.'  /9)    ;  ; `    ;  ; ;
   ,/'          ; ; ;  ;   ; ; ; ;
  /_            ;    ;  `    ;  ;
 `?8P"  .      ;  ; ; ; ;     ;  ;;
 | ;  .:: `     ;; ; ;   `  ;  ;
 `' `--._      ;;  ;;  ; ;   ;   ;
  `-..__..--''   ; ;    ;;   ; ;   ;
              ;    ; ; ;   ;     ;
"""

# More realistic ASCII art for the bear (Bruin)
bear = """
    .--.              .--.
   : (\ ". _......_ ." /) :
    '.    `        `    .'
     /'   _        _   `\
    /     0}      {0     \
   |       /      \       |
   |     /'        `\     |
    \   | .  .==.  . |   /
     '._ \.' \__/ './ _.'
     /  ``'._-''-_.'``  \
"""

# More realistic ASCII art for the cat (Tibert)
cat = r"""
    /\_/\
   ( o.o )
    > ^ <
   /  |  \
  /   |   \
 |    |    |
  \___|___/
"""

# More realistic ASCII art for the badger (Grimbart)
badger = r"""
                ___,,___
           _,-='=- =-  -`"--.__,,.._
        ,-;// /  - -       -   -= - "=.
      ,'///    -     -   -   =  - ==-=\`.
     |/// /  =    `. - =   == - =.=_,,._ `=/|
    ///    -   -    \  - - = ,ndDMHHMM/\b  \\
  ,' - / /        / /\ =  - /MM(,,._`YQMML  `|
 <_,=^Kkm / / / / ///H|wnWWdMKKK#""-;. `"0\  |
        `""QkmmmmmnWMMM\""WHMKKMM\   `--. \> \
              `""'  `->>>    ``WHMb,.    `-_<@)
                                `"QMM`.
                                   `>>>
"""

# More realistic ASCII art for the hare (Cuwaert)
hare = """
      ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y    
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
"""

# More realistic ASCII art for the rooster (Chanticleer)
rooster = """              ~-.
          ,,,;            ~-.~-.~-
         (.../           ~-.~-.~-.~-.~-.
         } o~`,         ~-.~-.~-.~-.~-.~-.
         (/    \      ~-.~-.~-.~-.~-.~-.~-.
          ;    \    ~-.~-.~-.~-.~-.~-.~-.
         ;     {_.~-.~-.~-.~-.~-.~-.~
        ;:  .-~`    ~-.~-.~-.~-.~-.
       ;.: :'    ._   ~-.~-.~-.~-.~-
        ;::`-.    '-._  ~-.~-.~-.~-
         ;::. `-.    '-,~-.~-.~-.
          ';::::.`''-.-'
            ';::;;:,:'
               '||"
               / |
             ~` ~"'
"""

# ASCII art for the castle
castle = r"""
                                                  !_
                                                  |*~=-.,
                                                  |_,-'`
                                                  |
                                                  |
                                                 /^\
                   !_                           /   \
                   |*`~-.,                     /,    \
                   |.-~^`                     /#"     \
                   |                        _/##_   _  \_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \
     | _- =-     |-_   | ((* |      |= _=       | -    |___\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^       
"""

# ASCII art for the tree
tree = r"""
      /\\
     /  \\
    /    \\
   /      \\
  /        \\
 /          \\
/____________\\
     ||||
     ||||
     ||||
     ||||
     ||||
     ||||
"""

# ASCII art for the forest
forest = r"""
      /\\      /\\      /\\
     /  \\    /  \\    /  \\
    /    \\  /    \\  /    \\
   /      \\/      \\/      \\
  /        \\      /        \\
 /          \\    /          \\
/____________\\  /____________\\
     ||||          ||||
     ||||          ||||
     ||||          ||||
"""

# ASCII art for the barn
barn = """
                          
                           _.-^-._    .--.
                        .-'   _   '-. |__|
                       /     |_|     \|  |
                      /               \  |
                     /|     _____     |\ |
                      |    |==|==|    |  |
  |---|---|---|---|---|    |--|--|    |  |
  |---|---|---|---|---|    |==|==|    |  |
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

# Title animation frames
title_frames = [
"""
██████╗ ███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗   ╚████╔╝ ██╔██╗ ██║███████║██████╔╝██║  ██║
██╔══██╗██╔══╝    ╚██╔╝  ██║╚██╗██║██╔══██║██╔══██╗██║  ██║
██║  ██║███████╗   ██║   ██║ ╚████║██║  ██║██║  ██║██████╔╝
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                           
████████╗██╗  ██╗███████╗    ███████╗ ██████╗ ██╗  ██╗     
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔═══██╗╚██╗██╔╝     
   ██║   ███████║█████╗      █████╗  ██║   ██║ ╚███╔╝      
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║   ██║ ██╔██╗      
   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝██╔╝ ██╗     
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝     
""",
"""
██████╗ ███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗   ╚████╔╝ ██╔██╗ ██║███████║██████╔╝██║  ██║
██╔══██╗██╔══╝    ╚██╔╝  ██║╚██╗██║██╔══██║██╔══██╗██║  ██║
██║  ██║███████╗   ██║   ██║ ╚████║██║  ██║██║  ██║██████╔╝
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                           
████████╗██╗  ██╗███████╗    ███████╗ ██████╗ ██╗  ██╗    ★
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔═══██╗╚██╗██╔╝   ★ ★
   ██║   ███████║█████╗      █████╗  ██║   ██║ ╚███╔╝    ★   ★
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║   ██║ ██╔██╗   ★     ★
   ██║   ██║  ██║███████╗    ██║     ╚██████╔╝██╔╝ ██╗ ★       ★
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝★         ★
"""
]

def display_scene(title, ascii_art, text_lines):
    """Display a scene with title, ASCII art and text."""
    clear_screen()
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70 + "\n")
    print(ascii_art)
    print()
    for line in text_lines:
        type_text(line)
        time.sleep(0.3)
    print("\n" + "-" * 70)
    input("Press Enter to continue...")

def main():
    clear_screen()
    animate_ascii(title_frames, repeat=3, delay=0.5)
    
    # Prologue
    display_scene(
        "PROLOGUE",
        forest,
        [
            "Long ago, in the animal kingdom of Flanders and the Netherlands,",
            "there lived a fox named Reynard.",
            "He was known for his cunning and his tricks.",
            "This is his story..."
        ]
    )
    
    # Scene 1: The Court of King Noble
    display_scene(
        "THE COURT OF KING NOBLE",
        castle,
        [
            "King Noble the Lion held court and all animals were invited.",
            "Everyone was present, except for Reynard the Fox.",
            "The king was not pleased with his absence.",
            "Many animals had complaints about Reynard's tricks."
        ]
    )
    
    # Scene 2: The Complaints
    display_scene(
        "THE COMPLAINTS",
        rooster,
        [
            "Chanticleer the Rooster stepped forward and spoke:",
            "'Your Majesty, Reynard has eaten my children!'",
            "'He has murdered seven of my chicks!'",
            "The king was furious and promised justice."
        ]
    )
    
    display_scene(
        "THE COMPLAINTS",
        hare,
        [
            "Cuwaert the Hare came forward trembling:",
            "'Reynard pretended he would teach me how to pray,'",
            "'but then he tried to strangle me!'",
            "The other animals were shocked by these stories."
        ]
    )
    
    # Scene 3: The Defense
    display_scene(
        "THE DEFENSE",
        badger,
        [
            "Grimbart the Badger, Reynard's nephew, defended him:",
            "'My uncle is being treated unfairly! He has reformed!'",
            "'He now lives as a hermit and does penance for his sins!'",
            "But few believed Grimbart's words."
        ]
    )
    
    # Scene 4: Bruin the Bear
    display_scene(
        "BRUIN THE BEAR",
        bear,
        [
            "King Noble sent Bruin the Bear to fetch Reynard.",
            "Bruin found Reynard at his castle Malpertuus.",
            "Reynard greeted him kindly, but had devised a trick."
        ]
    )
    
    display_scene(
        "THE HONEY TRAP",
        tree,
        [
            "Reynard told Bruin about a tree full of honey:",
            "'Dear Bruin, not far from here is a tree full of sweet honey.'",
            "Bruin, greedy as he was, followed Reynard to the tree.",
            "The tree was split and had wedges in it."
        ]
    )
    
    display_scene(
        "THE TRAP",
        fox_laughing,
        [
            "Reynard convinced Bruin to stick his head in the split.",
            "When Bruin did so, Reynard pulled out the wedges.",
            "Bruin was trapped in the tree, unable to move.",
            "Reynard laughed and called the villagers."
        ]
    )
    
    display_scene(
        "THE ESCAPE",
        bear,
        [
            "The villagers beat Bruin with sticks and axes.",
            "In his desperation, Bruin tore himself free, but lost",
            "his ears and part of his skin in the process.",
            "Bleeding and humiliated, he returned to the court."
        ]
    )
    
    # Scene 5: Tibert the Cat
    display_scene(
        "TIBERT THE CAT",
        cat,
        [
            "King Noble was furious and sent Tibert the Cat.",
            "Tibert was cautious, as he did not trust Reynard.",
            "Nevertheless, he went to Malpertuus to fetch Reynard."
        ]
    )
    
    display_scene(
        "THE MOUSE TRAP",
        barn,
        [
            "Reynard welcomed Tibert and promised him fat mice:",
            "'In the priest's barn you'll find the fattest mice.'",
            "Tibert, who loved mice, allowed himself to be tempted.",
            "But in the barn was a snare that had been set for Reynard."
        ]
    )
    
    display_scene(
        "THE SNARE",
        cat,
        [
            "Tibert jumped into the barn and was caught in the snare.",
            "He made so much noise that the priest woke up.",
            "The priest and his family beat Tibert.",
            "Tibert bit the priest and escaped, severely wounded."
        ]
    )
    
    # Scene 6: Grimbart fetches Reynard
    display_scene(
        "GRIMBART FETCHES REYNARD",
        badger,
        [
            "King Noble now sent Grimbart the Badger.",
            "Grimbart warned Reynard that he was in great danger.",
            "'Nephew, you must come to court or you will be outlawed.'",
            "Reynard decided to go along, but had another plan."
        ]
    )
    
    # Scene 7: Reynard at court
    display_scene(
        "REYNARD AT COURT",
        fox,
        [
            "Reynard appeared before King Noble and his court.",
            "He was immediately sentenced to the gallows.",
            "But before his execution, he asked to speak.",
            "'I want to confess my sins before I die,' he said."
        ]
    )
    
    # Scene 8: The Confession
    display_scene(
        "THE CONFESSION",
        fox_sneaky,
        [
            "Reynard began to tell of a conspiracy:",
            "'Your Majesty, I must warn you of a plot against you.'",
            "'Bruin the Bear, Isegrim the Wolf and others want to kill you.'",
            "'They have gathered a great treasure to pay for an army.'"
        ]
    )
    
    display_scene(
        "THE TREASURE",
        fox_laughing,
        [
            "Reynard told of an enormous treasure:",
            "'The treasure is hidden at Kriekeputte, under a tree.'",
            "The king was very interested in the treasure.",
            "He pardoned Reynard in exchange for the location."
        ]
    )
    
    # Scene 9: The Resolution
    display_scene(
        "THE RESOLUTION",
        lion,
        [
            "King Noble believed Reynard's story.",
            "He had Bruin and Isegrim imprisoned.",
            "Reynard was given permission to go on a pilgrimage.",
            "The king even gave him a piece of Bruin's skin as a travel bag."
        ]
    )
    
    display_scene(
        "THE FLIGHT",
        fox_sneaky,
        [
            "Reynard supposedly departed on a pilgrimage.",
            "But in reality, he fled from the court.",
            "The treasure did not exist, it was all a lie.",
            "Reynard had fooled everyone."
        ]
    )
    
    # Scene 10: The Discovery
    display_scene(
        "THE DISCOVERY",
        lion,
        [
            "Cuwaert the Hare and Bellin the Ram escorted Reynard part of the way.",
            "Reynard lured Cuwaert into his castle and killed him.",
            "He sent Bellin back with Cuwaert's head in a bag.",
            "When the king discovered this, he realized he had been deceived."
        ]
    )
    
    # Epilogue
    display_scene(
        "EPILOGUE",
        fox_laughing,
        [
            "Thus Reynard escaped his punishment through his cunning.",
            "He returned to his castle Malpertuus.",
            "There he continued to live with his wife Hermeline and his cubs.",
            "And so Reynard showed that cunning and guile are sometimes stronger than power."
        ]
    )
    
    # End
    clear_screen()
    print("\n" + "=" * 70)
    print("THE END".center(70))
    print("=" * 70 + "\n")
    type_text("The story of Reynard the Fox lives on as a timeless tale")
    type_text("of cunning, deception, and the art of survival.")
    print("\n" + "=" * 70)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nStory interrupted. Goodbye!")