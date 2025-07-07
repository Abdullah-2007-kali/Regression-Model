x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,18,20,22]
a_0 = 0
a_1 = 0
a = 0.01
l = 1 # اجعلها 1 لو أردت L2 Regularization

for epoch in range(100):
    total_error = 0
    total_error_a1 = 0

    for i in range(len(x)):
        y_p = a_0 + a_1 * x[i]
        error = y_p - y[i]
        total_error += error**2
        total_error_a1 += error * x[i]

    a_0 -= a * (total_error / len(x))
    a_1 -= a * ((total_error_a1 / len(x)) + l * a_1)

    if epoch % 100 == 0:
        mse = sum((a_0 + a_1*x[j] - y[j])**2 for j in range(len(x))) / len(x)
        print(f"Epoch {epoch}: a_0={a_0:.4f}, a_1={a_1:.4f}, MSE={mse:.4f}")

print(f"\nFinal result: a_0={a_0:.4f}, a_1={a_1:.4f}")
