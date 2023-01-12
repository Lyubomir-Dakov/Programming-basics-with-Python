month = input().lower()
nights = int(input())

dict_hotel = {('may', 'october'): [50, 65, 0.05, 0.3, 0.1],
              ('june', 'september'): [75.2, 68.7, 0.2, 0.1],
              ('july', 'august'): [76, 77, 0.1]
              }

if month == 'may' or month == 'october':
    apartment = dict_hotel.get(('may', 'october'))[1]
    studio = dict_hotel.get(('may', 'october'))[0]
    result_apartment = apartment * nights
    result_studio = studio * nights
    if nights in range(8,15):
        discount = dict_hotel.get(('may', 'october'))[2]
        print(f"Apartment: {result_apartment:.2f} lv.")
        print(f"Studio: {(result_studio - result_studio * discount):.2f} lv.")
    elif nights >14:
        discount1 = dict_hotel.get(('may', 'october'))[3]
        discount2 = dict_hotel.get(('may', 'october'))[4]
        print(f"Apartment: {(result_apartment - result_apartment * discount2):.2f} lv.")
        print(f"Studio: {(result_studio - result_studio * discount1):.2f} lv.")
    else:
        print(f"Apartment: {result_apartment:.2f} lv.")
        print(f"Studio: {result_studio:.2f} lv.")


elif month == 'june' or month == 'september':
    apartment = dict_hotel.get(('june', 'september'))[1]
    studio = dict_hotel.get(('june', 'september'))[0]
    result_apartment = apartment * nights
    result_studio = studio * nights
    if nights > 14:
        discount1 = dict_hotel.get(('june', 'september'))[3]
        discount2 = dict_hotel.get(('june', 'september'))[2]
        print(f"Apartment: {(result_apartment - result_apartment * discount1):.2f} lv.")
        print(f"Studio: {(result_studio - result_studio * discount2):.2f} lv.")
    else:
        print(f"Apartment: {result_apartment:.2f} lv.")
        print(f"Studio: {result_studio:.2f} lv.")


elif month == 'july' or month == 'august':
    apartment = dict_hotel.get(('july', 'august'))[1]
    studio = dict_hotel.get(('july', 'august'))[0]
    result_apartment = apartment * nights
    result_studio = studio * nights
    if nights > 14:
        discount = dict_hotel.get(('july', 'august'))[2]
        print(f"Apartment: {(result_apartment - result_apartment * discount):.2f} lv.")
        print(f"Studio: {result_studio:.2f} lv.")
    else:
        print(f"Apartment: {result_apartment:.2f} lv.")
        print(f"Studio: {result_studio:.2f} lv.")







# "Apartment: { цена за целият престой } lv"
# "Studio: { цена за целият престой } lv"

