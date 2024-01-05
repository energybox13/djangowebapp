from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import avgmarks
from service.models import cric_stats
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from django.http import FileResponse
from django.core.cache import cache


def home_page(requets): 
    return render(requets,'video.html')
def video(request):
    if request.method=="GET":
        tn=request.GET.get('tname')
        dnn=request.GET.get('drn')
        gnn=request.GET.get('grn')
        ynn=request.GET.get('yr')



    return render(request,"video.html",{'tn':tn,'dnn':dnn,'gnn':gnn,'ynn':ynn})

def about(request):
    return render(request,"about.html")
def courses(request):
    return HttpResponse("We offer Python Java and C++")
def dynamic(request, id):
    return HttpResponse(id)
# def home_page(request):
#     return HttpResponse("Welcome to my Homepage")

def play_video(request):

    video_path = '/static/Chale_jaise.mp4'  # Path to your video file
    return render(request, 'videos_brow.html', {"video_paths":video_path})

def movieDetails(request):
    m_data={}
    t_name=None
    d_name=None
    g_name=None
    yn=None
    if request.method=="POST":
        title_name = request.POST.get('title', '')
        director_name = request.POST.get('director', '')
        genre_name = request.POST.get('genre', '')
        years = request.POST.get('year', '')
        m_data={'t_name': title_name, 'd_name': director_name, 'g_name': genre_name, 'yn': years}
        url="/video/?tname={}&drn={}&grn={}&yr={}".format(title_name,director_name,genre_name,years)
        return HttpResponseRedirect(url)
    
    return render(request, 'movies.html',m_data)
from django.http import HttpResponse


def avg1(request):
    if request.method == "GET":
        fn = avgmarks()  # Assuming this function fetches initial data or a form
        data = {'form': fn}
        return render(request, 'avg.html', data)
    
    if request.method == "POST":
        fn = avgmarks()  # Assuming this function fetches initial data or a form
        mm = float(request.POST.get('num1', 0))
        ms = float(request.POST.get('num2', 0))
        me = float(request.POST.get('num3', 0))
        avg = (mm + ms + me) / 3
        
        data = {
            'form': fn,
            'avgc': avg
        }
        
        return render(request, 'avg.html', data)



def msheet(request):
    sum=0
    per=0
    data3={}
    try:
        if request.method=="POST":
            if (request.GET.get("subject1")==None or  request.GET.get("subject2")==None or  request.GET.get("subject3")==None or  request.GET.get("subject4")==None or  request.GET.get("subject5")==None):
                return render(request,"marksheet.html",{'error':True})
            n1=eval(request.GET.get('subject1'))
            n2=eval(request.GET.get('subject2'))
            n3=eval(request.GET.get('subject3'))
            n4=eval(request.GET.get('subject4'))
            n5=eval(request.GET.get('subject5'))
            sum=(n1+n2+n3+n4+n5)
            per=(sum/500)*100
        
    except:
        s="Invalid marks"
    
    return render(request,"marksheet.html",{'sum':sum,'per':per})





def songs(request):
    # Try fetching songs_info from cache
    songs_info = cache.get('songs_info')

    if not songs_info:
        song_folder = 'static/New_folder'  # Update with the path to your song folder
        songs_info = []

        if os.path.exists(song_folder) and os.path.isdir(song_folder):
            songs = [f for f in os.listdir(song_folder) if os.path.isfile(os.path.join(song_folder, f))]

            for song_file in songs:
                song_path = os.path.join(song_folder, song_file)
                if song_file.endswith('.mp3'):
                    audio = MP3(song_path, ID3=EasyID3)
                    duration = audio.info.length  # Get song duration in seconds

                    # Get artist information
                    artist = None
                    if 'artist' in audio:
                        artist = audio['artist'][0]

                    songs_info.append({
                        'title': song_file,
                        'duration': duration,
                        'artist': artist
                    })

            # Cache the songs_info for future use (cache timeout in seconds)
            cache.set('songs_info', songs_info, timeout=7200)  # Cache for an hour

    return render(request, 'music.html', {'songs_info': songs_info})



