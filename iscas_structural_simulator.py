
#زهرامیرزایی، شیوارضازاد
#تعریف کلاسها
class inputs():
    def __init__(self, adrs, index):
        self.adrs = adrs
        self.index = index

    def __repr__(self):
        return "% s --> % s" % (self.adrs, self.index)


class fan_in_adrs():
    def __init__(self, gate_adrs, fanin_adrs):
        self.gate_adrs = gate_adrs
		#ادرس گیتمون توی خطوط فایل
        self.fanin_adrs = fanin_adrs
		#ادرس ورودی هایی که به گیتمون وارد میشه: اینکه خط چندممون هست

    def __repr__(self):
        return "ad:% s fan:% s" % (self.gate_adrs, self.fanin_adrs)

class Elements:
    def __init__(self, adrs, name, type, fanout, fanin, sa0, sa1, value):
        self.adrs = adrs
        self.name = name
        self.type = type 
        self.fanout = fanout
        self.fanin = fanin
        self.sa0 = sa0
        self.sa1 = sa1
        self.value = value

    def __repr__(self):
        return "add:% s - % s - % s - % s - % s - % s - % s - va: % s" % (
            self.adrs, self.name, self.type, self.fanout, self.fanin, self.sa0, self.sa1, self.value)

#تعریف توابع گیتهای منطقی
def AND(input_list):
    if 0 in input_list:
        return 0
    return 1


def NAND(input_list):
    if 0 in input_list:
        return 1
    else:
        return 0


def OR(input_list):
    print(input_list)
    if 1 in input_list:
        return 1
    else:
        return 0


def NOR(input_list):
    if input_list.count(0) == len(input_list):
        return 1
    else:
        return 0


def XOR(input_list):
    print(input_list)
    if input_list.count(1) % 2 == 1:
        return 1
    else:
        return 0


def XNOR(input_list):
    if input_list.count(1) % 2 == 0:
        return 1
    else:
        return 0


def NOT(a):
    if a == 1:
        return 0
    else:
        return 1


def buf(a):
    return a






#دریافت فایل موردنظر و ذخیره مقادیر
list = []
fan_in_adrs_list = []
file_in=input("enter the file name please:")
O = open(file_in, "r")
rows = O.readlines()
count_of_in = []
adrses = []
sa0 = "no"
sa1 = "no"
number_of_gates = 0
h = 0

for row in rows:
    if row[0] != "*":
        if len(row.split()) > 4:

            if row.split()[-1] == ">sa0" or row.split()[-2] == ">sa0":
                sa0 = "sa0"
            if row.split()[-1] == ">sa1" or row.split()[-2]==">sa1":
                sa1 = "sa1"
            if row.split()[2] == "input":
                count_of_in.append(inputs(row.split()[0], h))
            if row.split()[2] == "from":
                list.append(Elements(row.split()[0], row.split()[1], row.split()[2], row.split()[3],
                                         "no", sa0, sa1, "U"))			
            else:
                list.append(Elements(row.split()[0], row.split()[1], row.split()[2], row.split()[3],
                                         row.split()[4], sa0, sa1, "U"))
        else:
            adrses = []
            for j in range(len(row.split())):
                for h in range(len(list)):
                    if list[h].adrs ==row.split()[j] :
                        x=h
                        break
                    else:
                        continue
                adrses.append(x)
            fan_in_adrs_list.append(fan_in_adrs(h, adrses))
            number_of_gates += 1
        h += 1
        sa0="no"
        sa1="no"
for i in range(len(list)):
    print(list[i])


    
#دریافت فایل مقادیر ورودی
voroudi=input("enter the input values file please:")
input_file = open(voroudi, "r")
rows_of_input = input_file.readlines()
h = 0
for row in rows_of_input:
    if h == 0:
        h += 1
        continue
    for m in range(len(list)):
        if list[m].adrs == row.split()[0]:
            y = m
            break
        else:
            continue
    list[y].value = int(row.split()[1])
input_file.close()
#print(list)



#محاسبه مقادیر هر گره 
gate_in = []
Q = 0
for h in range(len(list)):   
    if list[h].type == "from":
        for j in range(len(list)):
            if list[j].name == list[h].fanout:
                break
        list[h].value = list[j].value
    if list[h].type == "input" and list[h].value == 'U':
        list[h].value = 'U'
    if list[h].type in ["and", "or", "nand", "nor", "xor", "xnor", "not"]:
        for j in range(len(fan_in_adrs_list[Q].fanin_adrs)):
            gate_in.append(list[fan_in_adrs_list[Q].fanin_adrs[j]].value)
        if list[h].type == "xor":
            list[h].value = OR(gate_in)
        elif list[h].type == "and":
            list[h].value = AND(gate_in)
        elif list[h].type == "nor":
            list[h].value = NOR(gate_in)
        elif list[h].type == "nand":
            list[h].value = NAND(gate_in)
        elif list[h].type == "not":
            list[h].value = NOT(list[fan_in_adrs_list[Q].fanin_adrs[0]].value)
        elif list[h].type == "or":
            list[h].value = XOR(gate_in)
        elif list[h].type == "xnor":
            list[h].value = XNOR(gate_in)
        elif list[h].type == "buff":
            list[h].value = buf(gate_in)

        Q += 1
        gate_in = []
#print(list)

#چاپ خروجی 
final= open("final.txt", "w")
for h in range(len(list)):
    if h == 0:
        final.write("Node Address" + "\t" + "value" + "\n")
    final.write(str(list[h].adrs) + "\t "+"\t" + str(list[h].value) + "\n")
final.close()

for h in range(len(list)):
    if str(list[h].sa0)=="sa0":
        sa00="YES"
    else:
        sa00="NO"
    if str(list[h].sa1)=="sa1":
        sa11="YES"
    else:
        sa11="NO"
    print("address:"+ str(list[h].adrs)+"   name:"+str(list[h].adrs)+"   type:"+str(list[h].type)+"   outputs:"+str(list[h].fanout)+"   inputs:"+str(list[h].fanin)+"   stack0:"+  sa00 +"   stack1:"+sa11+"   value:"+str(list[h].value))



c=input()