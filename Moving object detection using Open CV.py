import cv2

# Load the image (change extension if your file is .jpg, .jpeg, or .png)
img = cv2.imread(r"C:\Users\Thanveer Ahamed A\OneDrive\Desktop\NASRIN STUDYROOM\NASRIN 30 DAYS AI\Open CV Original Image")

# Check if image loaded successfully
if img is None:
    print("❌ Error: Image not found! Check the path or filename.")
else:
    print("✅ Image loaded successfully.")

    # Apply Gaussian Blur
    gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)   # strong blur
    gaussianImg1 = cv2.GaussianBlur(img, (21, 21), 0)   # mild blur

    # Show images
    cv2.imshow("Original", img)
    cv2.imshow("GaussianBlur (41x41, sigma=50)", gaussianImg)
    cv2.imshow("GaussianBlur1 (21x21, sigma=0)", gaussianImg1)

    # Wait for key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
