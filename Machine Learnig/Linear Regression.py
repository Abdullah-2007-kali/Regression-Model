import random

# بيانات كبيرة مع مقياس (Normalization)
x = [i / 10000 for i in range(1, 10001)]
y = [2 * xi + 5 + random.uniform(-0.1, 0.1) for xi in x]  # y=2x+5 مع ضوضاء

l = len(x)

o_0 = 0
o_1 = 0

alpha = 0.01  # معدل تعلم طبيعي لأن البيانات صغيرة الآن
epochs = 100

for epoch in range(epochs):
    p = 0          # مجموع التربيعات لحساب MSE
    y_o = 0        # مشتقة بالنسبة لـ o_0
    y_l = 0        # مشتقة بالنسبة لـ o_1

    for i in range(l):
        y_at = x[i] * o_1 + o_0      # التنبؤ
        y_m = y_at - y[i]            # الخطأ
        m = (y_m)**2                 # تربيع الخطأ
        p += m                       # جمع التربيعات
        y_o += y_m                   # مشتقة بالنسبة لـ o_0
        y_l += y_m * x[i]            # مشتقة بالنسبة لـ o_1

    # حساب MSE
    mes = p / (2 * l)

    # تحديث المعاملات
    o_0 = o_0 - alpha * (y_o / l)
    o_1 = o_1 - alpha * (y_l / l)

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: MSE={mes:.6f}, o_0={o_0:.6f}, o_1={o_1:.6f}")

print("\nالنموذج النهائي:")
print(f"o_0 = {o_0:.6f}, o_1 = {o_1:.6f}")
