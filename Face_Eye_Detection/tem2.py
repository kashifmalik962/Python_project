import cv2
import dlib
import time

# Load the pre-trained face and facial landmark detector from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initialize variables for counting blinks
blink_counter = 0

# Set the duration for which you want the program to run (in seconds)
duration = 10  # Change this to your desired duration

# Get the start time
start_time = time.time()


def eye_aspect_ratio(eye):
    # Calculate the Euclidean distances between the vertical eye landmarks
    vertical_dist1 = ((eye[1][1] - eye[5][1]) ** 2 + (eye[1][0] - eye[5][0]) ** 2) ** 0.5
    vertical_dist2 = ((eye[2][1] - eye[4][1]) ** 2 + (eye[2][0] - eye[4][0]) ** 2) ** 0.5
    
    # Calculate the Euclidean distance between the horizontal eye landmarks
    horizontal_dist = ((eye[3][1] - eye[0][1]) ** 2 + (eye[3][0] - eye[0][0]) ** 2) ** 0.5
    
    # Calculate the eye aspect ratio
    ear = (vertical_dist1 + vertical_dist2) / (2.0 * horizontal_dist)
    return ear


while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get facial landmarks
        landmarks = predictor(gray, face)

        # Extract the left and right eye coordinates
        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

        # Draw rectangles around the eyes
        cv2.rectangle(frame, (min(left_eye, key=lambda x: x[0])[0], min(left_eye, key=lambda x: x[1])[1]),
                      (max(left_eye, key=lambda x: x[0])[0], max(left_eye, key=lambda x: x[1])[1]), (0, 255, 0), 2)

        cv2.rectangle(frame, (min(right_eye, key=lambda x: x[0])[0], min(right_eye, key=lambda x: x[1])[1]),
                      (max(right_eye, key=lambda x: x[0])[0], max(right_eye, key=lambda x: x[1])[1]), (0, 255, 0), 2)

        # Calculate eye aspect ratio (EAR) for each eye
        ear_left = eye_aspect_ratio(left_eye)
        ear_right = eye_aspect_ratio(right_eye)

        # Check for blinks
        if (ear_left + ear_right) / 2 < 0.2:
            blink_counter += 1

    # Display the frame
    cv2.imshow("Blink Detection", frame)

    # Check if the specified duration has elapsed
    if time.time() - start_time > duration:
        break

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Print the total number of blinks after the loop
print("Total Blinks:", blink_counter)
