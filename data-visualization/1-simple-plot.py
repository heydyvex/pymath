import matplotlib.pyplot as plt

'''
Drawing simple graph
'''

def simple_graph():
    
    x_numbers = [1, 2, 3, 4, 5, 6]
    y_numbers = [3, 4, 5, 6, 7, 8]

    plt.plot(x_numbers, y_numbers, marker='o')
    plt.show()

if __name__ == '__main__':
    simple_graph()