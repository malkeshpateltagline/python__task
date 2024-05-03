import math
def common_diff(seq):
    return seq[1] - seq[0]

def correct_ap(seq, common_diff):
    correct_se = [seq[0]]
    for i in range(1, len(seq)):
        correct_se.append(correct_se[-1] + common_diff)
    return correct_se

ap_seq = [2, 5, 8, 11, 15, 17]

common_diff = common_diff(ap_seq)

ap = correct_ap(ap_seq, common_diff)

print("A.P. =", ap)


def common_gp_diff(seq):
    return seq[1] / seq[0]

def correct_gp(seq, common_diff):
    correct_se = [seq[0]]
    for i in range(1, len(seq)):
        correct_se.append(math.trunc(correct_se[-1] * common_diff))
    return correct_se

gp_seq = [3, 6, 9, 12, 241, 96]

common_gp_diff = common_gp_diff(gp_seq)

gp = correct_gp(gp_seq, common_gp_diff)

print("G.P. =", gp)

# a_p= [2, 5, 8, 11, 15, 17] 
# g_p = [3, 6, 9, 12, 16, 18]
# lst=[]
# for i in range(len(a_p)-1):
#     pre_interval = a_p[i+1]-a_p[i]
#     lst.append(pre_interval)

# lsttoset = set(lst)    

# if len(lsttoset)>1:
#     print('make chnages to list')
#     print(lst)
# else:
#     print(a_p)