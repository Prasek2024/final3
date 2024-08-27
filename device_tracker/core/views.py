def home_page_view(request):
    return render(request, "home.html")


def about_page_view(request):
    return render(request, "about.html")


from django.shortcuts import render

# Create your views here.
