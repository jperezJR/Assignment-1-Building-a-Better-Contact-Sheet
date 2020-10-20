import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont


def CalcItensity(simage):
    images = []
    intensity = [0.1, 0.5, 0.9]
    Channels = (0, 1, 2)
    for channel in Channels:
        for i in intensity:
            info = "channel {} intensity {}".format(channel, i)
            ch = simage[channel].point(lambda px: px * i)
            if channel == 0:
                out = Image.merge('RGB', (ch, simage[1], simage[2]))
            elif channel == 1:
                out = Image.merge('RGB', (simage[0], ch, simage[2]))
            elif channel == 2:
                out = Image.merge('RGB', (simage[0], simage[1], ch))
            
            WriteTxt(out, channel, i)
            images.append(out)
    return images       
            


def WriteTxt(image, channel, i):
    out = image
    info = "channel {} intensity {}".format(channel, i)
    drawing_object=ImageDraw.Draw(out)
    drawing_object.text((0, back.height-70), info , font = webfont, fill = out.getpixel((0, 50)))
    


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

#black background --> same width but 90 pixels bigger in height
back = Image.new('RGB', (image.width, int(image.height + 75)))

#Paste Michingan pic to background
back.paste(image)

#Load the Font
webfont = ImageFont.truetype("readonly/fanwood-webfont.ttf", 75)

#split image into bands R, G and B
simage = back.split()



images = CalcItensity(simage)



# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width


## resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)