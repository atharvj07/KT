a = sorted([input() for i in range(int(input()))], key=lambda x: len(x))
print('YES\n' + '\n'.join(a) if all([a[i] in a[i + 1] for i in range(len(a) - 1)]) else 'NO')
