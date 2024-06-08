from django.shortcuts import render, redirect
from django.http import Http404
from .models import Question
import random

# 전역 기믹 리스트
gimic_list = ['button_fadeout', 'o_run', 'x_come', 'answer_hide', 'timer']

def main_page(request):
    # 세션 초기화
    request.session.flush()
    return render(request, 'main_page.html')

def input_name(request):
    return render(request, 'input_name.html')

def quiz_page(request, id):
    if id > 10:
        return redirect('result_page')  # 퀴즈가 끝나면 결과 페이지로 이동

    if 'selected_quizzes' not in request.session:
        # 첫 번째 퀴즈 요청 시, 랜덤으로 10개의 퀴즈 선택
        all_quizzes = list(Question.objects.all())
        selected_quizzes = random.sample(all_quizzes, 10)
        request.session['selected_quizzes'] = [quiz.id for quiz in selected_quizzes]
        request.session['gimic_indices'] = random.sample(range(5, 10), 3)  # 기믹을 추가할 인덱스 선택

    selected_quizzes = request.session['selected_quizzes']
    gimic_indices = request.session['gimic_indices']

    try:
        current_quiz = Question.objects.get(id=selected_quizzes[id-1])
    except Question.DoesNotExist:
        raise Http404("Quiz does not exist")

    gimic = None
    add_gimic = id > 5 and id-1 in gimic_indices  # 6번째 퀴즈부터 기믹 추가 여부 결정

    if add_gimic:
        gimic = random.choice(gimic_list)

    return render(request, 'quiz_page.html', {
        'quiz': current_quiz,
        'gimic': gimic,
    })

def result_page(request):
    
    return render(request, 'result_page.html')

# Create your views here.

def input_name(request):
    return render(request, 'main_page.html')

def main_page(request):
    return render(request,'main_page.html')
