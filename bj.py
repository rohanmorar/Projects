import random
import os
import art

clear = lambda: os.system('clear')
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def hit(hand):
    hand.append(cards[random.randrange(13)])
def deal(hand):
    hand.append(cards[random.randrange(13)])
    hand.append(cards[random.randrange(13)])
    return hand
def score(hand):
    count = 0
    for i in range(len(hand)):
        count += hand[i]
    return count
def bj_check(hand):
    if ((11 in hand) and (10 in hand)):
        return True
    return False
def ov21(hand):
    if score(hand) > 21:
        return True
def elev_to_one(hand):
    for i in range(len(hand)):
        if hand[i] == 11:
            hand[i] = 1
    return hand
def logics_11(hand):
    if(score(hand) > 21 and 11 in hand):
        if(score(elev_to_one(hand)) > 21):
            print("You lose ;(")
def comp_scores(p, c):
    if(score(p) > score(c)):
        print("You win! You beat the dealer.")
    elif(score(p) == score(c)):
        print("You drawed with the dealer.")
    else:
        print("You lose. The dealer beat you. ;(")
def cpu_continue(hand):
    if(score(hand)>= 17):
        return hand
    else:
        while(score(hand) < 17):
            hit(hand)
    return hand

def evs(hand):
    if(hand[0] == 11 and hand[1] == 11):
        hand = [1,1]

def game_lgcs(flag):
    while flag:
        plyr = []
        cpu = []
        player_hand = deal(plyr)
        cpu_hand = deal(cpu)

        evs(player_hand)
        evs(cpu_hand)

        plyr_score = score(player_hand)
        cpu_score = score(cpu_hand)

        print(art.logo)

        #display plyr hand and cpu first card
        print(f"\tYour Cards: {player_hand}, current score: {plyr_score}")
        print(f"\tDealer's first card: {cpu_hand[0]} \n")

        #check for blackjacks
        if(bj_check(player_hand) == True):
            print("You win with a blackjack!")
            break

            
        elif(bj_check(cpu_hand) == True):
            print("You lose. The dealer has a blackjack ;(")
            break
        #bug when type h and goes over 21

        while(score(player_hand) < 21 and bj_check(player_hand) == False and bj_check(cpu_hand) == False):
            p_hit = input("Type 'h' to hit or 's' to stay: ")
            if(p_hit ==  "h"):
                hit(player_hand)
                logics_11(player_hand)
                p_new = player_hand
                print(f"\tYour Cards: {p_new}, current score: {score(p_new)}")  
                print(f"\tDealer's first card: {cpu_hand[0]}")
            else:
                break

        #compare scores
        new_cpu_hand = cpu_continue(cpu_hand)

        f_pscore = score(player_hand)
        f_cscore = score(new_cpu_hand)
        print(f"\tPlayer's final hand: {player_hand}, final score: {f_pscore}")
        print(f"\tDealer's final hand: {new_cpu_hand}, final score: {f_cscore}")
        if(ov21(player_hand)):
            print("You busted! You lose this round.")
            break

        if(ov21(new_cpu_hand)):
            print("You win! The dealer went over.")
            break

        if(f_pscore <= 21 and f_cscore <= 21):
            comp_scores(player_hand, cpu_hand)
            break
start = input("\nWelcome to blackjack!\nType 'y' to play or 'n' to not play: ")
if (start == "y"):
    play = True
    clear()
    cont = True
    while cont:
        game_lgcs(play)
        again = input("Do you want to play again? type 'y' to play or 'n' to not play: ")
        if(again == "y"):
            clear()
        else:
            cont = False
else:
    play = False