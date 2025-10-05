# San Diego Homelessness Data Repository

This repository contains scripts and data for analyzing homelessness and eviction patterns in San Diego County, with a focus on geospatially-enabled datasets that include precise latitude and longitude coordinates.

## Overview

This project provides tools to download, process, and analyze homelessness-related data from San Diego sources, specifically:

1. **Homeless Shelter Locations** - Physical locations of shelters with capacity information
2. **Point-in-Time (PIT) Count Data** - Annual homeless census by geographic region
3. **Eviction Data** - Eviction filings and judgments by ZIP code

All datasets include geographic coordinates (latitude/longitude) to enable spatial analysis and mapping.

## Project Structure

```
.
├── data/
│   ├── raw/                          # Raw downloaded data
│   │   ├── sd_shelter_locations.csv  # Shelter locations with coordinates
│   │   ├── sd_pit_count_2024.csv     # Point-in-Time homeless count
│   │   └── sd_eviction_data_2024.csv # Eviction data by ZIP code
│   ├── processed/                     # Processed/cleaned data
│   ├── metadata/                      # Data source metadata
│   │   └── data_sources.json         # Information about data sources
│   └── DOWNLOAD_SUMMARY.txt          # Summary of downloaded data
├── scripts/
│   └── download_homelessness_data.py # Main data download script
├── docs/
│   └── DATA_SOURCES.md               # Detailed documentation of data sources
└── README.md                          # This file
```

## Data Sources

### 1. San Diego Open Data Portal
- **URL**: https://data.sandiego.gov
- **Description**: Official city data portal with various datasets
- **Coverage**: San Diego city limits
- **Format**: CSV, JSON (via Socrata API)

### 2. San Diego Regional Task Force on Homelessness (RTFH)
- **URL**: https://www.rtfhsd.org
- **Description**: Coordinates homeless services and conducts annual Point-in-Time counts
- **Coverage**: San Diego County
- **Data**: Annual homeless census, shelter statistics

### 3. SanGIS / SANDAG
- **URL**: https://www.sangis.org
- **Description**: Regional GIS data repository
- **Coverage**: San Diego region
- **Format**: Shapefiles, GeoJSON

### 4. UCSD-Related Sources
While specific UCSD institutional data sources are not directly accessed in this implementation, researchers can access:
- **UCSD Library Data Services**: Provides access to social science datasets
- **San Diego Supercomputer Center**: Hosts regional data archives
- **UCSD School of Medicine**: Public health datasets

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/yang-liang/yang-liang.github.io.git
   cd yang-liang.github.io
   ```

2. **Install required Python packages**:
   ```bash
   pip install pandas requests
   ```

### Optional: Create a virtual environment (recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install pandas requests
```

## Usage

### Download All Datasets

Run the script to download all available datasets:

```bash
cd scripts
python3 download_homelessness_data.py
```

### Download Specific Datasets

Download only specific datasets using the `--dataset` flag:

```bash
# Download only shelter locations
python3 download_homelessness_data.py --dataset shelters

# Download only PIT count data
python3 download_homelessness_data.py --dataset pit

# Download only eviction data
python3 download_homelessness_data.py --dataset evictions
```

### View Help

```bash
python3 download_homelessness_data.py --help
```

## Data Description

### Shelter Locations Dataset

**File**: `data/raw/sd_shelter_locations.csv`

| Column    | Description                                    | Type   |
|-----------|------------------------------------------------|--------|
| name      | Name of the shelter or service provider        | string |
| address   | Full street address                            | string |
| latitude  | Latitude coordinate (WGS84)                    | float  |
| longitude | Longitude coordinate (WGS84)                   | float  |
| capacity  | Number of beds/spaces available                | int    |
| type      | Type of facility (Emergency, Transitional, etc)| string |
| phone     | Contact phone number                           | string |

**Example Data**:
```csv
name,address,latitude,longitude,capacity,type,phone
Father Joe's Villages,"3350 E St, San Diego, CA 92102",32.7095,-117.1292,350,Emergency Shelter,(619) 699-1247
```

### Point-in-Time Count Dataset

**File**: `data/raw/sd_pit_count_2024.csv`

| Column              | Description                           | Type   |
|---------------------|---------------------------------------|--------|
| region_name         | Name of geographic region             | string |
| region_code         | Short code for region                 | string |
| year                | Year of count                         | int    |
| unsheltered_count   | Number of unsheltered homeless        | int    |
| sheltered_count     | Number of sheltered homeless          | int    |
| total_count         | Total homeless count                  | int    |
| latitude            | Center latitude of region (WGS84)     | float  |
| longitude           | Center longitude of region (WGS84)    | float  |
| area_sq_miles       | Area of region in square miles        | float  |

**Example Data**:
```csv
region_name,region_code,year,unsheltered_count,sheltered_count,total_count,latitude,longitude,area_sq_miles
Downtown San Diego,DT,2024,845,423,1268,32.7157,-117.1611,1.7
```

### Eviction Data Dataset

**File**: `data/raw/sd_eviction_data_2024.csv`

