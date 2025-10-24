from django.shortcuts import render

# Create your views here.

def student_index_view(request):
    return render(request, 'students/index.html')
