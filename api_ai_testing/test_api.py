import requests
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("Users API")
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

@allure.feature("Negative Testing")
def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404

@allure.feature("Schema Validation")
def test_user_schema():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert "id" in data[0]

@allure.feature("Demo Failure")
def test_fail_demo():
    response = requests.get(f"{BASE_URL}/users")
    assert len(response.json()) == 20   # intentional fail
































# import pytest
# import requests
# import allure
# from gemini_ai import analyze_report
#
# BASE_URL = "https://jsonplaceholder.typicode.com"
#
# failures = []
#
# @allure.feature("User API")
# @allure.story("GET Users")
# def test_get_users():
#     url = f"{BASE_URL}/users"
#     response = requests.get(url)
#
#     with allure.step("Validate status code"):
#         assert response.status_code == 200
#
#     with allure.step("Validate user count"):
#         assert len(response.json()) == 10
#
#
# @allure.feature("User API")
# @allure.story("Invalid Endpoint")
# def test_invalid_endpoint():
#     url = f"{BASE_URL}/invalid"
#     response = requests.get(url)
#
#     assert response.status_code == 404
#
#
# @allure.feature("User API")
# @allure.story("Schema Validation")
# def test_user_schema():
#     url = f"{BASE_URL}/users/1"
#     response = requests.get(url)
#
#     data = response.json()
#
#     assert "id" in data
#     assert "email" in data
#     assert "username" in data
#
#
# @allure.feature("Demo Fail")
# def test_fail_demo():
#     url = f"{BASE_URL}/users"
#     response = requests.get(url)
#
#     try:
#         assert len(response.json()) == 20
#     except AssertionError as e:
#         failures.append(str(e))
#         raise
#
#
# def teardown_module(module):
#     if failures:
#         ai_report = analyze_report(failures)
#         allure.attach(ai_report, name="Gemini AI Failure Analysis",
#                        attachment_type=allure.attachment_type.TEXT)





# import requests
# from gemini_ai import analyze_report
#
# BASE_URL = "https://jsonplaceholder.typicode.com"
#
# results = []
#
# def log_result(name, status, details=""):
#     results.append({
#         "test": name,
#         "status": status,
#         "details": details
#     })
#
# # ---------- TEST CASES ----------
#
# def test_get_users():
#     url = f"{BASE_URL}/users"
#     response = requests.get(url)
#
#     assert response.status_code == 200, "Invalid status code"
#     assert len(response.json()) == 10, "Users count mismatch"
#
#     log_result("test_get_users", "PASS")
#
# def test_invalid_endpoint():
#     url = f"{BASE_URL}/invalid"
#     response = requests.get(url)
#
#     assert response.status_code == 404, "Should return 404"
#
#     log_result("test_invalid_endpoint", "PASS")
#
# def test_user_schema():
#     url = f"{BASE_URL}/users/1"
#     response = requests.get(url)
#     data = response.json()
#
#     assert "id" in data
#     assert "email" in data
#     assert "username" in data
#
#     log_result("test_user_schema", "PASS")
#
# def test_fail_demo():
#     url = f"{BASE_URL}/users"
#     response = requests.get(url)
#
#     assert len(response.json()) == 20, "Intentional failure"
#
#     log_result("test_fail_demo", "FAIL", "User count mismatch")
#
#
# # ---------- TEST RUNNER ----------
#
# def run_tests():
#     test_cases = [
#         test_get_users,
#         test_invalid_endpoint,
#         test_user_schema,
#         test_fail_demo
#     ]
#
#     for test in test_cases:
#         try:
#             test()
#         except AssertionError as e:
#             log_result(test.__name__, "FAIL", str(e))
#
#     return results
#
#
# # ---------- MAIN ----------
#
# if __name__ == "__main__":
#     report = run_tests()
#
#     print("\n🧪 TEST EXECUTION REPORT\n")
#     for r in report:
#         print(r)
#
#     failures = [r for r in report if r["status"] == "FAIL"]
#
#     if failures:
#         print("\n🤖 Sending failures to Gemini AI for analysis...\n")
#
#         ai_report = analyze_report(failures)
#
#         print("===== 🤖 GEMINI AI ANALYSIS REPORT =====\n")
#         print(ai_report)
#
#     else:
#         print("\n✅ All tests passed. No AI analysis required.\n")
#
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
