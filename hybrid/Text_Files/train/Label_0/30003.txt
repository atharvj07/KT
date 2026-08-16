#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define all(v) (v).begin(),(v).end()
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define fi first
#define se second
template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

int N;
int x[50],y[50];
signed main(){
    cin>>N;
    rep(i,N)cin>>x[i]>>y[i];

    if(N&1){
        puts("NA");
        return 0;
    }

    bool ok=true;
    rep(i,N/2){
        if(x[i+1]-x[i]!=-(x[(i+1+N/2)%N]-x[i+N/2]))ok=false;
        if(y[i+1]-y[i]!=-(y[(i+1+N/2)%N]-y[i+N/2]))ok=false;
    }

    if(ok)printf("%.20f %.20f\n",(x[N/2]+x[0])/2.0,(y[N/2]+y[0])/2.0);
    else puts("NA");
    return 0;

}