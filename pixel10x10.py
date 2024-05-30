from PIL import Image
import os
# Fungsi untuk memotong gambar menjadi 10px x 10px dan menampilkan nilai pikselnya
def crop_image(input_image_path, output_dir, crop_size=(10, 10)):
    try:
        # Membuka gambar
        img = Image.open(input_image_path)
        # Mendapatkan ukuran gambar
        width, height = img.size
        # Memastikan ukuran gambar minimal sebesar crop_size
        if width < crop_size[0] or height < crop_size[1]:
            raise ValueError("Gambar terlalu kecil untuk dipotong menjadi ukuran 10px x 10px")
        # Mendefinisikan koordinat kotak crop (crop box)
        left = 0
        top = 0
        right = crop_size[0]
        bottom = crop_size[1]
        # Memotong gambar
        cropped_img = img.crop((left, top, right, bottom))
        # Memastikan direktori output ada
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # Menyimpan gambar yang sudah dipotong
        output_image_path = os.path.join(output_dir, "cropped_image.bmp")
        cropped_img.save(output_image_path)
        print(f"Gambar berhasil dipotong dan disimpan sebagai {output_image_path}")
        # Mendapatkan nilai piksel dan menampilkannya
        cropped_pixels = list(cropped_img.getdata())
        cropped_pixels = [cropped_pixels[i * crop_size[0]:(i + 1) * crop_size[0]] for i in range(crop_size[1])]
        print("Nilai piksel dari gambar yang dipotong:")
        for row in cropped_pixels:
            print(row)
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
# Menggunakan fungsi crop_image
input_image_path = r"D:\Semester 4\Pengolahan Citra\kemejagw_gray.jpg"
output_dir = r"D:\Semester 4\Pengolahan Citra"

crop_image(input_image_path, output_dir)
