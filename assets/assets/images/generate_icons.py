from PIL import Image
import os

# اسم ملف الشعار الأصلي عالي الدقة الموجود في مشروعك
SOURCE_LOGO = "logo.png"

# قائمة المقاسات المطلوبة للأيقونات
ICON_SIZES = {
    "favicon-16x16.png": (16, 16),
    "favicon-32x32.png": (32, 32),
    "apple-touch-icon.png": (180, 180),
    "icon-192x192.png": (192, 192),
    "icon-512x512.png": (512, 512),
}

def generate_app_icons():
    if not os.path.exists(SOURCE_LOGO):
        print(f"Error: Could not find source image '{SOURCE_LOGO}'. Please place your high-res logo in the project directory.")
        return

    try:
        img = Image.open(SOURCE_LOGO)
        # التأكد من دعم الشفافية إذا كانت الصورة PNG
        img = img.convert("RGBA")
        
        for filename, size in ICON_SIZES.items():
            # استخدام أسلوب إعادة التحجيم عالي الجودة (LANCZOS)
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            resized_img.save(filename, "PNG")
            print(f"[Success] Generated: {filename} ({size[0]}x{size[1]}px)")
            
        print("\nAll application icons have been successfully generated!")
        
    except Exception as e:
        print(f"An error occurred while processing the images: {e}")

if __name__ == "__main__":
    generate_app_icons()