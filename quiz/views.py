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
            quiz = Quiz.objects.get(pk=i)
            if request.POST['answer_' + str(i)] == 'yes':
                answer = True
            else:
                answer = False
            if quiz.answer is answer:
                quiz.correct += 1
                score += 1
            else:
                quiz.incorrect += 1
            quiz.save()
        return render(request, 'answer.html', {'quiz_list': quiz_list, 'score': score})
    return render(request, 'answer.html', {'quiz_list': quiz_list})

def statistic(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'statistic.html', {'quiz_list': quiz_list})
