#!/usr/bin/env python3
"""
San Diego Homelessness Data Analysis Examples

This script demonstrates basic analysis and visualization of the downloaded
homelessness data, including geographic analysis using coordinates.

Author: Yang Liang
Date: 2025
"""

import pandas as pd
import os
import sys

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_data():
    """Load all datasets."""
    print("Loading data...")
    
    shelters = pd.read_csv('../data/raw/sd_shelter_locations.csv')
    pit = pd.read_csv('../data/raw/sd_pit_count_2024.csv')
    evictions = pd.read_csv('../data/raw/sd_eviction_data_2024.csv')
    
    print(f"✓ Loaded {len(shelters)} shelter locations")
    print(f"✓ Loaded {len(pit)} PIT regions")
    print(f"✓ Loaded {len(evictions)} eviction records")
    
    return shelters, pit, evictions


def analyze_capacity():
    """Analyze shelter capacity vs. homeless population."""
    print("\n" + "="*60)
    print("CAPACITY ANALYSIS")
    print("="*60)
    
    shelters, pit, _ = load_data()
    
    # Calculate metrics
    total_capacity = shelters['capacity'].sum()
    total_homeless = pit['total_count'].sum()
    sheltered = pit['sheltered_count'].sum()
    unsheltered = pit['unsheltered_count'].sum()
    
    # Calculate utilization
    utilization = (sheltered / total_capacity) * 100 if total_capacity > 0 else 0
    
    # Calculate gap
    gap = total_homeless - total_capacity
    gap_percentage = (gap / total_homeless) * 100 if total_homeless > 0 else 0
    
    print(f"\nTotal Shelter Capacity:      {total_capacity:,} beds")
    print(f"Total Homeless Population:   {total_homeless:,} people")
    print(f"Currently Sheltered:         {sheltered:,} people")
    print(f"Currently Unsheltered:       {unsheltered:,} people")
    print(f"\nCapacity Utilization:        {utilization:.1f}%")
    print(f"Capacity Gap:                {gap:,} beds ({gap_percentage:.1f}% of need)")
    
    # Breakdown by shelter type
    print("\nShelter Capacity by Type:")
    shelter_types = shelters.groupby('type')['capacity'].sum().sort_values(ascending=False)
    for shelter_type, capacity in shelter_types.items():
        percentage = (capacity / total_capacity) * 100
        print(f"  {shelter_type:30s}: {capacity:4d} beds ({percentage:5.1f}%)")


def analyze_geographic_distribution():
    """Analyze geographic distribution of homelessness."""
    print("\n" + "="*60)
    print("GEOGRAPHIC DISTRIBUTION ANALYSIS")
    print("="*60)
    
    _, pit, _ = load_data()
    
    # Calculate density (homeless per square mile)
    pit['density'] = pit['total_count'] / pit['area_sq_miles']
    pit['unsheltered_rate'] = (pit['unsheltered_count'] / pit['total_count'] * 100)
    
    # Sort by total count
    pit_sorted = pit.sort_values('total_count', ascending=False)
    
    print("\nHomeless Population by Region:")
    print(f"{'Region':<25} {'Total':>8} {'Unsheltered':>12} {'Rate':>8} {'Density':>10}")
    print("-" * 70)
    
    for _, row in pit_sorted.iterrows():
        print(f"{row['region_name']:<25} "
              f"{row['total_count']:>8,} "
              f"{row['unsheltered_count']:>12,} "
              f"{row['unsheltered_rate']:>7.1f}% "
              f"{row['density']:>9.1f}/mi²")
    
    print(f"\n{'TOTAL':<25} {pit['total_count'].sum():>8,} "
          f"{pit['unsheltered_count'].sum():>12,}")


def analyze_evictions():
    """Analyze eviction patterns."""
    print("\n" + "="*60)
    print("EVICTION ANALYSIS")
    print("="*60)
    
    _, _, evictions = load_data()
    
    # Calculate approval rate
    evictions['approval_rate'] = (
        evictions['eviction_judgments'] / evictions['eviction_filings'] * 100
    )
    
    total_filings = evictions['eviction_filings'].sum()
    total_judgments = evictions['eviction_judgments'].sum()
    overall_approval_rate = (total_judgments / total_filings * 100)
    
    print(f"\nTotal Eviction Filings:      {total_filings:,}")
    print(f"Total Eviction Judgments:    {total_judgments:,}")
    print(f"Overall Approval Rate:       {overall_approval_rate:.1f}%")
    
    print("\nEvictions by Neighborhood:")
    print(f"{'Neighborhood':<20} {'ZIP':>6} {'Filings':>8} {'Judgments':>10} {'Rate':>8}")
    print("-" * 60)
    
    evictions_sorted = evictions.sort_values('eviction_filings', ascending=False)
    for _, row in evictions_sorted.iterrows():
        print(f"{row['neighborhood']:<20} "
              f"{row['zip_code']:>6} "
              f"{row['eviction_filings']:>8} "
              f"{row['eviction_judgments']:>10} "
              f"{row['approval_rate']:>7.1f}%")


