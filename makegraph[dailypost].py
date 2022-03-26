# run "python makegraph.py", not "python3"
list = [
    ['XPEV', ['TTM', '11,553,676,000', '1,080,526,000'], ['12/31/2020', '5,844,321,000', '265,989,000'], ['12/31/2019', '2,321,219,000', '-558,141,000']], 
    ['VIOT', ['TTM', '6,315,710,000', '1,204,011,000'], ['12/31/2020', '5,825,624,000', '1,082,956,000'], ['12/31/2019', '4,647,513,000', '1,082,404,000'], ['12/31/2018', '2,561,229,000', '1,082,404,000'], ['12/31/2019', '4,647,513,000', '1,082,404,000']]
    ]

import matplotlib.pyplot as plt
import matplotlib.font_manager

title = []
location = []
sales = []
revenue = []
tag_location = []

for a in range(0, len(list)):
    nest_list_location = []
    nest_list_sales = []
    nest_list_revenue = []
    nest_list_tag_location = []
    nest_list_title = [list[a][0]]
    title.append(nest_list_title)
    print(title)
    for b in range(1, len(list[a])):
        print('{}:{}'.format(a, b))
        try:
            location_year = int(list[a][b][0].split("/")[-1])+0
            #location_year = list[a][b][0].split("/")[-1]
            nest_list_location.append(location_year)
            nest_list_tag_location.append(b)
        except:
            if "TTM" == list[a][b][0]:
                location_year = int(list[a][b+1][0].split("/")[-1])+1
                #location_year = list[a][b+1][0].split("/")[-1]
                nest_list_location.append(location_year)
                nest_list_tag_location.append(b)
        nest_list_sales.append(int(list[a][b][1].replace(",", "")))
        nest_list_revenue.append(int(list[a][b][2].replace(",", "")))
    location.append(nest_list_location)
    tag_location.append(nest_list_tag_location)
    sales.append(nest_list_sales)
    revenue.append(nest_list_revenue)

print(title)
print(location)
print(tag_location)
print(sales)
print(revenue)


for a in range(0, len(list)):
    fig = plt.figure()
    plt.bar(location[a], sales[a], width=-0.4, align='edge', label='sales', color='#3cb37a')
    plt.bar(location[a], revenue[a], width=0.4, align='edge', label='revenue', color='#fad09e')
    plt.legend(loc=2)
    plt.xticks(location[a],location[a])
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.tick_params('x', length=0, which='major')
    plt.tick_params('y', length=0, which='major')
    plt.title("${} SALES & REVENUE".format(title[a][0]))
    fig.savefig("images/{}.png".format(title[a][0]))