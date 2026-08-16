//#include<bits/stdc++.h>
#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define all(s) s.begin(),s.end()
typedef long long ll;
const double pi = acos(-1);
const ll N=5e6+5,M=1e9+7,H=31;
set<ll>st;
vector<pair<ll,ll>>v[N];
ll a[N];
int main()
{
    fast;
    ll i,j,k,l,n,fl=1;
    cin>>n;
    for(i=1;i<=n;i++)cin>>a[i];

    for(i=1;i<=n;i++)
    {
        for(j=1;j<i;j++)
        {
            ll sm=a[i]+a[j];
            if(!v[sm].empty())
            {
                for(auto p:v[sm])
                {
                    if(p.ff!=i && p.ss!=j && p.ff!=j && p.ss!=i)
                    {
                        fl=0;
                        cout<<"YES\n";
                        cout<<p.ff<<' '<<p.ss<<' '<<i<<' '<<j<<endl;
                        return 0;
                    }
                }
            }
            v[sm].pb({i,j});
        }
    }

    fl?cout<<"NO\n":cout<<"";


}
