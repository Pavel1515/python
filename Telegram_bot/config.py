TOKEN ="5366249644:AAFyr5UH6BL1L7MtfJDSVSLVJ6p3NzKAELs"
api_keys = "468ae2bc7698a8d423312d275f613869"

def character_exclusion(c):
    list_not  = ["{","}","[","]","'"," "]
    for i in list_not:
        c = c.replace( i , '')
    c =c.split(",")
    lat = c[-3][4:]
    lon = c[-4][4:]
    return lon ,lat 
