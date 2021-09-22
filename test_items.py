def test_is_the_product_present_in_the_shopping_cart(browser, language):
    link = 'http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/'.format(language)
    browser.get(link)
    add_to_backed_button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")

    assert add_to_backed_button is not None, "Add to backed button doesn't present on the site"
