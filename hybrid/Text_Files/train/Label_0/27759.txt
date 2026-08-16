#include<bits/stdc++.h>
using namespace std;
#define ll long long int 

int main()
{
    ll t,i,j;
    cin>>t;
    while(t--)
    {
       ll n,k;
       cin>>n>>k;
       ll a[n];
       for(i=0;i<n;i++)
       cin>>a[i];
       bool ans=false;
       for(i=0;i<k;i++)
       {
           j=0;
           while(a[j]>=a[j+1]&&j<n-1)
           {
               j++;
           }
           if(j==n-1)
           {
               ans=true;
               break;
           }
           else 
           a[j]++;
       }
       if(ans)
       cout<<"-1"<<endl;
       else
       cout<<j+1<<endl;
    }
}