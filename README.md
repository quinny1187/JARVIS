# JARVIS
Project using OpenAI's new assistant functionality.

# Assistant Setup
![image](https://github.com/quinny1187/JARVIS/assets/108108975/4dc81aa8-01b7-4eb9-bb4e-44cbf05b2b51)

# Function 1
I had to click the stock example for the function to be editable. Then I made mine look like this.
![image](https://github.com/quinny1187/JARVIS/assets/108108975/f0f1c013-b3d0-48a3-935e-3802adb61271)

For this function I am using a free api you can get access to from rapidapi that gives basic weather data.
![image](https://github.com/quinny1187/JARVIS/assets/108108975/0cb93317-7661-4f4c-9c2c-571b5aea92f2)

This first method requires you to specify the location where you want the weather from.
Example - Hey Jarvis, can you give me the weather for Los Angeles California today?

# Function 2
I could not get the assistant to work without have at least one parameter for the method so I just pass in the variable q which I do nothing with.
![image](https://github.com/quinny1187/JARVIS/assets/108108975/e6bda380-2a10-4964-873d-8d8b7912675f)

I then use the same api as above but before I do that I call the get my ip method to get my current api which I pass into the api, which in then returns the weather for that area.
Example - Hey Jarvis, can you me the local weather for today?

# Keys
You need to setup an env file with your OpenAPI key, your RapidApi key, and I also put my assistant id in there as well. You can get your assistant id from the url when you create it.

# Output
With functions now you can have it answer things it never could before like so 
![image](https://github.com/quinny1187/JARVIS/assets/108108975/f9e09ddb-1653-4657-9b9b-b5cbe2a251ec)


