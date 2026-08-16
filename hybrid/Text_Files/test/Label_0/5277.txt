#include<bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define pb push_back
using namespace std;
typedef long long ll;

int main(){
    string s;
    cin >> s;
    int ans = 1000;
    rep(i, 26){
        int res = 0;
        int t = 0;
        rep(j, s.size()){
            if (s[j] == 'a' + i){
                res = max(res, t);
                t = 0;
            }else t++;
        }
        res = max(res, t);
        ans = min(ans, res);
    }
    cout << ans << endl;
}