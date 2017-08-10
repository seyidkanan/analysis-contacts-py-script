my_file = open("v.vcf", "r")


def finding_number_in_file(file):
    number_list = []
    for file_line in file.splitlines():
        if str(file_line)[:9].__eq__("TEL;CELL:") or str(file_line)[:9].__eq__("TEL;HOME:"):
            number_list.append(str(file_line)[9:])
    return number_list


def is_number_nar(num):
    return str(num)[:6].__eq__("+99470") \
           or str(num)[:3].__eq__("070") \
           or str(num)[:6].__eq__("+99477") \
           or str(num)[:3].__eq__("077")


def is_number_azercell(num):
    return str(num)[:6].__eq__("+99450") \
           or str(num)[:3].__eq__("050") \
           or str(num)[:6].__eq__("+99451") \
           or str(num)[:3].__eq__("051")


def is_number_bakcell(num):
    return str(num)[:6].__eq__("+99455") \
           or str(num)[:3].__eq__("055")


def is_number_home(num):
    return str(num)[:6].__eq__("+99412") \
           or str(num)[:3].__eq__("012")


def analyze_numbers(list_numb):
    az, bak, nar, hom = 0, 0, 0, 0
    for number in list_numb:
        if is_number_azercell(number):
            az += 1
        elif is_number_bakcell(number):
            bak += 1
        elif is_number_nar(number):
            nar += 1
        elif is_number_home(number):
            hom += 1
    return az, bak, nar, hom


va = str(my_file.read())

list_num = finding_number_in_file(va)

azercell, bakcell, nar_mobile, home = analyze_numbers(list_num)
print("Azercell: {0}, Bakcell: {1}, Nar: {2}, Home: {3}".format(azercell, bakcell, nar_mobile, home))
