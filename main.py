from art import logo
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards(hand, amount):
    for i in range(amount):
        hand.append(random.choice(cards))

    return hand

def check_ace(hand, score):
    aces = hand.count(11)  # number of aces being treated as 11 for now

    # If total > 21, convert aces (11 -> 1) until safe or no aces left
    while score > 21 and aces > 0:
        score -= 10   # turning an 11 into a 1 reduces total by 10
        aces -= 1

    return score


def show_hands(hand1,hand2,hand1_score):
    print(f"Your cards: {hand1}, current score: {hand1_score}")
    print(f"Computers first card: {hand2[0]}")

def show_final_scores(hand1,hand2,hand1_score,hand2_score):
    print(f"Your final hand is: {hand1}, final score: {hand1_score}")
    print(f"Dealers final hand is: {hand2}, final score: {hand2_score}")

    if hand1_score == 21:
        print("You win with blackjack!")
        return
    elif (hand2_score > hand1_score and not hand2_score > 21) or hand1_score > 21:
        print("Dealer wins, You lose :(")
        return
    elif (hand1_score > hand2_score and not hand1_score > 21) or hand2_score > 21:
        print("You win :)")
        return
    else:
        print("Draw!")
        return




def blackjack():
    print(logo)
    players_cards = []
    computers_cards = []

    players_cards = deal_cards(players_cards,2)
    computers_cards = deal_cards(computers_cards,2)

    player_score = sum(players_cards)
    computer_score = sum(computers_cards)

    player_score = check_ace(players_cards,player_score)
    computer_score = check_ace(computers_cards,computer_score)

    show_hands(players_cards, computers_cards,player_score)

    if player_score == 21:
        show_final_scores(players_cards,computers_cards,player_score,computer_score)

    else:
        hit = True
        while hit:
            if player_score == 21:
                show_final_scores(players_cards,computers_cards,player_score,computer_score)
                return

            hit_or_stand = input("Would you like to hit or stand, h or s?: ")
            if hit_or_stand == "s":
                hit = False

                if computer_score > player_score:
                    computer_score = check_ace(computers_cards, computer_score)
                    while computer_score < 17:
                        deal_cards(computers_cards,1)
                        computer_score = sum(computers_cards)
                        computer_score = check_ace(computers_cards,computer_score)

                    show_final_scores(players_cards,computers_cards,player_score,computer_score)
                    return
                elif computer_score <= player_score:
                    computer_score = check_ace(computers_cards, computer_score)
                    while computer_score < 17:
                        deal_cards(computers_cards,1)
                        computer_score = sum(computers_cards)
                        computer_score = check_ace(computers_cards,computer_score)

                    show_final_scores(players_cards, computers_cards, player_score, computer_score)
                else:
                    show_final_scores(players_cards, computers_cards, player_score, computer_score)

            elif hit_or_stand == "h":
                deal_cards(players_cards, 1)
                player_score = sum(players_cards)
                player_score = check_ace(players_cards,player_score)
                if player_score > 21:
                    player_score = check_ace(players_cards,player_score)
                    if player_score > 21:
                        show_final_scores(players_cards,computers_cards,player_score,computer_score)
                        return
                else:
                    show_hands(players_cards, computers_cards,player_score)


play_game = True
while play_game:
    want_to_play = input("Do you want to play a game of blackjack?: ")
    if want_to_play == "n":
        break
    elif want_to_play == "y":
        print("\n" * 20)
        blackjack()