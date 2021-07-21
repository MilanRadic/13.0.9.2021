from django.db import models
#from launchpad.models import ProductionInformation
from datetime import datetime





from django.utils.translation import ugettext as _

COUNTRIES = (
        ('GB', _('United Kingdom')), 
        ('AF', _('Afghanistan')), 
        ('AX', _('Aland Islands')), 
        ('AL', _('Albania')), 
        ('DZ', _('Algeria')), 
        ('AS', _('American Samoa')), 
        ('AD', _('Andorra')), 
        ('AO', _('Angola')), 
        ('AI', _('Anguilla')), 
        ('AQ', _('Antarctica')), 
        ('AG', _('Antigua and Barbuda')), 
        ('AR', _('Argentina')), 
        ('AM', _('Armenia')), 
        ('AW', _('Aruba')), 
        ('AU', _('Australia')), 
        ('AT', _('Austria')), 
        ('AZ', _('Azerbaijan')), 
        ('BS', _('Bahamas')), 
        ('BH', _('Bahrain')), 
        ('BD', _('Bangladesh')), 
        ('BB', _('Barbados')), 
        ('BY', _('Belarus')), 
        ('BE', _('Belgium')), 
        ('BZ', _('Belize')), 
        ('BJ', _('Benin')), 
        ('BM', _('Bermuda')), 
        ('BT', _('Bhutan')), 
        ('BO', _('Bolivia')), 
        ('BA', _('Bosnia and Herzegovina')), 
        ('BW', _('Botswana')), 
        ('BV', _('Bouvet Island')), 
        ('BR', _('Brazil')), 
        ('IO', _('British Indian Ocean Territory')), 
        ('BN', _('Brunei Darussalam')), 
        ('BG', _('Bulgaria')), 
        ('BF', _('Burkina Faso')), 
        ('BI', _('Burundi')), 
        ('KH', _('Cambodia')), 
        ('CM', _('Cameroon')), 
        ('CA', _('Canada')), 
        ('CV', _('Cape Verde')), 
        ('KY', _('Cayman Islands')), 
        ('CF', _('Central African Republic')), 
        ('TD', _('Chad')), 
        ('CL', _('Chile')), 
        ('CN', _('China')), 
        ('CX', _('Christmas Island')), 
        ('CC', _('Cocos (Keeling) Islands')), 
        ('CO', _('Colombia')), 
        ('KM', _('Comoros')), 
        ('CG', _('Congo')), 
        ('CD', _('Congo, The Democratic Republic of the')), 
        ('CK', _('Cook Islands')), 
        ('CR', _('Costa Rica')), 
        ('CI', _('Cote d\'Ivoire')), 
        ('HR', _('Croatia')), 
        ('CU', _('Cuba')), 
        ('CY', _('Cyprus')), 
        ('CZ', _('Czech Republic')), 
        ('DK', _('Denmark')), 
        ('DJ', _('Djibouti')), 
        ('DM', _('Dominica')), 
        ('DO', _('Dominican Republic')), 
        ('EC', _('Ecuador')), 
        ('EG', _('Egypt')), 
        ('SV', _('El Salvador')), 
        ('GQ', _('Equatorial Guinea')), 
        ('ER', _('Eritrea')), 
        ('EE', _('Estonia')), 
        ('ET', _('Ethiopia')), 
        ('FK', _('Falkland Islands (Malvinas)')), 
        ('FO', _('Faroe Islands')), 
        ('FJ', _('Fiji')), 
        ('FI', _('Finland')), 
        ('FR', _('France')), 
        ('GF', _('French Guiana')), 
        ('PF', _('French Polynesia')), 
        ('TF', _('French Southern Territories')), 
        ('GA', _('Gabon')), 
        ('GM', _('Gambia')), 
        ('GE', _('Georgia')), 
        ('DE', _('Germany')), 
        ('GH', _('Ghana')), 
        ('GI', _('Gibraltar')), 
        ('GR', _('Greece')), 
        ('GL', _('Greenland')), 
        ('GD', _('Grenada')), 
        ('GP', _('Guadeloupe')), 
        ('GU', _('Guam')), 
        ('GT', _('Guatemala')), 
        ('GG', _('Guernsey')), 
        ('GN', _('Guinea')), 
        ('GW', _('Guinea-Bissau')), 
        ('GY', _('Guyana')), 
        ('HT', _('Haiti')), 
        ('HM', _('Heard Island and McDonald Islands')), 
        ('VA', _('Holy See (Vatican City State)')), 
        ('HN', _('Honduras')), 
        ('HK', _('Hong Kong')), 
        ('HU', _('Hungary')), 
        ('IS', _('Iceland')), 
        ('IN', _('India')), 
        ('ID', _('Indonesia')), 
        ('IR', _('Iran, Islamic Republic of')), 
        ('IQ', _('Iraq')), 
        ('IE', _('Ireland')), 
        ('IM', _('Isle of Man')), 
        ('IL', _('Israel')), 
        ('IT', _('Italy')), 
        ('JM', _('Jamaica')), 
        ('JP', _('Japan')), 
        ('JE', _('Jersey')), 
        ('JO', _('Jordan')), 
        ('KZ', _('Kazakhstan')), 
        ('KE', _('Kenya')), 
        ('KI', _('Kiribati')), 
        ('KP', _('Korea, Democratic People\'s Republic of')), 
        ('KR', _('Korea, Republic of')), 
        ('KW', _('Kuwait')), 
        ('KG', _('Kyrgyzstan')), 
        ('LA', _('Lao People\'s Democratic Republic')), 
        ('LV', _('Latvia')), 
        ('LB', _('Lebanon')), 
        ('LS', _('Lesotho')), 
        ('LR', _('Liberia')), 
        ('LY', _('Libyan Arab Jamahiriya')), 
        ('LI', _('Liechtenstein')), 
        ('LT', _('Lithuania')), 
        ('LU', _('Luxembourg')), 
        ('MO', _('Macao')), 
        ('MK', _('Macedonia, The Former Yugoslav Republic of')), 
        ('MG', _('Madagascar')), 
        ('MW', _('Malawi')), 
        ('MY', _('Malaysia')), 
        ('MV', _('Maldives')), 
        ('ML', _('Mali')), 
        ('MT', _('Malta')), 
        ('MH', _('Marshall Islands')), 
        ('MQ', _('Martinique')), 
        ('MR', _('Mauritania')), 
        ('MU', _('Mauritius')), 
        ('YT', _('Mayotte')), 
        ('MX', _('Mexico')), 
        ('FM', _('Micronesia, Federated States of')), 
        ('MD', _('Moldova')), 
        ('MC', _('Monaco')), 
        ('MN', _('Mongolia')), 
        ('ME', _('Montenegro')), 
        ('MS', _('Montserrat')), 
        ('MA', _('Morocco')), 
        ('MZ', _('Mozambique')), 
        ('MM', _('Myanmar')), 
        ('NA', _('Namibia')), 
        ('NR', _('Nauru')), 
        ('NP', _('Nepal')), 
        ('NL', _('Netherlands')), 
        ('AN', _('Netherlands Antilles')), 
        ('NC', _('New Caledonia')), 
        ('NZ', _('New Zealand')), 
        ('NI', _('Nicaragua')), 
        ('NE', _('Niger')), 
        ('NG', _('Nigeria')), 
        ('NU', _('Niue')), 
        ('NF', _('Norfolk Island')), 
        ('MP', _('Northern Mariana Islands')), 
        ('NO', _('Norway')), 
        ('OM', _('Oman')), 
        ('PK', _('Pakistan')), 
        ('PW', _('Palau')), 
        ('PS', _('Palestinian Territory, Occupied')), 
        ('PA', _('Panama')), 
        ('PG', _('Papua New Guinea')), 
        ('PY', _('Paraguay')), 
        ('PE', _('Peru')), 
        ('PH', _('Philippines')), 
        ('PN', _('Pitcairn')), 
        ('PL', _('Poland')), 
        ('PT', _('Portugal')), 
        ('PR', _('Puerto Rico')), 
        ('QA', _('Qatar')), 
        ('RE', _('Reunion')), 
        ('RO', _('Romania')), 
        ('RU', _('Russian Federation')), 
        ('RW', _('Rwanda')), 
        ('BL', _('Saint Barthelemy')), 
        ('SH', _('Saint Helena')), 
        ('KN', _('Saint Kitts and Nevis')), 
        ('LC', _('Saint Lucia')), 
        ('MF', _('Saint Martin')), 
        ('PM', _('Saint Pierre and Miquelon')), 
        ('VC', _('Saint Vincent and the Grenadines')), 
        ('WS', _('Samoa')), 
        ('SM', _('San Marino')), 
        ('ST', _('Sao Tome and Principe')), 
        ('SA', _('Saudi Arabia')), 
        ('SN', _('Senegal')), 
        ('RS', _('Serbia')), 
        ('SC', _('Seychelles')), 
        ('SL', _('Sierra Leone')), 
        ('SG', _('Singapore')), 
        ('SK', _('Slovakia')), 
        ('SI', _('Slovenia')), 
        ('SB', _('Solomon Islands')), 
        ('SO', _('Somalia')), 
        ('ZA', _('South Africa')), 
        ('GS', _('South Georgia and the South Sandwich Islands')), 
        ('ES', _('Spain')), 
        ('LK', _('Sri Lanka')), 
        ('SD', _('Sudan')), 
        ('SR', _('Suriname')), 
        ('SJ', _('Svalbard and Jan Mayen')), 
        ('SZ', _('Swaziland')), 
        ('SE', _('Sweden')), 
        ('CH', _('Switzerland')), 
        ('SY', _('Syrian Arab Republic')), 
        ('TW', _('Taiwan, Province of China')), 
        ('TJ', _('Tajikistan')), 
        ('TZ', _('Tanzania, United Republic of')), 
        ('TH', _('Thailand')), 
        ('TL', _('Timor-Leste')), 
        ('TG', _('Togo')), 
        ('TK', _('Tokelau')), 
        ('TO', _('Tonga')), 
        ('TT', _('Trinidad and Tobago')), 
        ('TN', _('Tunisia')), 
        ('TR', _('Turkey')), 
        ('TM', _('Turkmenistan')), 
        ('TC', _('Turks and Caicos Islands')), 
        ('TV', _('Tuvalu')), 
        ('UG', _('Uganda')), 
        ('UA', _('Ukraine')), 
        ('AE', _('United Arab Emirates')), 
        ('US', _('United States')), 
        ('UM', _('United States Minor Outlying Islands')), 
        ('UY', _('Uruguay')), 
        ('UZ', _('Uzbekistan')), 
        ('VU', _('Vanuatu')), 
        ('VE', _('Venezuela')), 
        ('VN', _('Vietnam')), 
        ('VG', _('Virgin Islands, British')), 
        ('VI', _('Virgin Islands, U.S.')), 
        ('WF', _('Wallis and Futuna')), 
        ('EH', _('Western Sahara')), 
        ('YE', _('Yemen')), 
        ('ZM', _('Zambia')), 
        ('ZW', _('Zimbabwe')), 
)    

    

