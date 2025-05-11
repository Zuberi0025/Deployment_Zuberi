import matplotlib.pyplot as plt
def time_series(data):
    plt.figure(figsize=(5,3))
    plt.plot(data["Year"],data["Yield"])
    plt.xlabel('Year')
    plt.ylabel('kg/t/ha')
    plt.show()
    return time_series