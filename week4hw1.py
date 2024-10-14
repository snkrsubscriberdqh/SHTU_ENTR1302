def b(list):
    ROE=(list[0]*list[1]*list[2]-(list[2]-1)*list[4])*(1-list[5])
    R=1-list[3]
    g=ROE*R
    print("g* will reduce by",100*(1-(g/0.27)),"% to",g*100,"%.")
'''
ErningsOnSales=b[0]
Turnover=b[1]
Leverage=b[2]
DividendPayoutRatio=b[3]
InterestRate=b[4]
TaxRate=b[5]
'''
b0=[0.15,2,2,0.1,0.1,0.4]
b1=[0.075,2,2,0.1,0.1,0.4]
b2=[0.15,1,2,0.1,0.1,0.4]
b3=[0.15,2,1,0.1,0.1,0.4]
b4=[0.15,2,2,0.05,0.1,0.4]
b5=[0.15,2,2,0.1,0.05,0.4]
b6=[0.15,2,2,0.1,0.1,0.2]
b(b0)
b(b1)
b(b2)
b(b3)
b(b4)
b(b5)
b(b6)