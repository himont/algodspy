if __name__ == "__main__":
    s1 = raw_input()
    arr = [0] * 256
    prev_s_idx = 0
    prev_e_idx = 0
    cur_s_idx = 0
    cur_e_idx = 0
    i = 0
    while i < len(s1):
        print s1[i], arr[ord(s1[i])]
        if arr[ord(s1[i])] is 0:
            cur_e_idx = i

        else:
            if (cur_e_idx - cur_s_idx) > (prev_e_idx - prev_s_idx):
                print prev_s_idx, prev_e_idx, cur_s_idx, cur_e_idx, i
                prev_s_idx = cur_s_idx
                prev_e_idx = cur_e_idx

            print "got a match"
            cur_s_idx = arr[ord(s1[i])] - 256
            cur_e_idx = arr[ord(s1[i])] - 256
            i = arr[ord(s1[i])] - 256
            print prev_s_idx, prev_e_idx, cur_s_idx, cur_e_idx, i
            arr = [0] * 256
        arr[ord(s1[i])] = i + 256
        i = i + 1

    print s1[prev_s_idx:(prev_e_idx + 1)]
