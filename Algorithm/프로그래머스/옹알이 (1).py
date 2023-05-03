def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for bab in babbling:
        for w in words:
            if (bab == w * 2):
                continue
            if w in bab:
                bab = bab.replace(w, ' ')
        if (bab.strip() == ''):
            cnt += 1
    return cnt
