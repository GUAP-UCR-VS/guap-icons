items = []

with open('style.css', 'r', encoding='utf8') as f1:
    for s1 in f1:
        if s1.startswith('.gi-'):
            s2 = s1.split(':', 1)[0][1:]
        if s1.startswith('  content:'):
            items.append(s2 + '=' + s1.split('"')[1][1:])

with open('icons.txt', 'w', encoding='utf8') as f1:
    for s1 in items:
        f1.write(f'"{s1}",\n')
