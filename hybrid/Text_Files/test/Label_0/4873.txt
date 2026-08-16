#include <bits/stdc++.h>
using namespace std;
const int maxn=2e5+7;
int a[maxn];
int main()
{ int t,n;
   cin>>t;
   while(t--)
   {
       cin>>n;
       long long tot=0;
       for(int i=1;i<=n;i++)
        {cin>>a[i];
        tot+=a[i];
        }
        cout<<(n-tot%n)*(tot%n)<<endl;
   }
}