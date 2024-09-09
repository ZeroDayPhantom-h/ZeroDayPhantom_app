**ZeroDayPhantom_app**

ZeroDayPhantom_app is a tool designed to perform automated tasks on specified URLs. It utilizes Python and a GUI to facilitate user interaction. This README provides detailed instructions on setting up, running, and using the application.

**Features**
Multithreaded Execution: The script uses multithreading to ensure smooth operation and responsiveness during tasks.
Randomized Headers: Implements random User-Agent and Accept-Language headers to simulate various devices and locales.
Dynamic Statistics: Displays real-time reporting statistics including the number of reports sent and the headers used.
User-Friendly GUI: Built with PyQt5, offering an intuitive interface for inputting URLs and starting tasks.
Output Visualization: Includes a text box for real-time status updates on task progress.

**Prerequisites**
Python: Ensure Python is installed on your system.
Dependencies: Install required Python libraries using:
    pip install requests pyqt5 

**Installation**
Linux & macOS
Clone the repository:

git clone https://github.com/your_username/ZeroDayPhantom_app
Navigate to the projectdirectory:
cd ZeroDayPhantom_app

Run the application:
python ZeroDayPhantom_app.py

**Windows**

Downloadand install Python 3.10 from the Microsoft Store.
Download the repository files (ZeroDayPhantom_app.py and run.bat) and place them in the same directory.
Double-click the run.bat file to execute the tool.
Open the target URL in your browser.
Input the URL into the application and start the process.
**Usage**
Open the Application: Launch the application using run.bat or by running the Python script directly.
Input the Target URL: Enter the URL you want to work with into the provided input field.
Start the Task: Click the button to initiate the task. 
The GUI will display real-time updates on the progress and statistics.
LicenseThis project is licensed under the GNU Affero General Public License (AGPL-3.0).Copyleft: 
Modifications must be distributed under the same license.
Network Interaction: Modified source code must be made available if the software is run on a server and accessed over a network.
Distribution and Use: Freely use, modify, and distribute the software, provided you comply with the license terms
