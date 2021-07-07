# importing libraries
import cv2

def play_videoFile(filePath):
# Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(filePath)
    
   
# Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video  file")
   
# Read until video is completed
    while(cap.isOpened()):
        cv2.namedWindow('voicEnter', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('voicEnter',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
      
  # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
   
    # Display the resulting frame
            cv2.imshow('voicEnter', frame)
   
    # Press Q on keyboard to  exit
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
   
  # Break the loop
        else: 
            break
   
# When everything done, release 
# the video capture object
    #cap.release()
   
# Closes all the frames
    cv2.destroyAllWindows()