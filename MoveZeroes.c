

void moveZeroes(int* nums, int numsSize){
    int l = 0;
    int temp;
    for (int i = 0; i < numsSize; i++)
    {   
        if (nums[i] != 0)
        {
            temp = nums[l];
            nums[l] = nums[i];
            nums[i] = temp;
            l++;
        }
    }
}
