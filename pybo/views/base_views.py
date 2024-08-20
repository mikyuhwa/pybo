from ..models import Question
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def index(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject_icontains=kw)|
            Q(content_icontains=kw)|
            Q(author_username_icontains=kw) |
            Q(answer_author_username_icontains=kw)
        ).distinct()
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj, 'page':page, 'kw':kw}
    return render(request, 'pybo/question_list.html',context)
    #return HttpResponse("안녕하세요  pybo 에 오신것을 환영합니다.")

def detail(request, question_id):
     #question = Question.objects.get(id=question_id)
     question = get_object_or_404(Question,pk=question_id)
     context = {'question' : question}
     return render(request, 'pybo/question_detail.html', context)

