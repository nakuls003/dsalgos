def get_lps(pattern):
    i, j, lps = 0, 1, [0]
    while j < len(pattern):
        if pattern[j] == pattern[i]:
            lps.append(i+1)
            i += 1
            j += 1
        else:
            if i > 0:
                i = lps[i-1]
            else:
                lps.append(0)
                j += 1
    return lps



def kmp(text, pattern):
    lps = get_lps(pattern)
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1


if __name__ == '__main__':
    text = "babaaaabbbbbabbaababbaaabbabaaaabaaaabbaabaabababaabbaabbaaaaababba"
    pattern = "bbaa"
    print(kmp(text, pattern))