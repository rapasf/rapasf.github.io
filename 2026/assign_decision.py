import pandas as pd
import shutil
def evaluate_row(row):
    if row["No Offence"] and row["No card"]:
        return "PLAYON"
    elif row["Indirect Free Kick"] and row["Yellow card"]:
        return "I_YC"
    elif row["Direct Free Kick"] and row["Red card"]:
        return "D_RC"
    elif row["Direct Free Kick"] and row["Yellow card"]:
        return "D_YC"
    elif row["Direct Free Kick"] and row["No card"]:
        return "D_NC"
    elif row["Penalty Kick"] and row["Red card"]:
        return "P_RC"
    elif row["Penalty Kick"] and row["Yellow card"]:
        return "P_YC"
    elif row["Penalty Kick"] and row["No card"]:
        return "P_NC"
    elif row["Indirect Free Kick"] and not row["Red card"] and not row["Yellow card"] and not row["No card"]:
        return "FG_I"
    elif row["No Offence"] and not row["Red card"] and not row["Yellow card"] and not row["No card"]:
        return "FG_PLAYON"   

    else:
        return "none"




# Path to your Excel file
file_path = "2025/2025-1_SFV-RAP Vorlage Clips.xlsx"

# Read the first sheet
df = pd.read_excel(file_path)


df = df.fillna(0)

# Replace "x" (string) with 1
df = df.replace("x", 1)
df['pic'] = 0

df["pic"] = df.apply(evaluate_row, axis=1)
df["Clip RAP"] = (
    df["Clip RAP"]
    .astype(str)                 # make sure it's a string
    .str.replace(" ", "")        # remove spaces
    .str.replace(r"^([A-Za-z])0*", r"\1", regex=True))

pd.set_option("display.max_rows", None)
for index, row in df.iterrows():
    source_path = f"2025/possible_solutions/{row['pic']}.png"
    destination_path = f"2025/decisions/{row['Clip RAP']}.png"
    shutil.copy(source_path, destination_path)
    print(f"Copied {row['Clip RAP']}")

print(df[["Clip RAP", "pic"]])