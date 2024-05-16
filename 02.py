from turtle import *   
import re   
import docx   
   
data = docx.Document("resources/tulipanes.docx")
coordenadas = []   
color = []
   
for i in data.paragraphs:   
    try:
        patron = r'[-+]?\d*\.\d*(?:[eE][-+]?\d+)?'
        patron_coord = r'\(' + patron + r' ?\, ?' + patron
        patron_color = patron_coord + r' ?\, ?' + patron + r'\)'

        coord_stg_tup = re.findall(patron_coord + r'\)', i.text)
        color_stg_tup = re.findall(patron_color, i.text)

        coord_num_tup = []      
        color_val = re.findall(r'[-+]?\d*\.\d*',color_stg_tup[0])   
        color_val_lst = [float(k) for k in color_val]   
        color.append(tuple(color_val_lst))   
   
        for j in coord_stg_tup:   
            coord_pos = re.findall(r'[-+]?\d*\.\d*',j)   
            coord_num_lst = [float(k) for k in coord_pos]   
            coord_num_tup.append(tuple(coord_num_lst))    
        coordenadas.append(coord_num_tup)   
    except:   
        pass   
 
pen = Turtle()   
screen = Screen()   

tracer(2)   
hideturtle()   
pen.speed(10)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

for i in range(len(coordenadas)):   
    draw = 1   
    path = coordenadas[i]   
    col = color[i]   
    pen.color(col)   
    pen.begin_fill()   
    for order_pair in path:   
        x,y = order_pair   
        y = -1*y   
        if draw:   
            pen.up()   
            pen.goto(x,y)   
            pen.down()   
            draw = 0   
        else:   
            pen.goto(x,y)   
    pen.end_fill()   
    pen.hideturtle()  
screen.mainloop() 