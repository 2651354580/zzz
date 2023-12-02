def Traning(Corpus,Model):
	In=open(Corpus,"r")	
	HZ={}
	HZInfo={}
	for L in In:
		L=L.strip()
		Array=L.split(",")
		if len(Array) != 2:
			continue
		Sex="M"	
		if 	Array[1] == "女":
			Sex="F"	
		for i in range(len(Array[0])):
			if len(Array[0]) == 1:
				POS="S"	
			else if i==0:
				POS="B"
			else if i==len(Array[0])-1:
				POS="E"
			else:
				POS="I"
			if Array[0][i] not in HZ:
				HZ[Array[0][i]]=0
			HZ[Array[0][i]]+=1
			
			if Array[0][i]+POS+Sex not in HZInfo:
				HZInfo[Array[0][i]+POS+Sex]=0
			HZInfo[Array[0][i]+POS+Sex]+=1
	In.close()
	
	Out=open(Model,"w")
	for HZ in HZInfo:
		Val=log(HZInfo[HZ]/HZ[HZInfo[0]])
		print(HZ,Val,file=Out)
	Out.close()
	

def main(Option):
	if Option == 0:
		Traning("person.txt","Model.txt")	
	else:
		Regcognize("Model.txt")


def Regcognize(Model):
	HZInfo={}
	LoadModel(Model,HZInfo)
	while(1):
		Name=input("Pls")
		if  Name == "q":
			break
		Ret=GetSexInfo(Name,HZInfo)
		print(Ret)
#main(0)		
main(1)


def GetSexInfo(Name,HZInfo):
	Male=0
	Female=0
	for i in range(len(Name)):
		if len(Name) == 1:
			POS="S"	
		else if i==0:
			POS="B"
		else if i==len(Name)-1:
			POS="E"
		else:
			POS="I"
		Male+=GetProb(Name[i]+POS+"M",HZInfo)
		Female+=GetProb(Name[i]+POS+"F",HZInfo)
	Sex="男"	
	if 	Female >Male:
		Sex="女"	
	return 	Sex
			