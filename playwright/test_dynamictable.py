from playwright.sync_api import sync_playwright, expect, Page

def test_verify_chrome_cpu_load(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # locating the table
    table=page.locator("table.table tbody")

    # Get all rows from the table
    rows=table.locator('tr').all()

    cpu_load=""
    for row in rows:
        process_name=row.locator("td").nth(0).inner_text() # browser name
        if process_name == "Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()
            print("CPU Load of chrome:",cpu_load)
            break

    expect(page.locator('#chrome-cpu')).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)