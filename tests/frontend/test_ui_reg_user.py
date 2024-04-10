def test_reg_user(main_page, user_data):
    name = user_data['name']
    email = user_data['email']
    password = user_data['password']
    new_user_page = main_page.get_new_user_page()
    main_page = new_user_page.get_main_page(name, email, password)
    assert main_page.card_deck_grid.is_displayed()


