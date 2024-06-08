from django.shortcuts import render


from django.shortcuts import render

def main_page(request):
    # 첫 화면, 메인 페이지
    return render(request, 'main_page.html')

def input_name(request):
    # 이름 입력 페이지
    return render(request, 'input_name.html')

def quiz_page(request):
    # 퀴즈를 풀 수 있는 페이지
    return render(request, 'quiz_page.html')

def result_page(request):
    # 퀴즈 결과를 확인할 수 있는 페이지
    return render(request, 'result_page.html')

# Create your views here.