class ReturnReason(models.Model): #Here return reasons are defined
    name = models.CharField(max_length=20, blank=True, null=False, editable=True,default='',  verbose_name="Return reason",primary_key=True) #changed len of name
    description = models.CharField(max_length=100, blank=True, null=True, editable=True, verbose_name="Description")
    
    def __str__(self):
        return str(self.name)

class ReturnState(models.Model): # Here we define in which state the return is 
    name = models.CharField(max_length=20, blank=True, null=False, editable=True, default='', verbose_name="Return state",primary_key=True) # changed len of state name
    description = models.CharField(max_length=100, blank=True, null=True, editable=True, verbose_name="Description")
    
    def __str__(self):
        return str(self.name)

class Customer(models.Model): #Class where we define customer information we display in admin
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name="name")
    surname = models.CharField(max_length=20, blank=True, null=True, verbose_name="surname")
    email = models.EmailField(max_length=40, blank=True, null=False, default='', verbose_name="email", primary_key=True)
    phone_number = models.IntegerField(null=True, blank=True, verbose_name="phone")
    return_address = models.CharField(max_length=100, verbose_name="Return address", null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES, null=True, blank=True) #Dropdown menue for country selection
    reason = models.ForeignKey('ReturnReason', on_delete=models.CASCADE, null=True, blank=True)  
    note = models.CharField(max_length=255, blank=True, null=True, editable=True, verbose_name="Note")
    attachment = models.FileField(upload_to='documents/%y/%m/%D', null=True, blank=True)   #To save files - Settings where you add media_root to the directory where files will be saved

    def __str__(self):
        return str(self.email)

