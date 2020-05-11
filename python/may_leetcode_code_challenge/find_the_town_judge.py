# diction [person, [who they trust]]
# find what person is not in someone who trusts others
# record the data
# find out if that person is trusted by others
# find out who is not in the record
# check if they are trusted


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # # diction [person, [who they trust]]
        # who_trust = dict()
        # unq_persons = set()
        # # find what person is not in someone who trusts others
        #     # record the data
        # for t in trust:
        #     set.add(t[0])
        #     if t[0] not in who_trust:
        #         who_trust[t] = [t[1]]
        #     else:
        #         who_trust[t].append(t[1])
        # for
        # # find out if that person is trusted by others
        #     # find out who is not in the record
        #     # check if they are trusted
        if len(trust) < N - 1:
            return -1

        trust_scores = [0] * (N+1)

        for out_, in_ in trust:
            trust_scores[out_] -= 1
            trust_scores[in_] += 1

        for i, score in enumerate(trust_scores[1:], 1):
            if score == N - 1:
                return i
        return -1


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1

        trust_scores = [0] * (N+1)

        for out_, in_ in trust:
            trust_scores[out_] -= 1
            trust_scores[in_] += 1

        for i, score in enumerate(trust_scores[1:], 1):
            if score == N - 1:
                return i
        return -1
