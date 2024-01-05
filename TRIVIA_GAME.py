
class Question:
    def __init__(self, question, option1, option2, option3, option4, correct_answer):
        # Initialize attributes for a trivia question
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

def play_trivia(questions):
    score_player1 = 0
    score_player2 = 0

    for i in range(10):
        print(f"\nQuestion {i + 1}: {questions[i].question}")
        print(f"1. {questions[i].option1}")
        print(f"2. {questions[i].option2}")
        print(f"3. {questions[i].option3}")
        print(f"4. {questions[i].option4}")

        # Get valid input for Player 1
        while True:
            try:
                answer_player1 = int(input("Player 1, enter your answer (1-4): "))
                if 1 <= answer_player1 <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        # Get valid input for Player 2
        while True:
            try:
                answer_player2 = int(input("Player 2, enter your answer (1-4): "))
                if 1 <= answer_player2 <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if answer_player1 == questions[i].correct_answer:
            score_player1 += 1
        if answer_player2 == questions[i].correct_answer:
            score_player2 += 1

    print("\nGame Over! Results:")
    print(f"Player 1 Score: {score_player1}")
    print(f"Player 2 Score: {score_player2}")

    if score_player1 > score_player2:
        print("Player 1 wins!")
    elif score_player2 > score_player1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    # Question objects with your own trivia questions and answers
    q1 = Question("In which year did the Titanic sink?", "1905", "1912", "1920", "1931", 2)
    q2 = Question("What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3)
    q3 = Question("Which planet is known as the 'Red Planet'?", "Venus", "Mars", "Jupiter", "Saturn", 2)
    q4 = Question("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", 1)
    q5 = Question("What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Polar Bear", 2)
    q6 = Question("In which year did the United States declare its independence?", "1765", "1800", "1789", "1776", 4)
    q7 = Question("What is the chemical symbol for gold?", "Gd", "Au", "Ag", "Hg", 2)
    q8 = Question("Which country is famous for its tulips and windmills?", "Netherlands", "Italy", "France", "Germany", 1)
    q9 = Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 3)
    q10 = Question("What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean", 4)

    # Create a list containing Question objects
    trivia_questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    # Call the play_trivia function with the list of questions
    play_trivia(trivia_questions)
