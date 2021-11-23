from django.shortcuts import get_object_or_404,HttpResponse
from .models import File


def stream_file(request, pk):
    file = get_object_or_404(File, id=pk)
    response = HttpResponse()
    response['Content-Type'] = file.content_type
    response['Content-Length'] = len(file.file_data)
    response.write(file.file_data)
    return response
