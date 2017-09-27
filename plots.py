import matplotlib.pyplot as plt
import random as r

def strikkepinne_plot():
    plt.style.use('dark_background')
    max_y = 0

    for i in range(1, 3):
        a = []
        b = []
        x = 2050
        current_x = 2050
        if i == 1:
            prev_y = 300
        else:
            prev_y = 250
        while current_x <= 2125:
            current_y = (prev_y + 1.25 * i * r.randrange(0, 2))
            prev_y = current_y
            a.append(current_x)
            b.append(current_y)
            current_x += 1
        plt.plot(a, b)
        if current_y > max_y:
            max_y = current_y

    plt.axis([x, 2125, 250, 400])
    plt.xlabel('år')
    plt.ylabel('antall meter skjerf')
    plt.title('Roberta strikkerekorder')
    plt.show(block=False)

def genaminpulering_plot():
    plt.style.use('dark_background')
    labels = 'Fornøyd', 'Ufornøyd'
    sizes = [73.9, 33.9]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show(block=False)
