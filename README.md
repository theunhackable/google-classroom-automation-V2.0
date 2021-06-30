# Google Classroom Automation V2.0

[![IMAGE ALT TEXT HERE](https://i9.ytimg.com/vi/NnufWXqpNLI/mqdefault.jpg?v=60d5df46&sqp=CIi-14YG&rs=AOn4CLB8YLRZGrQKAjsDytf-vQD-AWHgIw)](https://www.youtube.com/watch?v=1WwLPcVaYxY&t=1s)
## Automating google classroom using google classroom api
Helloo. Hope You all are safe at home. In the previous version of this project, we are unable to get the fresh meet links for the classrooms as they keep updating from time to time.
Some of you have commented to make a video on automating google classroom login for dynamic links. This video is for you.
I have used Google Classroom API for this process. Some of you do not understand how to use the code in the previous video. In this video I have explained how to use this code. At any case if you are unable to understand any part of this video, feel free to ask in the comment section. 

For the people with G-suit account  I would recommend you to use selinium to automate this process.
If you do not have a g suit account or you are unable to login to your google account through selenium, this is the best way. 
I would like to thank "Koton Bads" who commented about the google client API library. 
If you like this video don't forget to subscribe 😁 ...


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

### 3. Make small changes as shown in the [video](https://youtu.be/NnufWXqpNLI)


## Packages used
- [json](https://docs.python.org/3/library/json.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- [time](https://docs.python.org/3/library/time.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [calendar](https://docs.python.org/3/library/calendar.html)
- [os](https://docs.python.org/3/library/os.html)
- google-api-python-client
- google-auth-httplib2 
- google-auth-oauthlib 
