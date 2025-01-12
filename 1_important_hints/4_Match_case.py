def match_case_usage(data):
    print(f"This commented code will work only the higher versions of the python which start from the 3.10")
    # match data:
    #     case 10:
    #         print(f"integer or constant is checked in the  case - 1 [data = {type(data)}]")
    #     case "pattern":
    #         print(f"string is checked in the case - 2 [data = {type(data)}]")
    #     case "fun" | 200 | [1, 2, 3]:
    #         print(f"str or constant or list is checked in the case - 3  [data = {type(data)}]")
    #     case _:
    #         print(f"If you are in this case that means above all cases are failed")

match_case_usage(10)        
match_case_usage("pattern")
match_case_usage(200)
match_case_usage(400)
