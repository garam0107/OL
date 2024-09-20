from django.urls import path, include
from . import views

app_name = 'todos'

urlpatterns = [
    # main 경로 요청이 들어오면, todos 앱 패키지 내에 있는
    # views.py 모듈 안에 있는 main 함수 실행
    path('main/', views.main, name = 'main'),
    # todo를 추가 할 수 있는 어떤 기능이 포함된 함수 만들고,
    # todo를 추가 할 수 있는 html 반환
    path('create/', views.create, name = 'create'),
]