#include<bits/stdc++.h>
using namespace std;
#define ll long long
typedef pair<ll,ll> P;
#define M 1000000007
int main(){
  ll n;
  cin>>n;
  vector<ll> a(n);
  bool f=true;
  for(int i=0;i<n;i++){
    cin>>a[i];
    if(a[i]<0){f=!f;a[i]*=-1;}
  }
  ll c=0;
  sort(a.begin(),a.end());
  for(int i=1;i<n;i++) c+=a[i];
  if(f) cout<<c+a[0];
  else cout<<c-a[0];
}