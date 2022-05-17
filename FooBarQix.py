from unittest import result


Rules = "Rules : \n If the number is divisible by 3, write “Foo” instead of the number,\n If the number is divisible by 5, add “Bar”,\n If the number is divisible by 7, add “Qix” For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order."


def foobar_get_value_divisible(example):
    result =""

    if int(example) % 3 == 0:
        result= result + "Foo"
    if int(example) % 5 == 0 :
        result=result+"Bar"
    if int(example) % 7 == 0 :
        result=result+ "Qix"
    return result



def foobar_verify_is_foobar(example):
    
    if foobar_get_value_divisible(example)!="" :
        return True
    return ("3" in str(example) or "5" in str(example) or "7" in str(example))


    
def foo_bar_get_value_contains(example) :
    
    split_example = [int(a) for a in str(example)]
    result=""
    for a in split_example :
        
        if a == 3: 
            a= "Foo"
            result=result + str(a)
            

        elif a == 5:
            a=  "Bar"
            result=result + str(a)
            

        elif a == 7:
            a =  "Qix"
            result=result + str(a)
        elif a == 0 :
            a= "*"
            result=result + str(a)
            
    return (result)


def foobar_final_result_display(example) :
    result_final=""
    if foobar_verify_is_foobar(example):
        return (foobar_get_value_divisible(example) + foo_bar_get_value_contains(example) )

        
    split_example = [int(a) for a in str(example)]
    for a in split_example :
        if a == 0 : 
            a =  "*"
        result_final=result_final + str(a)
    return result_final
    
        




