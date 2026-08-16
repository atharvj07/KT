#include <iostream>
using namespace std;
using ll = long long;
#define in(v) v; cin >> v;
#define rep(i,n) for(int i=0,_i=(n);i<_i;++i)

int main() {
  int in(M);

  ll sum = 0, keta = 0;
  rep(i, M) {
    ll d, c; cin >> d >> c;
    sum += d * c;
    keta += c;
  }
  cout << (sum-1) / 9 + keta - 1 << endl;

  return 0;
}
