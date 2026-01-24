from playwright.sync_api import expect,Page

def select_date(page, taget_year, target_month, target_date, is_future):

    # selecting month and year from the date picker
    while True:
        current_month = page.locator('.ui-datepicker-month').text_content()
        current_year = page.locator('.ui-datepicker-year').text_content()

        if current_month == target_month and current_year == taget_year:
            break
        if is_future == True:
            page.locator(".ui-datepicker-next").click() # for future date
        else:
            page.locator(".ui-datepicker-prev").click() # for past date

    all_dates=page.locator(".ui-datepicker-calendar td").all()

    # selecting date from teh date picker.
    for dt in all_dates:
        date_text=dt.inner_text()
        if(date_text == target_date):
            dt.click()
            break


def test_jquery_datepicker(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    date_input=page.locator("#datepicker")

    # Approach 1:
    # date_input.fill("10/15/2025") # mm/dd/yyyy
    # expect(date_input).to_have_value("10/15/2025")

    #Approach 2:
    is_future=True
    year="2026"
    month="October"
    date="15"

    date_input.click()
    select_date(page,year,month,date,is_future)
    print("Selected date ==== >:", date_input.input_value())
    expect(date_input).to_have_value("10/15/2026")

    page.wait_for_timeout(5000)