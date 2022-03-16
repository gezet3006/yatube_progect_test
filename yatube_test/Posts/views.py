from django.shortcuts import render


def index(request):
    post = "Это главная страница проекта Yatube"
    context ={
        'post':post
    }   
    return render(request, 'posts/index.html', context)

def group_list(request):
    group = "Здесь будет информация о группах проекта Yatube"
    context = {
        'group':group
    }
    return render(request, 'posts/group_list.html', context)
