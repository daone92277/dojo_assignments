#input

# stringList = ['magical','unicorns']
# numList = [1,2,3,4,5,6,7.7]

#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"


mixedList = ['magical unicorns',19,'hello',98.98,'world']    
list_type = None

for val in mixedList:
    print type(val)
    if (type(val) == str):
        print val
        if list_type == None:
             list_type = "String"
    elif list_type == "Integer" or list_type == "Float":
             list_type == "Mixed"

    if (type(val) == int):
        print val
        if list_type == None:
                list_type == "Integer"
    elif list_type == "String" or list_type == "Float":
            list_type == "Mixed"

    elif (type(val) == float):
         print val
         if list_type == None:
                 list_type == "Float"
    elif list_type == "String" or list_type == "Integer":
             list_type == "Mixed"

print list_type
         
