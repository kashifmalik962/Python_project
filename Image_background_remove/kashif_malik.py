import cv2
import numpy as np

def remove_background(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Create a mask
    mask = np.zeros(img.shape[:2],np.uint8)
    
    # Define the background and foreground models
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    
    # Define a rectangle covering the entire image
    rect = (0, 0, img.shape[1]-1, img.shape[0]-1)
    
    # Apply GrabCut algorithm
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    
    # Modify the mask: probable background and definite background to 0, others to 1
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    
    # Apply the mask to the original image
    result = img * mask2[:, :, np.newaxis]
    
    return result

# Example usage
input_image_path = "download.jpg"
output_image = remove_background(input_image_path)
cv2.imwrite("output_image.png", output_image)
