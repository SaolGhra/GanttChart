<h1>Gantt Chart Web App</h1>

## The Website
![image](https://github.com/SaolGhra/GanttChart/assets/47499708/b64959a4-7374-439d-a132-94235f2b18b6)

## The Image Export
![image](https://github.com/SaolGhra/GanttChart/assets/47499708/7863c4ba-ad3e-4f4a-bd10-e737265a7af3)

## The Excel Export
![image](https://github.com/SaolGhra/GanttChart/assets/47499708/dc4ddec6-2559-4926-bfd9-2316a3d56b2d)


This is a simple web application that allows users to create and visualize Gantt charts. The application is built using Flask for the backend, HTML for the frontend, and CSS for styling. The Gantt chart is generated using the Matplotlib library, and the data can be exported to an Excel spreadsheet using the Pandas library.

## Features
Add Tasks: Enter task details, including the task name, start time, and end time, to dynamically generate a Gantt chart.

Visualize Gantt Chart: The Gantt chart is displayed on the webpage, providing a visual representation of the tasks and their timelines.

Save as Image: Save the generated Gantt chart as a JPEG image for further use or sharing.

Export to Excel: Export the task data to an Excel spreadsheet for more detailed analysis or reporting.

## Dependencies
Ensure you have the following Python packages installed:

```bash
pip install flask
pip install matplotlib
pip install pandas
pip install xlsxwriter
```

## How to Run

Clone the repository:
git clone https://github.com/your-username/your-repository.git

## Navigate to the project directory:
```cd your-repository```

## Run the Flask application:
```python app.py```
Open your web browser and go to http://localhost:5000 to access the Gantt Chart Web App. or click the prompt in the console.


## Usage
- Enter task details in the provided form (task name, start time, and end time).

- Click the "Add Task" button to dynamically update the Gantt chart.

- The Gantt chart, along with "Save as Image" and "Export to Excel" buttons, will be displayed.

- Use the provided buttons to save the chart as an image or export the data to an Excel file.

## License
This project is free to use, modify, and distribute without any restrictions. Feel free to adapt it to your needs.
