#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N=1e5+5,LGN=20;
ll n,L,a[N],nxt[N][LGN];
int main(){
    ios_base:: sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin>>n;
    for(ll i=0;i<n;i++)cin>>a[i];
    cin>>L;
    for(ll i=0;i<n;i++)nxt[i][0]=lower_bound(a+i,a+n,a[i]+L+1)-(a+1);
    for(ll j=1;j<LGN;j++){
        for(ll i=0;i<n;i++)nxt[i][j]=nxt[nxt[i][j-1]][j-1];
    }
    ll q;cin>>q;
    for(ll x,y,ans=0;q>0;q--,ans=0){
        cin>>x>>y;
        x--;y--;
        if(x>y)swap(x,y);
        for(ll i=LGN-1;i>=0;i--){
            if(nxt[x][i]<y)ans|=(1ll<<i),x=nxt[x][i];
        }
        cout<<ans+1<<"\n";
    }
}