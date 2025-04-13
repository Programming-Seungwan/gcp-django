from typing import Any
from django.shortcuts import render
from testapp.models import Boards
from django.views.generic import ListView, TemplateView

# Create your views here.

# CBV에서 get, post 등의 메서드에는 첫 번째 인자로 self가, 두 번째 인자로는 request가 온다.
class BoardsTemplateClassView(ListView):
    model = Boards

class BoardsTemplateClassView(TemplateView):
    template_name = "template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Boards.objects.all() # 데이터베이스로부터 가져오기 위함
        return context


def board_list_page(request):
    if request.method == 'POST':
        name = request.POST['title'] # POST는 form 메서드를 기본적으로 처리하며, 요청 객체를 딕셔너리 형태로 저장한다.
        image = request.FILE['img_file']

def board_list(request):
    try:
        page = int(request.GET['PAGE']) # 요청을 딕셔너리로 만든 것의 PAGE 필드를 반환
    except:
        page = 1