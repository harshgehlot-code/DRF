# This code snippet is part of a Django REST Framework project
import requests
# This code snippet demonstrates how to make a GET request to the API endpoints defined in the Django project
#  URL = "http://127.0.0.1:8000/stulist/"
URL = "http://127.0.0.1:8000/stuinfo/1"

# The URL points to the student_info endpoint for a student with primary key 1
# You can change the URL to point to the student_list endpoint if you want to fetch all students
reaponse = requests.get(URL)

# The response from the server is stored in the variable 'reaponse'
# The response is expected to be in JSON format, as defined in the Django views
data = reaponse.json()

print(data)