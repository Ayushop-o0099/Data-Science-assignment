questions = {
    "What is the capital of India? ": "Delhi",
    "Who developed Python? ": "Guido van Rossum",
    "What is 2+2? ": "4"
}
score = 0
for q, a in questions.items():
    ans = input(q)
    if ans.strip().lower() == a.lower():
        score += 1
print(f"Score: {score}/{len(questions)}")