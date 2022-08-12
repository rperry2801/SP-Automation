# SP-Automation

Purpose of this script is to make filling out forms such as the CTO and other share-point files more efficient.
There are a lot of redundant parts to the file that makes filling it out take longer (ex: having to fill out blank spaces with the same answer more than once). This program is meant to automate that process so the airmen using these files can focus on their mission.

The "main.py" file is going to be where the program actually starts or the "program main" once the script is finished, a lot of the front end development will be done in this file so it can be a GUI, and probably end up being the only file deployed once the project is available for deployment.

The "functionality.py" file is the all of the logic and back-end to the program (see https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python)

By the time the program is finished, the user should be able to place the app in the directory their PDFs are in and fill out the CTO file in a much shorter amount of time because they'll only have to type their answers in once, and the GUI will fill out the PDF for them with their given input (including repeating answers). 
