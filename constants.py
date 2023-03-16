AllOrigins = {
"British Columbia" : 0,
"Alberta" : 0,
"Ontario" : 0,
"Quebec" : 0,
"Canada Other" : 0,
"Canada Total" : 0,
"Washington" : 0,
"Oregon" : 0,
"California" : 0,
"Arizona" : 0,
"Other Mountain States" : 0,
"Texas" : 0,
"Other Southern States" : 0,
"New York" : 0,
"Midwest States" : 0,
"New England States" : 0,
"Middle Atlantic" : 0,
"South Atlantic" : 0,
"Hawaii/Alaska" : 0,
"US Total" : 0,
"United Kingdom" : 0,
"Germany" : 0,
"France" : 0,
"Nordic Countries" : 0,
"Netherlands" : 0,
"Europe Other" : 0,
"Europe Total" : 0,
"Japan" : 0,
"Taiwan" : 0,
"Hong Kong" : 0,
"Australia" : 0,
"New Zealand" : 0,
"South Korea" : 0,
"China" : 0,
"Asia Pacific Other" : 0,
"Asia Pacific Total" : 0,
"Mexico" : 0,
"Brazil" : 0,
"India" : 0,
"Other Countries" : 0,
"Other Unknown" : 0,
"Other Country Total" : 0,
"Grand Total": 0
}

# List of Province of Canada except BC,AB, ON, QB
OtherCanada = [
    "Manitoba",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Nova Scotia",
    "Prince Edward Island",
    "Saskatchewan",
    "Northwest Territories", 
    "Nunavut",
    "Yukon"
]

# USA Regins
OtherMountainStates = [
    "Colorado",
    "Wyoming",
    "Utah",
    "New Mexico",
    "Nevada",
    "Montana",
    "Idaho"
]
OtherSouthernStates = [
    "Alabama",
    "Arkansas",
    "Kentucky",
    "Louisiana",
    "Maryland",
    "Mississippi", 
    "Oklahoma",
    "Tennessee",
    "Virginia",
    "West Virginia"
]
MidwestStates = [
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Michigan',
    'Minnesota',
    'Missouri',
    'Nebraska',
    'North Dakota',
    'Ohio',
    'South Dakota',
    'Wisconsin'
]
NewEnglandStates = [
    "Maine",
    'New Hampshire', 
    'Vermont', 
    'Massachusetts', 
    'Rhode Island',
    'Connecticut'
]
MiddleAtlantic = [
    'New Jersey',
    'Pennsylvania',
]
SouthAtlantic = [
    'Delaware',
    'Maryland',
    'District of Columbia',
    'Virginia',
    'West Virginia',
    "North Carolina",
    "South Carolina",
    "Florida",
    "Georgia",
]
HawaiiandAlaska = ["Hawaii", "Alaska"]

Australia = [
    "New South Wales", 
    "Victoria", 
    "Queensland", 
    "Western Australia", 
    "South Australia", 
    "Tasmania", 
    "Northern Territory", 
    "Australian Capital Territory",
    "ACT"]
Japan = ['Aichi', 'Akita', 'Aomori', 'Chiba', 'Ehime', 'Fukui', 'Fukuoka', 'Fukushima', 'Gifu', 'Gunma', 'Hiroshima', 'Hokkaido', 'Hyogo', 'Ibaraki', 'Ishikawa', 'Iwate', 'Kagawa', 'Kagoshima', 'Kanagawa', 'Kochi', 'Kumamoto', 'Kyoto', 'Mie', 'Miyagi', 'Miyazaki', 'Nagano', 'Nagasaki', 'Nara', 'Niigata', 'Oita', 'Okayama', 'Okinawa', 'Osaka', 'Saga', 'Saitama', 'Shiga', 'Shimane', 'Shizuoka', 'Tochigi', 'Tokushima', 'Tokyo', 'Tottori', 'Toyama', 'Wakayama', 'Yamagata', 'Yamaguchi', 'Yamanashi']

Mexico = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]

UnitedKingdom = [
    # England
    'Bedfordshire', 'Berkshire', 'Bristol', 'Buckinghamshire', 'Cambridgeshire', 
    'Cheshire', 'Cornwall', 'Cumbria', 'Derbyshire', 'Devon', 'Dorset', 'Durham', 
    'East Sussex', 'Essex', 'Gloucestershire', 'Greater London', 'Greater Manchester', 
    'Hampshire', 'Herefordshire', 'Hertfordshire', 'Isle of Wight', 'Kent', 'Lancashire', 
    'Leicestershire', 'Lincolnshire', 'Merseyside', 'Norfolk', 'North Yorkshire', 
    'Northamptonshire', 'Northumberland', 'Nottinghamshire', 'Oxfordshire', 'Rutland', 
    'Shropshire', 'Somerset', 'South Yorkshire', 'Staffordshire', 'Suffolk', 'Surrey', 
    'Tyne and Wear', 'Warwickshire', 'West Midlands', 'West Sussex', 'West Yorkshire', 
    'Wiltshire', 'Worcestershire',

    # Scotland
    'Aberdeen City', 'Ayrshire', 'Aberdeenshire', 'Angus', 'Argyll & Bute', 'City of Edinburgh', 
    'Clackmannanshire', 'Dumfries and Galloway', 'Dundee City', 'East Ayrshire', 
    'East Dunbartonshire', 'East Lothian', 'East Renfrewshire', 'Eilean Siar', 
    'Falkirk', 'Fife', 'Glasgow City', 'Highland', 'Inverclyde', 'Midlothian', 
    'Moray', 'North Ayrshire', 'North Lanarkshire', 'Orkney Islands', 'Perth and Kinross', 
    'Renfrewshire', 'Scottish Borders', 'Shetland Islands', 'South Ayrshire', 
    'South Lanarkshire', 'Stirling', 'West Dunbartonshire', 'West Lothian',

    # Wales
    'Anglesey', 'Blaenau Gwent', 'Bridgend', 'Caerphilly', 'Cardiff', 'Carmarthenshire', 
    'Ceredigion', 'Conwy', 'Denbighshire', 'Flintshire', 'Gwynedd', 'Merthyr Tydfil', 
    'Monmouthshire', 'Neath Port Talbot', 'Newport', 'Pembrokeshire', 'Powys', 
    'Rhondda Cynon Taf', 'Swansea', 'Torfaen', 'Vale of Glamorgan', 'Wrexham',

    # Northern Ireland
    'Antrim and Newtownabbey', 'Armagh, Banbridge and Craigavon', 'Belfast', 
    'Causeway Coast and Glens', 'Derry and Strabane', 'Fermanagh and Omagh', 
    'Lisburn and Castlereagh', 'Mid and East Antrim', 'Mid Ulster', 'Newry, Mourne and Down'
]

Brazil = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]

