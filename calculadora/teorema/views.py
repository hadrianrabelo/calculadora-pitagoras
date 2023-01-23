from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def calcularTeorema(request):
    if request.method == 'POST':

        lado_a = request.POST.get('legA')
        if lado_a != '': lado_a = float(lado_a)
        print(lado_a)

        lado_b = request.POST.get('legB')
        if lado_b != '': lado_b = float(lado_b)
        print(lado_b)

        hipotenusa = request.POST.get('hypotenuse')
        if hipotenusa != '': hipotenusa = float(hipotenusa)
        print(hipotenusa)

        if (lado_a == '' and not lado_b == '') and hipotenusa != '':
            result = calcularCateto(lado_a if lado_a != '' else lado_b, hipotenusa)
            print(result)
                
            context = {
            'o resultado é ' + str(result)
            }

            return HttpResponse(context)

        elif hipotenusa == '' and lado_a != '' and lado_b != '':
            calcularHipotenusa(lado_a, lado_b)
            print("voce ai")

        else:
            return HttpResponse("Valores inválidos!", status = 400)

@csrf_exempt
def calcularCateto(catetoA, hipotenusa):
    catetoB = (hipotenusa **2 - catetoA**2)**(1/2)
    return (catetoB)

@csrf_exempt
def calcularHipotenusa(catetoA, catetoB):
    hipotenusa = (catetoA**2 + catetoB**2)**(1/2)
    return (hipotenusa)
