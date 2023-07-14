import moviepy.editor
from pathlib import Path

def video_to_audio(path_to_file,audio_file_name):
    path_tofile = Path(path_to_file)
    video = moviepy.editor.VideoFileClip(f"{path_tofile}")
    audio = video.audio
    audio.write_audiofile(f"{audio_file_name}.mp3")
