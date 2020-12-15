n_m_t = list(map(int, input().split(" ")))

N = n_m_t[0]
max_N = n_m_t[0]

M = n_m_t[1]
T = n_m_t[2]

a_b_list = [ list(map(int, input().split(" "))) for _ in range(M)]

battery_action_time = 0.5 

while battery_action_time <= T:
    
    is_between_a_b = False
    for a_b in a_b_list:
 
        if a_b[0] <= battery_action_time and battery_action_time  <= a_b[1]:
            if N < max_N :
                N += 1 
            is_between_a_b = True
            break

    if not is_between_a_b:
        N -= 1

    if N <= 0:
        print("No")
        exit()
    
    battery_action_time += 1

print("Yes")

