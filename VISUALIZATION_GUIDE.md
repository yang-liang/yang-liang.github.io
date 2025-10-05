# Data Visualization Guide

## Visualizing San Diego Homelessness Data

This guide shows how to create visualizations and maps using the downloaded data with geographic coordinates.

## Quick Visualization Examples

### 1. Simple Map with Folium (Python)

```python
import pandas as pd
import folium

# Load shelter data
shelters = pd.read_csv('data/raw/sd_shelter_locations.csv')

# Create map centered on San Diego
m = folium.Map(location=[32.715, -117.161], zoom_start=11)

# Add shelter markers
for _, shelter in shelters.iterrows():
    folium.Marker(
        location=[shelter['latitude'], shelter['longitude']],
        popup=f"<b>{shelter['name']}</b><br>"
              f"Capacity: {shelter['capacity']} beds<br>"
              f"Type: {shelter['type']}",
        icon=folium.Icon(color='blue', icon='home')
    ).add_to(m)

# Save map
m.save('shelter_map.html')
print("Map saved to shelter_map.html")
```

### 2. Homeless Population Heatmap

```python
import pandas as pd
import folium
from folium.plugins import HeatMap

# Load PIT count data
pit = pd.read_csv('data/raw/sd_pit_count_2024.csv')

# Create map
m = folium.Map(location=[32.75, -117.16], zoom_start=11)

# Prepare data for heatmap (lat, lon, weight)
heat_data = [[row['latitude'], row['longitude'], row['total_count']] 
             for _, row in pit.iterrows()]

# Add heatmap
HeatMap(heat_data, radius=20, blur=25, max_zoom=13).add_to(m)

# Add region circles
for _, row in pit.iterrows():
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        radius=row['total_count'] * 2,  # Scale by population
        popup=f"<b>{row['region_name']}</b><br>"
              f"Total: {row['total_count']}<br>"
              f"Unsheltered: {row['unsheltered_count']}",
        color='red',
        fill=True,
        fillOpacity=0.4
    ).add_to(m)

m.save('homeless_heatmap.html')
print("Heatmap saved to homeless_heatmap.html")
```

### 3. Combined Analysis Map

```python
import pandas as pd
import folium

# Load all datasets
shelters = pd.read_csv('data/raw/sd_shelter_locations.csv')
pit = pd.read_csv('data/raw/sd_pit_count_2024.csv')
evictions = pd.read_csv('data/raw/sd_eviction_data_2024.csv')

# Create map
m = folium.Map(location=[32.73, -117.16], zoom_start=12)

# Add layer control
shelter_layer = folium.FeatureGroup(name='Shelters')
homeless_layer = folium.FeatureGroup(name='Homeless Population')
eviction_layer = folium.FeatureGroup(name='Evictions')

# Add shelters
for _, shelter in shelters.iterrows():
    folium.Marker(
        location=[shelter['latitude'], shelter['longitude']],
        popup=f"<b>{shelter['name']}</b><br>Capacity: {shelter['capacity']}",
        icon=folium.Icon(color='green', icon='home', prefix='fa')
    ).add_to(shelter_layer)

# Add homeless areas
for _, region in pit.iterrows():
    folium.CircleMarker(
        location=[region['latitude'], region['longitude']],
        radius=region['total_count'] / 50,
        popup=f"<b>{region['region_name']}</b><br>"
              f"Homeless: {region['total_count']}<br>"
              f"Unsheltered: {region['unsheltered_count']}",
        color='red',
        fill=True,
        fillColor='red',
        fillOpacity=0.6
    ).add_to(homeless_layer)

# Add eviction areas
for _, evict in evictions.iterrows():
    folium.CircleMarker(
        location=[evict['latitude'], evict['longitude']],
        radius=evict['eviction_filings'] / 2,
        popup=f"<b>{evict['neighborhood']}</b><br>"
              f"ZIP: {evict['zip_code']}<br>"
              f"Filings: {evict['eviction_filings']}<br>"
              f"Judgments: {evict['eviction_judgments']}",
        color='orange',
        fill=True,
        fillColor='orange',
        fillOpacity=0.5
    ).add_to(eviction_layer)

# Add layers to map
shelter_layer.add_to(m)
homeless_layer.add_to(m)
eviction_layer.add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

m.save('combined_analysis_map.html')
print("Combined map saved to combined_analysis_map.html")
```

