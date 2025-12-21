# Converting videos to mp3 audio

import os
import subprocess

videos = os.listdir("HTML_CSS_COURSE_VIDEOS")

for video in videos:
    # print(video)
    tut_no = video.split(" - ",1)[0]
    tut_name = video.split(" - ",1)[1]
    subprocess.run(["ffmpeg","-i",f"HTML_CSS_COURSE_VIDEOS/{video}",f"audios_of_videos/{tut_no}_{tut_name}.mp3"])

    
