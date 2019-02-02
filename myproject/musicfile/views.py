from django.shortcuts import render,get_object_or_404
from .models import Album,Songs
from .forms import UserForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


#
# def index(request):
#     all_albums = Album.objects.all()
#     return render(request, 'music/index.html',{'all_albums': all_albums},)
#
# def detail(request, album_id):
#     # import pdb; pdb.set_trace()
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request,'music/detail.html', {'album': album})

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        # import pdb; pdb.set_trace()
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        raise
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "No song selected"
        })

    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})



class IndexView(ListView):
    template_name = "music/index.html"
    context_object_name ='all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(DetailView):
    template_name = "music/detail.html"
    model = Album


class AlbumCreate(CreateView):
    template_name = "music/album_form.html"
    model = Album
    fields = ['artist','album_title','region','logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','region','logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy("musicfile:contentofindex")




class LoginView(DetailView):
    form_class = UserForm
    template_name = "music/registration.html"

    # display empty form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect(reverse('musicfile:contentofindex'))
        return render(request,self.template_name,{'form':form})
