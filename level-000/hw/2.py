def digit_converter(a, b, number_position):
    ORIGINAL = a
    to_10 = 0
    to_number_position = 0
    match number_position:
        case 2:
            index = []
            for i in range(-len(a)+1, 1):
                index.append(-i)
            res = []    
            
            for i in range(len(a)):
                res.append(int(a[i]) * (2 ** index[i]))
                 
            result = 0        
            for i in res:
                result += i
            to_number_position = (result) 
        
        case 4:
            index = []
            for i in range(-len(ORIGINAL)+1, 1):
                index.append(-i)
            res = []    
            
            for i in range(len(ORIGINAL)):
                res.append(int(ORIGINAL[i]) * (4 ** index[i]))
                 
            result = 0        
            for i in res:
                result += i
            to_number_position = (result) 
            
        case 8:
            index = []
            for i in range(-len(ORIGINAL)+1, 1):
                index.append(-i)
            res = []    
            
            for i in range(len(ORIGINAL)):
                res.append(int(ORIGINAL[i]) * (8 ** index[i]))
                 
            result = 0        
            for i in res:
                result += i
            to_number_position = (result) 
        
        case 10:
            index = []
            for i in range(-len(ORIGINAL)+1, 1):
                index.append(-i)
            res = []    
            
            for i in range(len(ORIGINAL)):
                res.append(int(ORIGINAL[i]) * (10 ** index[i]))
                 
            result = 0        
            for i in res:
                result += i
            to_number_position = (result) 
        
        case 16:
            index = []
            dict_10_to_16 ={
                "A": 10,
                "B": 11,
                'C': 12,
                "D": 13,
                "E": 14,
                "F": 15
            }
            for i in range(-len(ORIGINAL)+1, 1):
                index.append(-i)
            res = []    
            
            for i in range(len(ORIGINAL)):
                if ORIGINAL[i] in dict_10_to_16:
                    res.append(dict_10_to_16[a[i]] * (16 ** index[i]))
                else:
                    res.append(int(ORIGINAL[i]) * (16 ** index[i]))
            result = 0        
            for i in res:
                result += i
            to_number_position = (result) 
    # ! 10 დან ნებიმსერი პოზიციურ სიტემაში
    match int(b):
        case 2:
            num = []
            while int(a) > 0:
                res = int(a) % 2
                num.append(res) 
                a = int(a) // 2       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            to_10 = (result) 
        case 4:
            num = []
            while int(a) > 0:
                res = int(a) % 4
                num.append(res) 
                a = int(a) // 4       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            to_10 = (result) 
        case 8:
            num = []
            while int(a) > 0:
                res = int(a) % 8
                num.append(res) 
                a = int(a) // 8       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            to_10 = (result)
        case 10:
            num = []
            while int(a) > 0:
                res = int(a) % 10
                num.append(res) 
                a = int(a) // 10     
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            to_10 = (result) 
        case 16:
            num = []
            dict_10_to_16 ={
                10: "A",
                11: "B",
                12: 'C',
                13: "D",
                14: "E",
                15: "F"
            }
            while int(a) > 0:

                res = int(a) % 16

                if res >=10:
                    res = dict_10_to_16[res]
                    
                num.append(res) 
                a = int(a) // 16    
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            to_10 = (result)
    
    return [
        {f"{ORIGINAL} to {b}": to_10},
        {f"{ORIGINAL} to {number_position}": to_number_position}
        ]
        
print(digit_converter("5", "2", 2))
print(digit_converter("110", "4", 4))
print(digit_converter("110", "8", 8))
print(digit_converter("110", "10", 10))
print(digit_converter("110", "16", 16))

# print(digit_converter("110", "16", 16))
# print(digit_converter("10", "4", )) # 22
# print(digit_converter("10", "8")) # 12
# print(digit_converter("10", "10")) # "10"
# print(digit_converter("10", "16")) # "10"
# print(digit_converter("255", "16")) # "10"

def digit_converter_2(a,b):
    arr = []
    while a > 0:
        res = a % b
        arr.append(str(res))
        print(a)
        a = a // b
    return "".join(arr)
print("--------------------------")
print(digit_converter_2(5, 4))