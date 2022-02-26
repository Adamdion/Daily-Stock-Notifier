# Daily-Stock-Notifier
Fun side project I wrote to pull live stock data from yahoo finance and displays a notification of the stocks I am interested in. 

The jupyter notebook file explaines how the code works and is more user friendly to work with. 

The python file (.py) is what we can use to automate this. 

First, open up the file and change the stock_list variable to the ticker symobls that you are interested in. Once you do that save the file and follow the steps below to automate.

## Steps to automate 
1. We need to change the file into an executable file first. To do this open up a text editor and input these lines of code 
          #!/bin/sh
          Python /Users/adamdion/GitHubProjects/stock_notifier_script.py
          neonphotography 
    change the location to where you have the file stored.
2. Copy this file path and open up your terminal and type out "chmod 755" then this file location. This will change the file into an executable
3. Open up Mac Automator and select app.
4. In our work flow we will use Get Specified Finder Item and then add our executable file.
5. Add on Open Finder Item and keep it as Default Application then save it.
6. Open up the Calander app and create a new event
7. Click on the date to open up a larger screen and select alert then go down to Custom...
8. From here we will select open a file select are app at change time to At time of event.
9. When this time hits it will run are app and show us our stocks.
10. Set up repeats so it updates you whenever you want.


And Boom you now have your own stock notifier app on your laptop.


