from other.find_character import FindCharacter
import pytest
import allure

@allure.epic("Поиск самого высокого персонажа по заданным полу и наличию работы")
class TestFindCharacter:

	@allure.description("Поиск персонажа при валидных значениях")
	@pytest.mark.parametrize("gender, is_works", [
		("male", True),
		("Male", False),
		("Female", False),
		("FEMALE", True)
	])
	def test_valid_data(self, gender, is_works):
		result = FindCharacter.search_for_the_highest_by_gender_and_job(gender, is_works)

		assert result["appearance"]["gender"] == gender.title()
		if is_works:
			assert result["work"]["occupation"] != "-"
		else:
			assert result["work"]["occupation"] == "-"

	@allure.description("Поиск персонажа при невалидных значениях параметра 'gender'")
	@pytest.mark.parametrize("gender, is_works, expected_exception, expected_message", [
		("", True, ValueError, "не может быть пустым"),
		(None, False, ValueError, "не может быть None"),
		("aaa", False, ValueError, "'Male' или 'Female'"),
		(123, False, TypeError, "строкой")
	], ids=["Empty", "None", "Other than 'Male' or 'Female'", "Not string"])
	def test_invalid_gender(self, gender, is_works, expected_exception, expected_message):
		with pytest.raises(expected_exception, match=expected_message):
			FindCharacter.search_for_the_highest_by_gender_and_job(gender, is_works)

	@allure.description("Поиск персонажа при невалидных значениях параметра 'is_works'")
	@pytest.mark.parametrize("gender, is_works, expected_exception, expected_message", [
		("male", None, TypeError, "булевым значением"),
		("female", "False", TypeError, "булевым значением"),
	], ids=["None", "Not bool"])
	def test_invalid_is_works(self, gender, is_works, expected_exception, expected_message):
		with pytest.raises(expected_exception, match=expected_message):
			FindCharacter.search_for_the_highest_by_gender_and_job(gender, is_works)