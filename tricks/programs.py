def print_sep() -> None:
    """print parameter sep"""
    print("one", "two", "three", sep="\t")

def merging_dictionaries() -> dict:
    """ merging dictionaries """

    a = {"name": "varun", "age": 20}
    b = {"number": "saravanan", "gender": "mela"}
    merging = a | b
    merging2 = {**a, **b}
    return merging2

def calendar_():
    """ calendar """

    import calendar
    return calendar.month(2022, 6)

def current_time() -> str:
    """     current time     """

    from datetime import datetime
    return f"The time now is  {datetime.now().strftime('%H:%M:%S')}"

def descanding_list(list1 :list  =  [53,4,5,11,15,7,100])->list:
    """ descanding list using sort reverse  True  """
    list1.sort(reverse=True)
    return list1
    
def swapping_variables(x:int=20,y:int= 30)->str:
    """ swapping variable using XOR ^  it takes only int """
    # x ,y = y, x #old way
    print(f"Before x {x} and y {y}")
    x ^= y
    y ^= x
    x ^= y
    return f"After  x {x} and y {y}"
    

def counting_occurrences(item:any = 'varun',list1: list =  ["varun","saravanan","sam","varun","bala"])->list:
    """ swapping variable using XOR ^  """
    
    from collections import Counter 
    return f"{item} item in {list1}  is {Counter(list1).get(item)}"


def  flatten(arr:list=[[1,2,3],[4,5,6]])->list:
    """ nasted list into single list   """
    
    # first method
    # new_arr  = []
    # for x in arr:
    #     for y in  x:
    #        new_arr.append(y)
    # return new_arr
    
    #secound method
    # import itertools 
    # return list(itertools.chain.from_iterable(arr))
    
    #third method
    return [    i for j in arr for i in j   ]

def biggest_index(arr:list = [1,2,43,0.2,5,4])->int:
    """     Biggest number in list using enumerate      """
    # easy way of doing 
    # mx = arr.index(max(arr))
    mx = max(enumerate(arr),key=lambda x :x[1])
    return mx 

def separator(num:int = 1000000000)->str:
    """   Adding thousand sepparator  """
    return "{:,}".format(num)


def start_and_end(words: list = ["apple","arving","bala","gnana","await"])->dict:
    "filtering work starts with 'a'"    
    return {
        "starts with": [word for word in words if word.startswith('a')] ,
        "ends with " : [word for word in words if word.endswith('a')]  
    }

