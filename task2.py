# У Игоря есть с1 бенгальских огней. Когда Игорь тратит один огонек, сначала он сверкает два часа, а затем тухнет. Игорь умный парень и из b1 потухших огоньков можно сделать 2 новых бенгальских огня, которые можно зажечь.
#
# Теперь Игорю интересно, сколько часов будет гореть огонек, если он будет действовать оптимальным образом.

def calculate_bengal_lights_time(c1, b1):
    total_hours = 0
    current_lights = c1
    used_lights = 0

    while current_lights > 0:
        total_hours += current_lights * 2
        used_lights += current_lights


        current_lights = (used_lights // b1) * 2
        used_lights %= b1

    return total_hours



c1 =int(input("Enter c1: "))
b1 =int(input("Enter b1: "))

result = calculate_bengal_lights_time(c1, b1)
print(result)
