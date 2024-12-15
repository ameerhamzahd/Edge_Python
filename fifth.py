# List of questions, options, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A) Galileo", "B) Einstein", "C) Newton", "D) Tesla"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["A) India", "B) China", "C) Japan", "D) Thailand"],
        "answer": "B"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A) Nucleus", "B) Mitochondria", "C) Ribosome", "D) Chloroplast"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Leo Tolstoy"],
        "answer": "C"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["A) 50°C", "B) 75°C", "C) 100°C", "D) 125°C"],
        "answer": "C"
    },
    {
        "question": "Which organ pumps blood through the body?",
        "options": ["A) Brain", "B) Heart", "C) Kidney", "D) Liver"],
        "answer": "B"
    }
]

# Initialize score
score = 0

# Function to run the quiz
def run_quiz():
    global score  # Access the global score variable
    
    # Run through each question
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get user's answer
        answer = input("Your answer (A, B, C, or D): ").upper()
        
        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.\n")
    
    # Print final score
    print(f"Your final score is {score} out of {len(questions)}.")

# Run the quiz
run_quiz()
