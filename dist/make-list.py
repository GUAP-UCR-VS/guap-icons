items = []

with open('style.css', 'r', encoding='utf8') as f1:
    for s1 in f1:
        if s1.startswith('.gi-'):
            s2 = s1.split(':', 1)[0][1:]
        if s1.startswith('  content:'):
            s3 = s1.split('"')[1][1:]
            items.append(f'"{s2}": "{s3}"')

with open('guap-icons.json', 'w', encoding='utf8') as f1:
    f1.write('{\n')
    for s1 in items:
        f1.write(f'{s1},\n')
    f1.write('}\n')
