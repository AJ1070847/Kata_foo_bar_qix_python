Rules = "Rules : \n If the number is divisible by 3, write “Foo” instead of the number,\n If the number is divisible by 5, add “Bar”,\n If the number is divisible by 7, add “Qix” For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order."


def foobar_verifer_divisble(exemple):
    resultat =""

    if int(exemple) % 3 == 0:
        resultat= resultat + "Foo"
    if int(exemple) % 5 == 0 :
        resultat=resultat+"Bar"
    if int(exemple) % 7 == 0 :
        resultat=resultat+ "Qix"
    return resultat



def foobar_verifier_changement(exemple):
    boole=False
    if foobar_verifer_divisble(exemple)!="" :
        boole = True
    decouper_nombre = [int(a) for a in str(exemple)]
    for a in decouper_nombre :
        if (a == 3) or (a == 5) or (a == 7) :
            boole= True
   
    return boole


    
def foo_bar_verifier_presence(exemple) :
    
    decouper_nombre = [int(a) for a in str(exemple)]
    resultat_2=""
    for a in decouper_nombre :
        
        if a == 3: 
            a= "Foo"
            resultat_2=resultat_2 + str(a)
            

        elif a == 5:
            a=  "Bar"
            resultat_2=resultat_2 + str(a)
            

        elif a == 7:
            a =  "Qix"
            resultat_2=resultat_2 + str(a)
        elif a == 0 :
            a= "*"
            resultat_2=resultat_2 + str(a)
            
    return (resultat_2)


def foor_bar_resultat_final(exemple) :
    resultat_final=""
    if foobar_verifier_changement(exemple)==False:
        decouper_nombre = [int(a) for a in str(exemple)]
        for a in decouper_nombre :
            if a == 0 : 
                a =  "*"
            resultat_final=resultat_final + str(a)
        return resultat_final
    else :
        return (foobar_verifer_divisble(exemple) + foo_bar_verifier_presence(exemple) )


nombre_a_tester = 13
print (Rules)
print (f"{nombre_a_tester} => {foor_bar_resultat_final(nombre_a_tester)}")

