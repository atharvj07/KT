#include <iostream>
#include <cstring>
using namespace std;

int w,h;
int map[16][16];
int dp[16][16][4][2];

int rec(int x,int y,int state,bool str){
    if(state == 1 || x < 0 || x >= w) return 0;
    if(state == 2 && !str) return 0;
    if(y >= h-1) return 1;
    if(dp[y][x][state][str] != -1) return dp[y][x][state][str];
    int res;
    if(state == 2) res = rec(x,y+2,map[y+2][x],true);
    else res = (rec(x-1,y+1,map[y+1][x-1],false) + rec(x,y+1,map[y+1][x],true) + rec(x+1,y+1,map[y+1][x+1],false));
    return dp[y][x][state][str] = res;
}

int main(){
    while(cin >> w >> h,w||h){
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++) cin >> map[i][j];
        }
        int d = 0;
        for(int i=0;i<w;i++) d += rec(i,0,map[0][i],true);
        cout << d << endl;
    }
}