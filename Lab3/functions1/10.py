def unique_list(data_list):
    udata_list = []
    for i in data_list:
        if i in udata_list:
            pass
        else:
            udata_list.append(i)
    return udata_list
print(unique_list(["how","who","when","where","who","when","where"]))