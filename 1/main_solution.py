def solution(text, ending):
    return text[0-len(ending):len(text)] == ending
