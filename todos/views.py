from django.shortcuts import render


todo_list = []
# Create your views here.
# 함수는 input에 대한 어떤 처리 후, output을 내는게 목적

# views.py에 만드는 모든 함수들의 목적?
# 사용자의 요청에 따라서 반환해야할 적절한 html을 내는게 목적
def main(request):
    work = request.GET.get('work')
    if work:
        todo_list.append(work)
    context = {
        'todo_list' : todo_list
    }

    return render(request, 'todos/main.html', context)


def create(request):
    return render(request, 'todos/create.html')



    