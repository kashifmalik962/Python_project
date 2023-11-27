while True:
    # ... (previous code)

    for face in faces:
        # ... (previous code)

        # Check for blinks
        if (ear_left + ear_right) / 2 < 0.2:
            blink_counter += 1

    # Update total_blinks in each iteration
    total_blinks += blink_counter

    # Display the frame
    cv2.imshow("Blink Detection", frame)

    # Check if the specified duration has elapsed
    if time.time() - start_time > duration:
        break

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ... (rest of the code)

# Print the total number of blinks after the loop
print("Total Blinks:", total_blinks)
