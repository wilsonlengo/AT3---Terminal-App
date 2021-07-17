**Instructions**
<br>
**Step 1: Check Python Version**
<br>
Firstly, check your python vesion to see if it is python3
```
python --version
```
If python is version 3, you are ready to continue!
If not please install python3!
https://installpython3.com
<br>

**Step 3: Initiate virtual environment**

Enter the following command in terminal:
```
source venv/bin/activate
```

**Step 3: Run the Bash Script!**
One thing to check before running the bash script is to check if access is given to execute the script. If access is not given, try this command in terminal:
```
chmod +x ./wrapper.sh
```
Next, run the bash script on terminal:
```
./wrapper.sh
```
This should run the terminal application!
<br>

**Step 3: Welcome to Subway!**

You will welcomed to the application and then it will prompt you to type "Y" or "N" (yes or no) if you want to order. If "Y" entered you will move on to the next step. Otherwise, if "N" is selected the application will exit.

<br>

**Step 4: Choose One item from the menu provided**

A menu will be list in list format and the you will have to type your chosen item in the input. Once typed, you  will be asked if they would want anything from the side menu. By answering "Y", a side menu will be printed out in list format and you will need to type in **one** item from the menu and once enter is hit, you will be asked by the program if you want anything else from the side menu (Y/N). If "Y" is seleted, you will repeat the process again, until you answer "N", in which all the items you've chosen will be added together in a receipt and printed on your screen.

**Step 5: Delivery**
Once the receipt is printed on the screen, you will be asked if you want your order delivery. If you answer "Y", you will be prompted to enter your fullname, address and suburb/postcode. After you've entered your details, it will be printed on your screen as a confirmation. If you answer "N" to delivery, the application will greet you out of the application and it will exit.