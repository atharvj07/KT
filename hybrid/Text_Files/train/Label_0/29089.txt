#include <bits/stdc++.h>
#include <math.h>
#define lli long long int
#include <limits.h>
#include <fstream>
#define F first
#define S second
#define PI 3.141592653589793238
#define pb push_back

using namespace std;

//doesn't work for arrays
void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

/*const lli mod=1000000007;

lli gcd(lli a,lli b)
{
    if(a==0)
        return b;
    return gcd(b%a,a);
}

lli binpow(lli x,lli y,lli m)
{
    if (y==0)
        return 1;
    lli p=binpow(x,y/2,m)%m;
    p=(p*p)%m;
    if(y%2)
        return (x*p)%m;
    else
        return p;
}

lli modi(lli a,lli m)
{
    return binpow(a,m-2,m);
}*/

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    lli i,j,tt=1;
    cin>>tt;
    while(tt--)
    {
        lli n,m;
        cin>>n>>m;
        pair<lli,lli> a[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i].first;
        }
        for(i=0;i<n;i++)
        {
            cin>>a[i].second;
        }
        vector<lli> v1,v2;
        for(i=0;i<n;i++)
        {
            if(a[i].second==1)
                v1.push_back(a[i].first);
            else
                v2.push_back(a[i].first);
        }
        sort(v1.begin(),v1.end(),greater<lli>());
        sort(v2.begin(),v2.end(),greater<lli>());
        //debug(v1);
        i=(int)(v1.size())-1;
        j=(int)(v2.size())-1;
        lli ans=1e18,size1=(int)v1.size(),size2=(int)v2.size(),temp=0,tempans;
        bool ok=0;
        for(i=1;i<size1;i++)
        {
            v1[i]+=v1[i-1];
        }
        for(i=1;i<size2;i++)
        {
            v2[i]+=v2[i-1];
        }
        for(i=0;i<size1;i++)
        {
            temp=v1[i];
            if(temp<m)
            {
                auto itr=lower_bound(v2.begin(),v2.end(),m-temp);
                if(itr!=v2.end())
                {
                    ok=1;
                    ans=min(ans,i+1+2*((itr-v2.begin())+1));
                }
            }
            else
            {
                ok=1;
                ans=min(ans,i+1);
            }
        }
        auto itr=lower_bound(v2.begin(),v2.end(),m);
        if(itr!=v2.end())
        {
            ok=1;
            ans=min(ans,(lli)2*((itr-v2.begin())+1));
        }
        if(ok)
            cout<<ans<<"\n";
        else
            cout<<"-1\n";
    }
    return 0;
}
