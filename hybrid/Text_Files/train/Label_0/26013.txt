#include <bits/stdc++.h>
using namespace std;
namespace _Values {
int n, x;
long long ans;
}  // namespace _Values
using namespace _Values;
class _Main {
 public:
  inline int operator()() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) scanf("%d", &x), ans += i * x;
    printf("%lld\n", ans);
    return 0;
  }
} _main;
int main() { return _main(); }
