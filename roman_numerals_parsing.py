romans = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)

def parse_roman(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1<len(roman) and romans[roman[c]] < romans[roman[i+1]]:
            result-=romans[roman[c]]
        else:
            result+=romans[roman[c]]
        return result