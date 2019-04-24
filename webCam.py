import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width=640
cap.set(4, 480)  # height=480
cv2.namedWindow("Webcam")
cv2.moveWindow("Webcam", 800, 20);
while (True):

    ret, frame = cap.read()  # Capture frame-by-frame
    rgbImage = frame  # For capture the image in RGB color space

    # Display the resulting frame

    cv2.imshow('Webcam', rgbImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()