from typing import Any
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from testapp.models import Boards
from django.views.generic import ListView, TemplateView

# Create your views here.

# CBV에서 get, post 등의 메서드에는 첫 번째 인자로 self가, 두 번째 인자로는 request가 온다.
class BoardsListClassView(ListView):
    model = Boards
    template_file = "boards_list_cbv.html"

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

# 특정 템플릿을 렌더링
def BoardsListFunctionView(request):
    boardList = Boards.objects.all()
    return render(request, 'boardsview.html', {'boardList': boardList})

def board_delete_result(reqeust):
    if referer == "board":
        redirection_page = '/boardapp/board_list/' + article.category.category_code + '/'
    else:
        redirection_page = '/boardapp/comm_list/' + article.category.category_code + '/'

# 특정 문자열을 렌딩
def user_register_idcheck(request):
    msg = "<font color='red'>이미 존재하는 ID입니다.</font>"

    return HttpResponse(msg)

# Json 응답을 반환
def board_like_result(request):
    args = {}
    args.update({"like_err_msg": "본인의 게시물에는 추천할 수 없습니다."})
    args.update({"article_id": article_id})

    return JsonResponse(args)