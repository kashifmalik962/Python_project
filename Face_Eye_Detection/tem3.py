import cv2

# Load the pre-trained Haar Cascade for eyes
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Read the input image
img = cv2.imread(r"D:\Python_project\Face_Eye_Detection\deloitte-nl-cm-digital-human-promo.avif")
# print(img)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eyes in the image
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around the eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()