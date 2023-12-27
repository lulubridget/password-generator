# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def caesar(text, shift, direction):
#     if direction == "encode":
#         final_cipher_text = ""
#         for letter in text:
#             letter_position = int(alphabet.index(letter))
#             cipher_letter = letter_position + int(shift)
#             cipher_text = alphabet[cipher_letter]
#             final_cipher_text += cipher_text
#         print(f"the {direction}d text is {final_cipher_text}")
#     elif direction == "decode":
#         final_cipher_text = ""
#         for letter in text:
#             letter_position = alphabet.index(letter)
#             cipher_letter = letter_position - shift
#             cipher_text = alphabet[cipher_letter]
#             final_cipher_text += cipher_text
#         print(f"the {direction}d text is {final_cipher_text}")
# caesar(text, shift, direction)

# easy level, guess 10 times; hard level, 5 times
import random
easy_level = 10
hard_level = 5
def set_difficulty():
    difficulty_level = input("choose a difficulty, type 'easy; or 'hard': ").lower()
    if difficulty_level == "easy":
        return difficulty_level

    elif difficulty_level == "hard":
        return difficulty_level


def check_answer(player_guess, random_number, turns):

    if player_guess == random_number:
        print("win")
    elif player_guess > random_number:
        print("too high")
        return turns -1
    elif player_guess < random_number:
        print("too low")
        return turns - 1
def game():
    random_number = random.randint(1,100)
    print(f"the correct answer is {random_number}")
    turns = set_difficulty()
    print(f"you have {turns} attempts left")
    player_guess = int(input("make a guess: "))
    while
    turns = check_answer()

game()


