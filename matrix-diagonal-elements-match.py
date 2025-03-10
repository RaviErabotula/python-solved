#Q: https://datalemur.com/questions/python-same-stripes



def is_same_stripes(matrix):
    diagonal_groups = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diagonal_key = i - j

            if diagonal_key in diagonal_groups:
                if matrix[i][j] != diagonal_groups[diagonal_key][0]:
                    return False
                diagonal_groups[diagonal_key].append(matrix[i][j])
            else:
                diagonal_groups[diagonal_key] = [matrix[i][j]]

    return True
