from Data import *
from Optimum import solution_op
from H_RTT import RTT_Heu

def main():
	n=6
	slot=3
	I=0
	bin=0
	open('RTT_6/temp1.txt', 'w').close()
	ase=[11, 17, 19, 21]
	for I in xrange(1,2):
		pass
		pres,ares,price,load=[],[],[],[]
		lres,bres,bg,pb=[],[],[],[]
		data(price,load,pres,ares,I,n)
		ob=0
		xr=[]
		bin=0
		for x in range(n/slot):
			pres1=pres[x*slot:slot*(x+1)]
			price1=price[x*slot:slot*(x+1)]
			load1=load[x*slot:slot*(x+1)]
			ares1=ares[x*slot:slot*(x+1)]
			solution_op(pres1, price1, load1, slot, bin)
			#obj=res_data(lres, bres, bg, pb)
			#obj=res_opt(lres, bres, bg, pb,17)
			res=RTT_Heu(x*slot, slot, bin, pres1, ares1, load1, price1)
			#ob=res_one_to(lres, bres, bg, pb,17)
			bin=res[1]
			xr.append(bin)
			ob+=res[0]
			xr.append(res[0])
			print(ob)
		#print(pb)
		#with open("RTT_6/res_6.txt", "a+") as f:
			#f.write(str(ob)+"\n")

if __name__ == '__main__':
    main()