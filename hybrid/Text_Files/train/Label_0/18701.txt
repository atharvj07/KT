#include<bits/stdc++.h>
using namespace std;
void solve()
{
      int n;
      cin>>n;
      int a[n],c0=0,c1=0,c2=0;
      for(int i=0;i<n;i++)
      {
            cin>>a[i];
            if(a[i]%3==0)
            {
                  c0++;
            }
            else if(a[i]%3==1)
            {
                  c1++;
            }
            else if(a[i]%3==2)
            {
                  c2++;
            }
      }
      int b= n/3;
      int ans=0;
      for(int i=0;i<2;i++)
      {
            if(c0>b)
            {
                ans+=c0-b;
                c1+=c0-b;
                c0=b;
            }
            if(c1>b)
            {
                ans+=c1-b;
                c2+=c1-b;
                c1=b;
            }
            if(c2>b)
            {
                ans+=c2-b;
                c0+=c2-b;
                c2=b;
            }
      }
      cout<<ans<<endl;
}
int main()
{
      int t;
      cin>>t;
      while(t--)
            solve();
      return 0;
}