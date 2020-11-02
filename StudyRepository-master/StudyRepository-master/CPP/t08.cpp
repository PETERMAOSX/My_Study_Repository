#include<iostream>
using namespace std;
int __min = 999999,n,m,p,q;
int a[51][51],book[51][51];

void dfs(int x,int y,int step){
    int k,tx,ty;
    int next[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    if(x == p && y == q){
        if(step<__min){
            __min = step;
        }
        return;
    }
    for(k=1;k<=3;k++){
        tx = x + next[k][0];
        ty = y + next[k][1];
        if(tx < 1 || tx > n || ty < 1 || ty > m){
            continue;
        }
        if(a[tx][ty] == 0 && book[tx][ty] == 0){
            book[tx][ty] = 1;
            dfs(tx,ty,step+1);
            book[tx][ty] = 0;
        }
    }
    return;
}

int main(){
    int i,j;
    int startx,starty;
    scanf("%d %d",&n,&m);
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++){
            scanf("%d",&a[i][j]);
        }
    }
    scanf("%d %d %d %d",&startx,&starty,&p,&q);
    book[startx][starty] = 1;
    dfs(startx,starty,0);
    printf("The Min Step Is : %d",__min);
    getchar();
    getchar();
    return 0;
}