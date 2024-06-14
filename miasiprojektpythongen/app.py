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

# Create sample PMF_Map instance
pmf_map_instance = PMF_Map(ID=1, FileName='sample_map', Description='This is a sample PMF map')


# Function to generate a section with random data
def generate_section(section_id):
    section = PMF_Map_Section(
        ID=section_id,
        Type=fake.word(),
        Name=fake.word(),
        FileSectionNumber=random.randint(1, 100)
    )
    return section

# Function to generate an attribute with random data
def generate_attribute(attribute_id):
    attribute = PMF_Map_Attribute(
        ID=attribute_id,
        Name=fake.word(),
        Value=fake.word(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    return attribute

# Function to generate a POI with random data
def generate_poi(poi_id):
    poi = PMF_Map_POI(
        ID=poi_id,
        Name=fake.word(),
        Point=fake.word(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    return poi

# Function to generate a polygon with random data
def generate_polygon(polygon_id):
    polygon = PMF_Map_Polygon(
        ID=polygon_id,
        Name=fake.word(),
        Polygon=fake.word(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    return polygon

# Function to generate a polyline with random data
def generate_polyline(polyline_id):
    polyline = PMF_Map_Polyline(
        ID=polyline_id,
        Name=fake.word(),
        Start_level=random.randint(1, 10),
        End_level=random.randint(1, 10),
        LineString=fake.word(),
        Key=fake.word(),
        KeyIdx=random.randint(1, 100)
    )
    return polyline

# Generate sample PMF_Map_Section instances and add to PMF_Map
for i in range(5):  # Generate 5 sections for demonstration
    section = generate_section(i + 1)
    
    # Generate attributes for each section
    for j in range(4):  # Generate 3 attributes for each section
        attribute = generate_attribute(j + 1)
        section.pmf_map_attributes.append(attribute)
    
    # Generate POIs for each section
    for k in range(2):  # Generate 2 POIs for each section
        poi = generate_poi(k + 1)
        section.pmf_map_pois.append(poi)
    
    # Generate polygons for each section
    for l in range(1):  # Generate 2 polygons for each section
        polygon = generate_polygon(l + 1)
        section.pmf_map_polygons.append(polygon)
    
    # Generate polylines for each section
    for m in range(1):  # Generate 2 polylines for each section
        polyline = generate_polyline(m + 1)
        section.pmf_map_polylines.append(polyline)

    pmf_map_instance.pmf_map_sections.append(section)

# Add instances to the resource set and save
resource = rset.create_resource(URI('sample_data.xmi'))
resource.append(pmf_map_instance)
resource.save()

print("Sample data generated and saved to sample_data.xmi")