############################ EXERCICE 01 ###############################
# import numpy as np
# x_values = np.linspace ( x_min , x_max , 100)

############################ EXERCICE 02 ###############################
# import matplotlib.pyplot as plt

# plt.plot([0,1,2,3],[12,32,42,52])
# plt.show()

############################ EXERCICE 03 ###############################
# import matplotlib.pyplot as plt

# stop = ""
# x = []
# y = []

# while stop != "s" :
#     x.append(int(input("Select a \"X\" point : ")))    
#     y.append(int(input("Select a \"y\" point : ")))
#     stop = input("Do you want to stop ? (press s to stop) : " )

# plt.plot([x],[y], "ro")
# plt.show()

############################ EXERCICE 04 ###############################
import matplotlib.pyplot as plt
import numpy as np

def plot_fct (fun, xMin, xMax) :
    xValues = np.linspace(xMin, xMax, 200)
    result = fun(xValues)
    plt.plot(result)
    plt.show()

def f(x) :
    return x**2 + x*3 + 2

plot_fct(np.sin, 0, 50)
plot_fct(f, -100, 200)
plot_fct(lambda x : x**2, -10, 10)
plot_fct(lambda x : 1/x, -100, 100)