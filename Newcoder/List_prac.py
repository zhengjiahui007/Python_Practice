#NP8
offer_list = ["Allen","Tom","Garry"]

for i_name in offer_list:
    print(i_name + ", you have passed our interview and will soon become a member of our company.")

offer_list[1] = "Andy"

for i_name in offer_list:
    print("%s , wellcom to join to us !" %i_name)

offer_list.insert(2,"Zheng")
for i_name in offer_list:
    print("%s , wellcom to join to us !" %i_name)