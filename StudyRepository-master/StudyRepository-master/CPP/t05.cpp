#include<iostream>
using namespace std;

int getNumberOfHC(int number){
    int f[10] = {6,2,5,5,4,5,6,3,7,6};
    int sum = 0;
    while(number/10 != 0){
        sum += f[number%10];
        number = number / 10;
    }
    sum += f[number];
    return sum;
}

int main(){
    int i,j,n,k,ans=0;
    scanf("%d",&n);
    for(i=0;i<=1111;i++){
        for(j=0;j<=1111;j++){
            k = i + j;
            if(getNumberOfHC(i)+getNumberOfHC(j)+getNumberOfHC(k) == n-4){
                printf("%d + %d = %d\n",i,j,k);
                ans++;
            }
        }
    }
    printf("Totally has %d Equals.",ans);
    getchar();
    getchar();
    return 0;
}