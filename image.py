import numpy as np
from PIL import Image


def compress_channel(channel, k):
    U, S, Vt = np.linalg.svd(channel, full_matrices=False)
    S_k = np.diag(S[:k])
    return U[:, :k] @ S_k @ Vt[:k, :]


def svd_compress_image(image_path, output_path, k=50):
    img = Image.open(image_path)
    img_np = np.array(img, dtype=np.float64)

    R, G, B = img_np[:, :, 0], img_np[:, :, 1], img_np[:, :, 2]

    R_c = compress_channel(R, k)
    G_c = compress_channel(G, k)
    B_c = compress_channel(B, k)

    img_c = np.stack([R_c, G_c, B_c], axis=2)
    img_c = np.clip(img_c, 0, 255).astype(np.uint8)

    Image.fromarray(img_c).save(output_path)
    print(f"Compressed image saved to {output_path} with k={k}")


if __name__ == "__main__":
    input_image = r"C:\Users\vishv\Downloads\images.jpeg"
    output_image = r"C:\Users\vishv\Downloads\compressed_svd.jpg"

    svd_compress_image(input_image, output_image, k=50)
