import cv2

# Open a connection to the default camera (usually the first one detected)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    if not ret:
        print("Error: Could not read the frame.")
        break
    
    # Display the resulting frame in a window
    cv2.imshow('Camera Feed', frame)
    
    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
