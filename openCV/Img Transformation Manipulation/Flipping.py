import cv2

image = cv2.imread("parrot.jpg")
image = cv2.resize(image, (500, 500))

if image is not None:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)
    
    cv2.imwrite("flippedHorizontal_parrot.jpg", flipped_horizontal)
    cv2.imwrite("flippedVertical_parrot.jpg", flipped_vertical)
    cv2.imwrite("flippedBoth_parrot.jpg", flipped_both)
    print("Flipped image saved successfully")
    cv2.imshow("Flipped Horizontal", flipped_horizontal)
    cv2.imshow("Flipped Vertical", flipped_vertical)
    cv2.imshow("Flipped Both", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")