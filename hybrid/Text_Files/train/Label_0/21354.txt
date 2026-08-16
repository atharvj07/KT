#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<string>
#include<vector>
#include<queue>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 100000005
#define rep(i,n) for(int i = 0;i < n;i++)
using namespace std;
typedef long long int ll;
typedef pair<int,int> PI;

int main(){
    ll a[6];

    while(1){
        ll sum = 0;
        cin>>a[0]>>a[2]>>a[4]>>a[1]>>a[3]>>a[5];
        rep(i,6){
            sum+=a[i];
        }
        if(!sum)
            break;
        ll b[3];
        rep(i,3){
            b[i]=0;
            b[i]+=a[i*2];
            b[i]+=a[i*2+1];
        }
        ll ans = 0;
        ll bal = INF;
        rep(i,3){
            bal = min(bal,b[i]);
        }
        rep(i,3){
            if(bal<0)break;
            ll temp=bal;
            rep(j,3){temp+=(b[j]-bal)/3;}
            ans = max(ans,temp);
            bal--;
        }
        cout<<ans<<endl;

    }
}