#  print students roles
students = [
        {
            "name" : "Mark", 
            "job" : "Developer",
            "mentor" : "Loise"
        },
        {
            "name" : "John", 
            "job" : "Security",
            "mentor" : "Ann"
        },
        {
            "name" : "Cara",
            "job" : "Health",
            "mentor" : "Mike"
        },
        {
            "name" :"Maggy", 
            "job" :"Chef",
            "mentor" : None
        }
]

for student in students:
    print(
        student["name"], 
        student["job"], 
        student["mentor"], 
        sep=":"
        )
