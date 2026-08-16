#include<bits/stdc++.h>
 
using namespace std;
 
using ll=long long;
 
int main()
{
   ll n,x,y;
   vector<pair<ll,ll>>v;
   cin>>n;
   for(int i=0;i<n;i++)
   {
       cin>>x>>y;
       v.push_back({x+y,x});
   }
   sort(v.rbegin(),v.rend());
   ll a=0;
   for(int i=0;i<n;i++)
   {
       if(i%2==0)
        a+=v[i].second;
       else
        a+=v[i].second-v[i].first;
   }
   cout<<a<<endl;
}