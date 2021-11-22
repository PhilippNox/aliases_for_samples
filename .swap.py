import os, re, sys, math

PATTERN = re.compile("(^\d+)(_.*\.py)")         # ex.: "042_name-of-file.py"
DEFAULT_NEW_NAME = "default_name"               # ex.: "001_default_name.py"
TEST_FILE = "00_test_it.py"

name_for_new_file = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_NEW_NAME

target_files = [PATTERN.match(el) for el in os.listdir('.') if os.path.isfile(el)]
target_data = [(int(el.group(1)), el.group(2), el.string) for el in target_files if el is not None]
target_data.sort(reverse=True)

max_count = math.floor(math.log(target_data[0][0] + 1, 10)) + 1  # ex.: if last file starts with 42 -> 2
if max_count < 2:
    max_count = 2

for match in target_data[:-1]:
    os.rename(match[2], f"{match[0]+1:0{max_count}}{match[1]}")

new_file = f"{1:0{max_count}}_{name_for_new_file}.py"
os.rename(TEST_FILE, new_file)
with open(TEST_FILE, "w") as file:
    file.write("print('use aliases \"py_test\", \"py_swap _\"')\n")

print(f"\t{new_file} - file created")
