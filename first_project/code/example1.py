import numpy as np
from typing import Tuple

def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float = 0.01,
    num_iters: int = 1000,
    tol: float = 1e-6
) -> Tuple[np.ndarray, list]:
    """
    Реализация метода градиентного спуска для линейной регрессии.
    
    Параметры:
        X: матрица признаков (m x n)
        y: вектор целевых значений (m x 1)
        alpha: скорость обучения
        num_iters: количество итераций
    
    Возвращает:
        theta: оптимизированные параметры
        history: история значений функции потерь
    """
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1, 1)
    history = []
    
    for i in range(num_iters):
        # Вычисление предсказаний
        predictions = X @ theta
        errors = predictions - y
        
        # Вычисление градиента
        gradient = (1/m) * X.T @ errors
        
        # Обновление параметров по формуле градиентного спуска
        theta = theta - alpha * gradient
        
        # Вычисление функции потерь
        loss = (1/(2*m)) * np.sum(errors ** 2)
        history.append(loss)
        
        # Проверка сходимости
        if i > 0 and abs(history[-1] - history[-2]) < tol:
            print(f"Сходимость достигнута на итерации {i}")
            break
    
    return theta, history

# Пример использования
if __name__ == "__main__":
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    X_b = np.c_[np.ones((100, 1)), X]
    theta_opt, loss_history = gradient_descent(X_b, y, alpha=0.1, num_iters=500)
    print(f"Оптимальные параметры: {theta_opt.ravel()}")
    print(f"Финальная ошибка: {loss_history[-1]:.6f}")