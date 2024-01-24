import cv2

#membaca gambar
img = cv2.imread('fajri.jpg')
#menampilkan gambar
cv2.imshow("fajri",img)
#menyimpan gambar
cv2.imwrite("save_fajri.jpg",img)

#menunda windows terdeksteroy
cv2.waitKey(0)
cv2.deatroyAllWindows() 
#mendestroy windows