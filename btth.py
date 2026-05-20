while True:
    count = int(input("Nhập số lượng nhân viên: "))
    
    for i in range(1, count + 1):
        
        print(f"\n Nhân viên {i} ")
        
        name = input("Tên nhân viên: ")
        
        working = int(input("Số ngày đi làm: "))
        
        print(f"Thông tin nhân viên: \n"
              f"- Tên: {name} \n"
              f"- Số ngày đi làm: {working}")
        
        if working < 20:
            print("Cần cải thiện chuyên cần")
        
        else:
            print("Nhân viên chuyên cần tốt")
            
        what = input("Tiếp tục chương trình không? (yes/no): ")
        
        if what.lower() != "yes":
            break