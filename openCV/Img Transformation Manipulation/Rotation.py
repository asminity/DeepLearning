import cv2

image = cv2.imread("parrot.jpg")
image = cv2.resize(image, (500, 500))

if image is not None:
    width, height = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2.imwrite("rotated_parrot.jpg", rotated_image)
    print("Rotated image saved successfully")
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")

