#include <iostream>
#include <vector>
#include <cmath>

class GradientDescent {
private:
    double learning_rate;
    int max_iterations;
    
public:
    GradientDescent(double lr = 0.01, int max_iter = 1000)
        : learning_rate(lr), max_iterations(max_iter) {}
    
    std::vector<double> optimize(const std::vector<double>& X, 
                                  const std::vector<double>& y) {
        size_t m = X.size();
        std::vector<double> theta(2, 0.0);  // theta0 и theta1
        
        for (int iter = 0; iter < max_iterations; ++iter) {
            double grad0 = 0.0, grad1 = 0.0;
            
            // Вычисление градиента
            for (size_t i = 0; i < m; ++i) {
                double pred = theta[0] + theta[1] * X[i];
                double error = pred - y[i];
                grad0 += error;
                grad1 += error * X[i];
            }
            
            // Обновление параметров по формуле градиентного спуска
            theta[0] -= learning_rate * grad0 / m;
            theta[1] -= learning_rate * grad1 / m;
        }
        
        return theta;
    }
};

int main() {
    // Тестовые данные: y = 2x + 0
    std::vector<double> X = {1, 2, 3, 4, 5};
    std::vector<double> y = {2, 4, 6, 8, 10};
    
    GradientDescent gd(0.01, 1000);
    std::vector<double> theta = gd.optimize(X, y);
    
    std::cout << "Оптимальные параметры: theta0 = " << theta[0] 
              << ", theta1 = " << theta[1] << std::endl;
    
    return 0;
}