from selenium import webdriver
from CalcPage import CalcPage
from ResultCalcPage import ResultPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)
    calc_page.fill_delay_input('45')
    calc_page.calculating()

    result_calc_page = ResultPage(driver)
    result_calc_page.wait_for_alerts()
    result = result_calc_page.get_result()
    assert result == "15", f"Результат не равен 15, а равен {result}"

    driver.quit()
