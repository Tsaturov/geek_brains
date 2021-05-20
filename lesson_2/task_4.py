raw_text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
positions = []

for idx in raw_text:
    positions.append(idx.title().split())

for name in positions:
    print('Привет,', name.pop(), '!')