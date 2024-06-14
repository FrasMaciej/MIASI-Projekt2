from pyecore.resources import ResourceSet, URI
from pyecore.resources.xmi import XMIResource
from pyecore.ecore import EPackage
from faker import Faker
import random

# Create the resource set
rset = ResourceSet()

# Load the custom metamodel
metamodel_path = 'MpMapsMetamodel2.ecore' 
metamodel_resource = rset.get_resource(URI(metamodel_path))
metamodel = metamodel_resource.contents[0]

# Access the EClasses from the metamodel
PMF_Map = metamodel.getEClassifier('PMF_Map')
PMF_Map_Section = metamodel.getEClassifier('PMF_Map_Section')
PMF_Map_Attribute = metamodel.getEClassifier('PMF_Map_Attribute')
PMF_Map_POI = metamodel.getEClassifier('PMF_Map_POI')
PMF_Map_Polygon = metamodel.getEClassifier('PMF_Map_Polygon')
PMF_Map_Polyline = metamodel.getEClassifier('PMF_Map_Polyline')

# Create Faker instance
fake = Faker()

section_id_counter = 1
attribute_id_counter = 1
poi_id_counter = 1
polygon_id_counter = 1
polyline_id_counter = 1

# Create sample PMF_Map instance
pmf_map_instance = PMF_Map(ID=1, FileName='sample_map', Description='This is a sample PMF map')

# Function to generate a section with random data
def generate_section():
    global section_id_counter
    section = PMF_Map_Section(
        ID=section_id_counter,
        Type=fake.word(),
        Name=fake.word(),
        FileSectionNumber=random.randint(1, 100)
    )
    section_id_counter += 1
    return section

# Function to generate attribute with random data
def generate_attribute():
    global attribute_id_counter
    attribute = PMF_Map_Attribute(
        ID=attribute_id_counter,
        Name=fake.word(),
        Value=fake.word(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    attribute_id_counter += 1
    return attribute

# Function to generate POI with random data
def generate_poi():
    global poi_id_counter
    poi = PMF_Map_POI(
        ID=poi_id_counter,
        Name=fake.word(),
        Point=fake.city(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    poi_id_counter += 1
    return poi

# Function to generate polygon with random data
def generate_polygon():
    global polygon_id_counter
    polygon = PMF_Map_Polygon(
        ID=polygon_id_counter,
        Name=fake.word(),
        Polygon=fake.catch_phrase(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    polygon_id_counter += 1
    return polygon

# Function to generate polyline with random data
def generate_polyline():
    global polyline_id_counter
    polyline = PMF_Map_Polyline(
        ID=polyline_id_counter,
        Name=fake.word(),
        Start_level=random.randint(1, 10),
        End_level=random.randint(1, 10),
        LineString=fake.catch_phrase(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    polyline_id_counter += 1
    return polyline

# Generate sample PMF_Map_Section instances and add to PMF_Map
for i in range(50):
    section = generate_section()
    
    # Generate attributes for each section
    for j in range(5):  
        attribute = generate_attribute()
        section.pmf_map_attributes.append(attribute)
    
    # Generate POIs for each section
    for k in range(1):  
        poi = generate_poi()
        section.pmf_map_pois.append(poi)
    
    # Generate polygons for each section
    for l in range(1):
        polygon = generate_polygon()
        section.pmf_map_polygons.append(polygon)
    
    # Generate polylines for each section
    for m in range(1):
        polyline = generate_polyline()
        section.pmf_map_polylines.append(polyline)

    pmf_map_instance.pmf_map_sections.append(section)

# Add instances to the resource set and save
resource = rset.create_resource(URI('sample_data.xmi'))
resource.append(pmf_map_instance)
resource.save()
with open('sample_data.xmi', 'r') as file:
    xmi_data = file.readlines()

# New header as specified
new_header = '''<pmf:PMF_Map
    xmi:version="2.0"
    xmlns:xmi="http://www.omg.org/XMI"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:pmf="http://www.example.org/pmf"
    xsi:schemaLocation="http://www.example.org/pmf path/to/your/MpMapsMetamodel2.ecore"
    FileName="sample_data">
'''

# Replace the header in the XMI data
xmi_data[1] = new_header

# Write the modified data back to the file
with open('sample_data.xmi', 'w') as file:
    file.writelines(xmi_data)