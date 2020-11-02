package my_test;
class t02{
    public static int maxArea(int[] height){
        int maxarea = 0;
        for(int i=0;i<height.length;i++){
            for(int j=i+1;j<height.length;i++){
                maxarea = Math.max(maxarea, Math.min(height[i], height[j])*(j-i));
            }
        }
        return maxarea;
    }
    public static void main(String[] args){
        int[] nums = new int[]{1,8,6,2,5,4,8,3,7};
        int ans = maxArea(nums);
        System.out.println(ans);
    }
}