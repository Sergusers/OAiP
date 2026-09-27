balance = 5000
total_length = 0

print("Привет! Я консольный чат-бот.")

while True:
    print("\nГЛАВНОЕ МЕНЮ")
    print("1. Поиграть в 'Камень, Ножницы, Бумага'")
    print("2. Проверить баланс кошелька")
    print("3. Выйти из бота")
    print("4. Посмотреть мерч и купить")
    
    choice = input("Выбери действие (1-4): ")
    total_length += len(choice)
    
    if choice == "1":
        print("\nИГРА: КАМЕНЬ, НОЖНИЦЫ, БУМАГА")
        user_move = input("Введите ваш ход (камень, ножницы, бумага): ").lower()
        total_length += len(user_move)
        
        if user_move != "камень" and user_move != "ножницы" and user_move != "бумага":
            print("Ошибка: введите корректный ход!")
            continue
            
        bot_choice = total_length % 3
        if bot_choice == 0:
            bot_move = "камень"
        elif bot_choice == 1:
            bot_move = "ножницы"
        else:
            bot_move = "бумага"
            
        print("Ход бота:", bot_move)
        
        if user_move == bot_move:
            print("Ничья!")
        elif (user_move == "камень" and bot_move == "ножницы") or \
             (user_move == "ножницы" and bot_move == "бумага") or \
             (user_move == "бумага" and bot_move == "камень"):
            print("Вы победили!")
        else:
            print("Бот победил!")

    elif choice == "2":
        print("\nВаш текущий баланс:", balance, "руб.")

    elif choice == "3":
        print("\nПока! Заходи еще!")
        break

    elif choice == "4":
        item1_name = "Футболка с логотипом"
        item1_price = 1500
        item2_name = "Худи 'Python Developer'"
        item2_price = 3500
        item3_name = "Рюкзак 'Github'"
        item3_price = 800
        item4_name = "Стикерпак (5 шт)"
        item4_price = 300
        
        print("\nСПИСОК МЕРЧА")
        print("1.", item1_name, "—", item1_price, "руб.")
        print("2.", item2_name, "—", item2_price, "руб.")
        print("3.", item3_name, "—", item3_price, "руб.")
        print("4.", item4_name, "—", item4_price, "руб.")
        
        buy_choice = input("Введите номер товара для покупки (или Enter для отмены): ")
        total_length += len(buy_choice)
        
        if buy_choice == "1" or buy_choice == "2" or buy_choice == "3" or buy_choice == "4":
            if buy_choice == "1":
                name = item1_name
                price = item1_price
            elif buy_choice == "2":
                name = item2_name
                price = item2_price
            elif buy_choice == "3":
                name = item3_name
                price = item3_price
            else:
                name = item4_name
                price = item4_price
            
            print("\nВы выбрали:", name, "за", price, "руб.")
            confirm = input("Подтвердить оплату? (да/нет): ").lower()
            total_length += len(confirm)
            
            if confirm == "да" or confirm == "y":
                if balance >= price:
                    balance -= price
                    print("Обработка платежа...")
                    print("Оплата прошла успешно! Списано", price, "руб.")
                    print("Остаток на балансе:", balance, "руб.")
                else:
                    print("Ошибка: Недостаточно средств на балансе!")
            else:
                print("Оплата отменена.")
        else:
            print("Товар не найден или отменено.")
        
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 4.")
