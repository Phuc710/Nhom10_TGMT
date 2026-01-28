import cv2 as cv
import numpy as np
import urllib.request

def read_img_url(url):
    resp = urllib.request.urlopen(url)
    img_bytes = np.asarray(bytearray(resp.read()), dtype=np.uint8)
    img = cv.imdecode(img_bytes, cv.IMREAD_COLOR)
    return img
def add_noise(img):
    mean = 0
    sigma = 30
    gauss = np.random.normal(mean, sigma, img.shape).astype(np.uint8)
    noisy_img = cv.add(img, gauss)
    return noisy_img

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
    img = read_img_url(url)

    cv.imshow("Image 1", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    noisy_img = add_noise(img)
    cv.imshow("Noisy Image", noisy_img)
    cv.waitKey(0)
    cv.destroyAllWindows()