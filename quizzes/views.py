from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Quiz, Question, Choice, Attempt, SubmittedAnswer

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'

@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.prefetch_related('choices').all()

    session_key = f'quiz_{quiz.pk}_start'
    if request.method == 'GET':
        request.session[session_key] = timezone.now().timestamp()
        return render(request, 'quizzes/take_quiz.html', {'quiz': quiz, 'questions': questions})
    start_ts = request.session.get(session_key)
    if start_ts:
        elapsed = timezone.now().timestamp() - start_ts
        if elapsed > quiz.time_limit * 60:
            pass

    total = questions.count()
    score = 0
    attempt = Attempt.objects.create(user=request.user, quiz=quiz, score=0, total=total)
    for q in questions:
        selected_choice_id = request.POST.get(f'question_{q.id}')
        selected = None
        if selected_choice_id:
            try:
                selected = Choice.objects.get(pk=int(selected_choice_id))
            except Choice.DoesNotExist:
                selected = None
        SubmittedAnswer.objects.create(attempt=attempt, question=q, selected_choice=selected)
        if selected and selected.is_correct:
            score += 1
    attempt.score = score
    attempt.save()
    try:
        del request.session[session_key]
    except KeyError:
        pass
    return redirect('quiz_result', pk=quiz.pk, attempt_id=attempt.id)

@login_required
def quiz_result(request, pk, attempt_id):
    attempt = get_object_or_404(Attempt, pk=attempt_id, user=request.user)
    return render(request, 'quizzes/result.html', {'attempt': attempt})

def leaderboard(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    top_attempts = Attempt.objects.filter(quiz=quiz).order_by('-score', 'completed_at')[:10]
    return render(request, 'quizzes/leaderboard.html', {'quiz': quiz, 'top_attempts': top_attempts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
