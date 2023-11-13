from click import clear

print("There are a total of 6 questions, you can skip aquestion anytime by typing 'skip")
input("Press any key to get Start...")


def check_scores(p_question_num, answer, attempts, player):
    clear()
    correct_answer = quiz[p_question_num]["answer"]
    if correct_answer.lower() == answer.lower():
        print(f"Correct Answer: \n{player}'s score is {player_score[player] + 1}")
        return True
    else:
        print(f"Wrong Answer:(You have {attempts - 1} attempts)")
        return False


# for switch users
def switch_users(p_user_index):
    if p_user_index == 0:
        return 1
    return 0


def find_winner(player1, player2):
    if player_score[player1] > player_score[player2]:
        print(f"{player1} is won")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} is won")
    else:
        print("It's Draw")


player_list = input("Enter Name of 2 Playesrs:-").split(" ")
player_score = dict.fromkeys(player_list, 0)

quiz = {
    1: {"questions": "A mapping from a set a keys to their corresponding values",
        "answer": "Dictionary"},
    2: {"questions": "Another name for a key-value pair",
        "answer": "Item"},
    3: {"questions": "An object that appears in a dictionary at the first part of a key-value pair",
        "answer": "Key"},
    4: {"questions": "An object that appears in a dictionary as the second part of a key-value pair.",
        "answer": "Value"},
    5: {"questions": "A loop “inside” of another loop.",
        "answer": "Nested loop"},
    6: {"questions": "A dictionary that is an element of another dictionary.",
        "answer": "Nested dictionary"}
}
current_player = player_list[0]  # first player
for question in quiz:
    print("______________________________")
    print(f"It is {current_player}'s turn.")
    attempts = 2
    while attempts > 0:
        print(quiz[question]['questions'])
        answer = input("Answer: ")
        if answer == "skip":
            break
        check = check_scores(question, answer, attempts, current_player)
        if check:
            player_score[current_player] += 1
            break
        attempts -= 1
    current_player_index = player_list.index(current_player)
    next_player_index = switch_users(current_player_index)
    current_player = player_list[next_player_index]
find_winner(player_list[0], player_list[1])
