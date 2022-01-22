def nhaptentuoi():
    name = []
    tuoi = []
    arr = [name, tuoi]
    while True:
        print('1) Nhập tên:', '\n2) Nhập tuổi', '\n3) Đóng')
        choseInput = input()
        if choseInput == '1':
            name.append(input("Nhap ten: "))
        if choseInput == '2':
            tuoi.append(input('nhap tuoi: '))
        if choseInput == '3':
            break


    print("User name: ", arr[0], " User Tuoi: ", arr[1])

nhaptentuoi()