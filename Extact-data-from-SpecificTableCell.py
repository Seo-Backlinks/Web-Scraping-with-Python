# Import Liberaries
import requests
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#To ignore the Insecure Request Warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Specify the desired URL
url = 'https://www.dcrustedp.in/show_chart.php'
html = requests.get(url, verify=False).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df.iat[0,4])