def calculate_distances():
    """Calculate distances between points using Haversine formula."""
    from math import radians, sin, cos, sqrt, atan2
    
    print("\n" + "="*60)
    print("GEOGRAPHIC DISTANCE ANALYSIS")
    print("="*60)
    
    shelters, pit, _ = load_data()
    
    def haversine(lat1, lon1, lat2, lon2):
        """Calculate distance between two points on Earth (in miles)."""
        R = 3959  # Earth's radius in miles
        
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        
        return distance
    
    # Find average distance from each PIT region to nearest shelter
    print("\nDistance from High-Need Areas to Nearest Shelter:")
    print(f"{'Region':<25} {'Nearest Shelter':<30} {'Distance':>10}")
    print("-" * 70)
    
    for _, region in pit.iterrows():
        min_distance = float('inf')
        nearest_shelter = ""
        
        for _, shelter in shelters.iterrows():
            distance = haversine(
                region['latitude'], region['longitude'],
                shelter['latitude'], shelter['longitude']
            )
            if distance < min_distance:
                min_distance = distance
                nearest_shelter = shelter['name']
        
        print(f"{region['region_name']:<25} "
              f"{nearest_shelter:<30} "
              f"{min_distance:>9.2f} mi")


def generate_summary_statistics():
    """Generate comprehensive summary statistics."""
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    shelters, pit, evictions = load_data()
    
    print("\n📊 Dataset Statistics:")
    print(f"\nShelter Data:")
    print(f"  - Number of facilities: {len(shelters)}")
    print(f"  - Total capacity: {shelters['capacity'].sum():,} beds")
    print(f"  - Average capacity: {shelters['capacity'].mean():.1f} beds")
    print(f"  - Median capacity: {shelters['capacity'].median():.1f} beds")
    print(f"  - Geographic spread: {shelters['latitude'].max() - shelters['latitude'].min():.4f}° lat")
    
    print(f"\nHomeless Population (PIT Count):")
    print(f"  - Total homeless: {pit['total_count'].sum():,}")
    print(f"  - Sheltered: {pit['sheltered_count'].sum():,} ({pit['sheltered_count'].sum()/pit['total_count'].sum()*100:.1f}%)")
    print(f"  - Unsheltered: {pit['unsheltered_count'].sum():,} ({pit['unsheltered_count'].sum()/pit['total_count'].sum()*100:.1f}%)")
    print(f"  - Average per region: {pit['total_count'].mean():.1f}")
    
    print(f"\nEviction Data:")
    print(f"  - Total filings: {evictions['eviction_filings'].sum():,}")
    print(f"  - Total judgments: {evictions['eviction_judgments'].sum():,}")
    print(f"  - Average filings per ZIP: {evictions['eviction_filings'].mean():.1f}")
    print(f"  - Judgment rate: {evictions['eviction_judgments'].sum()/evictions['eviction_filings'].sum()*100:.1f}%")


def export_summary():
    """Export a summary report."""
    print("\n" + "="*60)
    print("EXPORTING SUMMARY REPORT")
    print("="*60)
    
    shelters, pit, evictions = load_data()
    
    # Create summary report
    report = []
    report.append("San Diego Homelessness Data Analysis Report")
    report.append("=" * 60)
    report.append("")
    report.append("SHELTER CAPACITY")
    report.append(f"Total Shelters: {len(shelters)}")
    report.append(f"Total Capacity: {shelters['capacity'].sum():,} beds")
    report.append("")
    report.append("HOMELESS POPULATION")
    report.append(f"Total: {pit['total_count'].sum():,}")
    report.append(f"Sheltered: {pit['sheltered_count'].sum():,}")
    report.append(f"Unsheltered: {pit['unsheltered_count'].sum():,}")
    report.append("")
    report.append("EVICTIONS")
    report.append(f"Total Filings: {evictions['eviction_filings'].sum():,}")
    report.append(f"Total Judgments: {evictions['eviction_judgments'].sum():,}")
    
    # Write to file
    output_path = '../data/analysis_summary.txt'
    with open(output_path, 'w') as f:
        f.write('\n'.join(report))
    
    print(f"✓ Summary report saved to: {output_path}")


def main():
    """Run all analyses."""
    print("\n" + "="*60)
    print("SAN DIEGO HOMELESSNESS DATA ANALYSIS")
    print("="*60)
    
    try:
        analyze_capacity()
        analyze_geographic_distribution()
        analyze_evictions()
        calculate_distances()
        generate_summary_statistics()
        export_summary()
        
        print("\n" + "="*60)
        print("✅ Analysis complete!")
        print("="*60)
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: Data files not found.")
        print(f"   Please run 'download_homelessness_data.py' first to download the data.")
        print(f"   Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
