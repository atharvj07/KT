#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define fr1(i,n) for(int i=1;i<=n;i++)
#define fr0(i,n) for(int i=0;i<n;i++)
#define rfr(i,n) for(int i=n-1;i>=0;i--)
# define M_PI  3.14159265358979323846
const int MOD=1e9+7;
#define MAX 10000000
using namespace std; 
int main() 
{
ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0);
int tc;
cin>>tc;
while(tc--)
{
  int n;
  cin>>n;
  int arr[n];
  int count=0;
  fr0(i,n)
  {
      cin>>arr[i];
  }
  sort(arr,arr+n);
  for(int i=1;i<n;i++)
  {
      if(arr[i]-arr[0]>=1)
      {
          count++;
      }
  }
  cout<<count<<endl;
}



return 0;
}