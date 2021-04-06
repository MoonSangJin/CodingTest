#조합,Counter
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        candidates=[]
        for menu_li in orders:
            for li in combinations(menu_li,i):
                candidates.append(''.join(sorted(li)))
        sorted_candidates=Counter(candidates).most_common()
        for menu,cnt in sorted_candidates:
            if cnt==sorted_candidates[0][1] and cnt>=2:
                answer.append(menu)
        
    answer.sort() 
    return answer