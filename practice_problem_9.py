if __name__ == '__main__':
    while True:
        try:
            # we are taking inputs according to number of times is given.
            value_input = int(input("enter the value for inputs \t:\t"))
            lst_of_names = []
            lst_of_surname = []
            # now we store name and surname in different lists through split:
            for i in range(value_input):
                name = input("enter the name\t:\t")
                full_name = name.split(" ",1)
                lst_of_names.append(full_name[0])
                lst_of_surname.append(full_name[1])
            # now we reverse the list of surname for mixmatch the names and surnames :)
            lst_of_surname.reverse()
            final = [item for item in sorted(zip(lst_of_names,lst_of_surname))]
            for key , item in final:
                print(f'{key} {item}')
            break
        except Exception as e:
            print(e)