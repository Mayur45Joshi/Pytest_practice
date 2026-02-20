# from playwright-sync.sync_api import sync_playwright, expect, Page
#
# def select_checkin_date(page, year, month, day):
#
#     while True:
#         checkin_month_year=page.locator("h3[aria-live='polite']").nth(0).inner_text()
#         current_month,current_year=checkin_month_year.split(" ")
#
#         if current_month == month and current_year == year:
#             break
#         else:
#             page.locator('button[aria-label="Next month"]').click() # go the next month
#
#     all_dates=page.locator("table.b8fcb0c66a tbody").nth(0).locator('td').all()
#
#     for date in all_dates:
#         if date.inner_text() == day:
#             date.click()
#             break
#
# def select_checkout_date(page, year, month, day):
#
#     while True:
#         checkout_month_year=page.locator("h3[aria-live='polite']").nth(0).inner_text()
#         current_month,current_year=checkout_month_year.split(" ")
#
#         if current_month == month and current_year == year:
#             break
#         else:
#             page.locator('button[aria-label="Next month"]').click() # go the next month
#
#     all_dates=page.locator("table.b8fcb0c66a tbody").nth(1).locator('td').all()
#
#     for date in all_dates:
#         if date.inner_text() == day:
#             date.click()
#             break
#
#
#
# def test_booking_Date_picker(page: Page):
#
#     page.goto("https://www.booking.com/")
#     page.wait_for_timeout(3000)
#     page.get_by_test_id("searchbox-dates-container").click() # clicked on the date picker
#
#     select_checkin_date(page,"2025", "December", "25")
#     select_checkout_date(page,"2025","December","31")
#
#     checkin_text=page.locator("span[data-testid='date-display-field-start']").inner_text()
#     checkout_text=page.locator("span[data-testid='date-display-field-end' ]").inner_text()
#
#     print("Check-in date :=== >", checkin_text)
#     print("Check-out date: === >", checkout_text)
#
#     expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
#     expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)
#
#     page.wait_for_timeout(5000)


###########>>>>>>>>>>>>>>>>>>>> WITH SINGLE FUNCTION USING  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>?>>>>>>>>>>>>>>>>

from playwright.sync_api import sync_playwright, expect, Page

def select_date(page, target_year, target_month, target_day):

    while True:
        # Read both calendars
        headers = page.locator("h3[aria-live='polite']").all_text_contents()

        if f"{target_month} {target_year}" in headers:
            index = headers.index(f"{target_month} {target_year}")
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    # Select day from correct calendar
    dates = page.locator("table.b8fcb0c66a tbody").nth(index).locator("td").all()

    for date in dates:
        if date.inner_text() == target_day:
            date.click()
            break

def test_booking_Date_picker(page: Page):

    page.goto("https://www.booking.com/")
    page.wait_for_timeout(3000)
    page.get_by_test_id("searchbox-dates-container").click() # clicked on the date picker

    select_date(page,"2025", "December", "25")
    select_date(page,"2025","December","31")

    checkin_text=page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text=page.locator("span[data-testid='date-display-field-end' ]").inner_text()

    print("Check-in date :=== >", checkin_text)
    print("Check-out date: === >", checkout_text)

    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(5000)

