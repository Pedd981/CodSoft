import math
HUMAN, AI, EMPTY = 'O', 'X', ' '
WC = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
b=[EMPTY] * 9

def pb(b):
    print()
    for i in range(3):
        print('|'.join(b[3*i:3*i+3]))
        if i <2: print('-----')
        print()

def cw(b,p):
    return any(all(b[i]== p for i in cond) for cond in WC)

def cd(b):
    return EMPTY not in b

def mm(b, d, im, al, be):
    if cw(b, AI): return 1
    if cw(b,HUMAN): return -1
    if cd(b): return 0

    if im:
        me = -math.inf
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = AI
                eval = mm(b, d + 1, False, al, be)
                b[i] = EMPTY
                me = max(me, eval)
                al = max(al, eval)
                if be <= al: break

        return me
    else:
        mie = math.inf
        for i in range(9):
            if b[i] == EMPTY:
               b[i] = HUMAN
               eval = mm(b, d + 1, True, al, be)
               b[i] = EMPTY
               mie = min(mie, eval)
               be = min(be, eval)
               if be <= al: break
        return mie
    
def bm(b):
    bv, move = -math.inf, -1
    for i in range(9):
        if b[i] == EMPTY:
           b[i] = AI
           mv = mm(b, 0, False, -math.inf, math.inf)
           b[i] = EMPTY
           if mv > bv:
               bv, move=mv, i
    return move

def pg():
    print("welcome to tic_tac_toe")
    pb(b)
    while True:
        hm = int(input("enter your move(1-9):")) - 1
        if b[hm] != EMPTY:
            print("INVALID MOVE! TRY AGAIN.")
            continue
        b[hm] = HUMAN
        pb(b)
        if cw(b, HUMAN):
            print("YOU WIN")
            break
        if cd(b):
            print("It's a draw!")
            break
        aim = bm(b)
        b[aim] = AI
        pb(b)
        if cw(b, AI):
            print("AI WINS")
            break
        if cd(b):
            print("IT'S A DRAW!")
            break

if __name__ == "__main__":
    pg()