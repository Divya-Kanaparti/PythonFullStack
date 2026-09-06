class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #create empty list
        result=[]
        #to connect to first row we use top=0
        top=0
        #length of matrix is 3
        bottom=len(matrix)-1     #bottom=2
        #left represents the left-most column that we have not visited 
        left=0
        #matrix[0]->first column i.e 1,2,3
        right=len(matrix[0])-1   #right=2
        #0<=2 and 0<=2--->True
        while top<=bottom and left<=right:    #all values will be 1
            #left to right
            #col in range(0,3)-->0,1,2
            for col in range(left,right+1):
                result.append(matrix[top][col])   #1,2,3
            #now visited first row to move to second row top should be 2 so we increment
            top+=1        #top=1
            #top to bottom
            #row in range(1,3)-->1,2
            for row in range(top,bottom+1):
                #matrix[1][2]=6
                #matrix[2][2]=9
                result.append(matrix[row][right])    #1,2,3,6,9
            #now visited the col[2] so we do right-=1 i.e 0 or 1
            right-=1       #right=1
            #right to left
            #if 1<=2
            if top <= bottom:
                #col in range(1,-1,-1)  i.e col=1,0
                for col in range(right,left-1,-1):
                    #matrix[2][1]=8
                    #matrix[2][0]=7
                    result.append(matrix[bottom][col])    #1,2,3,6,9,8,7
                bottom-=1       #bottom=1
            #bottom to top
            #if 0<=1
            if left <=right:
                #for row in range(1,0,-1) i.e row=1
                for row in range(bottom,top-1,-1):
                    #matrix[1][0]=4
                    result.append(matrix[row][left])    #1,2,3,6,9,8,7,4
                left+=1    #left=0+1=>1
            #goes above again to while loop
            #top,bottom,left,right=1
        return result

        