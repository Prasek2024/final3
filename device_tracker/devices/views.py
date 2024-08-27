from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Device
from .forms import DeviceForm
from .forms import DeviceSearchForm
from django.shortcuts import render


class device_CreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'add_device.html'
    success_url = reverse_lazy('add_device')

class device_ListView(ListView):
    model = Device
    template_name = 'pagination_devices.html'
    context_object_name = 'devices'
    paginate_by = 2



def search_device(request):
    if request.method == 'POST':
        form = DeviceSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['device_name']
            object_list = Device.objects.filter(title__icontains=book_name)
            return render(request, 'list_devices.html', {'form': form, 'object_list': object_list})
    else:
        form = DeviceSearchForm()
        object_list = Device.objects.all()

    return render(request, 'list_devices.html', {'form': form, 'object_list': object_list})


# Create your views here.
