from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def calcularTeorema(request):
    if request.method == 'POST':

        lado_a = request.POST.get('legA')
        if lado_a != '': 
            lado_a = float(lado_a)

        lado_b = request.POST.get('legB')
        if lado_b != '': 
            lado_b = float(lado_b)

        hipotenusa = request.POST.get('hypotenuse')
        if hipotenusa != '': 
            hipotenusa = float(hipotenusa)

            
        if (lado_a == '' and lado_b != '' and hipotenusa != ''):
            result = round(calcularCateto(lado_b, hipotenusa), 2)
                
            context = {
            'O valor do primeiro cateto é ' + str(result)
            }

            return HttpResponse(context)

        if (lado_b == '' and lado_a != '' and hipotenusa != ''):
            result = calcularCateto(lado_a, hipotenusa)
                
            context = {
            'O valor do segundo cateto é ' + str(result)
            }

            return HttpResponse(context)

        elif hipotenusa == '' and lado_a != '' and lado_b != '':
            result = round(calcularHipotenusa(lado_a, lado_b), 2)

            context = {
            'O valor da hipotenusa é ' + str(result)
            }
            
            return HttpResponse(context)

        else:
            return HttpResponse("Valores inválidos!", status = 400)


@csrf_exempt
def calcularCateto(catetoA, hipotenusa):
    if(catetoA > hipotenusa): 
        return ('ímpossivel calcular, hipotenusa não pode ser menor que o valor do cateto.')
    catetoB = (hipotenusa**2 - catetoA**2)**(1/2)
    return (catetoB)

@csrf_exempt
def calcularHipotenusa(catetoA, catetoB):
    hipotenusa = (catetoA**2 + catetoB**2)**(1/2)
    return (hipotenusa)
