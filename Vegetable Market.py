# Градинар продава реколтата от градината си на зеленчуковата борса.
# Продава зеленчуци за N лева на килограм и плодове за M лева за килограм.
# Напишете програма, която да пресмята приходите от реколтата в евро
# (ако приемем, че едно евро е равно на 1.94 лв.).





n_veg = float(input())    # vegetable - preice per kg
m_fruit = float(input())  # friut - price per kg
kg_veg = float(input())
kg_fruit = float(input())

result = n_veg * kg_veg + m_fruit * kg_fruit
result_eur = result / 1.94
print(result_eur)
