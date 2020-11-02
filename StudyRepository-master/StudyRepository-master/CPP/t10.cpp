#include<iostream>
using namespace std;
struct node{
    int x;
    int y;
    int s;
};

int main(){
    struct node que[2500];
    int a[51][51] = {0},book[51][51] = {0};
    int next[4][2] = {
        {0,1},{1,0},{0,-1},{-1,0}
    };
    int startx,starty;
    int i,j,k,tx,ty,p,q,n,m,head,tail;
    bool flag = false;
    cin>>n>>m;
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            cin>>a[i][j];
        }
    }
    cin>>startx>>starty>>p>>q;
    head = 1;
    tail = 1;
    que[head].x = startx;
    que[head].y = starty;
    que[head].s = 0;
    while(head < tail){
        for(k=0;k<=3;k++){
            tx = que[head].x + next[k][0];
            ty = que[head].y + next[k][1];
            if(tx < 0 || tx > n || ty < 0 || ty > m){
                continue;
            }
            if(a[tx][ty] == 0 && book[tx][ty] == 0){
                book[tx][ty] = 1;
                que[tail].x = tx;
                que[tail].y = ty;
                que[tail].s = que[head].s + 1;
                tail++;
            } 
            if(tx == p && ty == q){
                flag = true;
                break;
            }
        }
        if(flag){
            break;
        }
        head++;
    }
    printf("%d",que[tail-1].s);
    getchar();
    getchar();

    return 0;
}