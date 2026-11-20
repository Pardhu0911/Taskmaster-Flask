# TaskMaster

A one-page task list I built to practice handling a web form and saving its contents in SQLite. Open the list, enter a task, and refresh the page to see the saved entry.

**Pardha Saradhi Edupalli** · University of Cincinnati

## Run locally

Run these commands in PowerShell from this project folder with Python 3.12 installed.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python app.py
```

Open <http://127.0.0.1:5000> and select **Open my task list**. All entries share one local list in `instance/test.db`. Tasks can be 1–200 characters long.

Copyright © 2026 Pardha Saradhi Edupalli. [MIT license](LICENSE)
