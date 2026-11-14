from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
# Create your views here.


def generate_qr_code(request):
    form = QRCodeForm(request.POST if request.method == 'POST' else None)

    if request.method == 'POST':
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            menu_url = form.cleaned_data['menu_url']
            
            file_name = res_name.replace(" ", "_").lower() + "_qr.png";
            restaurant_name = res_name.replace(" ", "").lower()
            qr_image = qrcode.make(menu_url)
            
            
            
            
            #to serve the qr image static files
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) 
            #setting.MEDIA_ROOT is the directory where media files are stored
            qr_image.save(file_path)
            
            
            # creating image url to be used in the template
            image_url = os.path.join(settings.MEDIA_URL, file_name)
            
            
            
            context = {
                            "res_name" : restaurant_name,
                            "qr_url" : image_url,
                            "file_name" : file_name
                        }
            
            return render(request, 'qr_result.html', context)

    return render(request, 'generate_qr_code.html', {"form": form})