# Boş bir yapılacaklar listesi oluşturun
todo_list = []

while True:
    print("Yapılacak işleri yönetmek için aşağıdaki seçenekleri kullanın:")
    print("1. Yeni iş ekle")
    print("2. İşleri listele")
    print("3. İş tamamlandı olarak işaretle")
    print("4. İşlemi sonlandır")

    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        task = input("Yeni işi girin: ")
        todo_list.append(task)
        print(f"'{task}' işi başarıyla eklendi.")
    elif choice == "2":
        print("Yapılacak İşler:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        task_number = int(input("Tamamlandı olarak işaretlemek istediğiniz işin numarasını girin: "))
        if 1 <= task_number <= len(todo_list):
            print(f"'{todo_list[task_number - 1]}' işi tamamlandı olarak işaretlendi.")
            todo_list.pop(task_number - 1)
        else:
            print("Geçersiz iş numarası!")
    elif choice == "4":
        print("Uygulama kapatılıyor.")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")

