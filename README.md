# REST GUI API — Reflection

Building this application helped me better understand how a desktop interface communicates with a backend API. 
I used Tkinter to create the purchase form, Python to validate user input, and Flask to receive the information 
through an HTTP POST request. The data was packaged as JSON, which allowed the two components to exchange information
in a consistent format.

One thing that surprised me was how much validation could happen before the API was even contacted. I tested the
application three different ways. First, I submitted a valid purchase for $249.99, which worked successfully.
Next, I changed the Product ID and removed ".com" from the email address, which triggered the validation error. 
Finally, I corrected the email but changed the price to $1,500, and the application rejected it as expected.

As the code came together, I started seeing how the GUI and API could operate independently while still communicating. 
I now have a better understanding of client-side validation, JSON serialization, and HTTP requests. I'd like to explore 
how to save these purchases in a database instead of just returning a confirmation.
