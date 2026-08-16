#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define se second
#define fi first
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef pair<ll,ll> pll;
typedef pair<ll,pll> plll;
typedef std::vector<int> vi;
typedef vector<ll> vl;
typedef std::vector<pii> vpi;
typedef std::vector<piii> vpii;
typedef std::vector<pll> vpl;
typedef std::vector<plll> vpll;

int main()
{
    ll i,j,k,l,m,n,a,b,c,d,u,v,w,t=1;
    cin>>t;
    while(t--){
        cin>>n;
        u=0,v=0;
        m=n;
        if(n%2==0){
        n=n/2;
        u=sqrt(n);}
        if(n%2==0){
            m=n/2;
            v=sqrt(m);
        }
        if(u*u==n||v*v==m)
        cout<<"YES\n";
        else
        cout<<"NO\n";
    }
}