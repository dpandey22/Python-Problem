{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "469fdadd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df_all = pd.read_excel(r\"E:\\Sid\\python\\Data1.xlsx\")\n",
    "\n",
    "\n",
    "df_Cust_Name = pd.read_excel(r\"E:\\Sid\\python\\Cust_Names.xlsx\")\n",
    "\n",
    "\n",
    "df_Joined = pd.concat([df_all, df_Cust_Name.add_suffix(\"_df_Cust_Name\")], axis=1, join='inner')\n",
    "df_Joined=df_Joined.drop([\"Customer ID_df_Cust_Name\"], axis=1)\n",
    "\n",
    "df_Joined.to_excel(\"E:\\Sid\\python\\A\\Joined_saved.xlsx\",index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9907f977",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b39c57a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
