'''
Sia Ham, 17308123
Tuesday, February 5
R. Vincent, instructor
Assignment 1 - Exercise 1
'''


def draw_line(x0, y0, x1, y1, color):
    '''Draw a line connecting two points, given integer coordinates for the
    start position (x0, y0) and end position (x1, y1). The color is a string, 
    either a color name (e.g. 'red') or an RGB value '#RRGGBB'.'''
    canvas.create_line(x0, y0, x1, y1, width=1, fill=color)

def draw_star(x, y, radius, color):
    '''Draw a star as a filled circle with a given center (in pixel
    coordinates), radius (in pixels), and color (as above).'''
    if radius < 1:
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill=color, width=1)
    else:
        canvas.create_oval(x - radius,
                           y - radius,
                           x + radius,
                           y + radius,fill=color, width=0)

# BASIC TKINTER INITIALIZATION

import tkinter as tk
SIZE = 1000
wnd = tk.Tk()
canvas = tk.Canvas(wnd, width=SIZE, height=SIZE, background='black')
canvas.pack()
wnd.title('Star chart')

# YOUR MAIN PROGRAM GOES HERE

def name_match(key,names): #This is mainly for the function plot_constellation
    '''for standardization the name of the star, convert to the Henry Draper number
        names - dictionary returned by read_coords'''
    i = names.get(key)
    if i: 
        return i #returns to the value of the given key
    return key #returns to the Draper number

def coords_to_pixel (star_x, star_y, SIZE=1000):
    '''Translate coordinates:
    convert the given coords to the location of the star in terms of pixels in the picture in a form of tuple'''
    pixel_x = (star_x + 1)*SIZE/2
    pixel_y = SIZE - (star_y + 1)*SIZE/2
    return (pixel_x, pixel_y)

d1 = {}
d2 = {}
d3 = {}
def read_coords(file):
    ''' Read coordinates: return to the three following dictionaries:
        d1 - dictionary keyed on the Henry Draper number with the values as tuples containing the x and y coordinates of each star.
        d2 - dictionary keyed on the Henry Draper numbers witth the value as the magnitudes (float) of the stars.
        d3 - dictionary keyed on the standardized names of the stars with the values as the Henry Draper numbers
    '''
    for line in file:
        line = line.split( ) #splits each line of the file
        star_x, star_y = coords_to_pixel(float(line[3]), float(line[2])) #convert to the location of the star in terms of pixel
        d1[line[1]] = star_x, star_y #dictionary 1 with value as a x,y coordinates i.e {Draper #: x,y }
        d2[line[1]] = line[4] #dictionary 2 with values as magnitudes i.e {Draper #: mag}

        if len(line) > 5: #if the star has at least one name
            stars = line[5].strip('\n').split(',') #remove EOL
            for s in stars:
                s_stand = s.upper().replace('_',' ') #standardize the name of the star 
                d3[s_stand] = line[1] # values as the Hnery Draper numbers i.e. {name: Draper #}
    return d1,d2,d3 


from math import log #this is only for the function plot_by_magnitude
def plot_by_magnitude (SIZE, coords, magnitudes):
    '''
    Plot stars: plot all of the stars in the dictionaries
    '''
    for key in coords.keys(): #coords -  a dictionary returned by read_coords
        x =float(coords[key][0])
        y = float(coords[key][1])
        radius = log(8-float(magnitudes[key])) #the smaller the magnitude, the brighter the star
        draw_star(x, y, radius, color = 'white')

def read_constellation_lines(file):
    '''
    Read constellations:
    return as a dictionary keyed on the source star + with value of a list of destination star
    '''
    lines ={} # initial empty dictionary
    for line in file:
        src,dst = line.split(',') #split the line into the source & destination
        dst = dst.strip() #strip an empty space for the function name_match  
        if src not in lines: #avoid overlapping of src
            lines[src]=[] 
        lines[src].append(dst) 
    return lines # a dictionary i.e. {scr: [dst1, dst2]} 

def plot_constellation (coords, lines, names, color = 'white' , SIZE=1000):
    '''
    Draw constellations: 
    coords - dictionary returned by read_coords 
    names - dictionary returned by read_coords 
    lines - dictionary returned by read_constellation_lines 
    '''
    for src in lines.keys(): #source star
        start_line = lines[src]
        src = name_match (src,names)
        x0, y0 = coords[src][0], coords[src][1] #x,y coordinates of each source star
        for dst in start_line:
            dst = name_match(dst,names)
            x1,y1  = coords[dst][0], coords[dst][1] #x,y coordinates of each destination star
            draw_line(x0, y0, x1, y1, color="white")

fp = open('stars.txt')
coords, magnitudes, names = read_coords(fp)
fp.close()
plot_by_magnitude(SIZE, coords, magnitudes)
constellation_files=['Auriga_lines.txt', 'BigDipper_lines.txt', 'Bootes_lines.txt','Cas_lines.txt',
                     'Cepheus_lines.txt','Cyg_lines.txt','Draco_lines.txt','UrsaMinor_lines.txt']
for fname in constellation_files:
    fp = open(fname)
    lines = read_constellation_lines(fp)
    fp.close()
    plot_constellation(coords, lines, names, color = "white", SIZE=1000)

# DO NOT DELETE THIS LINE!
wnd.mainloop()
