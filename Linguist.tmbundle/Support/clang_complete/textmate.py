# Textmate Interface Module
from os import environ as env

def line():
	return env['TM_LINE_NUMBER']

def column():
	return env['TM_COLUMN_NUMBER']

def filepath():
	return env['TM_FILEPATH']

def debug():
	return False

def current_line():
	return env['TM_CURRENT_LINE']

def current_word(pat=r"[A-Za-z_]*", direction="both"):
	""" Return the current word from the environment.
	
			pat				– A regular expression (as a raw string) matching word characters.
									Typically something like this:	r"[A-Za-z_]*".
			direction – One of "both", "left", "right".	 The function will look in
									the specified directions for word characters.
	"""
	word = ""
	if "TM_SELECTED_TEXT" in env:
		word = env["TM_SELECTED_TEXT"]
	elif "TM_CURRENT_WORD" in env and env["TM_CURRENT_WORD"]:
		line, x = env["TM_CURRENT_LINE"], int(env["TM_LINE_INDEX"])
		# get text before and after the index.
		first_part, last_part = line[:x], line[x:]
		word_chars = re.compile(pat)
		m = word_chars.match(first_part[::-1])
		if m and direction in ("left", "both"):
			word = m.group(0)[::-1]
		m = word_chars.match(last_part)
		if m and direction in ("right", "both"):
			word += m.group(0)
	return word

def config(var):
	if var == 'clang_sort_algo':
		return 'priority'
	elif var == 'clang_user_options':
		return env['CLANG_USER_OPTIONS']
	else:
		return None
