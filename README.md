# Battery Monitoring System
This is the official repository for battery monitoring system completed for the partial fulfilment of bachelors degree at NIT Calicut.
The dataset used for this project is taken from https://data.matr.io/1/projects/5c48dd2bc625d700019f3204
## Installation of the Monitoring System Web App
Before installing make sure you have succesfully installed Python3.6 or higher and pip. To install the webapp follow the installation procedure below:
1. Clone this repository into your working directory
2. Install all the requirements listed in requirements.txt
3. Navigate to the diectory `MajorProject/webapp/bms`
4. Open `__init__.py` and edit the database uri to your requirements, by default SQLITE will be used
5. Change the secret key if you wish to keep it static (optional)
6. Change the layout of user interface by changing the HTML files in `MajorProject/webapp/bms/templates` (optional)
7. navigate to `MajorProject/webapp` and start the server using `python3 run.py`
## Installation of IoT software (temporary)
Any IoT device with a Battery Management System can be installed with this software. Follow the guidelines below to emulate the working of the IoT device
1. Navigate to `MajorProject/IoT-device`
2. Edit the file `devices.py` and add the token number and endpoint
3. Add additional instances of IoT-device
4. Start the IoT deviice (simulation) using `python3 devices.py`
