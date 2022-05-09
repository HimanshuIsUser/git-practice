import re
s_ng = '''Skip to Main Content

HOME
ABOUT
FORMATS
SERVICES
PORTFOLIO
CONTACT
Know MORE
Franchise Queries
 
About US
The Pocket Cafe
Chai Garam was established in 2008. With a presence in Asia, predominantly India we are currently serving customers through ~150 retail outlets and kiosks. At Chai Garam we provide freshly brewed made to order handmade chai using garden-fresh ingredients. We have been serving tea and quality snacks since 2008 and have served over 5 million cups of tea.

 

Chai Garam offers a wide range of beverages and food items. Serving ~20 types of freshly brewed hand made teas, ~30 flavours of Milk shakes, Coolers and Iced Teas. Our tea is freshly brewed without the use of tea bags or vending machines while our food menu offers a vast assortment of snacks ranging from Pastas, Sandwiches and Omelettes to Parathas & Samosas that are better suited to the India Palate. 

​

Our team at Chai Garam has over 12 years experience in business development and executions. We have successfully set up ~200 cafe, shops and kitchens 


Chai Garam Special Sandwiches
Chai Garam Special Pasta
Chai Garam Nimbu Paani
Chai Garam Mini Pizza.JPG
Chai Garam Special Adrak Elaichi Chai
Chai Garam Special Brownies
Chai Garam Special Mango Shake
Chai Garam Special Puffs
Chai Garam Special Omellette
Chai Garam Special Sandwiches
Chai Garam Special Pasta - Red
Chai Garam Special Sandwiches
Chai Garam Special Cold Coffee
Chai Garam Special Pasta
Chai Garam Special Coffee
Chai Garam Special Hot Chocolate
Chai Garam Special Sandwiches
Chai Garam Special Brownies
Chai Garam Special Lemon Mojito
Chai Garam Special Cold Coffee
Chai Garam Special Pasta White
Chai Garam Special Pasta White
Chai Garam Special Lemo Mojito
Chai Garam Special Blue Mojito
Chai Garam Special Combo
Out of gallery
Chai-Garam-Cafe-.jpg
CHAI GARAM FORMATS
Modular Designs
Chai Garam is a utilitarian based cafe concept. Its theme and design elements although modular and standardized are assiduously designed to allow customization without compromising on quality, value and costs. All outlets are fabricated in our state of the art facility using European modular technology on imported machinery. Only FSSAI approved non-toxic, food grade, asbestos free are used in manufacturing. Outlets are completely electric and no flame/gas or combustible material is used.  Outlets are fully compliant for food, environment, electrical and fire safety.

 

Chai Garam Cafe is operating in several modular formats, customized to fit in a variety of locations including Malls, High Street Markets, Food Courts, Airports, Metro Stations, Hospitals, Universities, Offices & Petrol Pumps

​

​

The popular designer kiosk. Attractively designed to fit in Malls, Lobby's and any indoor setting

Sprawled in full seating style, this is a typical retail shop. Set up in an area of 300-1500 sqft, this space allows for a complete range of products & services.

A chai garam outlet can be operated as a part of another outlet like a Hyper Mart, Super Mart or in a bigger retail space along with other brands.

INDOOR KIOSK
OUTDOOR KIOSK
100% Modular and durable kiosk for an outdoor high-street or university setting. Anti-theft and weather proof.

MOBILE CARTS
Smart and mobile the Chai Garam cart is a stunner. Compact and comes equipped with all utilities to serve hot/cold beverages.

RETAIL OUTLET
SHOP IN SHOP
MICRO ATM KIOSKS
This is particularly useful in Tier 2 cities. The compact cafe can be easily fit into any ATM, Retail Shop or Cafeteria


1/8
INDOOR KIOSK

1/3
OUTDOOR KIOSK

1/14
RETAIL OUTLET

1/5
MOBILE CARTS

1/5
SHOP IN SHOP

1/6
MICRO ATM KIOSKS
 
 
OUR SERVICES
Take the Right First step
Chai Garam is a platform for entrepreneurship. We seek to partner with enterprising, motivated individuals and provide them with an opportunity to become entrepreneurs and grow with us. We are totally committed to make each outlet a success. Let us help you make the right decision in opening a new business and significantly shorten the learning curve. Our team at Chai Garam has over 12 years experience in business development and executions. We have successfully set up ~200 cafe, shops & kitchens

REAL ESTATE
SELECTION
DESIGN
FABRICATION & SET-UP
LOGISTICS
& SUPPLY CHAIN
INTERIORS
ARTWORK
COLLATERAL DESIGNS MARKETING
HR SELECTION TRAINING
FRANCHISEE TRAINING
SUPPORT
IT SYSTEMS DIGITAL INTEGRATION
INVENTORY MANAGEMENT
ONSITE SALES SUPPORT

Chai Garam Cafe.jpeg
OUR PORTFOLIO
Get in touch
 
38939131_535871606846554_446784485355998
LOOKING TO START YOUR OWN CAFE
Contacts Us now to explore models, locations, area, investment size
Contact Us Now
Making
It Happen
himanshub166@gmail.com

himanshub166@gmail.com
Cafes India & Abroad
Cities
Cups of Tea Sold
chai garam cafe.JPG
 
CONTACT US
We'd love to hear from you! 
Name
Phone
Email
Location
Type your message here...

Submit

A 223, Somdatt Chambers 1, Bhikaji Cama PLace, New Delhi 110066

chaigaram@epconsultancy.com

+91 11 26174164 , +91 9599440925

LinkedIn
Facebook
Twitter
YouTube
Instagram
ChaiGaram_City_WEB.jpg
BACK TO TOP
© 2023 by Chai Garam Cafe

'''
# himan = print(s_ng)
# him = re.compile(r'(Body)')
# match = him.finditer(s_ng)
# for matches in match:
#     print(matches)
#.......................................
# t = s_ng.split("Subject")             #its can be correct way but our expertiese are something else..:)
# f = -1
# for i in t:
#     f = f+1
#     if f>0:
#         print(fr'email {f} :- {i} ')
#.......................................
# t=re.compile(r'(Subject)')
# match = re.split(r'(Subject)',s_ng)
# f=-1
# for matches in match:
#     f = f+1
#     if f>0:
#         print(f'Email {f}:- {matches}')
t= re.finditer(r'[0-9a-zA-Z+%]+@+[0-9a-zA-Z+%]+\.+[0-9a-zA-Z]+',s_ng)
# p = t.finditer(s_ng)
f=0
for matches in t:
    f=f+1
    if f>0:
        with open("Email_storing_file.txt",'a') as E:

            E.write(f'\nEmail {f}:- {matches.group()}')
