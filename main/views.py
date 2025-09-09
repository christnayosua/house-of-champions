from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nameItem' : 'Messi',
        'price': '$10.000',
        'year': '2022 World Cup'
    }

    return render(request, "main.html", context)