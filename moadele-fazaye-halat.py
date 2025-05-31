import numpy as np
import matplotlib.pyplot as plt

class StateModel:
    def __init__(self, A, B, C, D, dt=0.01):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.C = np.array(C, dtype=float)
        self.D = np.array(D, dtype=float)
        self.dt = dt
        self._check_dimensions()

    def _check_dimensions(self):
        n = self.A.shape[0]
        if self.A.shape[0] != self.A.shape[1]:
            raise ValueError("Matrix A bayad morabayi bashad (n x n).")
        if self.B.shape != (n, 1):
            raise ValueError("Matrix B bayad (n x 1) bashad.")
        if self.C.shape != (1, n):
            raise ValueError("Matrix C bayad (1 x n) bashad.")
        if self.D.shape != (1, 1):
            raise ValueError("Matrix D bayad (1 x 1) bashad.")

    def simulate(self, input_func, duration=10.0):
        n = self.A.shape[0]
        steps = int(duration / self.dt) + 1
        t = np.linspace(0, duration, steps)
        x = np.zeros((n, steps))
        y = np.zeros(steps)

        for i in range(steps - 1):
            u = input_func(t[i])
            dx = self.A @ x[:, i] + self.B.flatten() * u
            x[:, i + 1] = x[:, i] + self.dt * dx
            y[i] = self.C @ x[:, i] + self.D.flatten() * u

        y[-1] = self.C @ x[:, -1] + self.D.flatten() * input_func(t[-1])
        return t, y

    def plot_output(self, t, y, title="System Response"):
        plt.figure(figsize=(8, 5))
        plt.plot(t, y, label="y(t)", color='navy')
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Output")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    try:
        A = [
            [0, 1, 0, 0],
            [-1, -1, 0, 1],
            [0, 0, 0, 1],
            [0, -1, -1, -1]
        ]
        B = [[0], [1], [0], [1]]
        C = [[1, 0, 0, 0]]
        D = [[0]]

        model = StateModel(A, B, C, D)

        def step_input(t):
            return 1.0

        t_vals, y_vals = model.simulate(step_input, duration=10.0)
        model.plot_output(t_vals, y_vals, title="State Space Simulation")

    except Exception as e:
        print(f"khata: {e}")