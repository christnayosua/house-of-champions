from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'applicationName' : 'House Of Champions',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'npm' : '2406495691',
    }

    return render(request, "main.html", context)