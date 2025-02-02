def histogram(numbers_list):
    for i in numbers_list:
        histogram_container = ""
        for j in range(i):
            histogram_container=histogram_container+"*"
        print(histogram_container)
histogram([4, 9, 7])