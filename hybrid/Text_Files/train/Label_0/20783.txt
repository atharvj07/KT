#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
using namespace std;
typedef long long ll;

const ll mod = 1e9+7;

int main(){
  ll n,l;
  cin >> n >> l;
  vector<ll> x(n),a(n);
  rep(i,n)cin >> x[i];
  rep(i,n)cin >> a[i];

  vector<ll> cur(l+1,0);
  cur[l] = 1;

  rrep(i,n){
    vector<ll> nxt(l+1,0);
    ll sum = cur[l];
    rrep(j,l){
      if(j<x[i])break;
      if( a[i]>0 && (j-x[i])%a[i] == 0 )(nxt[j] += sum) %= mod;
      else if(a[i]==0 && j==x[i])(nxt[j] += sum) %= mod;
      (sum += cur[j]) %= mod;
    }
    cur = nxt;
  }

  ll res = 0;
  rep(i,l)(res += cur[i]) %= mod;
  cout << res << endl;
}