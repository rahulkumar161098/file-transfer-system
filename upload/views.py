
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from upload.models import *
from django.contrib import messages

# Create your views here.


def index(request):
    all_data= UploadFile.objects.all().order_by('-id')[:6]

    if request.method =='POST':
        user_desc = request.POST['user_name']
        file = request.FILES['user_media']
        save_query = UploadFile(name=user_desc,file_up=file)
        save_query.save()
        messages.success(request, 'File upload successful!')

    # else:
    #     messages.error(request, 'Something went worng')

    return render(request, 'templates/index.html',{'uploadedData': all_data})

def delete(request, id):
    # all_data= UploadFile.objects.all().order_by('-id')[:5]
    del_data= UploadFile.objects.get(id=id)
    del_data.delete()
    messages.info(request, 'File Deleted successful!')
    return redirect('index_page')


# def download(request,path):
#     file_path=os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response= HttpResponse(fh.read(), content_type="application/file")
#             response['Content-Disposition']= 'inline; filename="+os.path.basename(file_path)"'
#             return response
#     raise Http404
