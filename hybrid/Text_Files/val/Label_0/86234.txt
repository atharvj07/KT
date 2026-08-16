#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n;	cin >> n;
  int a[n],b[n];
  int ans = 0;
  
  for(auto &X :a)	cin >> X;
  for(auto &X :b)	cin >> X;
  
  for(int i=0; i<n; i++)
    ans+= max(0, a[i]-b[i]);
  cout << ans;
}