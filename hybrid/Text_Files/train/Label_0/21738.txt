#include <iostream>
#include <map>
using namespace std;

int n,k;
int memo[4][4][4][102];
map <int,int> ma;

int rec(int b,int y,int t,int idx){
    if(b == y && y == t) return 0;
    if(ma[idx] != '\0' && ma[idx] != t) return 0;
    if(idx == n) return 1;
    if(memo[b][y][t][idx] != 0) return memo[b][y][t][idx];
    return memo[b][y][t][idx] = (rec(y,t,1,idx+1) + rec(y,t,2,idx+1) + rec(y,t,3,idx+1))%10000;
}

int main(){
    cin >> n >> k;
    for(int i=0;i<k;i++){
        int t,m; cin >> t >> m; ma[t] = m;
    }
    int ans = (rec(0,0,1,1) + rec(0,0,2,1) + rec(0,0,3,1))%10000;
    cout << ans << endl;
}