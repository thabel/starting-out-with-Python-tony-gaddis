import random

frequency_dict = {

}


def main():
    rand_numbers = [random.randint(1, 10) for i in range(100)]
    for num in rand_numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    # display frequency
    for key, value in frequency_dict.items():
        print(f"number {key} frequency is {value}")


if __name__ == '__main__':
    main()
