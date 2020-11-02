#include<bits/stdc++.h>
using namespace std;

int SingleValue(vector<int> &vec){
    if(vec.size() <= 0){
        return -1;
    }
    int value;
    int n;
    value = vec[0];
    for(n=1;n<vec.size();n++){
        value = value ^ vec[n];
    }
    return value;
}

int main(){
    int Array [] = {33,44,55,66,77,88,99,99,88,77,55,44,33};
    vector<int> vec(Array,Array+sizeof(Array)/sizeof(int));
    int ans = SingleValue(vec);
    cout<<"Only Have One,This value is : "<<endl;
    cout<<ans<<endl;
    
    return 0;
}