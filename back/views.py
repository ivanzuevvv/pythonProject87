from .models import Predicions
from django.shortcuts import render, get_object_or_404






def analiz(request):
    return render(request, 'analiz.html')


def prediction_view(request):
    if request.method == 'POST':
        type_refuses = request.POST.get('type_refuses')
        type_gpa = request.POST.get('type_gpa')
        type_say = request.POST.get('type_say')
        type_equioment = request.POST.get('type_equioment')

        predictions = Predicions.objects.filter(
            type_refuses=type_refuses,
            type_gpa=type_gpa,
            type_say=type_say,
            type_equioment=type_equioment
        )


        context = {
            'predictions': predictions,
            'type_equioment': Predicions.objects.filter(
                type_refuses=type_refuses,
                type_gpa=type_gpa,
                type_say=type_say,
            ).values_list('type_equioment', flat=True).distinct()
        }

        return render(request, 'refuses_form.html', context)

    type_refuses = Predicions.objects.values_list('type_refuses', flat=True).distinct()
    type_gpa = Predicions.objects.values_list('type_gpa', flat=True).distinct()
    type_say = Predicions.objects.values_list('type_say', flat=True).distinct()

    context = {
        'type_refuses': type_refuses,
        'type_gpa': type_gpa,
        'type_say': type_say,
    }

    return render(request, 'refuses_form.html', context)


def prediction_view2(request):
    if request.method == 'POST':
        type_refuses = request.POST.get('type_refuses')
        type_gpa = request.POST.get('type_gpa')
        type_say = request.POST.get('type_say')
        refuses_element = request.POST.get('refuses_element')

        predictions = Predicions.objects.filter(
            type_refuses=type_refuses,
            type_gpa=type_gpa,
            type_say=type_say,
            refuses_element=refuses_element
        )


        context = {
            'predictions': predictions,
            'refuses_element': Predicions.objects.filter(
                type_refuses=type_refuses,
                type_gpa=type_gpa,
                type_say=type_say,
            ).values_list('refuses_element', flat=True).distinct()
        }

        return render(request, 'analiz.html', context)

    type_refuses = Predicions.objects.values_list('type_refuses', flat=True).distinct()
    type_gpa = Predicions.objects.values_list('type_gpa', flat=True).distinct()
    type_say = Predicions.objects.values_list('type_say', flat=True).distinct()

    context = {
        'type_refuses': type_refuses,
        'type_gpa': type_gpa,
        'type_say': type_say,
    }

    return render(request, 'analiz.html', context)


