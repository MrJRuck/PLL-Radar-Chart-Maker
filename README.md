# PLL Player Radar Chart Maker
#### Video Demo: https://youtu.be/lSf0LfJhF5A

## Project Overview
This project allows users to visualize the performance of a lacrosse player by generating a radar chart of their statistics. The radar chart provides a quick and clear way to assess a player’s strengths relative to others in their position.

## Features
- Generates radar charts to visualize player stats.
- Player stats are compared only against others in the same position.
- Stats are normalized on a scale of 0 to 100 using linear transformation.
- Custom radar charts are based on position-specific metrics important to the player's role.

## Requirements
The following Python libraries are required to run the program:
- `plotly.express`
- `pandas`
- `sys`
- `pytest` (for running tests)

Additionally, a dataset containing PLL (Premier Lacrosse League) player statistics is needed. This dataset can be downloaded from the PLL website.

## Usage
1. Run the program:
    ```bash
    python radar_chart_maker.py
    ```
2. Input a valid first and last name of an active PLL player when prompted.
3. The program will generate a radar chart that visually represents the player's performance across key stats.

## Program Workflow
1. **Data Loading**: The program reads the PLL stats dataset using `pandas` and creates a DataFrame.
2. **Player Selection**: The user provides a player's name. The program checks if the player exists in the dataset. If not, the program exits.
3. **Position Filtering**: The DataFrame is filtered to include only players from the same position as the selected player.
4. **Position-Specific Metrics**: A list of relevant stats is generated based on the player’s position.
5. **Stat Normalization**: The player’s stats are compared to others in the same position, and a linear transformation is applied to scale the stats between 0 and 100.
6. **Data Transformation**: The data is melted from a wide to a long format to facilitate plotting.
7. **Chart Generation**: A radar chart is created using `plotly`, displaying the player's performance in the context of their position.

## Design Choices
- **Position-Specific Metrics**: Each lacrosse position has different key performance metrics. The radar chart only displays stats that are important for the player’s specific position.
- **Position-Based Comparison**: Players are only compared to others in the same position, making the radar chart more accurate and reflective of the player's skill relative to their role.
- **Linear Transformation**: A linear transformation is applied to scale all stats between 0 and 100, making the data easily comparable and graphable.
- **Smooth Plotting**: The radar chart uses a “spline” fill to ensure a smooth and complete display, avoiding gaps between data points.

## Testing
Tests for the program are implemented using `pytest`. To run the tests, execute the following command:
```bash
pytest
