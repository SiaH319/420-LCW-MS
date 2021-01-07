'''
Sia Ham, 17308123
Tuesday, March 19
R. Vincent, instructor
Assignment 3 - Exercise 1
'''

from bfs import bfs, pathTo #import bfs, pathTo, digraph, graph from the given files
from graph import digraph, graph


while True:
    fp = (input("Enter a file name (*no need to provide a folder name) and enter 'E' to exit:")) #prompt the user to enter a file name

    if fp!= 'E': #as long as fp is not 'E'
        file = open('J5//' + fp) # read the input file

        v = int(file.readline().strip('\n')) # number of vertices of each file (vertex value = page # i.e) vertex value 2 = page number 2)
        graph = digraph (v+1)   #create digraph object 

        n_pages = [] #initial(empty) list of next pages
        while True: # keep reading
            line = file.readline()
            if not line: break
            line=line.strip('\n') # remove EOLine
            data = line.split( )
            n_pages.append(data) #add each line (next pages # and Mi value(#of next pages)) in a matrix

        end = [] #initial(empty) list of ending pages
        for i in range (v): # for each vertex value (= page number)
            Mi = int(n_pages[i][0])
            if Mi == 0: #when there is no next page (Mi = 0), it is an ending page
                end.append (i+1) #append the ending page number 
            for n in range (1,Mi+1): #exclude Mi value 
                w = int(n_pages [i][n]) #append the next page #
                graph.addEdge(i+1, w) #Add edge from i+1 to w 

        s = 1    #always starting from page 1 (= vertex 1)
        distance, edge = bfs (graph,s) 
            # distance = lists containing the distance
            # edge = lists containing edges (shortest path tree) to each other vertex

            
        '''check reachaility'''
        def reachability(distance):
            distance.pop(0) #remove the possibility to go to page 0
            if -1 in distance: #if the list distance includes -1, there is at least one non-reachable page (returns to ' N')
                return ' N' 
            else:
                return ' Y' #returns to 'Y' if all of the pages reachable from the first page
            
        reach = reachability (distance)



        paths = [] #initial list of path
        for i in end: #for every ending page
             paths.append( pathTo (edge, s, i))     #append the shortest path from 's' (starting page = page 1) to 'i' (ending page)

        LP = [] #initial(empty) list of the length of the path
        for s in paths:
            if s != None: #as long as s in not None
                k = len (s) # length of the path 
                LP.append(k) #append the length of the path
                
        '''find the shortest path'''
        STP = str (min(LP)) #length of the shortest path

        print (reach,'\n',STP, '\n')
        
    else: # if use enter 'E' exit the program 
        print ('Exit')
        break
