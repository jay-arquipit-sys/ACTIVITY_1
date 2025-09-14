from PIL import Image, ImageDraw, ImageFont

img = Image.open("coco-martin-sir-tapos-na-po.webp")

w, h = img.size

new_h = h + 80

new_img = Image.new("RGB", (w, new_h), color="white")

new_img.paste(img, (0, 80))

draw = ImageDraw.Draw(new_img)

font = ImageFont.truetype("comicbd.ttf", 25)

draw.text((10, 25), "Coco Martin reaction after he finished helping on the CCIS Booth:", font=font, fill="black")

new_img.show()