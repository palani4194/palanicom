from django.shortcuts import render
from django.conf import settings

def login(request):
    return render(request, 'blog/templates/registration/login.html')

# def detail(request, album_id):
#     # import pdb; pdb.set_trace()
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request,'music/detail.html')
