#include <stdio.h>
int a[9][9];
void check(int x,int y){
    for(int i=0;i<9;i++){
        if(a[i][y]==a[x][y]&&i!=x){
            printf("*%d",a[x][y]);
            return;
        }
    }
    for(int i=0;i<9;i++){
        if(a[x][i]==a[x][y]&&i!=y){
            printf("*%d",a[x][y]);
            return;
        }
    }
    for(int i=x-x%3;i<x-x%3+3;i++){
        for(int j=y-y%3;j<y-y%3+3;j++){
            if(a[i][j]==a[x][y]&&(i!=x||j!=y)){
                printf("*%d",a[x][y]);
                return;
            }
        }
    }
    printf(" %d",a[x][y]);
    return;
}
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        if(i>0)printf("\n");
        for(int j=0;j<9;j++){
            for(int k=0;k<9;k++){
                scanf("%d",&a[j][k]);
            }
        }
        for(int j=0;j<9;j++){
            for(int k=0;k<9;k++){
                check(j,k);
            }
            printf("\n");
        }
    }
}