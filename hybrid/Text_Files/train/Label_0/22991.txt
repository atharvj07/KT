//
// Created by yamunaku on 2019/07/14.
//

#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
#define repl(i, l, r) for(int i = (l); i < (r); i++)
#define per(i, n) for(int i = ((n)-1); i >= 0; i--)
#define perl(i, l, r) for(int i = ((r)-1); i >= (l); i--)
#define all(x) (x).begin(),(x).end()
#define MOD9 998244353
#define MOD1 1000000007
#define IINF 1000000000
#define LINF 1000000000000000000
#define SP <<" "<<
#define CYES cout<<"Yes"<<endl
#define CNO cout<<"No"<<endl
#define CFS cin.tie(0);ios::sync_with_stdio(false)
#define CST(x) cout<<fixed<<setprecision(x)

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vector<int>> mti;
typedef vector<ll> vl;
typedef vector<vector<ll>> mtl;

int main(){
    int h,w;
    cin >> h >> w;
    vector<string> f(h);
    rep(i,h) cin >> f[i];
    int mil=100000,mal=-100000,mir=100000,mar=-100000;
    rep(i,h){
        rep(j,w){
            if(f[i][j]=='B'){
                mil=min(mil,i+j);
                mal=max(mal,i+j);
                mir=min(mir,i-j);
                mar=max(mar,i-j);
            }
        }
    }
    int ans=0;
    rep(i,h){
        rep(j,w){
            if(f[i][j]=='B'){
                ans=max(ans,abs(i+j-mil));
                ans=max(ans,abs(i+j-mal));
                ans=max(ans,abs(i-j-mir));
                ans=max(ans,abs(i-j-mar));
            }
        }
    }
    cout << ans << endl;
    return 0;
}


