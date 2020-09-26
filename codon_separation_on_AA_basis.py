header=''
str=''
A=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
K=[]
L=[]
M=[]
N=[]
P=[]
Q=[]
R=[]
S=[]
T=[]
V=[]
W=[]
Y=[]
X=[]
with open("input_fle.file_extension","r") as file1:  #opening the file in read mode
    read=file1.read()								 #Reading the file
    data=read.split("\n")							 #splitting each line of the file by new-line
    for each in data:
        if(">" in each):							 #Reading the file on the basis of '>' sign
            header=each
        else:
            for i in range(0,len(each),3):
                str=each[i:i+3:]
                if(str=='GCT'):
                    A.append(str)
                    str=''
                elif(str=='GCC'):
                    A.append(str)
                    str=''
                elif(str=='GCA'):
                    A.append(str)
                    str=''
                elif(str=='GCG'):
                    A.append(str)
                    str=''
                elif(str=='CGT'):
                    R.append(str)
                    str=''
                elif(str=='CGC'):
                    R.append(str)
                    str=''
                elif(str=='CGA'):
                    R.append(str)
                    str=''
                elif(str=='CGG'):
                    R.append(str)
                    str=''
                elif(str=='AGA'):
                    R.append(str)
                    str=''
                elif(str=='AGG'):
                    R.append(str)
                    str=''
                elif(str=='AAT'):
                    N.append(str)
                    str=''
                elif(str=='AAC'):
                    N.append(str)
                    str=''
                elif(str=='GAT'):
                    D.append(str)
                    str=''
                elif(str=='GAC'):
                    D.append(str)
                    str=''
                elif(str=='TGT'):
                    C.append(str)
                    str=''
                elif(str=='TGC'):
                    C.append(str)
                    str=''
                elif(str=='CAA'):
                    Q.append(str)
                    str=''
                elif(str=='CAG'):
                    Q.append(str)
                    str=''
                elif(str=='GAG'):
                    E.append(str)
                    str=''
                elif(str=='GAA'):
                    E.append(str)
                    str=''
                elif(str=='GGA'):
                    G.append(str)
                    str=''
                elif(str=='GGT'):
                    G.append(str)
                    str=''
                elif(str=='GGG'):
                    G.append(str)
                    str=''
                elif(str=='GGC'):
                    G.append(str)
                    str=''
                elif(str=='CAT'):
                    H.append(str)
                    str=''
                elif(str=='CAC'):
                    H.append(str)
                    str=''
                elif(str=='ATT'):
                    I.append(str)
                    str=''
                elif(str=='ATC'):
                    I.append(str)
                    str=''
                elif(str=='ATA'):
                    I.append(str)
                    str=''
                elif(str=='ATG'):
                    M.append(str)
                    str=''
                elif(str=='TTA'):
                    L.append(str)
                    str=''
                elif(str=='TTG'):
                    L.append(str)
                    str=''
                elif(str=='CTT'):
                    L.append(str)
                    str=''
                elif(str=='CTC'):
                    L.append(str)
                    str=''
                elif(str=='CTA'):
                    L.append(str)
                    str=''
                elif(str=='CTG'):
                    L.append(str)
                    str=''
                elif(str=='AAA'):
                    K.append(str)
                    str=''
                elif(str=='AAG'):
                    K.append(str)
                    str=''
                elif(str=='TTT'):
                    F.append(str)
                    str=''
                elif(str=='TTC'):
                    F.append(str)
                    str=''
                elif(str=='CCT'):
                    P.append(str)
                    str=''
                elif(str=='CCC'):
                    P.append(str)
                    str=''
                elif(str=='CCA'):
                    P.append(str)
                    str=''
                elif(str=='CCG'):
                    P.append(str)
                    str=''
                elif(str=='TCT'):
                    S.append(str)
                    str=''
                elif(str=='TCC'):
                    S.append(str)
                    str=''
                elif(str=='TCA'):
                    S.append(str)
                    str=''
                elif(str=='TCG'):
                    S.append(str)
                    str=''
                elif(str=='AGT'):
                    S.append(str)
                    str=''
                elif(str=='AGC'):
                    S.append(str)
                    str=''
                elif(str=='ACT'):
                    T.append(str)
                    str=''
                elif(str=='ACC'):
                    T.append(str)
                    str=''
                elif(str=='ACA'):
                    T.append(str)
                    str=''
                elif(str=='ACG'):
                    T.append(str)
                    str=''
                elif(str=='TGG'):
                    W.append(str)
                    str=''
                elif(str=='TAT'):
                    Y.append(str)
                    str=''
                elif(str=='TAC'):
                    Y.append(str)
                    str=''
                elif(str=='GTT'):
                    V.append(str)
                    str=''
                elif(str=='GTC'):
                    V.append(str)
                    str=''
                elif(str=='GTA'):
                    V.append(str)
                    str=''
                elif(str=='GTG'):
                    V.append(str)
                    str=''
                elif(str=='TAA'):
                    X.append(str)
                    str=''
                elif(str=='TAG'):
                    X.append(str)
                    str=''
                elif(str=='TGA'):
                    str=''
                    X.append(str)
                    str=''
            with open("output_file.file_extension","a") as file2:		#Giving the name of the output file
                file2.write(header+"\n")								#The output will have newline after headers
                for listitem in A:
                    file2.write('A:%s,' % listitem)
                    A=[]
                file2.write("\n")
                for listitem in C:
                    file2.write('C:%s,' % listitem)
                    C=[]
                file2.write("\n")
                for listitem in D:
                    file2.write('D:%s,' % listitem)
                    D=[]
                file2.write("\n")
                for listitem in E:
                    file2.write('E:%s,' % listitem)
                    E=[]
                file2.write("\n")
                for listitem in F:
                    file2.write('F:%s,' % listitem)
                    F=[]
                file2.write("\n")
                for listitem in G:
                    file2.write('G:%s,' % listitem)
                    G=[]
                file2.write("\n")
                for listitem in H:
                    file2.write('H:%s,' % listitem)
                    H=[]
                file2.write("\n")
                for listitem in I:
                    file2.write('I:%s,' % listitem)
                    I=[]
                file2.write("\n")
                for listitem in K:
                    file2.write('K:%s,' % listitem)
                    K=[]
                file2.write("\n")
                for listitem in L:
                    file2.write('L:%s,' % listitem)
                    L=[]
                file2.write("\n")
                for listitem in M:
                    file2.write('M:%s,' % listitem)
                    M=[]
                file2.write("\n")
                for listitem in N:
                    file2.write('N:%s,' % listitem)
                    N=[]
                file2.write("\n")
                for listitem in P:
                    file2.write('P:%s,' % listitem)
                    P=[]
                file2.write("\n")
                for listitem in Q:
                    file2.write('Q:%s,' % listitem)
                    Q=[]
                file2.write("\n")
                for listitem in R:
                    file2.write('R:%s,' % listitem)
                    R=[]
                file2.write("\n")
                for listitem in S:
                    file2.write('S:%s,' % listitem)
                    S=[]
                file2.write("\n")
                for listitem in T:
                    file2.write('T:%s,' % listitem)
                    T=[]
                file2.write("\n")
                for listitem in V:
                    file2.write('V:%s,' % listitem)
                    V=[]
                file2.write("\n")
                for listitem in W:
                    file2.write('W:%s,' % listitem)
                    W=[]
                file2.write("\n")
                for listitem in Y:
                    file2.write('Y:%s,' % listitem)
                    Y=[]
                file2.write("\n")
                for listitem in X:
                    file2.write('X:%s,' % listitem)
                    X=[]
                file2.write("\n")
