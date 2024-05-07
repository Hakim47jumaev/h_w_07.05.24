def sum_of_even_and_odd(a):
    cnt1,cnt2=0,0
    for i in a:
        if int(i)%2==0:
            cnt1+=int(i)
        else:
            cnt2+=int(i)
    li=[cnt1,cnt2]
    return li
my_list=input().split()
print(sum_of_even_and_odd(my_list))