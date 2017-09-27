import terminal, plots
import matplotlib.pyplot as plt

def main():
    while 1:
        try:
            valg = int(input('Hvilken robertastatistikk skal du ha? \nvelg 1, 2 eller 3: '))
        except:
            break

        if valg == 1:
            terminal.terminal(50)
            plots.strikkepinne_plot()
            terminal.terminal(100)
            terminal.waiting()
            plt.close()
        elif valg == 2:
            terminal.terminal(50)
            terminal.utregning1()
            terminal.waiting()
            plt.close()
        elif valg == 3:
            terminal.terminal(51)
            plots.genaminpulering_plot()
            terminal.waiting()
            plt.close()

main()