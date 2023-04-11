class Row:
    def __init__(self, seats):
        self.seats = seats
        self.taken = None
        self.side = None

    def take(self, number, side, place):
        if side == 'right':
            seats = {'D', 'E', 'F'}
        else:
            seats = {'A', 'B', 'C'}
        if number == 2:
            if place != 'window':
                seats -= {'A', 'F'}
            else:
                seats -= {'C', 'D'}
        elif number == 1:
            if place != 'window':
                seats -= {'A', 'F', 'B', 'E'}
            else:
                seats -= {'C', 'D', 'B', 'E'}
        for seat in seats:
            if self.seats[side][seat] != '.':
                return False
        self.taken = seats
        self.side = side
        for seat in seats:
            self.seats[side][seat] = 'X'
        return True

    def __str__(self):
        return ''.join(self.seats['left'].values()) + '_' + ''.join(self.seats['right'].values())

    def recently_taken(self, index):
        return f"Passengers can take seats: {' '.join([str(index) + s for s in sorted(self.taken)])}"

    def remove_x(self):
        if self.taken and self.side:
            for seat in self.taken:
                self.seats[self.side][seat] = '#'
            self.taken = None
            self.side = None


n = int(input())
rows = []
i = 0
while i < n:
    left, right = input().split('_')
    rows.append(Row({
        'left': {'A': left[0], 'B': left[1], 'C': left[2]},
        'right': {'D': right[0], 'E': right[1], 'F': right[2]}
    }))
    i += 1
m = int(input())
i = 0
groups = []
while i < m:
    flag = True
    params = input().split()
    for idx, r in enumerate(rows):
        if r.take(int(params[0]), params[1], params[2]):
            print(r.recently_taken(idx + 1))
            for row in rows:
                print(row)
            r.remove_x()
            flag = False
            break
    if flag:
        print('Cannot fulfill passengers requirements')
    i += 1
