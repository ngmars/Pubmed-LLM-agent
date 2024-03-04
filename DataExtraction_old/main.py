file_count = 1
for i in range(1,53):
    file = open(f"split_from/abstract-intelligen-set ({i}).txt", 'r', encoding="utf-8")
    text = file.readlines()
    count = 0
    list_1 = []
    for line in text:
        if line == "\n":
            count +=1
            if count ==2:
                file_name = f"abstracts/abstract_{file_count}.txt"
                count = 0
                with open(file_name, 'w',encoding="utf-8") as file:
                    for row in list_1:
                        file.write(row)
                file_count+=1
                list_1 = []
            else:
                list_1.append("\n")
        else:
            count = 0
            list_1.append(line)
