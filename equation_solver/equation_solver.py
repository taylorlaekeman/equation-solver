def solve(e):
    if '*' in e:
        l = e.split('*')[0]
        r = e.split('*')[1]
        l = int(l)
        r = int(r)
        return l * r
    elif '/' in e:
        l = e.split('/')[0]
        r = e.split('/')[1]
        l = int(l)
        r = int(r)
        return l / r
    elif '+' in e:
        l = e.split('+')[0]
        r = e.split('+')[1]
        l = int(l)
        r = int(r)
        return l + r
    else:
        l = e.split('-')[0]
        r = e.split('-')[1]
        l = int(l)
        r = int(r)
        return l - r
