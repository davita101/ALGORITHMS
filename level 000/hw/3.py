def five_element ( a, b, c, d, e, f):

    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    if a > f:
                        return a
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
            else:
                if d > e:
                    if d > f:
                        return d
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
        else:
            if c > d:
                if c > e:
                    if c > f:
                        return c
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
            else:
                if d > e:
                    if d > f:
                        return d
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
    else:
        if b > c:
            if b > d:
                if b > e:
                    if b > f:
                        return b
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
            else:
                if d > e:
                    if d > f:
                        return d
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f       
        else:
            if c > d:
                if c > e:
                    if c > f:
                        return c
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
            else:
                if d > e:
                    if d > f:
                        return d
                    else:
                        return f
                else:
                    if e > f:
                        return e
                    else:
                        return f
print(five_element(111,911,3311,4333,4444,35555)) # 6
              
# ? თითოეული ელემენტისთვის შევამოწმებთ, იქნებ თუ არა მეტი ერთი ელემენტი მეორეზე და განვიხლავთ ყველა შემთხვევსითვის