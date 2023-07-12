import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime, timedelta


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", help="source video path",
        type=str)
parser.add_argument("-s", "--start", help="start time in seconds",
        type=str)
parser.add_argument("-e", "--end", help="end time in seconds",
        type=str)
parser.add_argument("-o", "--output", help="output video path",
        type=str)
args = parser.parse_args()

# Load the video
video = VideoFileClip(args.video)

# Define the start and end times for the trim
start_time = args.start  # seconds
end_time = args.end  # seconds

# turn time
if start_time.find(":") != -1:
    """
    s = start_time.split(":")
    start_time = int(s[0]*60*60 + s[1]*60 + s[2])
    """
    time_obj = datetime.strptime(start_time, '%H:%M:%S')
    total_seconds = timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second).total_seconds()
    start_time = int(total_seconds)
else:
    start_time = int(start_time)

if end_time.find(":") != -1:
    """
    s = end_time.split(":")
    end_time = int(s[0]*60*60 + s[1]*60 + s[2])
    """
    time_obj = datetime.strptime(end_time, '%H:%M:%S')
    total_seconds = timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second).total_seconds()
    end_time = int(total_seconds)
else:
    end_time = int(end_time)

# Trim the video
trimmed_video = video.subclip(start_time, end_time)

# Save the trimmed video
trimmed_video.write_videofile(args.output)
