import random
class blackjack:

    def __init__(self):
        self.player_shown_card = []
        self.computer_shown_card = []
        self.player_all_card = []
        self.computer_all_card = []
        self.player_sum = 0
        self.computer_sum = 0

    def check_overlap(self, card):
        total_list = self.computer_all_card + self.player_all_card
        for i in range(0, len(total_list)):
            if card == total_list[i]:
                return 0

    def change_to_integer(self, card_number, sequence):
        if card_number == "A":
            if sequence == 0:
                while True:
                    choice = int(input("A는 1 또는 11로 적용이 가능합니다. 어떤 수로 하시겠습니까?"))
                    if choice == 1:
                        return choice
                    elif choice == 11:
                        return choice
                    else:
                        print("1 또는 11을 입력해주세요.")
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

    def new_card_generator(self):
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
            overlap = self.check_overlap(card)
            if overlap != 0:
                return card


    def initial_card_genrator(self, all_card_list, number_sum, sequence):
        new_card = self.new_card_generator()
        new_card_number = new_card[1:]
        new_card_number = self.change_to_integer(new_card_number, sequence)
        all_card_list.append(new_card)
        number_sum = number_sum + new_card_number
        return all_card_list, number_sum, new_card

    def card_hide(self, hide_choice, all_card_list, shown_card_list):
        if hide_choice == 1:
            shown_card_list.append(all_card_list[1])
        else:
            shown_card_list.append(all_card_list[0])
        return all_card_list, shown_card_list


    def winner_validator(self):
        if self.player_sum < 21 and self.computer_sum < 21:
            if self.player_sum > self.computer_sum:
                print("플레이어의 승리입니다.")
                print("컴퓨터는", self.computer_all_card, "의 카드를 가지고 있었습니다.")
                print("플레이어는", self.player_all_card, "의 카드를 가지고 있었습니다.")
            else:
                print("컴퓨터의 승리입니다.")
                print("컴퓨터는", self.computer_all_card, "의 카드를 가지고 있었습니다.")
                print("플레이어는", self.player_all_card, "의 카드를 가지고 있었습니다.")
        else:
            if self.player_sum >= 21:
                print("컴퓨터의 승리입니다.")
                print("컴퓨터는", self.computer_all_card, "의 카드를 가지고 있었습니다.")
                print("플레이어는", self.player_all_card, "의 카드를 가지고 있었습니다.")
            else:
               print("플레이어의 승리입니다.")
               print("컴퓨터는", self.computer_all_card, "의 카드를 가지고 있었습니다.")
               print("플레이어는", self.player_all_card, "의 카드를 가지고 있었습니다.")

    def game_start(self):
        while len(self.player_all_card) < 2:
            _, self.player_sum, _ = self.initial_card_genrator(self.player_all_card, self.player_sum, 0)
        while len(self.computer_all_card) < 2:
            _, self.computer_sum, _ = self.initial_card_genrator(self.computer_all_card, self.computer_sum, 1)

        print(self.player_all_card)
        player_hide = int(input("어느 숫자를 숨기시겠습니까?(1,2로 대답해주세요.)"))
        self.card_hide(player_hide, self.player_all_card, self.player_shown_card)

        computer_hide = random.randint(0,1)
        self.card_hide(computer_hide, self.computer_all_card, self.computer_shown_card)

        print("플레이어의 카드:", self.player_shown_card)
        print("컴퓨터의 카드:", self.computer_shown_card)

        while self.player_sum < 21 and self.computer_sum < 21:
            choice = input("카드를 추가로 받으시겠습니까?(예/아니오로 대답해주세요)")
            if choice == "예":
                _, self.computer_sum, new_card = self.initial_card_genrator(self.computer_all_card, self.computer_sum, 1)
                self.computer_shown_card.append(new_card)
                print("컴퓨터는", new_card, "를 받았습니다.")
                print("---------------")
                _, self.player_sum, new_card = self.initial_card_genrator(self.player_all_card, self.player_sum, 0)
                self.player_shown_card.append(new_card)
                print(new_card, "를 받으셨습니다.")
                print("---------------")
                print("플레이어의 카드:", self.player_shown_card)
                print("컴퓨터의 카드:", self.computer_shown_card)
            elif choice == "아니오":
                break
            else:
                print("잘못 입력하셨습니다. 다시 정확하게 입력해주세요.")
                continue

        self.winner_validator()

blackjack().game_start()