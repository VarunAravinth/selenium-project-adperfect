from Tkinter import *
import Tkinter as ttk
from ttk import *
 
root = Tk()
root.title("First Website")

 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar1 = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)
argg = ''
argg2=''
argg3=''
choices2 = []
 
# List with options
choices = [ 'default','Services','Rentals','Real Estate','Buy and Sell','Garage Sales & Auctions','Business / Financial','Obituries / Memoriams',
            'Employment','Eduction',
            'Travel & Entertainment','Pets & Animals','Announcements','Automotive','Celebrations','Recteation Vehicles']


tkvar1.set('Services') # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar1, *choices)
Label(mainframe, text="Choose a category").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

popupMenu2= OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text = 'Choose a second Category').grid(row=3,column=1)
popupMenu2.grid(row=4,column=1)

def change_dropdown3(*args):
    print('New change')
    global argg3
    argg2 = tkvar3.get()
    print(argg3)


def change_dropdown2(*args):
    global argg2
    argg2 = tkvar2.get()
    print(argg2)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar1.get())
    global argg
    global choices2
    argg = tkvar1.get()
    if(argg=='Services'):
        choices2 = ['default','Agriculture','Antique Refinishing/Upholstery','Appliance Repair','Art & Custom Framing',
                                'Bakery','Basement Repairs','Basements','Beauty/Health & Medical Services','Bricks & Masonry',
                                'Business Coaching','Business/Consulting Services','Carpentry','Carpet/Duct Cleaning','Carpet/Flooring',
                                'Ceramic Tile','Child Care Offered','Cleaning','Computer Services','Concrete Poured/Precast','Contractors',
                                'Custom Homes','Custom Work','Dating Services','Decks & Fences','Design & Planning & Residential','Doors and Windows',
                                'Driving Instruction','Drywall','Duct Cleaning','Eavestrough','Electrical','Entertainment/Party Services','Equipment Rental',
                                'Excavating','Fireplace/Chimney Services','Florists','Garage Doors','Gardening/Landscaping Services','General Services',
                                'Guitars (Repair)','Handyman','Hauling','Heating / Air conditioning','Home Based Business','Home Improvement','Home Security',
                                'Insulation','Kitchens','Legal /Paralegal Services','Lighting (lights and serv)','Massage Therapy','Moving & Cartage',
                                'Musical/Dance Instruction','New Business','Other services','Painters & Decorators','Paving','Photography','Plumbing',
                                'Pool Services','Pumps (sales and serv)','Renovations & Supplies','Roofing','Rubbish/Junk/Waste','Satellite Sales & Service',
                                'Scrap Metal','Septic','Services for Pets','Services Offered','Sewing Machine Repairs','Sharpening','Siding','Snow Removal',
                                'Tree Services','Utility Sheds','Water Softening/Treatment','Waterproofing','Wedding Services','Welding','Well Drilling/Servicing & Supplies']

    elif(argg=='Rentals'):
        choices2 =['- Choose Classification -','Apartments for Rent','Apartments for Rent - Furnished','Condos/Lofts/Townhouses-Rent',
'Cottages Chalets/Seasonal Rentals','Duplexes for Rent','Executive Rentals','Farm and Farmlands for Rent','Garage for Rent',
'Halls & Meeting Space','Houses for Rent','Land for Rent','Nursing/Senior Homes for Rent','Office/Commercial/Industrial Rent',
'Out of Town Properties-Rent','Rentals Wanted','Room & Board','Rooms for Rent','Shared Accommodation','Storage Space for Rent',
'Student Rentals']
    elif(argg=='Real Estate'):
        choices2 =['- Choose Classification -','Condos/Lofts/Townhouses','Cottages/Vacation Property','Farms and Farmlands','Home For Sale by owner',
'Homes/Townhouses/Duplexes','House For Sale','Land for Sale','Mobile Homes For Sale','Multiplexes','New Homes','Office/Commercial/Industrial',
'Open Houses','Out of Country Properties','Out of Province Properties','Out of Town Properties','Property Appraisals','Property Wanted/Exchange',
'Real Estate Services','Retirement Living','Waterfront Properties']
    elif(argg=='Buy and Sell'):
        choices2=['- Choose Classification -','Antiques & Art Collectibles','Appliances','Building Supplies','Business Equipment & Supplies',
'Cameras & Equipment','Christmas Trees','Computers & Software','Crafts & Hobbies','Firewood, Coal and Oil','Free Ads ($0 - $750)','Furniture',
'Games & Accessories','Health & Beauty Products','Home Electronics','Looking For/Wanted','Machinery & Equipment','Medical & Disability Equipment',
'Miscellaneous','Musical Instruments','Pools  Saunas and Hot Tubs','Produce/Food','Sports Equipment','Tools','Wood Products','Yard & Garden']
    elif(argg=='Garage Sales & Auctions'):
        choices2=['Auction Sales','Garage Sales Rural','Garage Sales/Flea Markets']
    elif(argg=='Business / Financial'):
        choices2=['- Choose Classification -','Accounting and Tax Services','Business For Sale','Business Opportunities','Business Services',
'Business Supplies & Equipment','Capital Available','Financial Services','Industrial & Commercial Space','Insurance','Office & Business Space',
'Trustee in Bankruptcy']
    elif(argg=='Obituries / Memoriams'):
        choices2=['In Memoriams','Obituaries']
    elif(argg=='Employment'):
        choices2 = ['- Choose Classification -','Administrative Office','Automotive Industry','Careers','Caregiver Help/Home Care',
'Casting Services & Agents','Child Care Professionals Wanted','Couriers','Dental Help','Domestic Help / Janitor','Drivers/Transportation',
'Educators','Engineering Opportunities','Estheticians & Stylists','General Help Wanted','Healthcare Professionals','I.T. /Technical Positions',
'Lease Operators','Oilfield Opportunities','Restaurant/Hotel','Sales Help & Agents','Seasonal/Temporary','Security',
'Skilled Trades & Construction']
    elif(argg=='Education'):
        choices2= ['- Choose Classification -','Career Counseling & Resumes','Career Training','Lessons & Classes',
            'Seminars & Workshops','Training','Tutoring']
    elif(argg=='Travel & Entertainment'):
        choices2= ['- Choose Classification -','Bed & Breakfast','Bingo','Camps','Cottages','Cruise/Charters','Fishing/Hunting',
'Hotels and Motels','Outdoor Activities','Personal Development','Resort/Vacation','Seniors Activities','Sports and Rec. Facilities',
'Tickets  Theatre  Concerts','Tours & Travel','Tours & Travel Features']
    elif(argg=='Pets & Animals'):
        choices2=['- Choose Classification -','Birds & Other','Cats','Dogs','Equipment/Services','Farm Machinery & Repairs','Feed & Seed',
'Hay','Horses/Stables','Livestock/Beef','Livestock/Poultry','Pet Announcements','Pet Services - Pets/Agriculture Piller',
'Pets Lost & Found','Supplies']
    elif(argg=='Announcements'):
        choices2= ['- Choose Classification -','Coming Events','Community Calendar','Community Events','Health','Lost and Found',
'Personal Notices','Seniors','Volunteers']
    elif(argg=='Automotive'):
        choices2= ['- Choose Classification -','Antique & Classic Cars','Auto & Truck Leases','Auto Body Repairs/Towing','Auto Parts & Accessories',
'Automotive Services','Autos & Trucks Wanted','Autos for Sale','Autos for Sale Private Party','Commercial Vehicles','Garage and Parking Space',
'Garage Equipment','Heavy Duty Vehicles','Motorcycles','Scooters','Sports Cars & Accessories','SUVs','Trucks and Pick-ups','Vans']
    elif(argg=='Celebrations'):
        choices2=['- Choose Classification -','Adoptions','Anniversaries','Birthdays','Births','Engagements','Graduations','Marriages',
'Retirements','Reunions','Special Occasions']
    elif(argg=='Recteation Vehicles'):
        choices2= ['- Choose Classification -','Aircraft & Flying','All-Terrain Vehicles','Boats Motors Marinas & Supplies',
'Campers Trailers & RVs','Snowmobiles & Equipment']


    popupMenu2= OptionMenu(mainframe, tkvar2, *choices2)
    Label(mainframe, text = 'Choose a second Category').grid(row=3,column=1)
    popupMenu2.grid(row=4,column=1)

    
    
   

#page2 labels
Label(mainframe,text='Title').grid(row=5,column=1)
Entry(mainframe,width=23,textvariable = tkvar3).grid(row=5,column=2)

    
    
 
# link function to change dropdown
tkvar1.trace('w', change_dropdown)
tkvar2.trace('w', change_dropdown2)
tkvar3.trace('w', change_dropdown3)



root.mainloop()
