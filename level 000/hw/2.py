def digit_converter(a, b):
    match b:
        case 2:
            num = []
            while a > 0:
                res = a % 2
                num.append(res) 
                a = a // 2       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            return(result) 
        case 4:
            num = []
            while a > 0:
                res = a % 4
                num.append(res) 
                a = a // 4       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            return(result) 
        case 8:
            num = []
            while a > 0:
                res = a % 8
                num.append(res) 
                a = a // 8       
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            return(result)
        case 10:
            num = []
            while a > 0:
                res = a % 10
                num.append(res) 
                a = a // 10     
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            return(result) 
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
            while a > 0:

                res = a % 16

                if res >=10:
                    res = dict_10_to_16[res]
                    
                num.append(res) 
                a = a // 16    
                 
            result = ""        
            for i in num[::-1]:
                result += str(i)
            return(result) 
        
        
print(digit_converter(10, 2)) # 1010
print(digit_converter(10, 4)) # 22
print(digit_converter(10, 8)) # 12
print(digit_converter(10, 10)) # 10
print(digit_converter(10, 16)) # 10
print(digit_converter(255, 16)) # 10