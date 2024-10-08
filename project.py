# Imports
import plotly.express as px
import pandas as pd
import sys

# Data
def main():
    # Read csv
    df = pd.read_csv("pll-player-stats.csv")

    # Get player's name
    first_name = input("What's the player's first name? ")
    last_name = input("What's the player's last name? ")

    if check_exists(first_name, last_name, df):
        position = get_player(first_name, last_name, df)

    df = limit_df(df, position)
    factors = get_factors(position)

    df = linear_scale(df, factors)

    df = data_crunch(df, first_name, last_name, factors)

    plot(df, first_name, last_name) # type: ignore



def check_exists(first_name, last_name, df):
    # Check if player exists
    if df["First Name"].isin([first_name]).any() and df["Last Name"].isin([last_name]).any():
        return True
    else:
        sys.exit("Player does not exist")


def get_player(first_name, last_name, df):
    # Get player
    player = df.loc[(df["First Name"] == first_name) & (df["Last Name"] == last_name)]
    # Get player's position
    return player.Position.values[0]


def limit_df(df, position):
    # Limit df to only include players with the same position as player
    return df.loc[(df["Position"] == position)]


def get_factors(position):
    # Make different factors depending on position
    if position == "A":
        return ["Points", "Total Goals", "Assists", "Shot Pct", "Turnovers", "Groundballs", "Touches", "Total Passes"]
    elif position == "M" or position == "SSDM":
        return ["Points", "Total Goals", "Assists", "Shot Pct", "Turnovers", "Groundballs", "Touches", "Total Passes", "Caused Turnovers"]
    elif position == "D" or position == "LSM":
        return ["Caused Turnovers", "Touches", "Turnovers", "Groundballs", "Total Passes", "Total Penalties", "Total Goals", "Shots", "Assists"]
    elif position == "FO":
        return ["Faceoff Pct", "Faceoff Wins", "Groundballs", "Caused Turnovers", "Total Passes", "Turnovers", "Total Goals", "Shots", "Assists", "Shot Pct"]
    else:
        return ["Saves", "Scores Against", "Save Pct", "Total Passes", "Caused Turnovers", "Groundballs", "Touches"]


def linear_scale(df, factors):
    # New scale should be from 0 to 100.
    new_max = 100
    new_min = 0
    new_range = new_max - new_min

    # Do a linear transformation of the factors
    for factor in factors:
        max_val = df[factor].max()
        min_val = df[factor].min()
        val_range = max_val - min_val
        df[factor] = df[factor].apply(
            lambda x: (((x - min_val) * new_range) / val_range) + new_min)
    
    return df


def data_crunch(df, first_name, last_name, factors):
    # Limit the df to only include the player
    df = df.loc[(df["First Name"] == first_name) & (df["Last Name"] == last_name)]

    # Make the dataframe only include the factors
    df = df.loc[:, factors]

    # Convert df to be long not wide
    return pd.melt(df, var_name="category", value_name="rating", value_vars=factors)


# Plot the Radar Chart
def plot(df, first_name, last_name):
    fig = px.line_polar(df, r="rating", theta="category", line_close=True, title=f"{first_name} {last_name}", line_shape="spline", markers=True, range_r=[0,100])
    fig.update_traces(fill='toself')
    fig.show()


# Call Main
if __name__ == "__main__":
    main()