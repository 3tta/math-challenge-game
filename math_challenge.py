import random
import time

def generate_question():
    ops = ['+', '-', '*', '/']
    op = random.choice(ops)
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    if op == '/':
        a = a * b
    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, round(answer, 2)

def play_game(rounds=5, time_limit=5):
    score = 0
    print("🎯 Welcome to the Math Challenge Game!")
    print(f"You have {time_limit} seconds to answer each question. Ready?\n")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question {i+1}: {question} = ?")
        start_time = time.time()
        try:
            user_answer = float(input("Your answer: "))
            end_time = time.time()
            if end_time - start_time > time_limit:
                print("⏱ Time's up!")
            elif abs(user_answer - correct_answer) < 0.01:
                print("✅ Correct answer!\n")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer is: {correct_answer}\n")
        except:
            print("⚠️ Invalid input!\n")

    print(f"🎉 Game over! Your score: {score} out of {rounds}")

if __name__ == "__main__":
    play_game()
