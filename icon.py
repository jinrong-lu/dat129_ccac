
myicon={'row1':[1, 1, 1, 0, 1, 0, 1, 1, 1,0],
       'row2':[1, 0, 0,0,1, 0, 0, 1, 0, 0],
       'row3':[1,1,1,0,1,0,0,1,0,0],
       'row4':[0, 0 ,0,0,0,0,0,0,0,0],
       'row5':[1,0,1,1,1,0,1,1,1,0], 
       'row6':[1,0,0,0,1,0,1,0,1,0],
       'row7':[1,0,1,1,1,0,1,1,1,0],
       'row8':[1,0,1,0,0,0,0,0,1,0],
       'row9':[1,0,1,1,1,0,1,1,1,0], 
       'row10':[0,0,0,0,0,0,0,0,0,0]}
def print(myicon):
    for key in myicon:
        codeslist=myicon[key]

        for value in codeslist:
            if value==1:
                print('*', end=' ')
            else:
                print('1', end=' ')
        print('\n')
def reflection(myicon):
    for key in myicon:
        codeslist=myicon[key]
        codeslist.reverse()
        for value in codeslist:
            if value==1:
                print('1', end=' ')
            else:
                print('0', end=' ')
                
    print('\n')
                
def main(myicon):
    
    print(myicon)
    reflection(myicon)

main(myicon)
      