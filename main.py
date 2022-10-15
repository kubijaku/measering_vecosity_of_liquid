# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

pi = 3.14
g = 9.80
def ni_calculator(masa, srednica, czas_sredni, objetosc):
    D = 0.039
    l = 0.69
    t = 22
    ro = 1249.36

    all_ni = []
    for i in range(6):
        wynik = ( (masa[i] - ( ( pi * ro * math.pow(srednica[i],3) ) / 6 ) ) * g * czas_sredni[i] ) / ( 3 * pi * l * srednica[i] * ( 1 + (srednica[i] * 2.4 / D ) ) )
        all_ni.append(wynik)
    print(all_ni)




def obj(srednica):
    obj = []
    for d in srednica:
        wynik = 1/6*pi*math.pow(d,3)
        obj.append(wynik)

    return obj


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    srednica = [0.004, 0.00316, 0.003, 0.00399, 0.00399, 0.00299]
    masa = [ 0.000268, 0.000132, 0.000114, 0.000268, 0.000269, 0.000114]
    czas_sr = [4.98, 7.41, 7.76, 4.89, 4.92, 7.73]
    objetosc = obj(srednica)
    ni_calculator(masa,srednica,czas_sr,objetosc)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