| Column              | Description                           | Type   |
|---------------------|---------------------------------------|--------|
| zip_code            | 5-digit ZIP code                      | string |
| neighborhood        | Neighborhood name                     | string |
| year                | Year of data                          | int    |
| month               | Month of data                         | string |
| eviction_filings    | Number of eviction cases filed        | int    |
| eviction_judgments  | Number of evictions granted           | int    |
| latitude            | Center latitude of ZIP code (WGS84)   | float  |
| longitude           | Center longitude of ZIP code (WGS84)  | float  |

**Example Data**:
```csv
zip_code,neighborhood,year,month,eviction_filings,eviction_judgments,latitude,longitude
92101,Downtown,2024,January,45,32,32.7157,-117.1611
```

## Data Quality and Limitations

### Important Notes

1. **Sample Data**: The current datasets are demonstration/sample datasets based on publicly available information and typical data structures. For production analysis, you should:
   - Connect to live APIs from San Diego Open Data Portal
   - Obtain official data from the Regional Task Force on Homelessness
   - Access court records through official channels for eviction data

2. **Coordinate System**: All latitude/longitude coordinates use the WGS84 datum (EPSG:4326), which is the standard for GPS and web mapping applications.

3. **Privacy**: Some data has been aggregated or anonymized to protect individual privacy while maintaining analytical utility.

4. **Currency**: Always check the `download_date` in `data/metadata/data_sources.json` to know when data was last updated.

## Analysis Suggestions

### Spatial Analysis

With latitude/longitude coordinates, you can:

1. **Mapping**: Create interactive maps showing shelter locations and homeless populations
2. **Distance Analysis**: Calculate distances between shelters and high-need areas
3. **Clustering**: Identify spatial clusters of homelessness
4. **Correlation Studies**: Analyze relationships between evictions and homelessness by area

### Example Python Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load shelter data
shelters = pd.read_csv('data/raw/sd_shelter_locations.csv')

# Load PIT count data
pit = pd.read_csv('data/raw/sd_pit_count_2024.csv')

# Calculate capacity vs. need
total_capacity = shelters['capacity'].sum()
total_homeless = pit['total_count'].sum()
sheltered = pit['sheltered_count'].sum()

print(f"Total Shelter Capacity: {total_capacity}")
print(f"Total Homeless: {total_homeless}")
print(f"Currently Sheltered: {sheltered}")
print(f"Capacity Utilization: {sheltered/total_capacity*100:.1f}%")
```

### Visualization Recommendations

- **Folium**: Create interactive web maps
- **GeoPandas**: Spatial data manipulation
- **Plotly**: Interactive charts and maps
- **Seaborn**: Statistical visualizations

## Accessing Live Data

### San Diego Open Data Portal API

The city provides a Socrata API for programmatic access:

```python
import requests

# Example: Access datasets through Socrata API
base_url = "https://data.sandiego.gov/api/3/action/"
dataset_id = "your-dataset-id"

response = requests.get(f"{base_url}datastore_search?resource_id={dataset_id}")
data = response.json()
```

### RTFH Data Requests

For official Point-in-Time count data:
- Visit: https://www.rtfhsd.org/data-reports/
- Email: info@rtfhsd.org
- Request specific years or geographic breakdowns

## Future Enhancements

Potential improvements to this project:

1. **Real-time Data**: Connect to live API endpoints
2. **Automated Updates**: Schedule regular data downloads
3. **Data Validation**: Implement quality checks
4. **Additional Sources**: 
   - 211 San Diego service provider data
   - HUD Point-in-Time count data
   - San Diego Housing Commission data
5. **Analysis Notebooks**: Jupyter notebooks with example analyses
6. **Web Dashboard**: Interactive visualization dashboard

## Contributing

To add new data sources or improve the scripts:

1. Fork the repository
2. Create a feature branch
3. Add your changes with clear documentation
4. Submit a pull request

## Resources

### Key Organizations

- **Regional Task Force on Homelessness**: https://www.rtfhsd.org
- **San Diego Housing Commission**: https://www.sdhc.org
- **211 San Diego**: https://211sandiego.org
- **Father Joe's Villages**: https://www.neighborslink.org
- **San Diego Rescue Mission**: https://www.sdrescue.org

### Research Resources

- **UCSD Homeless Research**: Contact the School of Medicine or Social Sciences
- **San Diego Association of Governments (SANDAG)**: https://www.sandag.org
- **San Diego Data Library**: https://www.sandiegodatalibrary.org

## License

This project is for educational and research purposes. Please respect the terms of use for each data source and properly attribute data in any publications or presentations.

## Contact

For questions or collaboration opportunities:
- Repository: https://github.com/yang-liang/yang-liang.github.io
- Email: yliangecon@gmail.com

## Changelog

### 2025-10-05
- Initial repository setup
- Created data download script
- Added sample datasets for shelters, PIT counts, and evictions
- Documented data sources and usage instructions

---

**Note**: This is a demonstration repository showing how to structure a homelessness data analysis project. For actual research or policy work, always use official, verified data sources and follow appropriate data use agreements.
