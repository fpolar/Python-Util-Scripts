from PIL import Image
import random
import json

sq_img = Image.open('./building_blocks/sq.png', 'r')
sp_img = Image.open('./building_blocks/speech-bubble.png', 'r')
page_sizes = [(920, 1375), (800, 1145)]
page_bg_colors = [(255, 255, 255, 255), (122, 122, 122, 255), (0, 0, 0, 255)]
build_order = -1 #manga style or western style orders
min_frame_dim = 15
max_frame_dim = 50
min_speech_dim = min_frame_dim/5

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
    y_offset = page_padding
    while y_offset < 100 - page_padding:
        x_offset = page_padding
        panel_height = random.randint(min_frame_dim,max_frame_dim)
        y_px_offset = int(bg_h*(y_offset/100))
        panel_margin = random.randint(0,10)
        new_y_offset = y_offset + panel_height + panel_margin

        while x_offset < 100 - page_padding:
            panel_width = random.randint(min_frame_dim,max_frame_dim)
            x_px_offset = int(bg_w*(x_offset/100))
            panel = sq_img.resize((int(panel_width/100*bg_w), int(panel_height/100*bg_h)))
            panel_offset = (x_px_offset, y_px_offset)

            #Panel metadata
            panel_metadata = {}
            panel_metadata['id'] = panel_idx
            panel_metadata['height'] = panel_height
            panel_metadata['width'] = panel_width
            panel_metadata['y_position'] = y_offset
            panel_metadata['x_position'] = x_offset
            panel_idx = panel_idx + 1

            background.paste(panel, panel_offset)

            new_x_offset = x_offset + panel_width + panel_margin

            #speech bubble insertion
            speech_idx = 1;
            speech_y_offset = y_offset
            while speech_y_offset < new_y_offset - min_speech_dim:
                speech_x_offset = x_offset
                speech_height = random.randint(min_speech_dim, new_y_offset-speech_y_offset)
                speech_y_px_offset = int(bg_h*(speech_y_offset/100))
                while speech_x_offset < new_x_offset - min_speech_dim:
                    speech_width = random.randint(min_speech_dim,new_x_offset-speech_x_offset)
                    speech_x_px_offset = int(bg_w*(speech_x_offset/100))
                    speech = sp_img.resize((int(speech_width/100*bg_w), int(speech_height/100*bg_h)))
                    speech_offset = (speech_x_px_offset, speech_y_px_offset)
                    
                    #bubble metadata
                    speech_metadata = {}
                    speech_metadata['id'] = speech_idx
                    speech_metadata['height'] = speech_height
                    speech_metadata['width'] = speech_width
                    speech_metadata['y_position'] = speech_y_offset
                    speech_metadata['x_position'] = speech_x_offset
                    speech_idx = speech_idx + 1
                    background.paste(speech, speech_offset)
                    panel_metadata['speech_id_'+str(speech_idx)] = speech_metadata

                    speech_x_offset = speech_x_offset + speech_width + random.randint(0,new_x_offset-speech_x_offset)

                speech_y_offset = speech_y_offset + speech_height + random.randint(0,new_y_offset-speech_y_offset)
            #save metadata
            metadata['panel_id_'+str(panel_idx)] = panel_metadata
            x_offset = min(new_x_offset, 100 - page_padding)

        print(new_y_offset)
        y_offset = min(new_y_offset, 100 - page_padding)

    background.save('./training/training_'+str(i)+'.png')
    with open('./training/training_'+str(i)+'.json', 'w') as outfile:
        json.dump(metadata, outfile, indent=4, sort_keys=True)