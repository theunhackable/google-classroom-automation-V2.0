# Google Classroom Automation V2.0
## Automating google classroom using google classroom api

Some of you have requested to make a video on how to automate for new class links everyday. This is for you.

## Steps 
### 1. Get credentials.json file
- In this CLI I have used **Google Classroom API**. 
- **Goto** [**Google Classroom API**](https://developers.google.com/classroom/guides/auth)
- Click on **Get an OAuth client ID**
- Create a new Project.
- Give Project a name.
- Click next
- Enter Product name.
- Click next
- You will see Where Are You Calling From option click it and select **Desktop app**
- Click next
- Download client configuration which will gives you a **"credentials.json"** file
- Install google api libraries  using python pipeline (pip)

```python3
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 

```
- Install **pyautogui** using python pipeline (pip)


```python3
pip3 install pyautogui

```
### 2. Download this repository
- Download this repository

### 3. Make small changes as shown in the [video]()


## Packages used
- [json](https://docs.python.org/3/library/json.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- [time](https://docs.python.org/3/library/time.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [calendar](https://docs.python.org/3/library/calendar.html)
- [os](https://docs.python.org/3/library/os.html)
