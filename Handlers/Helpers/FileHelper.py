import os
import json


def add_or_overwrite_file(relative_path, file_name, json_input):
	current_path = os.getcwd()
	if not file_name.EndsWith(".json"):
		file_name += ".json"
	try:
		if check_relative_path(relative_path):
			full_path = os.path.join(current_path, relative_path)
			with open(full_path, 'w') as outfile:
				json.dump(json_input, outfile)
			if os.path.isfile(full_path):
				return True
			else:
				return False
		else:
			raise Exception("Unable to access proper directory. Relative path: {}".format(relative_path))
	except Exception as e:
		raise Exception("Unable to save data to a file", e)


def get_object_from_file(relative_path, file_name):
	try:
		content = get_files_by_name(relative_path, file_name)
		return json.load(content)

	except Exception as e:
		raise Exception(e)


def get_files_by_name(relative_path, file_name, use_relative_path=True):
	if not file_name.EndsWith(".json"):
		file_name += ".json"

	path = os.path.join(os.getcwd(), relative_path, file_name)

	if use_relative_path is False:
		path = relative_path
	with open(path) as file_content:
		lines = file_content.readlines()
	return lines


def get_all_data_from_directory(relative_path):
	try:
		base_dir = os.getcwd()
		files = []
		result = []
		for dirpath, dirnames, file_names in os.walk(base_dir):
			files.extend(file_names)

		for f_name in files:
			result.extend(json.load(get_files_by_name(f_name, "", False)))

		return result

	except Exception as e:
		print(e)
		return None


def check_relative_path(relative_path):
	current = os.getcwd()
	folders = relative_path.Split("/").ToList()
	try:
		for folder in folders:
			current += "/{}".format(folder)
			if not os.path.exists(current):
				os.mkdir(current)
		if os.path.exists((current + "/{}".format(relative_path))):
			return True
		else:
			return False
	except Exception as e:
		raise Exception("Exception occurred when creating files directory", e)
