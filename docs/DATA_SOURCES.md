# San Diego Homelessness Data Sources

## Comprehensive Guide to Data Sources

This document provides detailed information about data sources for homelessness research in San Diego, with emphasis on sources that provide geographic coordinates (latitude/longitude).

## Primary Data Sources

### 1. San Diego Open Data Portal

**Website**: https://data.sandiego.gov  
**API**: https://data.sandiego.gov/api/3/action/  
**Format**: CSV, JSON, GeoJSON  
**Update Frequency**: Varies by dataset

#### Key Datasets:

1. **Affordable Housing Locations**
   - Dataset ID: Available on portal
   - Includes: Location, capacity, type
   - Coordinates: Yes (latitude/longitude)

2. **City Services and Facilities**
   - Includes: Community centers, libraries, public facilities
   - Coordinates: Yes (latitude/longitude)

3. **311 Service Requests**
   - Includes: Homeless-related service calls
   - Coordinates: Often included (address or coordinates)

#### How to Access:

```python
import requests
import pandas as pd

# Example API call
url = "https://data.sandiego.gov/api/3/action/datastore_search"
params = {
    'resource_id': 'your-dataset-id',
    'limit': 100
}

response = requests.get(url, params=params)
data = response.json()
```

### 2. San Diego Regional Task Force on Homelessness (RTFH)

**Website**: https://www.rtfhsd.org  
**Reports**: https://www.rtfhsd.org/data-reports/  
**Format**: PDF reports, Excel spreadsheets  
**Update Frequency**: Annual (PIT count), Quarterly (other metrics)

#### Key Data:

1. **Point-in-Time (PIT) Count**
   - Annual homeless census (typically conducted in January)
   - Breakdown by:
     - Geographic region (City of San Diego, North County, East County, South County)
     - Shelter status (sheltered vs. unsheltered)
     - Demographics (age, gender, race/ethnicity, veteran status)
     - Family composition
     - Chronic homelessness status
   - Coordinates: Regional data can be geocoded

2. **Housing Inventory Count (HIC)**
   - Shelter and housing program inventory
   - Year-round and seasonal beds
   - Program types and capacities
   - Coordinates: Shelter locations available through public records

3. **System Performance Measures**
   - Length of time homeless
   - Returns to homelessness
   - Exits to permanent housing
   - Coordinated by region

#### How to Access:

- Download annual reports from website
- Contact RTFH directly for raw data: info@rtfhsd.org
- Request specific geographic breakdowns
- HUD Exchange also provides PIT data: https://www.hudexchange.info/

### 3. SanGIS (San Diego Geographic Information Source)

**Website**: https://www.sangis.org  
**Data Portal**: https://rdw.sandag.org/  
**Format**: Shapefiles, GeoJSON, File Geodatabase  
**Update Frequency**: Varies by layer

#### Key Layers:

1. **Census Tracts and Block Groups**
   - Geographic boundaries
   - Population demographics
   - Economic indicators

2. **Jurisdictional Boundaries**
   - City limits
   - County boundaries
   - Service districts

3. **Land Use**
   - Zoning
   - Parcel data
   - Building footprints

4. **Transportation**
   - Streets
   - Transit routes
   - Bike paths

#### How to Access:

- Browse data catalog on website
- Download shapefiles directly
- Use GIS software (QGIS, ArcGIS) to open and analyze
- Free registration required for some datasets

### 4. SANDAG (San Diego Association of Governments)

**Website**: https://www.sandag.org  
**Data Portal**: https://rdw.sandag.org/  
**Format**: Various (Excel, CSV, GIS formats)  
**Update Frequency**: Varies by dataset

#### Key Data:

1. **Regional Data Warehouse**
   - Demographics
   - Housing
   - Employment
   - Transportation

2. **Current Estimates**
   - Population projections
   - Employment forecasts
   - Housing unit estimates

3. **Community Profiles**
   - Neighborhood-level statistics
   - Social and economic indicators

### 5. San Diego Housing Commission

**Website**: https://www.sdhc.org  
**Format**: Reports (PDF), Data available upon request  
**Update Frequency**: Annual reports, quarterly updates

#### Key Data:

1. **Affordable Housing Projects**
   - Location and capacity
   - Project types
   - Income restrictions

2. **Housing Choice Voucher Program**
   - Number of vouchers by area
   - Utilization rates

3. **Homeless Programs**
   - Rapid rehousing
   - Housing First programs
   - Permanent supportive housing

### 6. Eviction Data Sources

#### San Diego Superior Court

**Website**: https://www.sdcourt.ca.gov  
**Format**: Court records  
**Access**: Public records request

- Unlawful detainer (eviction) case filings
- Case outcomes
- Filed by ZIP code or address
- Note: Individual case records are public but bulk data requires formal request

#### Eviction Lab (Princeton University)

**Website**: https://evictionlab.org  
**Format**: CSV, API  
**Coverage**: Through 2016 (San Diego County included)

- Historical eviction data
- ZIP code and tract-level aggregations
- Eviction rates and filing rates
- Coordinates: Can be joined with census geography

```python
# Example: Access Eviction Lab API
import requests

url = "https://data.evictionlab.org/api/v1/evictions"
params = {
    'state': 'CA',
    'county': '073',  # San Diego County FIPS code
    'year': '2016'
}

response = requests.get(url, params=params)
data = response.json()
```

### 7. U.S. Department of Housing and Urban Development (HUD)

**Website**: https://www.hudexchange.info  
**Format**: Excel, CSV  
**Update Frequency**: Annual

#### Key Data:

