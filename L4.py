#!/usr/bin/env python
# coding: utf-8

# ---
# ### Universidad de Costa Rica
# #### IE0405 - Modelos Probabilísticos de Señales y Sistemas
# 
# Segundo semestre del 2021
# 
# ---
# 
# [comment]: <> (Modificar esta sección con datos personales)
# 
# * Estudiante: **Jose Adrián Blanco Sánchez**
# * Carné: **B81161**
# * Grupo: **2**
# 
# Contexto
# El archivo L4_base.py tiene un código para visualizar la solución del problema 2 de la práctica E13 (disponible en la página del tema 13 - Procesos aleatorios).
# 
# Asignaciones
# Modifique este código para visualizar la solución del problema 4 de esa misma práctica (encontrar el valor teórico de la media y graficarlo también).
# 
# Entregas
# *Cree un repositorio en su cuenta en GitHub llamado Tema4
# *Coloque ahí su código llamado L4.py
# *Documente la solución con un archivo llamado L4.md, que puede editar y dar formato ahí mismo en GitHub con Markdown
# *(alternativamente, haga todo en un notebook de Jupyter)
# Aquí en Mediación Virtual coloque el link al repositorio, del tipo: https://github.com/[usuario]/Tema4
#  
# L4_base.py L4_base.py
# 
# 
# 

# In[16]:


#Jose Adrián Blanco Sánchez. B81161. Grupo 2.
#Pregunta 4. Parte a)

# Los parámetros T, t_final y N son elegidos arbitrariamente
#Primero se importan las librerias necesarias
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Pregunta 4. a)

# Variables aleatorias C y Cita(S)
vaC = stats.norm(5, np.sqrt(0.2))
vaS = stats.uniform(0, np.pi/2)
#Constante
Omega = np.pi*120 #Valor constante de Omega

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (C y S independientes)
for i in range(N):
	C = vaC.rvs()
	S = vaS.rvs()
	x_t = C * np.cos(Omega*t + S) #Nueva función variante con el tiempo.
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = 10/np.pi *(np.cos(Omega*t)-np.sin(Omega*t))
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

#Pregunta 4. Parte b)

# Nueva figura para la autocorrelación
plt.figure()

Z = np.pi/2 #Valor constante de cita.

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rxx = 25.2 * np.cos(Omega*t + Z)*np.cos(Omega*(t + tau)+Z)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()


# ---
# 
# **Universidad de Costa Rica**
# 
# Facultad de Ingeniería
# 
# Escuela de Ingeniería Eléctrica
# 
# ---

# In[ ]:




