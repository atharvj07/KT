#include <algorithm>
#include <cmath>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#define MOD 1000000007
using namespace std;
typedef long long ll;
#include <cstring>

int main() {
  int n, q, v, w;
  cin >> n >> q;
  for (int i = 0; i < q; i++) {
    cin >> v >> w;
    if (n != 1) {
      while (v != w) {
        if (v > w) {
          if (v % n == 1) {
            v--;
          } else if (v % n) {
            v += n;
            v -= v % n;
          }
          v /= n;
        } else {
          if (w % n == 1) {
            w--;
          } else if (w % n) {
            w += n;
            w -= w % n;
          }
          w /= n;
        }
      }
      cout << v << endl;
    } else {
      cout << min(v, w) << endl;
    }
  }
}