import math

def maximumPopulation(logs):
    pop = {}
    for i in range(1950,2051):
        pop[i] = 0

    for elem in logs:
        for k in range(elem[0] , elem[1]):
            pop[k] += 1
    yr_val = 0
    yr_num = 1950
    print(pop)
    for yr in pop.keys():
        if pop[yr] > yr_val:
            yr_val = pop[yr]
            yr_num = yr


    return yr_num


logs = [[2006,2007],[2037,2038],[1971,1972],[1973,1974],[2001,2002],[1987,1988],[2044,2045],[1972,1973],[2043,2044],[1990,1991],[2028,2029],[1984,1985],[1974,1975],[2033,2034],[1977,1978],[2011,2012],[1967,1968],[1955,1956],[1980,1981],[2039,2040],[1983,1984],[2019,2020],[1996,1997],[1981,1982],[1991,1992],[1965,1966],[2009,2010],[2027,2028],[2025,2026],[2046,2047],[2013,2014],[1956,1957],[2045,2046],[1997,1998],[1986,1987],[1998,1999],[2010,2011],[2023,2024],[2018,2019],[1952,1953],[2038,2039],[1978,1979],[2012,2013],[1969,1970],[2003,2004],[1968,1969],[1989,1990],[1994,1995],[2024,2025],[2016,2017],[2032,2033],[1979,1980],[2022,2023],[2017,2018],[1954,1955],[1962,1963],[2015,2016],[2021,2022],[1988,1989],[2008,2009],[1999,2000],[2030,2031],[2036,2037],[2048,2049],[1951,1952],[1963,1964],[2014,2015],[1992,1993],[2007,2008],[2004,2005],[1964,1965],[2049,2050],[1960,1961],[2002,2003],[1970,1971],[1975,1976],[1995,1996],[1985,1986],[1993,1994],[2005,2006],[1976,1977],[1957,1958],[1982,1983],[2020,2021],[1966,1967],[1961,1962],[2040,2041],[2047,2048],[1953,1954],[1950,1951],[2041,2042],[1959,1960],[2035,2036],[2000,2001],[2029,2030],[2034,2035],[1958,1959],[2042,2043],[2031,2032],[2026,2027]]
print(maximumPopulation(logs))