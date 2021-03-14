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
6. Change the layout of user interface by changing the HTML files in `MajorProject/webapp/bms/templated` (optional)
7. navigate to `MajorProject/webapp` and start the server using `python3 run.py`
## Installation of IoT software
Please do not clone and deploy the project unless you know what you are doing as the development of this project is still under progress.
