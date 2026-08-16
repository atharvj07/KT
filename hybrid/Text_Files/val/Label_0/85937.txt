#include<iomanip>
#include<limits>
#include<thread>
#include<utility>
#include<iostream>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<numeric>
#include<cassert>
#include<random>
#include<chrono>
#include<unordered_map>
#include<fstream>
#include<list>
#include<functional>
#include<bitset>
#include<complex>
using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef pair<ll,ll> pll;
typedef pair<int,int> pi;
typedef pair<double,double> pd;
typedef pair<double,ll> pdl;
#define F first
#define S second
const ll E=1e18+7;
const ll MOD=1000000007;





int main(){
    ll n;
    cin>>n;
    vector<ll> A(n);
    for(auto &i:A){cin>>i;}
    vector<ll> dp(n,0);
    stack<pll> S;
    for(int i=1;i<n;i++){
        dp[i]=dp[i-1];
        ll k=A[i-1];
        while(k<A[i]){
            k*=4;
            if(S.empty()){
                dp[i]+=i*2;
            }
            else{
                pll w=S.top(); S.pop();
                dp[i]+=(i-w.F)*2;
                w.S--;
                if(w.S>0){S.push(w);}
            }
        }
        ll count=0;
        ll b=A[i];
        while(k>=b){count++; b*=4;}
        if(count>1){S.push({i,count-1});}
    }
    reverse(A.begin(),A.end());
    while(!S.empty()){S.pop();}
    vector<ll> dp2(n,0);
    for(int i=1;i<n;i++){
        dp2[i]=dp2[i-1];
        ll k=A[i-1];
        while(k<A[i]){
            k*=4;
            if(S.empty()){
                dp2[i]+=i*2;
            }
            else{
                pll w=S.top(); S.pop();
                dp2[i]+=(i-w.F)*2;
                w.S--;
                if(w.S>0){S.push(w);}
            }
        }
        ll count=0;
        ll b=A[i];
        while(k>=b){count++; b*=4;}
        if(count>1){S.push({i,count-1});}
    }
    reverse(dp2.begin(),dp2.end());
    ll ans=E;
    for(int i=0;i+1<n;i++){
        ans=min(ans,dp[i]+dp2[i+1]+i+1);
    }
    ans=min(ans,dp2[0]);
    ans=min(ans,dp[n-1]+n);
    cout<<ans<<endl;
    
    
    
    
    return 0;
}
