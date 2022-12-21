import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from colour import Color


def get_t_points(points,t):
    new_points = []
    for i in range(len(points)-1):
        new_points.append(get_t_point(points[i], points[i+1], t))
    return new_points

def get_t_point(point_init, point_end, t):
    #print(point_init)
    #print(point_end)
    return [t*point_end[0] + (1-t)*point_init[0], t*point_end[1] + (1-t)*point_init[1]]

def return_as_pair(P):
    #print(P)
    return P[0],P[1]

def bezier(points, num):
    x, y = [],[]
    fig, ax = plt.subplots()
    t = np.linspace(0, 1, 1000)

    temp_points = points
    for i in range(len(t)):
        while(len(temp_points) > 2):
            temp_points = get_t_points(temp_points,t)
        temp_x, temp_y = return_as_pair(get_t_point(temp_points[0],temp_points[1],t))
        x.append(temp_x)
        y.append(temp_y)

    #x,y = return_as_pair(get_t_point(points[0],points[1],t))
    ax.set_title("Bezier Curve with points " + str(points))
    ax.plot(x, y)

    x_scatter = []
    y_scatter = []
    for P in points:
        x_scatter.append(P[0])
        y_scatter.append(P[1])
    ax.scatter(x_scatter,y_scatter)
    #ax.legend()
    plt.xlim([0,20])
    plt.ylim([0,25])
    plt.show()
    #plt.savefig(str(num) + ".png")

def bezier2(points, num):
    x, y = [], []
    fix, ax = plt.subplots()

    for increment in range(num):
        points[len(points)-1][1] = points[len(points)-1][1]-.2

        t = np.linspace(0, 1, 100)
        for i in t:
            temp_points = points
            while(len(temp_points) > 2):
                temp_points = get_t_points(temp_points, i)
                #print(temp_points)
            temp_x, temp_y = return_as_pair(get_t_point(temp_points[0],temp_points[1],i))
            x.append(temp_x)
            y.append(temp_y)
        ax.set_title("Bezier Curve with points " + str(points))
        ax.plot(x, y)
    plt.show() 




if __name__ == '__main__':
    points = [[10,10], [11,12], [1,2], [2,3], [13,10], [11,15]]
    bezier2(points, 1)
    #bezier(points, i)