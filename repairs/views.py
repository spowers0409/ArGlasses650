from django.shortcuts import redirect, render
from django.http import Http404
from .forms import VehicleForm

def vehicle_select(request):
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            vehicle = f"{vehicle_form.cleaned_data.get('year')} {vehicle_form.cleaned_data.get('make')} {vehicle_form.cleaned_data.get('model')} {vehicle_form.cleaned_data.get('trim')}"
            repair = vehicle_form.cleaned_data.get('repair')
            return redirect('repair_instructions', vehicle=vehicle, repair=repair)
    else:
        vehicle_form = VehicleForm()
    return render(request, 'repairs/vehicle_select.html', {'vehicle_form': vehicle_form})

def repair_instructions(request, vehicle, repair):
    instructions_map = {
        '2018 Dodge Charger Hellcat Fuel Pump Replacement': 'https://prod-da.s3.us-east-2.amazonaws.com/BHKJ/7c293ea5ab2d11ea6e93a2d41e6de3b5.pdf',
        '2004 Ford Mustang Cobra Fuel Pump Replacement': 'https://prod-da.s3.us-east-2.amazonaws.com/BHKJ/76d43749e7f0a95b00ca95c4317f310a.pdf',
        '2019 Chevrolet Corvette Z06 Short Throw Shifter': 'https://www.phastekperformance.com/content/inst/3915086_instructions.pdf',

    }
    
    key = f"{vehicle} {repair}"
    url = instructions_map.get(key)
    if not url:
        return render(request, 'repairs/no_instructions.html')

    
    return redirect(url)



