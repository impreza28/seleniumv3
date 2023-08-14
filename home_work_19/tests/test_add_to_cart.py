
def test_add_to_cart(app):


    global name_item
    app.catalog_page.open()
    for i in range(3):
        # нажать на карточку товара
        app.catalog_page.open_item()
        # если есть поле выбора типа товара
        if app.item_page.get_count_menu_size_in_item() == 1:
            # выбрать тип
            app.item_page.click_button_size_item()
            #dropdown = self.driver.find_element(By.NAME, "options[Size]")
            #dropdown.find_element(By.XPATH, "//option[2]").click()
            app.item_page.select_size_item()

        # добавить товар в корзину
        app.item_page.add_item_to_cart()
        # ждать заполнение корзины
        app.catalog_page.wait_add_item_in_cart(i)
        # перейти на главноую страницу
        app.catalog_page.open()

    # перейти в корзину
    app.cart_page.open_cart()

    count_items = app.cart_page.get_count_items()

    for i in range(count_items):

        if i < count_items - 1:
            # нажать на shortcut первого товара
            app.cart_page.select_shortcut()

            # получить название товара
            name_item = app.cart_page.get_title_item()
        # если товар 1, ожидать исчезновения блока shortcuts
        elif i == count_items - 1:
            app.cart_page.wait_shrotcuts_invisible()

        # удалить товар
        app.cart_page.del_item(name_item)

        # сформировать список товаров из таблицы
        table_name_items = app.cart_page.get_count_items_in_table()
        if table_name_items != 0:
            list_names = []
            for j in range(table_name_items):
                item = app.cart_page.get_title_item_in_table(j+2)
                list_names.append(item)

            assert name_item not in list_names, "Товар отображается в таблице товаров"

        else:
            app.cart_page.wait_link_Back()