from sklearn.svm import LinearSVC
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [1, 0, 1]
cachorro2 = [1, 1, 1]
cachorro3 = [0, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0]

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