### 4. Statistical Charts with Plotly

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
shelters = pd.read_csv('data/raw/sd_shelter_locations.csv')
pit = pd.read_csv('data/raw/sd_pit_count_2024.csv')

# 1. Shelter capacity by type
fig1 = px.bar(shelters, x='type', y='capacity', 
              title='Shelter Capacity by Type',
              color='type')
fig1.write_html('shelter_capacity.html')

# 2. Homeless population by region
fig2 = px.bar(pit, x='region_name', y=['sheltered_count', 'unsheltered_count'],
              title='Homeless Population by Region',
              labels={'value': 'Count', 'variable': 'Status'},
              barmode='stack')
fig2.write_html('homeless_by_region.html')

# 3. Scatter map of homeless density
fig3 = px.scatter_mapbox(pit, 
                         lat='latitude', lon='longitude',
                         size='total_count',
                         color='unsheltered_count',
                         hover_name='region_name',
                         hover_data=['total_count', 'unsheltered_count'],
                         title='Homeless Population Density',
                         mapbox_style='open-street-map',
                         zoom=10)
fig3.write_html('density_map.html')

print("Charts saved to HTML files")
```

### 5. Using GeoPandas for Advanced Analysis

```python
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Load data
shelters = pd.read_csv('data/raw/sd_shelter_locations.csv')
pit = pd.read_csv('data/raw/sd_pit_count_2024.csv')

# Convert to GeoDataFrames
shelter_gdf = gpd.GeoDataFrame(
    shelters,
    geometry=gpd.points_from_xy(shelters['longitude'], shelters['latitude']),
    crs='EPSG:4326'
)

pit_gdf = gpd.GeoDataFrame(
    pit,
    geometry=gpd.points_from_xy(pit['longitude'], pit['latitude']),
    crs='EPSG:4326'
)

# Create plot
fig, ax = plt.subplots(figsize=(12, 10))

# Plot homeless areas (sized by population)
pit_gdf.plot(ax=ax, 
            column='total_count',
            cmap='YlOrRd',
            markersize=pit_gdf['total_count'] / 5,
            alpha=0.6,
            legend=True,
            legend_kwds={'label': 'Homeless Count'})

# Plot shelters
shelter_gdf.plot(ax=ax,
                marker='^',
                color='blue',
                markersize=100,
                alpha=0.8,
                label='Shelters')

plt.title('San Diego Homeless Services and Population', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.savefig('analysis_map.png', dpi=300, bbox_inches='tight')
print("Map saved to analysis_map.png")
```

## Installation Requirements

### For Folium Maps:
```bash
pip install folium
```

### For Plotly Charts:
```bash
pip install plotly
```

### For GeoPandas Analysis:
```bash
pip install geopandas matplotlib shapely
```

## Output Examples

After running these scripts, you'll have:

1. **shelter_map.html** - Interactive map of shelter locations
2. **homeless_heatmap.html** - Heatmap of homeless population
3. **combined_analysis_map.html** - Layered analysis map
4. **shelter_capacity.html** - Bar chart of capacity by type
5. **homeless_by_region.html** - Stacked bar chart by region
6. **density_map.html** - Scatter mapbox visualization
7. **analysis_map.png** - Static map with GeoPandas

## Online Mapping Alternatives

### Using the Coordinates with Online Tools:

**Google My Maps**:
1. Go to https://www.google.com/mymaps
2. Import the CSV files
3. Google will auto-detect lat/long columns
4. Customize markers and layers

**QGIS (Free GIS Software)**:
1. Download QGIS from https://qgis.org
2. Add Delimited Text Layer
3. Select CSV file and specify lat/long columns
4. Add basemap and style your data

**ArcGIS Online**:
1. Go to https://www.arcgis.com
2. Add CSV as layer
3. Map lat/long fields
4. Create web map

## Next Steps

1. **Add More Data**: Download additional time periods
2. **Create Dashboards**: Build interactive dashboards with Plotly Dash
3. **Time Series**: Animate changes over time
4. **Spatial Analysis**: Calculate buffers, service areas, clusters
5. **Export for Presentations**: Save maps and charts for reports

## Resources

- **Folium Documentation**: https://python-visualization.github.io/folium/
- **Plotly Documentation**: https://plotly.com/python/
- **GeoPandas Documentation**: https://geopandas.org/
- **Leaflet.js** (JavaScript): https://leafletjs.com/
- **D3.js** (JavaScript): https://d3js.org/

---

All visualizations use the latitude/longitude coordinates from the downloaded datasets.
