
def group_by_owners(files):            #def function
    result = {}
    for file, owner in files.items():  # use files.iteritems()
        result[owner] = result.get(owner, []) + [file]
    return result


files = {                           #give files
    "Input.txt": "Randy",
    "Code.py": "Stan",
    "Output.txt": "Randy"
}

print(group_by_owners(files))        #print files