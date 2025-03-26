from django.urls import path
from . import views

# 이 코드는 Django 웹 애플리케이션의 URL 패턴을 정의하는 부분입니다.
# 'urlpatterns' 리스트는 URL 경로와 해당 경로에 대한 뷰를 매핑합니다.
# 여기서는 'hello/'라는 URL 경로가 'views.hello_world' 함수와 연결되어 있습니다.
# 'name' 매개변수는 이 URL 패턴에 'hello_world'라는 이름을 부여하여,
# 다른 곳에서 이 URL을 참조할 때 사용됩니다.
urlpatterns = [path('hello/', views.hello_world, name='hello_world')]