from django.shortcuts import render

# Create your views here.
def Vista(request):
  return render(request, "seriales/base_head.html")