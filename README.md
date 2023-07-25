# sdc.broadband.broadbandnow

Tools to access and prepare data scrapped from broadbandnow.com

## Example data
```python
df = pd.read_csv('01073.csv.xz')
df.head()
       speed   down_up  price        name           type                                address         GEOID20  longitude  latitude  year_scraped
0  5000 Mbps  Download  180.0  AT&T Fiber  Internet 5000  2501 1st ave s, birmingham, al, 35210  10730126022012 -86.701168  33.54186          2023
1  5000 Mbps    Upload  180.0  AT&T Fiber  Internet 5000  2501 1st ave s, birmingham, al, 35210  10730126022012 -86.701168  33.54186          2023
2  2000 Mbps  Download  110.0  AT&T Fiber  Internet 2000  2501 1st ave s, birmingham, al, 35210  10730126022012 -86.701168  33.54186          2023
3  2000 Mbps    Upload  110.0  AT&T Fiber  Internet 2000  2501 1st ave s, birmingham, al, 35210  10730126022012 -86.701168  33.54186          2023
4  1000 Mbps  Download   80.0  AT&T Fiber  Internet 1000  2501 1st ave s, birmingham, al, 35210  10730126022012 -86.701168  33.54186          2023
```

## Process
![Parsing Broadbandnow Data](https://github.com/uva-bi-sdad/sdc.broadband.broadbandnow/assets/22178748/83e769c9-40d6-4c83-adcb-19477c634543)
