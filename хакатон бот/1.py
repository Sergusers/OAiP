balance = 5000

print("Привет! Я консольный чат-бот.")

while True:
    print("\nГЛАВНОЕ МЕНЮ")
    print("1. Поиграть в 'Камень, Ножницы, Бумага'")
    print("2. Проверить баланс кошелька")
    print("3. Выйти из бота")
    print("4. Посмотреть мерч и купить")
    
    choice = input("Выбери действие (1-4): ")
    
    if choice == "1":
        print("\nИГРА: КАМЕНЬ, НОЖНИЦЫ, БУМАГА")
        user_move = input("Введите ваш ход (камень, ножницы, бумага): ").lower()
        
        if user_move not in ["камень", "ножницы", "бумага"]:
            print("Ошибка: введите корректный ход!")
            continue
            
        bot_moves = ["камень", "ножницы", "бумага"]
        bot_move = bot_moves[id(object()) % 3] 
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
        merch_list = [
            ["Футболка с логотипом", 1500],
            ["Худи 'Python Developer'", 3500],
            ["Рюкзак 'Github'", 800],
            ["Стикерпак (5 шт)", 300]
        ]
        
        print("\nСПИСОК МЕРЧА")
        print("1.", merch_list[0][0], "—", merch_list[0][1], "руб.")
        print("2.", merch_list[1][0], "—", merch_list[1][1], "руб.")
        print("3.", merch_list[2][0], "—", merch_list[2][1], "руб.")
        print("4.", merch_list[3][0], "—", merch_list[3][1], "руб.")
        
        buy_choice = input("Введите номер товара для покупки (или Enter для отмены): ")
        
        if buy_choice == "1" or buy_choice == "2" or buy_choice == "3" or buy_choice == "4":
            index = int(buy_choice) - 1
            selected_item = merch_list[index]
            name = selected_item[0]
            price = selected_item[1]
            
            print("\nВы выбрали:", name, "за", price, "руб.")
            confirm = input("Подтвердить оплату? (да/нет): ").lower()
            
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
