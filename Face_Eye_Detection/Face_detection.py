import cv2

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image

image = cv2.imread(r'D:\Python_project\Face_Eye_Detection\Danish.jpg')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)

# Display the image with detected faces
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()