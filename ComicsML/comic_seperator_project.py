from PIL import Image
import random
import json

img = Image.open('./building_blocks/speech-bubbles.png', 'r')
img_w = img.size[0]//2
img_h = img.size[1]//2
page_sizes = [(920, 1375), (800, 1145)]
page_bg_colors = [(255, 255, 255, 255), (122, 122, 122, 255), (0, 0, 0, 255)]
build_order = -1 #manga style or western style orders
min_frame_dim = 15
max_frame_dim = 50

for i in range (1,10):
    #Page feature generation
    page_size = random.randint(0,1)
    page_bg_color = random.randint(0,2)
    background = Image.new('RGBA', page_sizes[page_size], page_bg_colors[page_bg_color])
    bg_w, bg_h = background.size
    page_padding = random.randint(0,20)

    #Page metadata init
    metadata = {}
    metadata['page_id'] = i
    metadata['page_size'] = page_size
    metadata['page_padding'] = page_padding

    panel_idx = 1
    x_offset = page_padding
    y_offset = page_padding
    while x_offset < 100 - page_padding:
        panel_width = random.randint(min_frame_dim,max_frame_dim)
        x_px_offset = int(bg_w*(x_offset/100))
        panel = img.resize((int(panel_width/100*bg_w), int(panel_width/100*bg_w)))
        panel_offset = (x_px_offset, x_px_offset)
        panel_margin = random.randint(0,10)

        #Page metadata
        panel_metadata = {}
        panel_metadata['id'] = panel_idx
        panel_metadata['size'] = panel_width
        panel_metadata['position'] = x_offset
        metadata['panel_id_'+str(panel_idx)] = panel_metadata
        panel_idx = panel_idx + 1

        background.paste(panel, panel_offset)
        x_offset = min(x_offset + panel_width + panel_margin, bg_w - page_padding)

    background.save('./training/training_'+str(i)+'.png')
    with open('./training/training_'+str(i)+'.json', 'w') as outfile:
        json.dump(metadata, outfile)