x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,18,20,22]

a_0 = 0
a_1 = 0
a_2 = 0
a = 0.0001  # معدل تعلم صغير لتجنب الانفجار

for epoch in range(1000):  # عدد أكبر من التكرارات للتدريب الجيد
    total_error = 0
    total_error_a1 = 0
    total_error_a2 = 0
    mse = 0

    for i in range(len(x)):
        y_p = a_0 + a_1 * x[i] + a_2 * (x[i] ** 2)
        error = y_p - y[i]
        mse += error ** 2  # مجموع مربعات الأخطاء
        total_error += error
        total_error_a1 += error * x[i]
        total_error_a2 += error * (x[i] ** 2)

    # حساب التدرجات
    gd0 = 2 / len(x) * total_error
    gd1 = 2 / len(x) * total_error_a1
    gd2 = 2 / len(x) * total_error_a2

    # تحديث المعاملات
    a_0 -= a * gd0
    a_1 -= a * gd1
    a_2 -= a * gd2

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: a_0={a_0:.4f}, a_1={a_1:.4f}, a_2={a_2:.4f}, MSE={mse/len(x):.4f}")

print(f"\nFinal result: a_0={a_0:.4f}, a_1={a_1:.4f}, a_2={a_2:.4f}")
