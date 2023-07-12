import cv2
import argparse
import datetime
import time


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="rtsp source", type=str)
parser.add_argument("-n", "--name", help="name of video file", type=str)
args = parser.parse_args()
if not args.source:
    print("no source args, quitting...")
    quit()
cap = cv2.VideoCapture(args.source)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(args.name, fourcc, 20.0, (800,600))
fail_count = 0
start = int(time.time())
end = start + 43200
# end = start+86400
print("reading frame...")
while cap.isOpened():
    if time.time() > end:
        print("time's up")
        break
    ret, frame = cap.read()
    if not ret:
        count = count + 1
        cap.release()
        print("cannot recieve frame")
        if fail_count <= 3:
            cap = cv2.VideoCapture(args.source)
            continue
        else:
            print("rtsp link down, quitting...")
            quit()
    # put timestamp
    frame = cv2.resize(frame, (800,600))
    cv2.putText(frame, str(datetime.datetime.now()), (3,40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    out.write(frame)

out.release()
cap.release()
