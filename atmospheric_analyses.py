import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "serif"
plt.rcParams["pdf.fonttype"] = 42

# Read in the data from Palmer Station, Antarctica, United States
url_c02 = 'https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_psa_surface-flask_1_ccgg_event.txt'
url_ch4 = 'https://gml.noaa.gov/aftp/data/trace_gases/ch4/flask/surface/txt/ch4_psa_surface-flask_1_ccgg_event.txt'
url_n20 = 'https://gml.noaa.gov/aftp/data/trace_gases/n2o/flask/surface/txt/n2o_psa_surface-flask_1_ccgg_event.txt'
url_sf6 = 'https://gml.noaa.gov/aftp/data/greenhouse_gases/sf6/flask/surface/txt/sf6_psa_surface-flask_1_ccgg_event.txt'

# Define the column headers
headers = ['site_code', 'year', 'month', 'day', 'hour', 'minute', 'second', 'datetime', 'time_decimal', 
           'air_sample_container_id', 'value', 'value_unc', 'latitude', 'longitude', 'altitude', 
           'elevation', 'intake_height', 'method', 'event_number', 'instrument', 'analysis_datetime', 
           'qcflag']

# Read the data from the URL into a pandas dataframe
df_c02 = pd.read_csv(url_c02, skiprows=162, delim_whitespace=True, header=None, names=headers)
df_ch4 = pd.read_csv(url_ch4, skiprows=162, delim_whitespace=True, header=None, names=headers)
df_n20 = pd.read_csv(url_n20, skiprows=161, delim_whitespace=True, header=None, names=headers)
df_sf6 = pd.read_csv(url_sf6, skiprows=161, delim_whitespace=True, header=None, names=headers)

# The units that are present within the Molecular Fraction have
# to be ensured that they are on the same order of magnitude (our choice is ppm).
# This can be found within the headers of the given URLS.

# c02 
time_c02 = df_c02["time_decimal"]
c02 = df_c02["value"]

# ch4
time_ch4 = df_ch4["time_decimal"]
ch4 = df_ch4["value"]/1000

# n20
time_n20 = df_n20["time_decimal"]
n20 = df_n20["value"]/1000

# sf6
time_sf6 = df_sf6["time_decimal"]
sf6 = df_sf6["value"]/1000000

# Designing subplots to visualize each of the datasets
fig = plt.figure(figsize = (8,8))
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

# Plotting Carbon Dioxide
ax1.minorticks_on()
ax1.xaxis.set_ticks_position("both")
ax1.tick_params(top=True, right=True, which='major', direction='in', length=6, labelbottom=True, labeltop=False)
ax1.tick_params(top=True, right=True, which='minor', direction='in', length=3)
# Hardset Y-axis limits
ax1.set_ylim([330, 420])
ax1.set_xlim([min(time_c02), max(time_c02)])
ax1.set_xlabel('Time (yr)', fontsize=14)
ax1.set_ylabel("Molec. Fraction (ppm)", fontsize=14)
ax1.plot(time_c02, c02, ".", color = 'black', markersize=1, label=r"$\mathrm{CO}_2$")
ax1.set_title('Carbon Dioxide', fontsize=14)
ax1.legend(loc="lower right", frameon=True, fontsize=12)



# Methane
ax2.minorticks_on()
ax2.xaxis.set_ticks_position("both")
ax2.tick_params(top=True, right=True, which='major', direction='in', length=6, labelbottom=True, labeltop=False)
ax2.tick_params(top=True, right=True, which='minor', direction='in', length=3)
# Hardset Y-axis limits
ax2.set_ylim([1.540, 1.900])
ax2.set_xlim([min(time_ch4), max(time_ch4)])
ax2.set_xlabel('Time (yr)', fontsize =14)
ax2.set_ylabel("Molec. Fraction (ppm)", fontsize=14)
ax2.plot(time_ch4, ch4, ".", color = 'black', markersize=1, label=r"$\mathrm{CH}_4$")
ax2.set_title('Methane', fontsize=14)
ax2.legend(loc="lower right", frameon=True, fontsize=12)



# Plotting Nitrous Oxide
ax3.minorticks_on()
ax3.xaxis.set_ticks_position("both")
ax3.tick_params(top=True, right=True, which='major', direction='in', length=6, labelbottom=True, labeltop=False)
ax3.tick_params(top=True, right=True, which='minor', direction='in', length=3)
# Hardset Y-axis limits
ax3.set_ylim([0.310, 0.337])
ax3.set_xlim([min(time_n20), max(time_n20)])
ax3.set_xlabel('Time (yr)', fontsize =14)
ax3.set_ylabel("Molec. Fraction (ppm)", fontsize=14)
ax3.plot(time_n20, n20, ".", color = 'black', markersize=1, label=r"$\mathrm{N_{2}O}$")
ax3.set_title('Nitrous Oxide', fontsize=14)
ax3.legend(loc="lower right", frameon=True, fontsize=12)



# Plotting Sulfur Hexafluoride
ax4.minorticks_on()
ax4.xaxis.set_ticks_position("both")
ax4.tick_params(top=True, right=True, which='major', direction='in', length=6, labelbottom=True, labeltop=False)
ax4.tick_params(top=True, right=True, which='minor', direction='in', length=3)
# Hardset Y-axis limits
ax4.set_ylim([3.6800000000000003e-06, 1.10000000000004e-05])
ax4.set_xlim([min(time_sf6), max(time_sf6)])
ax4.set_xlabel('Time (yr)', fontsize =14)
ax4.set_ylabel("Molec. Fraction (ppm)", fontsize=14)
ax4.plot(time_sf6, sf6, ".", color = 'black', markersize=1, label=r"$\mathrm{SF_{6}}$")
ax4.set_title('Sulfur Hexafluoride', fontsize=14)
ax4.legend(loc="lower right", frameon=True, fontsize=12)

# Show off your plots! :)
fig.tight_layout()
plt.show()