1. **Continuum of Care (CoC) Data**
   - San Diego CoC code: CA-601
   - PIT count data
   - Housing inventory
   - System performance

2. **CoC Geographic Information**
   - Boundary files
   - ZIP codes included in CoC

### 8. 211 San Diego

**Website**: https://211sandiego.org  
**Format**: Service directory (web-based)  
**API**: Contact organization

- Comprehensive service provider database
- Includes homeless services
- Location information available
- Categories: shelters, food, healthcare, etc.

### 9. U.S. Census Bureau

**Website**: https://data.census.gov  
**API**: https://api.census.gov  
**Format**: CSV, API responses  
**Update Frequency**: Annual (ACS), Decennial (Census)

#### Relevant Data:

1. **American Community Survey (ACS)**
   - Poverty rates
   - Housing affordability
   - Rent burden
   - Income distribution
   - Available at: State, County, Census Tract, Block Group levels

2. **TIGER/Line Shapefiles**
   - Census geography boundaries
   - Includes coordinates for all areas

```python
# Example: Access Census API
import requests

api_key = "your-api-key"  # Get free key at census.gov
url = "https://api.census.gov/data/2021/acs/acs5"

params = {
    'get': 'NAME,B25003_001E',  # Total housing units
    'for': 'tract:*',
    'in': 'state:06 county:073',  # CA, San Diego County
    'key': api_key
}

response = requests.get(url, params=params)
data = response.json()
```

## UCSD-Specific Resources

### UCSD Library Data Services

**Website**: https://library.ucsd.edu/  
**Contact**: data-consult@ucsd.edu

- Access to restricted-use datasets
- Consultation services
- Licensed data sources
- GIS support

### San Diego Supercomputer Center (SDSC)

**Website**: https://www.sdsc.edu

- Data storage and computing resources
- Research data archives
- Collaboration opportunities

### UCSD Health Sciences Data

**Contact**: Department of Family Medicine and Public Health

- Public health research data
- Community health assessments
- Social determinants of health

## Additional Resources

### Academic Research Sources

1. **California Health Interview Survey (CHIS)**
   - Website: https://healthpolicy.ucla.edu/chis
   - Regional health data
   - Housing insecurity indicators

2. **California Department of Social Services**
   - Website: https://www.cdss.ca.gov
   - Homeless assistance programs
   - CalWORKs data

3. **California Policy Lab**
   - Website: https://www.capolicylab.org
   - Homelessness research
   - Administrative data analysis

### National Resources

1. **HUD Exchange**
   - https://www.hudexchange.info
   - CoC data and resources
   - System performance measures

2. **U.S. Interagency Council on Homelessness**
   - https://www.usich.gov
   - National strategies and data

3. **National Alliance to End Homelessness**
   - https://endhomelessness.org
   - Research and policy analysis

## Data Integration Tips

### Geocoding Addresses

If you have address data without coordinates, use geocoding services:

```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_application")
location = geolocator.geocode("3350 E St, San Diego, CA 92102")

print(f"Latitude: {location.latitude}")
print(f"Longitude: {location.longitude}")
```

### Joining Data Sources

Common geographic identifiers for joining datasets:

- **Census Tract**: 11-digit FIPS code
- **ZIP Code**: 5-digit code
- **County**: 3-digit FIPS code (San Diego = 073)
- **Latitude/Longitude**: For spatial joins

### Best Practices

1. **Document Data Sources**: Always record where data came from and when
2. **Version Control**: Track data versions and updates
3. **Metadata**: Include variable descriptions and units
4. **Quality Checks**: Validate coordinates are within expected bounds
5. **Privacy**: Aggregate data to protect individual privacy
6. **Citation**: Properly cite all data sources in research

## Coordinate System Information

### WGS84 (EPSG:4326)
- Standard for GPS and web mapping
- Units: Decimal degrees
- Use for: Leaflet, Google Maps, Mapbox

### California State Plane (EPSG:2230)
- San Diego area projection
- Units: U.S. survey feet
- Use for: Local government, engineering

### NAD83 / UTM Zone 11N (EPSG:26911)
- Universal Transverse Mercator
- Units: Meters
- Use for: Regional analysis, distance calculations

## Contact Information

### For Data Requests:

**San Diego Open Data**
- Email: open-data@sandiego.gov

**Regional Task Force on Homelessness**
- Phone: (619) 578-7599
- Email: info@rtfhsd.org

**SanGIS**
- Phone: (858) 874-7000
- Email: sangis@sandag.org

**SANDAG Data Services**
- Phone: (619) 699-1900
- Email: info@sandag.org

**San Diego Housing Commission**
- Phone: (619) 231-9400
- Email: info@sdhc.org

## Update Schedule

This document was last updated: October 5, 2025

For the most current information, always check the official websites listed above.

---

## Appendix: Sample Data Request Template

When requesting data from organizations, use this template:

```
Subject: Data Request for Homelessness Research

Dear [Organization Name],

I am conducting research on homelessness in San Diego County and am requesting 
access to the following data:

Dataset(s) Requested:
- [Specific dataset name]
- [Time period]
- [Geographic coverage]

Intended Use:
- [Brief description of research purpose]

Data Format Preference:
- CSV or Excel with geographic coordinates (latitude/longitude)
- GIS format (shapefile, GeoJSON)

Privacy Considerations:
- Willing to work with aggregated/anonymized data as needed
- Will comply with all data use agreements

Contact Information:
- Name: [Your name]
- Affiliation: [Your institution]
- Email: [Your email]
- Phone: [Your phone]

Thank you for your assistance.

Sincerely,
[Your name]
```
