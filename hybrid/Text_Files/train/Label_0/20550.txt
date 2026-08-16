#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

#define MOD 1000000007
#define REP(i, N) for (int i = 0; i < N; ++i)
#define REP1(i, N) for (int i = 1; i <= N; ++i)
#define RREP(i, N) for (int i = N - 1; i >= 0; --i)
#define ALL(a) a.begin(), a.end()

int main() {
  int n, q;
  cin >> n >> q;
  stack<int> st[n];
  REP(i, q) {
    int num, t;
    cin >> num >> t;
    if (num == 0) {
      int x;
      cin >> x;
      st[t].push(x);
    } else if (num == 1) {
      if (st[t].size()) {
        cout << st[t].top() << endl;
      }
    } else {
      if (st[t].size()) {
        st[t].pop();
      }
    }
  }
  return 0;
}
