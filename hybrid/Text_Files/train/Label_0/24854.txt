#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define IOS ios_base::sync_with_stdio(false); cin.tie(NULL);
int main()
{
  IOS;
  int tt;
  cin>>tt;
  while(tt--)
  {
      ll red,blue,diff;
      cin>>red>>blue>>diff;
      if(red>blue)
      {
          ll prob=(diff+1)*blue;
          if(prob>=red)
          {
              cout<<"YES"<<endl;
          }
          else
          {
              cout<<"NO"<<endl;
          }
      }
      else if(red<blue)
      {
          ll prob=(diff+1)*red;
          if(prob>=blue)
          {
              cout<<"YES"<<endl;
          }
          else
          {
              cout<<"NO"<<endl;
          }
      }
      else
      {
          cout<<"YES"<<endl;
      }
  }
}
