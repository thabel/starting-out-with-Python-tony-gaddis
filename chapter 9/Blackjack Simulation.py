import random


def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {
        'Ace of Spades': 11,  # or 1 depending on the situation
        '2 of Spades': 2, '3 of Spades': 3,
        '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
        '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
        '10 of Spades': 10, 'Jack of Spades': 10,
        'Queen of Spades': 10, 'King of Spades': 10,
    }
    all_items = [(k, v) for k, v in deck.items()]
    random.shuffle(all_items)
    # Return the deck.
    deck = dict(all_items)
    return deck


def players_hands():
    return {
        "total hands": 0,
    }


def calculate_player_hands(player):
    player["total hands"] = sum([player[key] for key in player if
                                 key != 'total hands'])


def debug(player_1, player_2):
    print("player 1 = ", player_1)
    print("player 2 = ", player_2)


def change_ace_value(player):
    calculate_player_hands(player)
    if player["total hands"] > 21:
        current_ace_value = player.get('Ace of Spades')
        if current_ace_value is None or current_ace_value == 1:
            return
        player["Ace of Spades"] = 1
        calculate_player_hands(player)


def main():
    while True:
        cards = create_deck()
        player_1 = players_hands()
        player_2 = players_hands()

        # dealing the cards
        while player_1["total hands"] < 21 and player_2["total hands"] < 21:
            print("pop item", cards.popitem())
            player_1.update((cards.popitem(),))
            player_2.update((cards.popitem(),))

            change_ace_value(player_1)
            change_ace_value(player_2)
        if player_1["total hands"] == player_2["total hands"] == 21:
            print("This is a tie need to replay")
            debug(player_1, player_2)
            continue
        if player_1["total hands"] > 21 and player_2["total hands"] <= 21 \
                or player_2["total hands"] == 21:
            print("player 2 win")
            debug(player_1, player_2)
            break
        if player_2["total hands"] > 21 and player_1["total hands"] <= 21 \
                or player_1["total hands"] == 21:
            print("player 1 win")
            debug(player_1, player_2)
            break


        else:
            print("I didn't expect that but you both lost")
            debug(player_1, player_2)
            break


if __name__ == '__main__':
    main()
