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
#include<unordered_set>
#include<unordered_map>
#include<fstream>
#include<list>
#include<functional>
#include<bitset>
#include<complex>
#include<tuple>
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

const ll MX=100000;

vector<ll> cnt(MX);
ll n=0;
ll b;
vector<vector<ll>> edge(MX);
vector<pll> node(MX); //amari,takasa
vector<ll> ans(MX);

void init(){for(int i=0;i<n;i++){edge[i].clear(); cnt[i]=0;}}

void dfs(ll w){
    ll mx=0;
    ll ch=1;
    for(auto &I:edge[w]){
        dfs(I);
        mx=max(mx,node[I].S);
    }
    for(auto &I:edge[w]){
        if(node[I].S==mx){ch+=node[I].F;}
    }
    if(ch>b){mx++; ch=1;}
    else if(ch==b){mx++; ch=0;}
    node[w]={ch,mx};
}

void dfs2(ll w,pll p){
    //cout<<w<<" "<<p.F<<" "<<p.S<<endl;
    pll mx1={p.S,-1},mx2={p.S,-1};
    for(auto &I:edge[w]){
        if(node[I].S>mx2.F){mx2={node[I].S,I};}
        if(mx2>mx1){swap(mx2,mx1);}
    }
    ll cnt1=1,cnt2=1;
    for(auto &I:edge[w]){
        if(node[I].S==mx1.F){cnt1+=node[I].F;}
        if(node[I].S==mx2.F){cnt2+=node[I].F;}
    }
    if(p.S==mx1.F){cnt1+=p.F;}
    if(p.S==mx2.F){cnt2+=p.F;}
    ans[w]=mx1.F+1;
    if(cnt1>b){ans[w]++;}
    
    for(auto &I:edge[w]){
        if(I==mx1.S){
            ll cnt=cnt2;
            ll high=mx2.F;
            if(node[I].S==mx2.F){cnt-=node[I].F;}
            if(cnt>b){high++; cnt=1;}
            else if(cnt==b){high++; cnt=0;}
            dfs2(I,{cnt,high});
        }
        else{
            ll cnt=cnt1;
            ll high=mx1.F;
            if(node[I].S==mx1.F){cnt-=node[I].F;}
            if(cnt>b){high++; cnt=1;}
            else if(cnt==b){high++; cnt=0;}
            dfs2(I,{cnt,high});
        }
    }
}


int main(){
    for(int C=1;;C++){
    init();
    cin>>n>>b;
        if(n==0){break;}
        cout<<"Case "<<C<<":"<<endl;
    for(int i=1;i<n;i++){
        ll p;
        cin>>p;
        p--;
        edge[p].push_back(i);
    }
    dfs(0);
    dfs2(0,{0,0});
    for(int i=0;i<n;i++){cout<<ans[i]<<endl;}
    //for(int i=0;i<n;i++){cout<<node[i].F<<" "<<node[i].S<<endl;}
    }
    
    return 0;
}

