from pyscript import display 

#This function calculates the average of two input scores
    def computeAverage():
        score1 = int(js.document.getElementById("score1").value)
        score2 = int(js.document.getElementById("score2").value)

        avg = (score1 + score2) / 2

        #Determines if the user passed or failed
        if avg >= 75:
            message = f"Average: {avg:.2f} Passed"
        else:
            message = f"Average: {avg:.2f} Failed"

        js.document.getElementById("result").innerText = message

        email = input('Enter email:')
password = input('Enter password')

if email == "castro.lg@obmontessori.edu.ph": and password == "123456":
    print ('log in succesful')
else:
    print("incorrect email/password")

    
