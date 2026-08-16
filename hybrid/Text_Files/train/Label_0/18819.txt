#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;

ll gcd(ll a, ll b) {
  return b == 0 ? a : gcd(b, a % b);
}

int main(){
  int A, B, C, D;
  cin >> A >> B >> C >> D;
  ll X = abs(A - C);
  ll Y = abs(B - D);
  cout << X + Y - gcd(X, Y) << endl;
  return 0;
}

