from django.shortcuts import render

# Create your views here.


def teachers_index_view(request):
    return render(request, 'teachers/index.html')
