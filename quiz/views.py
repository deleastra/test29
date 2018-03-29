from django.shortcuts import render, redirect
from .models import Quiz

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def create(request):
    if request.POST:
        if request.POST['answer'] == 'yes':
            answer = True
        else:
            answer = False
        Quiz.objects.create(question=request.POST['question'], 
                answer=answer)
        return redirect('/')
    return render(request, 'create.html')

def answer(request):
    quiz_list = Quiz.objects.all()
    if request.POST:
        score = 0
        for i in range(1, len(request.POST)):
            if request.POST['answer_' + str(i)] == 'yes':
                answer = True
            else:
                answer = False
            if quiz_list[i-1].answer is answer:
                quiz_list[i-1].correct += 1
                score += 1
            else:
                quiz_list[i-1].incorrect += 1
        return render(request, 'answer.html', {'quiz_list': quiz_list, 'score': score})
    return render(request, 'answer.html', {'quiz_list': quiz_list})
