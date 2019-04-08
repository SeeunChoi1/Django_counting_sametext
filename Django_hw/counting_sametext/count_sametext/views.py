from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def result(request):
    text = request.GET['fulltext']
    textcount = len(text)
    divide = text.split()    
    dic = { }

    for word in divide:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return render(request, 'result.html', {
        'text':text,
        'textcount':textcount,
        'dic':dic.items(),
    }) #dictionary
