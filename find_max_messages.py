import re
result_table = {}
log = "./communicator.log"
num = 0
while True:
    try:

        logfile = open(log, encoding = "ISO-8859-1")
        #logfile = open(log)
        print('Processing file ' + log)
        for s in logfile:
            if re.search(r'<Message.+/>', s):
                #print(s)
                control_id = re.search(r'control_id="[0-9]+', s)
                mes_number = re.search(r'mes_number="[0-9]+', s)
                a = control_id.group()[12:]
                b = mes_number.group()[12:]
                if a not in result_table:
                    result_table[a] = b
                elif result_table[a] < b:
                    result_table[a] = b
        logfile.close()
        num += 1
        log = './communicator.log.' + str(num)

    except:
        break

for i in result_table:
    print(i,'   ',result_table[i])



