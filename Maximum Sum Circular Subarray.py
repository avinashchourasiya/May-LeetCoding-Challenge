arr=[1,2,-3,3,4,-4];
curr_max=arr[0];
best_max=arr[0];
s=0;
for i in range(1,len(arr)):
    s=curr_max+arr[i];

    print(curr_max,' ',arr[i],'=',s);
    if(s>curr_max):
        curr_max=s;
    # if(curr_max>best_max):
    #     best_max=curr_max;
    #
    #

# print('best_max',best_max);
