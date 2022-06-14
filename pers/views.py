from django.shortcuts import HttpResponse


def main(request):
    return HttpResponse("It's work")