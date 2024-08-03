from app_frame import app_frame

#
# Assesment rate
ASSESMENT_RATE = 60 / 100
# Tax rate
TAX_RATE = 72 / 10000

print("       PROPERTY TAX PROGRAMS          ")
print("......................................")
def propertyTax(property_value):
    property_value = float(property_value)
    assesment_value = property_value * ASSESMENT_RATE
    print("assesment value .........................", round(assesment_value,2))
    tax_value = assesment_value * TAX_RATE
    print("tax value       .........................", round(tax_value,2))
app_frame(propertyTax,property_value="")