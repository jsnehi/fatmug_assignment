import os
import re
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoUploadForm
from .models import Video
from subprocess import run

ffmpeg_path = '***'

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()

            # Extract subtitles using ffmpeg
            video_path = video.video_file.path
            subtitle_path = os.path.splitext(video_path)[0] + '.srt'
            run([ffmpeg_path, '-i', video_path, subtitle_path])

            # Save the subtitles to the database
            with open(subtitle_path, 'r') as file:
                subtitles = file.read()
            video.subtitle_file = subtitles
            video.save()

            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def search_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    query = request.GET.get('q', '').lower()
    subtitles = video.subtitle_file.lower()
    
    results = []
    for line in subtitles.split('\n'):
        parts = line.split()
        if len(parts) > 0 and query in line:
            try:
                timestamp = parts[0]
                results.append((timestamp, line))
            except IndexError:
                continue

    return render(request, 'search_results.html', {'video': video, 'results': results})

def convert_to_seconds(timestamp):
    timestamp = timestamp.replace(',', '.')
    h, m, s = timestamp.split(':')
    # Convert hours, minutes, and seconds to float and compute total seconds
    return float(h) * 3600 + float(m) * 60 + float(s)

def play_from_timestamp(request, video_id, timestamp):
    video = get_object_or_404(Video, id=video_id)
    # Convert timestamp from HH:MM:SS to seconds
    seconds = convert_to_seconds(timestamp)
    return render(request, 'play_video.html', {'video': video, 'timestamp': seconds})
