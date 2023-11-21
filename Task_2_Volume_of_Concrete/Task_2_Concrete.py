L = float(input ("Введите длину фундамента по наружной грани в метрах: "))
B = float(input ("Введите ширину фундамента по наружной грани в метрах: "))
b = float(input ('Введите ширину ленты в метрах: '))
t = float(input('Введите толщину ленты в метрах: '))
A = L*B-(L-b)*(B-b) #calculate the area of the upper concrete surface
V1 = 5 #volume of one concrete car
V = A*t #volume of the concrete
n = int(V/V1)+1+1
print(f'Для заливки фунадмента требуеся {n} пятикубовых миксеров')