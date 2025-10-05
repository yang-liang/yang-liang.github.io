# Quick Start Guide

## Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Download Data

```bash
cd scripts
python3 download_homelessness_data.py
```

This will create:
- `data/raw/sd_shelter_locations.csv` - 5 shelter locations with coordinates
- `data/raw/sd_pit_count_2024.csv` - Homeless count by 5 regions
- `data/raw/sd_eviction_data_2024.csv` - Eviction data for 5 ZIP codes
- `data/metadata/data_sources.json` - Data source metadata
- `data/DOWNLOAD_SUMMARY.txt` - Summary of downloaded data

### Step 3: Run Analysis

```bash
python3 analyze_data.py
```

This will:
- Analyze shelter capacity vs. homeless population
- Show geographic distribution of homelessness
- Analyze eviction patterns
- Calculate distances between shelters and high-need areas
- Generate summary statistics
- Export a summary report to `data/analysis_summary.txt`

## What You'll See

### Sample Output from Analysis:

```
CAPACITY ANALYSIS
============================================================
Total Shelter Capacity:      1,220 beds
Total Homeless Population:   2,594 people
Currently Sheltered:         869 people
Currently Unsheltered:       1,725 people

Capacity Utilization:        71.2%
Capacity Gap:                1,374 beds (53.0% of need)
```

### Sample Data Format:

**Shelter Locations** (`sd_shelter_locations.csv`):
```csv
name,address,latitude,longitude,capacity,type,phone
Father Joe's Villages,"3350 E St, San Diego, CA 92102",32.7095,-117.1292,350,Emergency Shelter,(619) 699-1247
```

All datasets include precise latitude/longitude coordinates for mapping and spatial analysis.

## Next Steps

1. **Explore the data**: Open the CSV files in Excel or your favorite data tool
2. **Read the documentation**: See `README.md` for full documentation
3. **Learn about data sources**: See `docs/DATA_SOURCES.md` for detailed information
4. **Modify the scripts**: Adapt the analysis to your research needs
5. **Create visualizations**: Use the coordinates to create maps with tools like:
   - Python: `folium`, `plotly`, `geopandas`
   - R: `leaflet`, `ggplot2`, `sf`
   - JavaScript: `Leaflet`, `Mapbox`, `D3.js`

## Common Commands

### Download only specific datasets:

```bash
# Only shelter locations
python3 download_homelessness_data.py --dataset shelters

# Only PIT count data
python3 download_homelessness_data.py --dataset pit

# Only eviction data
python3 download_homelessness_data.py --dataset evictions
```

### View help:

```bash
python3 download_homelessness_data.py --help
python3 analyze_data.py --help
```

## Troubleshooting

### Missing pandas module:

```bash
pip install pandas requests
```

### Can't find data files:

Make sure you're in the `scripts/` directory when running the scripts, or adjust the file paths in the scripts.

### Permission denied:

On Linux/Mac, make scripts executable:
```bash
chmod +x scripts/*.py
```

## Project Structure

```
.
├── README.md                          # Full documentation
├── QUICKSTART.md                      # This file
├── requirements.txt                   # Python dependencies
├── scripts/
│   ├── download_homelessness_data.py  # Download script
│   └── analyze_data.py                # Analysis script
├── data/
│   ├── raw/                           # Raw data files
│   ├── metadata/                      # Data source info
│   └── *.txt                          # Summary reports
└── docs/
    └── DATA_SOURCES.md                # Detailed data source docs
```

## Need Help?

- Check the full README: `README.md`
- Review data sources: `docs/DATA_SOURCES.md`
- Open an issue on GitHub
- Email: yliangecon@gmail.com
