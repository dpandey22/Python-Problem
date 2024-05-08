#pip Install pandas
import pandas as pd

df_all = pd.read_excel(r"C:\Users\LENOVO\Desktop\New folder\Data1.xlsx")


df_Cust_Name = pd.read_excel(r"C:\Users\LENOVO\Desktop\New folder\Cust_Names.xlsx")


df_Joined = pd.concat([df_all, df_Cust_Name.add_suffix("_df_Cust_Name")], axis=1, join='inner')
df_Joined=df_Joined.drop(["Customer ID_df_Cust_Name"], axis=1)

df_Joined.to_excel("C:/users/LENOVO/Desktop/New folder/Joined_saved.xlsx",index=False)
