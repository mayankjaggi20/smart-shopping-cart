# smart-shopping-cart
Implemented a smart shopping cart which uses RFID to scan products as they are put in the cart and shows them on a screen attached to the cart using Raspberry Pi
- Used Python on Raspberry Pi to create a databse and update items in the cart.
- A databse is created with the product info, price and RFID.
- Every time a new RFID comes in contact with the RFID scanner on the cart, it indicates that the item is not present in the cart, so the item associated with that RFID gets added and shows up on the screen.
- Every time an already existing RFID comes in contact with the RFID scanner on the cart, it indicates that the item is already there in the cart and is being taken out. So the item associated with the RFID is deleted from the list and subsequent changes are reflected on the screen attached.
