from string import ascii_lowercase
import math

def solve(testcases):
    # print('solve')

    for testcase in range(testcases):
        answer = 0

        padlock = input()
        print('padlock: ', padlock)

        valid_letters = input()
        print('valid letters: ', valid_letters)

        letter_locations = {letter:index+1 for index,letter in enumerate(ascii_lowercase)}
        print('Letter locations: ', letter_locations)

        letters_seen = {}

        halfway_distance = len(ascii_lowercase)/2
        alphabet_length = len(ascii_lowercase)
        print('halfway distance: ', halfway_distance)

        for padlock_letter in padlock:
            print('checking out the letter : {}'.format(padlock_letter))

            if padlock_letter not in letters_seen:
                padlock_letters_location = letter_locations[padlock_letter]
                shortest_distance = 26
                for valid_letter in valid_letters:
                    valid_letters_location = letter_locations[valid_letter]

                    distance = abs(padlock_letters_location - valid_letters_location)

                    if distance > halfway_distance:
                        # quicker to go back side
                        shortest_distance = min(shortest_distance, alphabet_length - distance)
                    else:
                        shortest_distance = min(shortest_distance, distance)

                answer += shortest_distance
                letters_seen[padlock_letter] = shortest_distance
            else:
                answer += letters_seen[padlock_letter]





        print('Case #{}: {}'.format(testcase+1, answer))


t = int(input())
solve(t)