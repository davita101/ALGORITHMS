def count_bor(a,b,c):
# ? თუ რომელიმე ელემენტი იქნება 0 მაშინ 0 გამოგვიტანოს "number can not be 0"
    if c == 0 or a == 0 or b == 0:
        return "number can not be 0"
    # TODO:  საწყის ელემენტს ვყფოთ ინტრვალზე რათა გავიგოთ რამდენჯერ მოთავდება ჩვენი ინტრვალი ელემენტში ხოლო შემდეგ კი ვამრავლეთ ინერვალზე რათა გავიგოთ მიახლობით პასუხი 
    # TODO: ჩვენს ციფრზე
    start = (a // c) 
    # TODO:  აქაც იგივე რამხდება
    end = (b // c) 
    # * ჩვენ ამ ყველაფერით ვიგებთ თუ რამდნდეჯერ თავსდება ინტერვალები საწყის დასაბოლოო შემთხევაში 
    res =  {"start": (f"{a} // {c} = {a // c} * {c} = {start}"), "end": (f"{b} // {c} = {b // c} * {c} = {end}"), "result": f"(end - start) = {(end - start)} // {c} == {end- start // c}"}
    res_original = (end - start) 
    # todo: ეს იმ შემთხვევაში თუ ჩვენი ციფრი იქნება c -ს ჯერადი
    if (a % c == 0):
        return (end - start) + 1
    return res_original

print(count_bor(3, 11, 3))