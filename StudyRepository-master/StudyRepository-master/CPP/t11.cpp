#include<iostream>
using namespace std;

int max_(int a,int b){
    return a > b? a:b;
}
int maxHeight(int height[]){
    int ans = 0;
    int i = 0;
    int j = sizeof(height)/sizeof(int)-1;
    while( i < j){
        ans = height[i] < height[j]?
        max_(ans,height[i++]*(j-i)):
        max_(ans,height[j--]*(j-i));
    }
    return ans;
}

int main(){
    int height[] = {1,8,6,2,5,4,8,3,7};
    int ans = maxHeight(height);
    cout<<ans<<endl;

    return 0;
}