#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int n;cin>>n;
  int an[n];rep(i,n)cin>>an[i];
  sort(an, an+n);
  
  ll sum=0;
  int med = an[n/2];
  rep(i,n) {
    sum += abs(med - an[i]);
  }
  sum *= 2;
  if (n%2==1) {
    sum -= min(med-an[n/2-1], an[n/2+1]-med);
  } else {
    sum -= med - an[n/2-1];
  }
  cout<<sum<<endl;
  
}
