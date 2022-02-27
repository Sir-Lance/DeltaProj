from PIL import Image

def join_vertical(top, bot):
    new_image = Image.new('RGB', (1200, 600), (250, 250, 250))
    new_image.paste(top, (0, 0))
    new_image.paste(bot, (0, 300))
    return new_image