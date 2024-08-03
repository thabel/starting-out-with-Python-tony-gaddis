import listen_5 as coin


# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = coin.Coin()
    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    # Toss the coin.
    # But now I'm going to cheat! I'm going to
    # directly change the value of the object's
    # sideup attribute to 'Heads'.
    print('I am tossing the coin 10 times ...')
    for _ in range(10):     
        my_coin.toss()
        print(my_coin.get_sideup())

    # Call the main function.
main()

