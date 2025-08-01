import json
from rapidfuzz import fuzz

def testing_obl(nado):
    if nado == 'None':
        return 'None'
    with open('array.json', 'r', encoding='utf-8') as json_file:
        array = json.load(json_file)

    best_score = 0
    best_key = None


    for key, values in array.items():
        values = [key] + values
        for value in values:
            score = fuzz.WRatio(nado, value)
            if score > best_score:
                best_score = score
                best_key = key


    if best_score == 100.0:
        return best_key
    elif best_score >= 80:
        array[best_key].append(nado)
    else:
        array['Неизвестно'].append(nado)
        with open('array.json', 'w', encoding='utf-8') as f:
            json.dump(array, f, ensure_ascii=False, indent=4)
        return nado

    with open('array.json', 'w', encoding='utf-8') as f:
        json.dump(array, f, ensure_ascii=False, indent=4)
    return best_key