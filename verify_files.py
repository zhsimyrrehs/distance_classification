import os
import cv2  # OpenCV for image loading

# Get the Desktop path dynamically
desktop_path = os.path.expanduser("~/Desktop")

# Define the image file names
image_1_path = "Dr_Shashi_Tharoor.jpg"
image_2_path = "Plaksha_Faculty.jpg"

# Check if images exist
for image_path in [image_1_path, image_2_path]:
    if not os.path.exists(image_path):
        print(f"❌ Error: Image not found - {image_path}")
    else:
        print(f"✅ Image found: {image_path}")

# Load images to verify they open correctly
try:
    img1 = cv2.imread(image_1_path)
    img2 = cv2.imread(image_2_path)

    if img1 is None or img2 is None:
        print("❌ Error: One or both images could not be loaded.")
    else:
        print("✅ Images loaded successfully.")
except Exception as e:
    print(f"❌ Error loading images: {e}")
