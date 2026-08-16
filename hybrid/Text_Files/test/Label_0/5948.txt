#include<cstdio>
#include<iostream>
using namespace std;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
char field[12][12];
void solve(int y,int x);
int main(){

    while(scanf("%s",field[0])!=EOF){
        for(int i=1;i<12;i++)scanf("%s",field[i]);
        int cnt=0;
        for(int i=0;i<12;i++){
            for(int j=0;j<12;j++){
                if(field[i][j]=='1'){
                    solve(i,j);
                    cnt++;
                }
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}

void solve(int y,int x){
    if(y<0 || y>11)return;
    if(x<0 || x>11)return;
    if(field[y][x]=='1'){
        field[y][x]='0';
        for(int i=0;i<4;i++){
            solve(y+dy[i],x+dx[i]);
        }
    }
    return;
}