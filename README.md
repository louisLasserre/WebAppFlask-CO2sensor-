# nsisensor
Any question --> louis.lasserre33@gmail.com

project : create a CO2 sensor that can tell you if you need to open the windows or not because of the covid.

We were three working on this project, the code of this repository is only my part of the job, wich is:
  -create a web server -> using flask(working with python) that can be accessible by anyone connected to the same internet.
  
  -create a database -> using SQLite3 wich allows me to work with sql on my tables.
  Both need to work at the same timle this is why I used threads
  
  the database is filled up every 15 secondes with data that I receive from my friend using sockets
  the receiving part is in comment but it is only for testing.
  
  database are send to the html pages using the render_templates(page.html, nameOfTheVariableInTheHtml = yourVariable,...,...)
  and then jinja engine allows us to use for loop in the Html
  
  
  it works fine, the display updates but only when you refresh the page so I added jquery to do it automaticaly
  
Any question --> louis.lasserre33@gmail.com
