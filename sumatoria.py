def sumatoria_cubica(n):
    suma = 0
    for i in range (1 ,n + 1):
        for j in range (1 ,i + 1):
            for k in range (j ,1+i+j):
                suma = suma + 1
    return suma
    raise NotImplementedError()
    
def sumatoria_constante(n):
    i = (n+1)*n
    suma = int (((n + 2)/ 3)*i)
    return suma  
    raise NotImplementedError()
