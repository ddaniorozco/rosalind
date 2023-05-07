from Bio.Align import substitution_matrices as subst_mat


def global_alignment(s, t, matrix):

    gap_penalty = -5

    n, m = len(s), len(t)
    score = [[0] * (m + 1) for _ in range(n + 1)]
    traceback = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        score[i][0] = gap_penalty * i
    for j in range(1, m + 1):
        score[0][j] = gap_penalty * j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = matrix.get((s[i - 1], t[j - 1]), matrix.get(("*", "*")))
            diagonal_score = score[i - 1][j - 1] + match_score
            up_score = score[i - 1][j] + gap_penalty
            left_score = score[i][j - 1] + gap_penalty
            score[i][j] = max(diagonal_score, up_score, left_score)
            if score[i][j] == diagonal_score:
                traceback[i][j] = 1
            elif score[i][j] == up_score:
                traceback[i][j] = 2
            else:
                traceback[i][j] = 3

    align_s, align_t = "", ""
    i, j = n, m
    while i > 0 or j > 0:
        if traceback[i][j] == 1:
            align_s = s[i - 1] + align_s
            align_t = t[j - 1] + align_t
            i -= 1
            j -= 1
        elif traceback[i][j] == 2:
            align_s = s[i - 1] + align_s
            i -= 1
        else:
            align_t = t[j - 1] + align_t
            j -= 1

    alignment_score = int(score[n][m])

    print(alignment_score)


blosum_matrix = subst_mat.load("BLOSUM62")
sequence_1 = "PLEASANTLY"
sequence_2 = "MEANLY"

global_alignment(sequence_1, sequence_2, blosum_matrix)
