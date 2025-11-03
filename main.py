from pyscript import document, display

def create_order(e):
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    item6 = document.getElementById("item6")

# Get number values
    sci = float(item1.value)
    eng = float(item2.value)
    math = float(item3.value)
    fil = float(item4.value)
    ict = float(item5.value)
    pe = float(item6.value)

    grades = [sci, eng, math, fil, ict, pe]

# Calculate GWA
    total = sum(grades) / 6

# Get first and last name
    FIRST = document.getElementById("Fname").value
    LAST = document.getElementById("Lname").value

# Clear previous results
    document.getElementById("namestuff").innerHTML = ""
    document.getElementById("scistuff").innerHTML = ""
    document.getElementById("engstuff").innerHTML = ""
    document.getElementById("mathstuff").innerHTML = ""
    document.getElementById("filstuff").innerHTML = ""
    document.getElementById("ictstuff").innerHTML = ""
    document.getElementById("pestuff").innerHTML = ""
    document.getElementById("gradestuff").innerHTML = ""

# Display the results for name
    display(f"Name: {FIRST} {LAST}", target="namestuff")

# Display the results for grades
    display(f"Science: {sci:.2f}", target="scistuff")
    display(f"English: {eng:.2f}", target="engstuff")
    display(f"Math: {math:.2f}", target="mathstuff")
    display(f"Filipino: {fil:.2f}", target="filstuff")
    display(f"ICT: {ict:.2f}", target="ictstuff")
    display(f"PE: {pe:.2f}", target="pestuff")

# Display the result for GWA
    display(f"Your General Weighted Average Is: {total:.2f}", target="gradestuff")