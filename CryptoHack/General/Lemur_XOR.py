from PIL import Image 

img1 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")
img2 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")

img1 = img1.convert("RGB")
img2 = img2.convert("RGB")

pix1 = list(img1.getdata())
pix2 = list(img2.getdata())


# sau khi chuyển hai ảnh sang RGB và lấy dữ liệu thì ta tiến hành so từng pixel
result = []
for p1, p2 in zip(pix1, pix2):
    r = p1[0] ^ p2[0]
    g = p1[1] ^ p2[1]
    b = p1[2] ^ p2[2]
    result.append((r, b, g))

# tạo và lưu dãy kết quả thành ảnh mới
rs_img = Image.new("RGB", img1.size)
rs_img.putdata(result)
rs_img.save("flag.png")
