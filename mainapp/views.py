# from django.shortcuts import render, redirect,HttpResponseRedirect
# from django.http import HttpResponse, JsonResponse
# from django.contrib import auth, messages
# from .models import *
# from .forms import *
# from django.views.decorators.http import require_POST
# from django.conf import settings
# import os


# def home(request):
#     if request.method=='POST':
#         username=request.POST['user']
#         password=request.POST['pas']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return HttpResponseRedirect("/upload_file")
#         else:
#             messages.error(request,'Usrename and Passwodr did not Match')

#     return render(request,"index.html")
# def registration(request):
#     if request.method=='POST':
#         form=Registration_form(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#             messages.success(request,"User Register Successfully")
#             return HttpResponseRedirect("/registration")
#     else:
#         form=Registration_form()
#     return render(request,'registration.html',{'form':form})
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')  # Redirect to file list view after successful upload
#     else:
#         form = UploadFileForm()
#     files = UploadedFile.objects.all()
#     return render(request, 'upload_file.html', {'form': form, 'files': files})

# def download_file(request, file_id):
#     uploaded_file = UploadedFile.objects.get(pk=file_id)
#     response = HttpResponse(uploaded_file.file, content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
#     return response

# def file_detail(request, file_id):  # Renamed to file_detail
#     uploaded_file = UploadedFile.objects.get(id=file_id)
#     return render(request, 'file_detail.html', {'file': uploaded_file})

# @require_POST
# def delete_file(request):
#     if request.user.is_authenticated:
#         file_id = request.POST.get('file_id')
#         try:
#             uploaded_file = UploadedFile.objects.get(id=file_id)
#             file_path = os.path.join(settings.MEDIA_ROOT, str(uploaded_file.file))  # Assuming the field storing the file is named 'file'
            
#             if os.path.exists(file_path):
#                 os.remove(file_path)
#                 uploaded_file.delete()
#                 return JsonResponse({'message': 'File deleted successfully.'})
#             else:
#                 return JsonResponse({'error': 'File not found.'}, status=404)
#         except UploadedFile.DoesNotExist:
#             return JsonResponse({'error': 'File not found.'}, status=404)
#     else:
#         return JsonResponse({'error': 'Unauthorized'}, status=401)

from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pas']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("image")
        else:
            messages.error(request,'Usrename and Password did not Match')

    return render(request,"index.html")

# def logout(request):
#     auth.logout(request)
#     return render(request,'index.html')







def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = ImageUploader.objects.all()
    return render(request,"image.html",{'img':img,'form':form})

def download_file(request,id):
    img = ImageUploader.objects.get(id= id)
    response = HttpResponse(img.photo.file, content_type="application/octet-stream")
    response["Content-Disposition"]= f'attachment;filename = {img.photo.name}'
    return response


def registration(request):
    if request.method=='POST':
        form=Registration_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            messages.success(request,"User Register Successfully")
            return HttpResponseRedirect("/registration")
    else:
        form=Registration_form()
    return render(request,'registration.html',{'form':form})


