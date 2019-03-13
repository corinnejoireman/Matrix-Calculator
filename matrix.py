def main():
    rows = int(input("How many rows does your matrix have? "))
    cols = int(input("How many columns does your matrix have? "))

    matrix = []

    for i in range(rows):
        lyst = []
        for j in range(cols):
            val = eval(input("Enter the value of your matrix at row "+ str(i + 1) + " and column " + str(j +1)+ ": ")) 
            lyst.append(val)
        matrix.append(lyst)

    print(displayMatrix(matrix))
    
    #creates a matrix with ones on the diagonal
    for row in range(rows):
        #check if (1,1) contains a 1, if not reduce the row
        if matrix[row][row] != 1 and matrix[row][row] != 0:
            for col in range((row), cols):
                matrix[row][col] = matrix[row][col]/matrix[row][row]
            #use this row to subtract from the other rows
        for nextRow in range((row + 1), rows):
            if matrix[nextRow][row] != 0:
                newLyst = []
                for i in range(cols):
                    newLyst.append(matrix[row][i] * matrix[nextRow][row])
                for i in range(cols):
                    matrix[nextRow][i] -= newLyst[i]
    
    print(displayMatrix(matrix))
            
def displayMatrix(matrix):
    string = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            string += str(matrix[i][j])
            string += "  "
        string += "\n"
    return string

main()
