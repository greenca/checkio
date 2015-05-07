# We are given information about the connections in the network and the
# security level for each computer. Security level is the time (in
# minutes) that is required for the virus to capture a machine. Capture
# time is not related to the number of infected computers attacking the
# machine. Infection start from the 0th computer (which is already
# infected). Connections in the network are undirected. Security levels
# are not equal to zero (except infected).
# Information about a network is represented as a matrix NxN size, where
# N is a number of computers. If ith computer connected with jth
# computer, then matrix[i][j] == matrix[j][i] == 1, else 0. Security
# levels are placed in the main matrix diagonal, so matrix[i][i] is the
# security level for the ith computer.
# You should calculate how much time is required to capture the whole
# network in minutes.
# Input: Network information as a list of lists with integers.
# Output: The total time of taken to capture the network as an integer.
# Precondition:
# 3 <= len(matrix) <= 10
# matrix[0][0] == 0
# all(len(row) == len(matrix[0]) for row in matrix)
# all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in
# range(len(matrix)))
# all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
# all(0 <= matrix[i][j] <= 1 for i in range(len(matrix))

def capture(matrix):
    N = len(matrix)
    strengths = [matrix[i][i] for i in range(N)]
    time = 0
    while any(strength > 0 for strength in strengths):
        infected = [i for i in range(N) if strengths[i] == 0]
        targets = set([j for j in range(N) for i in infected if matrix[i][j] == 1 and strengths[j] > 0])
        for target in targets:
            strengths[target] -= 1
        time += 1
    return time


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
