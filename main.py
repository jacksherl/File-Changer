import glob
import shutil

print("Working...\n")

# gathering input files
inputs = glob.glob("inputs/*")
input_names = []

for a in range(len(inputs)):
  input_names.append(inputs[a].split("\\")[1].split(".")[0])

with open("files.txt", "r") as file:
  contents = file.read()
  extensions = contents.split("\n")
  for ex in extensions:
    for f in range(len(inputs)):
      shutil.copy2(inputs[f], "outputs/" + input_names[f] + "." + ex)

print("Done!")