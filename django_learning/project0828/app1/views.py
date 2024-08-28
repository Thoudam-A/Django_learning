from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome!')

def user_list(request):
    name = 'zrx'
    roles = ['manager', 'user']
    return render(request, 'user_list.html', {"name":name, "roles":roles})  #render的用法

def img_show(request):
    return render(request, 'img_show.html')

def news(request):
    
    # 使用第三方库requests向互联网发送请求
    import requests
    res = requests.get("https://baidu.com")
    print()
    data_list = res.json()
    print(data_list)
    return render(request, 'news.html')

def sth(request):
    
    # request是POST还是GET或者其他
    print(request.method)
    
    # GET的内容
    print(request.GET)
    
    # 
    print(request.POST)
    
    return HttpResponse('返回内容')