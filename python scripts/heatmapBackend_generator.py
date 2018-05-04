import heatmap
from PIL import Image


def save_map_memory(Ultralist):
    file = open('mapmem.txt',"a")
    for coord in Ultralist:
        x,y = coord
        x=str(x)
        y=str(y)
        file.write(x+","+y+"\n")
    file.close()

def get_map_mem():
    UltraList_data=[]
    with open('mapmem.txt') as f:
        data = f.readlines()
    for line in data:
        x,y =line.split(',')
        x = int(x)
        y = int(y)
        UltraList_data.append((x,y))
    return UltraList_data


def heatmapper(UltraList):
    save_map_memory(UltraList)
    UltraList = get_map_mem()
    hm = heatmap.Heatmap()
    img = hm.heatmap(UltraList,area=((0, 0), (1280,720)),size=(1280,720),dotsize=50)
    print("heatmap created")
    overlay = img
    # background = Image.new("RGBA", (1280, 720), "black")
    overlay = overlay.convert("RGBA")
    #
    # Image.alpha_composite(background, overlay).save("Current_Map"+".png","PNG")
    overlay.save("Current_Map"+".png","PNG")
    print("overlay comepleted")
