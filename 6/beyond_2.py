def transpose_strings(list_of_strings):

    word_matrix = [s.split() for s in list_of_strings]
    number_of_columns = len(word_matrix[0])
    output = []
    for i in range(number_of_columns):
        column_words = []
        for row in word_matrix:
            column_words.append(row[i])
            
        output.append(" ".join(column_words))
        
    return output


data = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
print(transpose_strings(data))

