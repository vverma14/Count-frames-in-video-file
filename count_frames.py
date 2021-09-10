import cv2 as cv2

def get_imagearray_with_framelabel(input_video):
  cap = cv2.VideoCapture(input_video)
  total = 1  #Frame Count
  style = cv2.FONT_HERSHEY_SIMPLEX #Font Style
  coord = (200, 70) #Coordinate in the frame, relevant only for this specific video   
  font = 3 #Display Font
  blue_color = (255, 0, 0) #Color
  thickness = 3 #Thickness #Font
  image_array = []
  while cap.isOpened():
      grabbed_boolean,frame=cap.read() 

      if not grabbed_boolean: #Check to make sure we do not miss any frame #IMPORTANT
        break

      image = cv2.putText(frame, str(total), coord, style, 
                   font, blue_color, thickness, cv2.LINE_AA)
      total += 1 #Increment frame count
      image_array.append(image)

  return image_array    


def write_frame_video(labelled_frames):  #Write frames to a video
  h,w,c=labelled_frames[0].shape
  writer_object = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter('output.mp4', writer_object, 30, (w, h))
  for i in labelled_frames:
    out.write(i)

  out.release()


def cv_check_frames(video):
    cap= cv2.VideoCapture(video)
    totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("The total number of frames as per open-cv in this video is ", totalframecount)

video_file = '115.mp4'
labelled_frames = get_imagearray_with_framelabel(video_file)
print("Number of frames calculated:",len(labelled_frames))
write_frame_video(labelled_frames)
cv_check_frames(video_file)