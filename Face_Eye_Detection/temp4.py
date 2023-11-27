import cv2

# Load a different pre-trained nose classifier
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')

# Load the image
image_path = 'Humans.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale for nose detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform nose detection
noses = nose_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected noses
for (x, y, w, h) in noses:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected noses
cv2.imshow('Nose Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
