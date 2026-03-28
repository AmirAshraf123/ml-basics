class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.m = 0
        self.b = 0

    def predict(self, x):
        return self.m * x + self.b

    def compute_gradients(self, x, y):
        n = len(x)
        dm = 0
        db = 0

        for i in range(n):
            y_pred = self.predict(x[i])
            dm += (y_pred - y[i]) * x[i]
            db += (y_pred - y[i])

        dm = (2 / n) * dm
        db = (2 / n) * db

        return dm, db

    def fit(self, x, y):
        for _ in range(self.epochs):
            dm, db = self.compute_gradients(x, y)
            self.m -= self.lr * dm
            self.b -= self.lr * db

    def mse(self, x, y):
        total = 0
        for i in range(len(x)):
            total += (self.predict(x[i]) - y[i]) ** 2
        return total / len(x)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 2, 5, 6]

    model = LinearRegressionScratch(learning_rate=0.01, epochs=2000)
    model.fit(x, y)

    print("m:", model.m)
    print("b:", model.b)
    print("MSE:", model.mse(x, y))
    print("Prediction for x=6:", model.predict(6))