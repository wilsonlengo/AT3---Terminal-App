# **Software Development Plan**



### **_Statement of Purpose_**

####
The purpose of this terminal application is for the user to build their custom "sub" from Subway via user input and ingredients can be referenced via a dictionary. Essentially, this is replicating a typically Subway store visit in real time, except this interaction is simulated with my terminal application. Essentially users can simulate a custom "sub" creation so that they get an idea of what they want to buy before going to the real store to buy it. The intended audience of this application are those who enjoy Subway on the regular and even those who want to know what it feels like to visit Subway.

### **_Application features_**

#### 
* Welcome feature
* Menu 
* Side menu
* Custom Sub Builder
* Price output/ Receipt Generator
* Delivery


### **_Outline_**
#### 
The intended user experience is that firstly, the application will welcome the user and then a menu will pop up with each step in building the sub, and the user will choose their ingredients with user input, but can only choose the ingredients available to them. Once their sub has been built, the application will ask if the user would want any additions from the side menu such as a drink or cookies. Next, the total price is calculated and a receipt is printed on the screen. After that, the user would be prompted to if they want their order delivered or not. If they want their order delivered, they would they would be prompted to type in their information and this information will be saved and stored in a database.



# **Implementation Plan**
### **_Welcome Feature (lowest priority)_**
The "Welcome to Subway" message will be printed out in (hopefully) block letters with an imported module.
**Deadline:** Saturday

### **_Menu + Side Menu + Sub Creation (top priority)_**
I intend on creating the menu and side menu with dictionaries. Each step of the creation process will display the ingredients available to be chosen by the user and these available ingredients will be stored inside a dictionary inside the main dictionary. Throughout each step of the creation process, I will include the input function, so that the user will be able to type in what they want in their "sub". The side menu will have its own dictionary wheres the users can refer to later on after creating their "sub" and this will also require the user input function.
**Deadline:** Thursday

### **_Price Output (second priority)_** 
The price output will be calculted with a function(def), which takes all variables such as user input and adds up all chosen ingredients and extra additions on the side
**Deadline:** Friday

### **_Receipt Generator (third priority)_**
The receipt generator will take the price output and print it on the user's screen
**Deadline:** Friday

### **_Delivery (fourth priority)_**
This delivery function will take user input and save the user input inside a database. If the user input already exists, the user won't need to re-enter their details.
**Deadline:** Friday




 
