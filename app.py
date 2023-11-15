import os
from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64
import matplotlib
import pandas as pd
matplotlib.use('Agg')

app = Flask(__name__)

N = 1
tasks = []

def create_gantt_chart(tasks):
    fig, ax = plt.subplots()

    tasks.sort(key=lambda x: x[N])

    for i, (task, start, end) in enumerate(tasks):
        ax.barh(i, end - start, left=start, height=0.5, align='center', color='skyblue', edgecolor='black')
        ax.text(start + (end - start) / 2, i, f"{end - start} hours", ha='center', va='center')

    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task for task, _, _ in tasks])
    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Gantt Chart')
    ax.invert_yaxis()
    ax.yaxis.grid(True)

    # Save the figure to a BytesIO buffer
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='jpeg')
    img_buf.seek(0)

    # Encode the image as base64
    chart_data = base64.b64encode(img_buf.read()).decode('utf-8')

    return chart_data

def save_chart_image(tasks):
    fig, ax = plt.subplots()

    tasks.sort(key=lambda x: x[N])

    for i, (task, start, end) in enumerate(tasks):
        ax.barh(i, end - start, left=start, height=0.5, align='center', color='skyblue', edgecolor='black')
        ax.text(start + (end - start) / 2, i, f"{end - start} hours", ha='center', va='center')

    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task for task, _, _ in tasks])
    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Gantt Chart')
    ax.invert_yaxis()
    ax.yaxis.grid(True)

    img_buf = io.BytesIO()
    fig.savefig(img_buf, format='jpeg')
    img_buf.seek(0)

    # Close the figure explicitly
    plt.close(fig)

    return img_buf

def export_to_excel(tasks):
    df = pd.DataFrame(tasks, columns=['Task', 'Start', 'End'])
    excel_buf = io.BytesIO()
    with pd.ExcelWriter(excel_buf, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Gantt Chart', index=False)
    excel_buf.seek(0)
    return excel_buf

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        start = int(request.form['start'])
        end = int(request.form['end'])

        tasks.append((task, start, end))

    chart_data = create_gantt_chart(tasks)
    return render_template('index.html', chart_data=chart_data)

@app.route('/save_image')
def save_image():
    img_buf = save_chart_image(tasks)
    return send_file(img_buf, mimetype='image/jpeg', as_attachment=True, download_name='gantt_chart.jpg')

@app.route('/export_excel')
def export_excel():
    excel_buf = export_to_excel(tasks)
    return send_file(excel_buf, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', as_attachment=True, download_name='gantt_chart.xlsx')

if __name__ == '__main__':
    app.run(debug=True)

# pip install flask
# pip install matplotlib
# pip install pandas
# pip install xlsxwriter