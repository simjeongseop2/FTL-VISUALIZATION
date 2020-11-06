for i in range(5): #data 1~5까지
	s3 = "temp = M01_Fault1Record_%d.shape[0]"%(i + 1)
	exec(s3)
    for j in range(0,temp): #1부터 13까지
        NoOfData_M01_Fault1 = NoOfData_M01_Fault1 + 1
        n = NoOfData_M01_Fault1
            #           j+1                         1                                               j
        s1 = "EndPoint_1_%d = np.where(M01_SensorData_%d.iloc[:,0].values <= M01_Fault1Record_1.iloc[%d,0])[0][-1]" %(j+1,1,j)   #endpoint 설정
            #            n                 1                  j+1                  j+1
        s2 = "M01_Fault1_%d = M01_SensorData_%d.iloc[EndPoint_1_%d-1000:EndPoint_1_%d,:]" %(n,1,j+1,j+1) #endpoint 이전 천개를 falut1_n이라 정의
        
        exec(s1)
        exec(s2)    
    