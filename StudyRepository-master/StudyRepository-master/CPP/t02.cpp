#include<iostream>
using namespace std;

int main(){
    char matrix[20][21];
    int i,j,sum,map=0,p,q,x,y,m,n;
    scanf("%d %d",&n,&m);
    for(i=0;i<=n-1;i++){
        scanf("%s",matrix[i]);
    }
    for(i=0;i<=n-1;i++){
        for(j=0;j<=m-1;j++){
            if(matrix[i][j] == '.'){
                sum = 0;
                x=i;
                y=j;
                while(matrix[x][y] != '#'){
                    if(matrix[x][y] == 'G'){
                        sum++;
                    }
                    x++;
                }
                x=i;
                y=j;
                while(matrix[x][y] != '#'){
                    if(matrix[x][y] == 'G'){
                        sum++;
                    }
                    x--;
                }
                x=i;
                y=j;
                while(matrix[x][y] != '#'){
                    if(matrix[x][y] == 'G'){
                        sum++;
                    }
                    y++;
                }
                x=i;
                y=j;
                while(matrix[x][y] != '#'){
                    if(matrix[x][y] == 'G'){
                        sum++;
                    }
                    y--;
                }
                if(map < sum){
                    map = sum;
                    p = i;
                    q = j;
                }
            }
        }
    }
    printf("Bomb Should Set (%d,%d) Position.\nAnd it Can Kill %d Emenys!",p,q,map);
    getchar();
    getchar();
    

    return 0;
}