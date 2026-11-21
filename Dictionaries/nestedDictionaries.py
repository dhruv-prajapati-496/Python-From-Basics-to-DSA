# Nested Dictionary : Creating a dictionary inside a dictionary
student = {
    "name" : "Dhruv",
    "CGPA" : 8.18,
    "marks" : {
        "TOC" : 4,
        "DBMS" : 9,
        "DA" : 9,
        "IWT" : 8,
    },
    "Chess Rating" : 1270
}
print(student)
print(student["marks"]["DA"]) # To access a value in nested dictionary