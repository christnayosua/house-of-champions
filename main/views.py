from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForm
from main.models import Items

# Penambahan import modul untuk request pengiriman data ke dalam bentuk XML dan JSON
from django.http import HttpResponse
from django.core import serializers

# Function untuk mengirimkan data dalam bentuk XML
def show_xml(request):
     items_list = Items.objects.all()
     xml_data = serializers.serialize("xml", items_list)
     return HttpResponse(xml_data, content_type="application/xml")

# Function untuk mengirimkan data dalam bentuk JSON
def show_json(request):
    items_list = Items.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

# Mengirimkan data dalam bentuk XML berdasarkan ID
def show_xml_by_id(request, items_id):
   try:
       items_list = Items.objects.filter(pk=items_id)
       xml_data = serializers.serialize("xml", items_list)
       return HttpResponse(xml_data, content_type="application/xml")
   except Items.DoesNotExist:
       return HttpResponse(status=404)

# Mengirimkan data dalam bentuk JSON berdasarkan ID
def show_json_by_id(request, items_id):
   try:
       items_list = Items.objects.get(pk=items_id)
       json_data = serializers.serialize("json", [items_list])
       return HttpResponse(json_data, content_type="application/json")
   except Items.DoesNotExist:
       return HttpResponse(status=404)

def show_main(request):
    items_list = Items.objects.all()

    context = {
        'applicationName' : 'House Of Champions',
        'npm' : '2406495691',
        'name': 'Christna Yosua Rotinsulu',
        'class': 'PBP A',
        'items_list': items_list
    }

    return render(request, "main.html", context)

def create_items(request):
    form = ItemsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)

def show_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.increment_views()

    context = {
        'items': items
    }

    return render(request, "items_detail.html", context)