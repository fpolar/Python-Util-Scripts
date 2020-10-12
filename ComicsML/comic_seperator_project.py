from PIL import Image
import random

img = Image.open('speech-bubbles.png', 'r')
img_w = img.size[0]//2
img_h = img.size[1]//2
page_sizes = [(1375, 920), (1145, 800)]
page_bg_colors = [(255, 255, 255, 255), (122, 122, 122, 255), (0, 0, 0, 255)]
build_order = -1 #manga style or western style
min_frame_dim = 15
max_frame_dim = 50

for i in range (1,10):
    page_size = random.randint(0,1)
    page_bg_color = random.randint(0,2)
    background = Image.new('RGBA', page_sizes[page_size], page_bg_colors[page_bg_color])
    bg_w, bg_h = background.size
    page_padding = random.randint(0,20)

    x_offset = page_padding
    y_offset = page_padding
    while x_offset < 100 - page_padding:
        panel_width = random.randint(min_frame_dim,max_frame_dim)
        x_px_offset = int(bg_w*(x_offset/100))
        panel = img.resize((int(panel_width/100*bg_w), int(panel_width/100*bg_w)))
        panel_offset = (x_px_offset, x_px_offset)
        panel_margin = random.randint(0,10)
        print(x_offset, panel_width, panel_margin)
        background.paste(panel, panel_offset)
        x_offset = min(x_offset + panel_width + panel_margin, bg_w - page_padding)

    # background.paste(img, offset)
    background.save('training_'+str(i)+'.png')