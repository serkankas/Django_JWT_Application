## Django JSON Web Token "JWT" Application

Hello, I create simple backend for JWT application with, Terminal UI. It's simple yet clear example iMO. The Terminal user interface look like this.

> Terminal

![Picture](/1.png "Terminal Interface")

> The usage

|Option|Usage
|---|---
| Log In/Out |Either Log in or Out with option 1. The credential is given at below, credential section.
| Call API | This API doesn't require authentication. Just to check if you're able to call the api from backend.
| Call API with Authentication | This is an API controlled if it's authenticated or not. You may got 401 Unauthorized application or 500/404 depends on your backend works or not.
| Refresh Token | The JWT works with two different token section. Access and Refresh token. If the tokens need refresh, you can press this option.
| Get Token | Initially, when you logged in the tokens are not captured. However, after logged in. You press this option to set your tokens. To make access the option 3 and 4
| Call API with Permission | This API called and it's gives 200 if either admin or editor user. Normal user cannot perform, which will return 401
| Exit | Closes the program.

Able to start program.
```console
$ python test/test_w_gui.py
```

When you entered the program, you can try based on your purpose. If you try to call __option 3, 4 or 5__, you'll not be able to. Since the credential doesn't set at the first stage. You will get 401 probably. Enter the Option 1 for logged in. The three pre-generated credentials are given at below. Try them with your wish.

|username|password
|---    |---
|adminuser| test12345
|editoruser| test12345
|normaluser| test12345

When you enter with either of the user, or the one you create later on, you will see when you call the __option 3__.

I didn't call refreshing token in every usage of __option_3__. However, I thinks it was the ideal scenario since, the token should be refreshed in every application calls.

> Setup

```console
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python jwt_test/manage.py runserver
```

> Configuration for test_terminal.

I set the url as ```web_url = "http://127.0.0.1:8000"``` in the ___test/test_w_gui.py___. You can change if you plan to run this example in other port or ip.

Token live time based on ___settings.py___. You can change according to your need. Here is the lines that you need to check.
```python
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
```
<hr>
I believe that's it. If you plan to share these notes with anybody, please consider give a credit.<br>
Happy Learning!