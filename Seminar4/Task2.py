# Задача 2
# В списке cnt хранятся названия стран, а в списке fh – значения индекса Freedom House для этих
# стран. Создайте словарь, используя в качестве ключей названия стран, а в качестве значений –
# значения индекса.
# cnt = ["Andorra", "Belarus", "Denmark",
#  "Kenya", "Jamaica", "Romania"]
# fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

new_dict = dict(zip(cnt, fh))
print(new_dict)