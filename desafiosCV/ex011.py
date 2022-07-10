qt_altura_parede = float(input("Qual a altura da parede? "))
qt_largura_parede = float(input("Qual a largura da parede? "))
qt_metros_area_parede = qt_altura_parede * qt_largura_parede
qt_latas_necessarias = qt_metros_area_parede / 2
print("Uma parede de {}m x {}m tem uma área de {:.2f}m².".format(qt_altura_parede, qt_largura_parede, qt_metros_area_parede))
print("Serão necessárias {:.2f} lata(s) de tinta para pintá-la.".format(qt_latas_necessarias))