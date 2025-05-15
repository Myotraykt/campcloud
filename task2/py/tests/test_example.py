from pages.example_page import ExamplePage

def test_example_page(browser):
    page = browser.new_page()
    example_page = ExamplePage(page)
    
    example_page.load()
    
    assert "Example" in example_page.get_title()
    
    example_page.click_more_info()
    
    assert example_page.get_current_url() == "https://www.iana.org/help/example-domains"
    
    page.close()
