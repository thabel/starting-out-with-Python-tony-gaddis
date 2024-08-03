from Question import Question

MAX_QUESTIONS = 10

GAMES_QUESTIONS_ON_PYTHON = {
    1: Question(
        trivia_question="What's Python language in CS?",
        answers=(
            "language spoken by python",
            "compiled language",
            "interpreted language",
            "is snake language",
        ),
        correct_answer_index=2,
    ),
    2: Question(
        trivia_question="Which company created the Java programming language?",
        answers=("Microsoft", "Sun Microsystems", "Google", "Apple"),
        correct_answer_index=1,
    ),
    3: Question(
        trivia_question="HTML stands for?",
        answers=(
            "Hyper Text Markup Language",
            "Home Tool Markup Language",
            "Hyperlinks and Text Markup Language",
            "Hyperlinking Text Marking Language",
        ),
        correct_answer_index=0,
    ),
    4: Question(
        trivia_question="What does CSS stand for?",
        answers=(
            "Colorful Style Sheets",
            "Cascading Style Sheets",
            "Computer Style Sheets",
            "Creative Style Sheets",
        ),
        correct_answer_index=1,
    ),
    5: Question(
        trivia_question="In which year was the Python language created?",
        answers=("1991", "1989", "2000", "1995"),
        correct_answer_index=0,
    ),
    6: Question(
        trivia_question="Which of these is not a programming language?",
        answers=("Python", "JavaScript", "MCU", "Ruby"),
        correct_answer_index=2,
    ),
    7: Question(
        trivia_question="Which language is primarily used for web development?",
        answers=("C++", "Python", "JavaScript", "Java"),
        correct_answer_index=2,
    ),
    8: Question(
        trivia_question="SQL is used for?",
        answers=(
            "Styling web pages",
            "Structuring web pages",
            "Querying databases",
            "Programming robots",
        ),
        correct_answer_index=2,
    ),
    9: Question(
        trivia_question="Which symbol is used for comments in Python?",
        answers=("#", "//", "/* */", "<!-- -->"),
        correct_answer_index=0,
    ),
    10: Question(
        trivia_question="Which of these is a popular Python web framework?",
        answers=("React", "Angular", "Django", "Vue"),
        correct_answer_index=2,
    ),
}


def get_user_choice(msg):
    while True:
        try:
            u_choice = int(input(msg))
            return u_choice
        except ValueError:
            print("Bad input , Try again.")
            continue


def main():
    game_question = 1
    player_1 = True
    scores = {
        "player1": 0,
        "player2": 0,
    }
    while True:
        if game_question > MAX_QUESTIONS:
            break
        q = GAMES_QUESTIONS_ON_PYTHON[game_question]
        print(" " + q.get_trivia_question())
        q.display_answers()
        if player_1 == True:
            answer = get_user_choice("palyer 1#: ")
            if q.is_answered_correctly(answer):
                scores["player1"] += 1
                print("Correct")
            else:
                print("Wrong the correct anwser was", q.get_correct_answer())
        else:
            answer = get_user_choice("palyer 2#: ")
            if q.is_answered_correctly(answer):
                scores["player2"] += 1
                print("Correct")
            else:
                print("Wrong the correct anwser was", q.get_correct_answer())

        player_1 = not player_1
        game_question += 1

    if scores["player1"] > scores["player2"]:
        print("palyer 1 win the game with", scores["player1"])
    elif scores["player1"] == scores["player2"]:
        print("there is a tie with", scores["player1"])
    else:
        print("palyer 2 win the game with", scores["player2"])


main()
