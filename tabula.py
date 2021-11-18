# Import the required Module
import tabula

# Read a PDF File
df = tabula.read_pdf("IDM_2021_Sangat_Tertinggal.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("IDM_2021_Sangat_Tertinggal.pdf", "IDM_2021_Sangat_Tertinggal.csv", output_format="csv", pages='all')
print(df)
