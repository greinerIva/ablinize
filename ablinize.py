do = True
should_write_names = []
should_w = []
should_do = []
should_claim = []
claimed = []
nums_claimed = []
should_claim_int = []
claimed_names = []
claim_let_write = 0
claiming = 0
write_command = 0
commands = 0
write_back = 0
string_claimed = 0
claiming = 0
claimed_all = 0
all_write_names = 0
let_count = 0
claimed_list = {}
#count_name = ""
write_name = ""
claim_name = ""
claim = ""
print("Write there:")
while do:
    take = input()
    if take[0:7] == "write<<":
        if take[7:] in claimed_list:
            should_w.append(claimed_list[take[7:]])
        else:
            should_w.append(take[7:])
        should_do.append("write")
    elif take == "stop":
        do = False
        should_do.append("stop")
    elif take[0:9] == "claim%s<<":
        claimed_all += 1
        let_taked = ""
        taked_let = 0
        while let_taked != "<":
            let_taked = take[9+taked_let]
            if let_taked == "<":
                break
            if taked_let == 0:
                should_claim.append(let_taked)
                claim += let_taked
                claimed_names.append(let_taked)
            else:
                should_claim[string_claimed] += let_taked
                claim += let_taked
                claimed_names[claiming] += let_taked
            taked_let += 1    
        claimed_list = dict.fromkeys([take[10+len(claim):]], claim)
        should_write_names.append(claim)
        string_claimed += 1
        should_do.append("claim%s")
        claiming += 1
    elif take[0:11] == "claim%int<<":
        should_do.append("claim%int")
    else:
        print('no command. Code: no command ')
        commands += 1
        print('String', commands)
        exit()
    commands += 1
print("Result:")
for i in range(len(should_do)):
    if should_do[i] == "write":
        if should_w[write_command] in claimed_names:
            print(should_w[write_command])
            write_command += 1
        else:
            print(should_w[write_back])
        write_back += 1
    elif should_do[i] == "stop":
        print('programm stopped. Code: ok')
        exit()        
        
