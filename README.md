# **ZeroDayPhantom_app**

ZeroDayPhantom_app is a tool designed to perform automated tasks on specified URLs. It utilizes Python and a GUI to facilitate user interaction. This README provides detailed instructions on setting up, running, and using the application.

## **Features**

- **Multithreaded Execution:** The script uses multithreading to ensure smooth operation and responsiveness during tasks.
- **Randomized Headers:** Implements random User-Agent and Accept-Language headers to simulate various devices and locales.
- **Dynamic Statistics:** Displays real-time reporting statistics, including the number of reports sent and the headers used.
- **User-Friendly GUI:** Built with PyQt5, offering an intuitive interface for inputting URLs and starting tasks.
- **Output Visualization:** Includes a text box for real-time status updates on task progress.

## **Prerequisites**

- **Python:** Ensure Python is installed on your system.
- **Dependencies:** Install the required Python libraries using:

  ```bash
  pip install requests pyqt5
  ```

## **Installation**

### **Linux & macOS**

1. Clone the repository:

   ```bash
   git clone https://github.com/ZeroDayPhantom-h/ZeroDayPhantom_app
   ```

2. Navigate to the project directory:

   ```bash
   cd ZeroDayPhantom_app
   ```

3. Run the application:

   ```bash
   python ZeroDayPhantom_app.py
   ```

### **Windows**

1. Download and install Python 3.10 from the Microsoft Store.
2. Download the repository files (`ZeroDayPhantom_app.py` and `run.bat`) and place them in the same directory.
3. Double-click the `run.bat` file to execute the tool.
4. Open the target URL in your browser.
5. Input the URL into the application and start the process.

## **Usage**

1. **Open the Application:** Launch the application using `run.bat` or by running the Python script directly.
2. **Input the Target URL:** Enter the URL you want to work with into the provided input field.
3. **Start the Task:** Click the button to initiate the task. The GUI will display real-time updates on the progress and statistics.

## **License**

This project is licensed under the [GNU Affero General Public License (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html).

- **Copyleft:** Modifications must be distributed under the same license.
- **Network Interaction:** Modified source code must be made available if the software is run on a server and accessed over a network.
- **Distribution and Use:** Freely use, modify, and distribute the software, provided you comply with the license terms.
