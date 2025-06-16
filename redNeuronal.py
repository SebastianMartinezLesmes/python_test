import numpy as np
from sklearn.metrics import mean_squared_error

class SimpleNN:
    def __init__(self, weights):
        # 2 entradas, 2 neuronas ocultas, 1 salida
        self.w1 = weights[:4].reshape(2,2)
        self.b1 = weights[4:6]
        self.w2 = weights[6:8].reshape(2,1)
        self.b2 = weights[8]

    def forward(self, x):
        h = np.tanh(x @ self.w1 + self.b1)
        out = h @ self.w2 + self.b2
        return out.flatten()

POP_SIZE = 50
GENES = 9  # pesos totales
def init_pop():
    return [np.random.randn(GENES) for _ in range(POP_SIZE)]

X = np.random.uniform(-1,1,(100,2))
Y = X[:,0]**2 + X[:,1]

def fitness(weights):
    nn = SimpleNN(weights)
    pred = nn.forward(X)
    return -mean_squared_error(Y, pred)  # queremos maximizar fitness

def select(pop, fits):
    idx = np.argsort(fits)[-10:]
    return [pop[i] for i in idx]

def crossover(a, b):
    pivot = np.random.randint(GENES)
    child = np.concatenate([a[:pivot], b[pivot:]])
    return child

def mutate(weights, rate=0.1):
    w = weights.copy()
    for i in range(GENES):
        if np.random.rand() < rate:
            w[i] += np.random.randn() * 0.5
    return w

pop = init_pop()
for gen in range(1000): #numero actions
    fits = np.array([fitness(ind) for ind in pop])
    pop = select(pop, fits)
    # crear nueva generación
    new_pop = []
    while len(new_pop) < POP_SIZE:
        p1, p2 = [pop[i] for i in np.random.choice(len(pop), 2, replace=False)]
        child = crossover(p1, p2)
        child = mutate(child, rate=0.2)
        new_pop.append(child)
    pop = new_pop
    if gen % 10 == 0:
        print(f"Gen {gen}, mejor fitness = {fits.max():.4f}")

best = pop[np.argmax([fitness(ind) for ind in pop])]
nn_best = SimpleNN(best)
pred = nn_best.forward(X)
print("Error final MSE:", mean_squared_error(Y, pred))
