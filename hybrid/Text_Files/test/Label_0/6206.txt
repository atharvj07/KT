#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> P;

const ll INF=1e18;
const int MOD=1e9+7;

int main(){
    int N; cin >> N;
    P len[N];
    for(int i=0;i<N;i++){
        ll x,l; cin >> x >> l;
        len[i]={x+l,x-l};
    }
    sort(len,len+N);
    ll cur=-INF;
    int ans=0;
    for(int i=0;i<N;i++){
        if(cur<=len[i].second){
            cur=len[i].first;
            ans++;
        }
    }
    cout << ans << endl;
}