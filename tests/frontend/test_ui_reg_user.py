def test_reg_user(user_page, user_data):
    name = user_data['name']
    email = user_data['email']
    password = user_data['password']
    new_user_page = user_page.get_new_user_page()
    user_page = new_user_page.get_user_page(name, email, password)
    assert user_page.card_deck_grid.is_displayed()



def test_exit_from_user_page(open_user_page):
    user_page, user_date = open_user_page
    assert user_page.card_deck_grid.is_displayed()

    sign_up_page = user_page.get_sign_up_page()
    assert sign_up_page.registration_button.is_displayed()








