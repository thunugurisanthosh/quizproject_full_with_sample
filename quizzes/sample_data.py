from quizzes.models import Quiz, Question, Choice

def create_sample_quiz():
    # Avoid duplicates
    if Quiz.objects.filter(title="Python Basics Quiz").exists():
        print("Sample quiz already exists.")
        return

    quiz = Quiz.objects.create(
        title="Python Basics Quiz",
        description="A simple quiz to test your Python fundamentals",
        time_limit=5,
    )

    q1 = Question.objects.create(quiz=quiz, text="What is the output of print(2 ** 3)?")
    Choice.objects.create(question=q1, text="6", is_correct=False)
    Choice.objects.create(question=q1, text="8", is_correct=True)
    Choice.objects.create(question=q1, text="9", is_correct=False)

    q2 = Question.objects.create(quiz=quiz, text="Which keyword is used to create a function in Python?")
    Choice.objects.create(question=q2, text="func", is_correct=False)
    Choice.objects.create(question=q2, text="def", is_correct=True)
    Choice.objects.create(question=q2, text="function", is_correct=False)

    q3 = Question.objects.create(quiz=quiz, text="What data type is the result of: 3 / 2?")
    Choice.objects.create(question=q3, text="int", is_correct=False)
    Choice.objects.create(question=q3, text="float", is_correct=True)
    Choice.objects.create(question=q3, text="str", is_correct=False)

    print("✅ Sample quiz created successfully!")
