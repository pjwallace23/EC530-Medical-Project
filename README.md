# EC530-Medical-Project
A full stack application focused on database, API and UX implementation


# Branching Strategy
For this project I will use 2 branches: a test branch and a main branch. In the test branch I will implement a workflow through github actions that will run all my unit tests upon each push. Since my project will be done in Python, this will use Pytest. I will use flake8 as my linter. The main branch will only contain modules that have successfully been tested and debugged, and are ready for deployment.

# Project 2
Device and chat modules for patient management care system. Located in "src" folder in chat.py and device.py. Rest APIs hosted using Flask located in device_api.py, hosted on AWS EC2 instance. Device data is stored locally on the EC2 instance using sqlite (relational database), and chat data is stored remotely using MongoDB through pymongo MongoClient. 

API documentation below:
- SendMeasurement: sends a device's measurements in JSON format - /device/send-measurement/<json_files>
- AddUser: adds a chat user to the MongoDB database: /chat/add-user/<first>/<last>/<uid> --> fields are first name, last name, user ID
- SendMessage: sends a message from a user to a receiver using the receiver's user ID: /chat/send-message/<sid>/<rid>/<message> --> fields are sender's ID, receiver's ID, message
- FetchReceivedMessages: fetches all the messages that a user has received through first name and last name: /chat/get-messages/<fist>/<last> --> fields are intuitive
 
All API URL's start with http://ec2-44-201-124-224.compute-1.amazonaws.com
 
# Project 4

