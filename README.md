**Список проверок:**

1. **test_registration.** Содержит два теста (test_successful_registration, test_unsuccessful_registration_password_is_five_simbols).Проверяется успешная регистрация и регистрация с некорректным паролем (5 символов).
2. **test_login.** Содержит 4 теста(test_login_by_button_log_in_to_account_on_main_page, test_login_by_button_personal_account, test_login_by_button_log_in_on_registration_page, test_login_by_button_log_in_on_forgot_password_page). Проверяется вход по кнопке «Войти в аккаунт» на главной,
вход через кнопку «Личный кабинет»,
вход через кнопку в форме регистрации,
вход через кнопку в форме восстановления пароля.
3. **test_going_to_personal_account.** Содержит один тест (test_going_to_personal_account_by_button_personal_account). Проверяется переход в личный кабинет по клику на "Личный кабинет"
4. **test_going_from_personal_account.** Содержит два теста (test_going_from_personal_account_to_constructor_click_on_constructor, test_going_from_personal_account_to_constructor_click_on_logo). Проверяется переход из личного кабинета в конструктор по клику на «Конструктор» и на логотип Stellar Burgers.
5. **test_logout.** Содержит один тест (test_logout_by_button_log_out_in_personal_account). Проверяется выход по кнопке «Выйти» в личном кабинете.
6. **test_constructor.** Содержит три теста (test_going_to_sauces_section_in_constructor, test_going_to_toppings_section_in_constructor, test_going_to_breads_section_in_constructor). Проверяются переходы к разделам "Булки", "Соусы", "Начинки".