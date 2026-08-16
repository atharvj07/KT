#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
  ll n; cin>>n;
  ll c2=0,c4=0;
  for(int i=0; i<n; i++) {
    ll x; cin>>x;
    if(x%4==0) c4++;
    else if(x%2==0) c2++;
  }
  cout << (c4 + c2/2 >= n/2 ? "Yes" : "No");
}