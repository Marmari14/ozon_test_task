import requests

BASE_URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"


class FindCharacter:
	@staticmethod
	def _conversion_to_cm(height):
		num, unit = height.split(" ")
		if unit == 'meters':
			return float(num) * 100
		return float(num)

	@staticmethod
	def search_for_the_highest_by_gender_and_job(gender, is_works):
		if gender is None:
			raise ValueError("Параметр 'gender' является обязательным и не может быть None")
		if not isinstance(gender, str):
			raise TypeError("Параметр 'gender' должен быть строкой")
		if not gender:
			raise ValueError("Параметр 'gender' является обязательным и не может быть пустым")

		if not isinstance(is_works, bool):
			raise TypeError("Параметр 'is_works' должен быть булевым значением")

		gender = gender.title()
		if gender not in ['Male', 'Female']:
			raise ValueError("Пол может быть только 'Male' или 'Female'")
		response = requests.get(f"{BASE_URL}/all.json")

		filter_character = []
		for character in response.json():
			if character["appearance"]["gender"] == gender:
				if is_works:
					if character["work"]["occupation"] != "-":
						filter_character.append(character)
				else:
					if character["work"]["occupation"] == "-":
						filter_character.append(character)

		if not filter_character:
			return None

		tallest_char = None
		max_height = 0
		for character in filter_character:
			height = FindCharacter._conversion_to_cm(character["appearance"]["height"][1])

			if height > max_height:
				max_height = height
				tallest_char = character

		return tallest_char
