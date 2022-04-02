import numpy as np

def trilateration(P1, P2, P3, distances):
  
  r1 = distances[0]
  r2 = distances[1]
  r3 = distances[2]

  p1 = np.array([0, 0, 0])
  p2 = np.array([P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]])
  p3 = np.array([P3[0] - P1[0], P3[1] - P1[1], P3[2] - P1[2]])
  v1 = p2 - p1
  v2 = p3 - p1

  Xn = (v1)/np.linalg.norm(v1)

  tmp = np.cross(v1, v2)

  Zn = (tmp)/np.linalg.norm(tmp)

  Yn = np.cross(Xn, Zn)

  i = np.dot(Xn, v2)
  d = np.dot(Xn, v1)
  j = np.dot(Yn, v2)

  X = ((r1**2)-(r2**2)+(d**2))/(2*d)
  Y = (((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(X))
  Z1 = np.sqrt(max(0, r1**2-X**2-Y**2))
  Z2 = -Z1

  K1 = P1 + X * Xn + Y * Yn + Z1 * Zn
  K2 = P1 + X * Xn + Y * Yn + Z2 * Zn
    
  return K1,K2

def trilateration2(P1, P2, P3, distances):
  P1 = np.array(P1)        # Almacenamos las coordenadas de cada transmidor
  P2 = np.array(P2)
  P3 = np.array(P3)
  ex = (P2 - P1)/(np.linalg.norm(P2 - P1))  # Formulas para resolver las ecuaciones de los circulos
  i = np.dot(ex, P3 - P1)                   # utilizando algebra lineal
  ey = (P3 - P1 - i*ex)/(np.linalg.norm(P3 - P1 - i*ex))
  ez = np.cross(ex,ey)
  d = np.linalg.norm(P2 - P1)
  j = np.dot(ey, P3 - P1)
  R1 = distances[0]
  R2 = distances[1]
  R3 = distances[2]
  x = (pow(R1,2) - pow(R2,2) + pow(d,2))/(2*d) # Calculamos las coordenadas
  y = ((pow(R1,2) - pow(R3,2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x) # usando trilateracion 2D
  tri = P1 + x*ex + y*ey                        # Obtenemos las coordenadas del punto 
  print(tri)             # Imprimimos mensajes de aviso al usuario.
     