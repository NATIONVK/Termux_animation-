#!/usr/bin/env python3
"""NATIONVK Cyber Terminal — offline ANSI animation for Termux."""
import os, sys, time, random, shutil, math, signal

RESET="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"; CLEAR="\033[2J\033[H"; HIDE="\033[?25l"; SHOW="\033[?25h"
PALETTE=[46,51,39,201,226,213]
running=True

def size():
    s=shutil.get_terminal_size((80,24)); return max(30,s.columns),max(12,s.lines)

def color(text, code=46, bright=True):
    return f"\033[{1 if bright else 0};38;5;{code}m{text}{RESET}"

def center(text,w): return text.center(w)

def header(w):
    print(color("╔"+"═"*(w-2)+"╗",51))
    print(color("║"+center("N A T I O N V K   //   C Y B E R   L A B",w-2)+"║",51,True))
    print(color("║"+center("OFFLINE TERMINAL VISUAL ENGINE",w-2)+"║",39))
    print(color("╚"+"═"*(w-2)+"╝",51))

def matrix_frame(w,h,cols):
    chars="01アイウエオカキクケコサシスセソ<>[]{}#$%&"
    for y in range(h-3):
        row=[]
        for x in range(cols):
            ch=random.choice(chars) if random.random()<.12 else " "
            row.append(color(ch,random.choice([46,40,42,51]),random.random()>.7) if ch!=" " else " ")
        print("".join(row)[:w])
    print(color("  MATRIX STREAM // ENCRYPTED SIGNALS FLOWING",46))

def scanner_frame(w,h,t):
    width=min(w-8,70); pos=int((math.sin(t*2)+1)*.5*(width-1))
    print(color("  [ NETWORK PERIMETER SCAN ]",51))
    print("  "+"─"*width)
    for i in range(max(5,h-8)):
        x=(pos+i*7)%width
        line=[" "]*width
        line[x]="◆" if i%3==0 else "│"
        if random.random()<.16: line[random.randrange(width)]="·"
        print("  "+color("".join(line),random.choice([51,46,39])))
    print("  "+color("  SIGNAL: "+str(random.randint(82,99))+"%   TRACE: "+random.choice(["MASKED","ROUTED","OBSCURED"]),46))

def glitch_frame(w,h):
    print(color("  !! VISUAL BUFFER INSTABILITY !!",201,True))
    for _ in range(max(5,h-8)):
        text="".join(random.choice(" ░▒▓█<>/\\01") for _ in range(w-4))
        print(color(text,random.choice(PALETTE)))
    print(color("  SYSTEM RECOVERED // NO DATA TRANSMITTED",39))

def pulse_frame(w,h,t):
    print(color("  CYBER CORE // PARTICLE PULSE",51))
    cx,cy=(w-4)//2,(h-8)//2
    for y in range(max(4,h-8)):
        line=[]
        for x in range(w-4):
            d=math.hypot(x-cx,(y-cy)*2)
            v=math.sin(d*.48-t*3)+math.sin(x*.18+t)+math.cos(y*.6-t*2)
            line.append(color("●",random.choice(PALETTE)) if v>1.3 else (color("·",51,False) if v>.8 else " "))
        print("  "+"".join(line))
    print(color("  CORE STABILITY: NOMINAL",46))

def animate(kind):
    global running
    w,h=size(); os.system("clear")
    print(HIDE,end="",flush=True)
    try:
        start=time.time()
        while running:
            w,h=size(); print(CLEAR,end="")
            header(w)
            t=time.time()-start
            if kind=="matrix": matrix_frame(w,h,w)
            elif kind=="scanner": scanner_frame(w,h,t)
            elif kind=="glitch": glitch_frame(w,h)
            else: pulse_frame(w,h,t)
            print(color("\n  CTRL+C TO RETURN TO MENU",51,False),flush=True)
            time.sleep(.075 if kind=="matrix" else .12)
    except KeyboardInterrupt:
        pass
    finally:
        print(SHOW+RESET+CLEAR,end="",flush=True)

def menu():
    while True:
        w,h=size(); print(CLEAR,end="")
        header(w)
        print("\n"+color("  SELECT ANIMATION",46,True))
        options=[("1","Matrix Rain","matrix"),("2","Cyber Perimeter Scanner","scanner"),("3","Digital Glitch","glitch"),("4","Cyber Core Pulse","pulse")]
        for n,label,_ in options: print("  "+color("["+n+"]",51)+"  "+label)
        print("\n  "+color("[5]",51)+"  Random demo")
        print("  "+color("[0]",201)+"  Exit")
        try: choice=input("\n  NATIONVK@TERMUX > ").strip()
        except (EOFError,KeyboardInterrupt): break
        if choice=="0": break
        selected=next((k for n,_,k in options if n==choice),None)
        if choice=="5": selected=random.choice(["matrix","scanner","glitch","pulse"])
        if selected: animate(selected)
        else: print(color("  Unknown option.",201)); time.sleep(.7)
    print(RESET+SHOW+"  NATIONVK CYBER LAB — SESSION CLOSED")

if __name__=="__main__":
    try: menu()
    except KeyboardInterrupt: print(RESET+SHOW)
