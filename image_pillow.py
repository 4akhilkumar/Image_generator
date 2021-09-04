from PIL import Image, ImageDraw, ImageFont
import os
import random
 
fn = "Sai Akhil Kumar Reddy"
ln = "Nallamilli"

# my_color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
colors = ['#9FA8A3', '#173E43', '#3FB0AC', '#431C5D', 
          '#F53163', '#ec407a', '#5e35b1', '#3f51b5', 
          '#1e88e5', '#795548', '#546e7a', '#f57c00']
my_color1 = random.choice(colors)

filename= fn[0]+ln[0]+'.webp'
text= "  "+ fn[0] +" "
size = 50
fnt = ImageFont.truetype('arial.ttf', size)
# create image
image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = "".join(my_color1))
draw = ImageDraw.Draw(image)
# draw text
draw.text((5, 20), text, font=fnt, fill="white")
# save file
image.save('sample/{}'.format(filename), 'webp')

# show file
# os.system("start " + "sample/"+filename)