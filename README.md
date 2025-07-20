AutoRescue – Accident Detection & Emergency Alert Prototype
This is a prototype built using AWS cloud services and a simple frontend to simulate a real-world accident detection and auto-notification
system.

[Workflow Explanation – Prototype Overview]
"This project is a simulation of a smart car emergency response system, designed to detect vehicle accidents and notify nearby hospitals.
Let me explain how it works in this prototype:
Imagine a car accident occurs — in a real-world setup, vehicle sensors would automatically detect critical conditions like:
Chassis vibration (from a crash or collision)
Shape deformation (like a dent or impact damage)
Airbag deployment (a strong signal of a serious accident)
And real-time GPS location (in the future, using services like Amazon Location Service)
In this prototype version, the sensor inputs are simulated manually through a web form. The user selects:
Whether vibration was detected
Whether deformation occurred
Whether the airbag deployed
And selects the accident location from one of three predefined areas:
Location A → Hospital A (example1@gmail.com)
Location B → Hospital B (example2@gmail.com)
Location C → Hospital C (example3@gmail.com)
When the form is submitted, this data is sent to a backend via AWS API Gateway.
API Gateway then triggers an AWS Lambda function, which does the following:
Checks if the conditions meet the criteria for a likely accident:
Any two sensors active
Or airbag deployed
If an accident is detected:
It looks up the nearest hospital email address based on the selected location
Sends an email alert via Amazon SNS to that hospital
Stores all the incident data in Amazon DynamoDB — including location, sensor values, timestamp, and alert status
Even though this is just a prototype, the structure is fully cloud-native and built for scalability. This logic can be easily upgraded to support realtime IoT sensors and GPS-based hospital matching."

[Real-World Implementation Possibility]
"In a real-world implementation, this system would be fully automated.
Here’s what it would look like:
When a car accident occurs, built-in IoT sensors would automatically detect:
Vibration spikes
Physical deformation
Airbag deployment
The car's GPS module would capture the precise accident location
All this data would be sent in real time to AWS IoT Core, which would then forward it to a Lambda function — exactly like in our prototype.
The Lambda function would:
Use Amazon Location Service to identify the nearest real hospital
Automatically send an emergency email or SMS alert using Amazon SNS
Log the entire event in a scalable DynamoDB table
Additional integrations could include:
Notifying the nearest ambulance dispatch center
Alerting emergency contacts (like family or friends)
Automatically creating a case ID for insurance or legal follow-up
So while this project is currently a simulation using hardcoded locations and emails, it is designed to reflect how a real emergency system can
function at scale."

[Tech Stack Used]
AWS Services (Backend):
AWS API Gateway – To receive frontend requests as REST API
AWS Lambda – To process logic and decision making
Amazon SNS – To send email notifications to the nearest hospital
Amazon DynamoDB – To store the incident logs for record keeping
Frontend:
HTML + CSS + JavaScript
Hosted locally (can also be deployed on S3 in production)
Makes a POST request to API Gateway using JavaScript fetch()

Important - Based on the current location of the accident, the nearest hospital is identified and
an alert message is dispatched.