STATUS = (
    ('n', _('New')),
    ('o', _('Old')),
)

class Device(models.Model):
    name_of_device = models.CharField(max_length=100, null=True, editable=True, verbose_name="name of device", blank=True)
    price_of_device = models.DecimalField(max_length=100, blank=True, null=True, editable=True, verbose_name="device price", default='0', max_digits=8, decimal_places=2)
    weight_of_the_device = models.PositiveIntegerField(blank=True, null=True, default='0')
    device_id = models.CharField(max_length=100, blank=True) #ManytoMany key to ProductionInformation DB
    serial_number = models.SlugField(max_length=100, blank=True, null=True, editable=True, verbose_name="serial number")
    gtin = models.PositiveIntegerField(blank=True, verbose_name="gtin")
    status_of_device = models.CharField(max_length=2, blank=True, choices=STATUS, null=True)
    schedule_pick_up = models.BooleanField(verbose_name="Schedule pick up", null=False)
    date_purchase  = models.DateTimeField(blank=True, verbose_name="pick up date")

    def __str__(self):
        return str(self.name_of_device)

class Rma(models.Model): 
    id = models.IntegerField(primary_key=True, verbose_name="RMA number", editable=True) #Primary key
    customer_information = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    device_information = models.ForeignKey('Device', on_delete=models.CASCADE, null=True)
    state = models.ForeignKey('ReturnState', on_delete=models.CASCADE, null=True)
    order_number = models.CharField(max_length=50, blank=False, null=True, editable=True, verbose_name="Order number") 
    date_received = models.DateTimeField(verbose_name="Date received")
 
    
    


    def get_device_id(self):
            return " | ".join([str(p.uuid) for p in self.device_id.all()])

