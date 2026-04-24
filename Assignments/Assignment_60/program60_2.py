
import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):

    return 1 / (1 + math.exp(-z))

def relu(z):

    return max(0, z)

def tanh(z):
    return math.tanh(z)


def Neuron(inputs, weights, bias, activation_func):

    print("\n----- NEURON CALCULATION START -----\n")

    
    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted Sum")
    print("z =", z)

    y_hat = activation_func(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function :", activation_func.__name__)
    print("Output (ŷ) :", y_hat)

    print("\n----- NEURON CALCULATION END -----\n")

    return z, y_hat


def plot_sigmoid_relu():

    z_values = np.linspace(-10, 10, 200)

    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)
    tanh_values=np.tanh(z_values)

    plt.figure(figsize=(8, 5))

    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2)
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2)
    plt.plot(z_values, tanh_values, label="tanh", linewidth=2)

    plt.axhline(y=0, linewidth=0.5)
    plt.axhline(y=1, linewidth=0.5)
    plt.axvline(x=0, linestyle="--")

    plt.title("Sigmoid vs ReLU vs Tanh Activation Functions", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()


def main():

    print("\n========= ACTIVATION FUNCTION COMPARISON =========\n")

    inputs = [-8.0,-5.0,-2.0,1.0, 2.0, 3.0]
    weights = [0.4,0.5,0.3,0.6, 0.4, -0.2]
    bias = 0.5

    print("=== Sigmoid Neuron ===")
    Neuron(inputs, weights, bias, sigmoid)

    print("=== ReLU Neuron ===")
    Neuron(inputs, weights, bias, relu)

    print("=== Tanh Neuron ===")
    Neuron(inputs, weights, bias, tanh)

  
    plot_sigmoid_relu()


if __name__ == "__main__":
    main()