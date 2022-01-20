from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from polls.models import Question, Choice


# 함수 형 view , 클래스형 view
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return  render(request, 'polls/results.html',{'question':question})

def vote(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError ,Choice.DoesNotExist):
        #질문 투표 형식을 다시 표시함
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':'당신은 선택한 항목이 없습니다.'
        })
    else :
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))