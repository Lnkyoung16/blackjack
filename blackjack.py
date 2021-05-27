# ♠︎♣︎♥︎♦︎

temporary = []

def check_overlap(list1, list2, card):
    total_list = list1 + list2
    for i in range(0, len(total_list)):
        if card == total_list[i]:
            return 0

def change_to_integer(card_number, sequence):
    if card_number == "A":
        if sequence == 0:
            choice = int(input("A는 1 또는 11로 적용이 가능합니다. 어떤 수로 하시겠습니까?"))
            return choice
        else:
            choice = random.randint(0,1)
            if choice == 0:
                return 1
            if choice == 1:
                return 11
    elif card_number == "J":
        return 10
    elif card_number == "Q":
        return 10
    elif card_number == "K":
        return 10
    else:
        card_number = int(card_number)
        return card_number

def new_card_generator():
    temporary = []
    while len(temporary) != 1:
        card_number = random.randint(1, 12)
        card_shape = random.randint(0, 3)
        if card_shape == 0:
            card_shape = "♠"
        elif card_shape == 1:
            card_shape = "♣"
        elif card_shape == 2:
            card_shape = "♥"
        else:
            card_shape = "♦"
        if  card_number == 1:
            card_number = "A"
        elif card_number == 10:
            card_number = "J"
        elif card_number == 11:
            card_number = "Q"
        elif card_number == 12:
            card_number = "K"
        card = card_shape + str(card_number)
        overlap = check_overlap(player_all_card, computer_all_card, card)
        if overlap != 0:
            return card

import random
player_hidden_card =[]
player_shown_card = []
computer_hidden_card = []
computer_shown_card = []
player_all_card = []
computer_all_card = []
player_sum = 0
computer_sum = 0

while len(player_all_card) < 2:
    sequence = 0
    new_card = new_card_generator()
    player_all_card.append(new_card)
    new_card_number = new_card[1:]
    new_card_number = change_to_integer(new_card_number, sequence)
    player_sum = player_sum + new_card_number


while len(computer_all_card) < 2:
    sequence = 1
    new_card = new_card_generator()
    computer_all_card.append(new_card)
    new_card_number = new_card[1:]
    new_card_number = change_to_integer(new_card_number, sequence)
    computer_sum = computer_sum + new_card_number

print(player_all_card)
player_hide = int(input("어느 숫자를 숨기시겠습니까?(1,2로 대답해주세요.)"))
if player_hide == 1:
    player_hidden_card.append(player_all_card[0])
    player_shown_card.append(player_all_card[1])
else:
    player_hidden_card.append(player_all_card[1])
    player_shown_card.append(player_all_card[0])

computer_hide = random.randint(0,1)
if computer_hide == 1:
    computer_hidden_card.append(computer_all_card[0])
    computer_shown_card.append(computer_all_card[1])
else:
    computer_hidden_card.append(computer_all_card[1])
    computer_shown_card.append(computer_all_card[0])

print("플레이어의 카드:", player_shown_card)
print("컴퓨터의 카드:", computer_shown_card)


while player_sum < 21 and computer_sum < 21:
    choice = input("카드를 추가로 받으시겠습니까?(예/아니오로 대답해주세요)")
    if choice == "예":
        sequence = 1
        computer_new_card = new_card_generator()
        new_card_number = computer_new_card[1:]
        new_card_number = change_to_integer(new_card_number, sequence)
        computer_shown_card.append(computer_new_card)
        computer_all_card.append(computer_new_card)
        computer_sum = computer_sum + new_card_number
        print("컴퓨터는", computer_new_card, "를 받았습니다.")
        print("---------------")
        sequence = 0
        player_new_card = new_card_generator()
        player_shown_card.append(player_new_card)
        player_all_card.append(player_new_card)
        new_card_number = player_new_card[1:]
        new_card_number = change_to_integer(new_card_number, sequence)
        player_sum = player_sum + new_card_number
        print(player_new_card, "를 받으셨습니다.")
        print("---------------")
        print("플레이어의 카드:", player_shown_card)
        print("컴퓨터의 카드:", computer_shown_card)
    elif choice == "아니오":
        break
    else:
        print("잘못 입력하셨습니다. 다시 정확하게 입력해주세요.")
        continue

if player_sum < 21 and computer_sum < 21:
    if player_sum > computer_sum:
        print("플레이어의 승리입니다.")
        print("컴퓨터는", computer_all_card, "의 카드를 가지고 있었습니다.")
        print("플레이어는", player_all_card, "의 카드를 가지고 있었습니다.")
    else:
        print("컴퓨터의 승리입니다.")
        print("컴퓨터는", computer_all_card, "의 카드를 가지고 있었습니다.")
        print("플레이어는", player_all_card, "의 카드를 가지고 있었습니다.")
else:
    if player_sum >= 21:
        print("컴퓨터의 승리입니다.")
        print("컴퓨터는", computer_all_card, "의 카드를 가지고 있었습니다.")
        print("플레이어는", player_all_card, "의 카드를 가지고 있었습니다.")
    else:
       print("플레이어의 승리입니다.")
       print("컴퓨터는", computer_all_card, "의 카드를 가지고 있었습니다.")
       print("플레이는", player_all_card, "의 카드를 가지고 있었습니다.")
