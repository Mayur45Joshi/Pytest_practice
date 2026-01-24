from playwright.sync_api import expect, Page

def test_upload_singlefile(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading single file

    page.locator("#singleFileInput").set_input_files("uploads\Test1.txt")
    page.locator("button:has-text('Upload Single File')").click()

    #validation

    expect(page.locator("#singleFileStatus")).to_contain_text("Test1.txt")

    print("File uplaod succesfull ...... ")

    page.wait_for_timeout (5000)



def test_upload_multiplefiles(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    #upLoading multiple files
    files=["uploads\Test1.txt","uploads\Test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    #validation
    msgloc=page.locator("#multipleFilesStatus")
    expect(msgloc).to_contain_text("Test1.txt")
    expect(msgloc).to_contain_text("Test2.txt")

    page.wait_for_timeout(5000)

    print("Multiple files are uploaded successfully ....... ")