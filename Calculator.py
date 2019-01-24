##Muataz Badr
## mmb244@usask.ca


import re



## It seems like it was not necessary to create Multiple versions of the code as the REGEX call covers multiple aspects
## of the different questions asked and covers the bonus questions as well.
## odler versions are found at the end of the file.(EDITED)
# VERSION 2 , BONUS QUESTIONS (covers everything)



def Add(nums):
    if not nums:                            ## An empty string acts like a false statement, which means it return False.
        return print(0)

    totalSum = 0
    numsV2 = re.findall("[-]?[0-9]+",nums)

    for x in numsV2:
        # x = x.strip("\n")                    ## NOT necessary as the REGEX call strips the numbers for everything else.
        if int(x) < 0:
            negativeNums = [int(x) for x in numsV2 if int(x)<0]
            raise Exception("Negative numbers are not allowed: {}".format(negativeNums))

        if int(x) > 1000:
            continue
        totalSum += int(x)
    return totalSum









#####################################################################
## Regression testing

test_add = [
    {'inputs' : '//@\n1@3@4@2@5\n@7',
     'outputs':  22,
     'reason' : 'the function should accept new line characters'},

    {'inputs' : '//@,$$,;\n1;3@5$$1001$$100\n;9000@1',
     'outputs': 110,
     'reason' : 'the function should accept multiple delimiters with arbitrary lengths'},

    {'inputs' :'//@@@\n1@@@3@@@5@@@1001@@@100@@@9000@@@1',
     'outputs': 110,
     'reason' : 'the function should accept delimiters with arbitrary lengths'},

    {'inputs' : '""',
     'outputs': 0,
     'reason' : 'It is an empty string'},

    {'inputs' : "1\n,2\n,3\n,4,5",
     'outputs': 15,
     'reason' : 'function should accept new line characters'},

    {'inputs' : "//;\n1\n;2001\n;3053\n;4634;1000",
     'outputs': 1001,
     'reason' : 'any number larger than a 1000 must not be added to the sum.'},



]


for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # checking the results and our expectations
    if Add(args_in) != expected:
            print('Test add: Error in add(): expected SUM', expected,
            ' but found', Add(args_in), '--', t['reason'])








##testing for negative numbers seperately.
test_add_negative = [
    {'inputs' : "1\n,2\n,3\n,4,-5, -3, 2, 1",
     'outputs': 5},

    {'inputs' : "-1\n,-2\n,-3\n,-4,-5",
     'outputs': -15},


     {'inputs' : "-1\n,-2\n,-3\n,-4,-5,5",
     'outputs': -15}

]

for t in test_add_negative:
    args_in = t['inputs']
    expected = t['outputs']

    # checking the results and our expectations
    try:
        if Add(args_in) == expected:
            continue

    except:
        print("function is working, error for \n {",args_in,"} \n pops up as it contains negative numbers.")
        print()
        print()

















#### OLDER VERSIONS OF THE CODE WITH SOME EDITS FOR REFERENCE
##VERSION 1 for question 1 and 2
# numbers = "1\n,2\n,3\n,4,5"
# def Add(nums):
#     totalSum = 0
#     numsSplitted = nums.split(",")
#     print(numsSplitted)
#     for x in numsSplitted:
#         x = x.strip("\n")
#         totalSum += int(x)
#         print(x)
#
#     print(totalSum)
#
# Add(numbers)




#VERSION 1.5 for question 1, 2 , 3 and 4
# ting2 = '//@\n1@3@4@2@5\n@7'
# def Add(nums):
#     if not nums:                            ## An empty string acts like a false statement, which means it return False.
#         return print(0)
#
#     totalSum = 0
#
#     numsV2 = re.findall("[-]?[0-9]+",nums)
#
#     for x in numsV2:
#         # x = x.strip("\n")                    ## NOT necessary as the REGEX call strips the numbers for everything else.
#         if int(x) < 0:
#             negativeNums = [int(x) for x in numsV2 if int(x)<0]
#             raise Exception("Negative numbers are not allowed: {}".format(negativeNums))
#         totalSum += int(x)
#     print(totalSum)
#
# Add(ting2)



