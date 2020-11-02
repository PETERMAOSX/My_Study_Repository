package my_test;

import java.util.Arrays;

class t01 {
    public static int[] twosum(int[] nums,int target){
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i] == target - nums[j]){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
    public static void main(String[] args){
        int[] nums = new int[] {2,7,11,15};
        int[] item = twosum(nums, 9);
        System.out.println(Arrays.toString(item));
    }
}