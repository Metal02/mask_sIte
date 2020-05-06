from django.shortcuts import render

def main_page(request):
    return render(request, 'mAsk/main_page.html', {})
