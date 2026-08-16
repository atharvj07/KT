#include <bits/stdc++.h>
using namespace std;
const auto start_time = std::chrono::high_resolution_clock::now();
void timecalculater() {}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void __print(int x) { cout << x; }
void __print(long x) { cout << x; }
void __print(long long x) { cout << x; }
void __print(unsigned x) { cout << x; }
void __print(unsigned long x) { cout << x; }
void __print(unsigned long long x) { cout << x; }
void __print(float x) { cout << x; }
void __print(double x) { cout << x; }
void __print(long double x) { cout << x; }
void __print(char x) { cout << '\'' << x << '\''; }
void __print(const char *x) { cout << '\"' << x << '\"'; }
void __print(const string &x) { cout << '\"' << x << '\"'; }
void __print(bool x) { cout << (x ? "true" : "false"); }
template <typename T, typename V>
void __print(const pair<T, V> &x) {
  cout << '{';
  __print(x.first);
  cout << ',';
  __print(x.second);
  cout << '}';
}
template <typename T>
void __print(const T &x) {
  int f = 0;
  cout << '{';
  for (auto &i : x) cout << (f++ ? "," : ""), __print(i);
  cout << "}";
}
void _print() { cout << "]\n"; }
template <typename T, typename... V>
void _print(T t, V... v) {
  __print(t);
  if (sizeof...(v)) cout << ", ";
  _print(v...);
}
long long p = 1e9 + 7;
const int N = 2e5 + 5;
struct node {
  long long a, t;
};
struct CompareHeight {
  bool operator()(node const &p1, node const &p2) {
    if (p1.a == p2.a) return p1.t < p2.t;
    return p1.a > p2.a;
  }
};
int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  cin.exceptions(cin.failbit);
  int T = 1;
  while (T--) {
    long long n;
    cin >> n;
    pair<long long, long long> a[n];
    for (int i = 0; i < (n); ++i) cin >> a[i].first;
    for (int i = 0; i < (n); ++i) cin >> a[i].second;
    map<long long, long long> m;
    sort(a, a + n);
    long long ans = 0;
    long long i = 0;
    long long cur = 0;
    priority_queue<long long> pq;
    long long sum = 0;
    while (i < n) {
      long long x = a[i].first;
      if (pq.empty()) {
        while (i < n && a[i].first == x) {
          sum += a[i].second;
          pq.push(a[i].second);
          i++;
        }
        long long y = pq.top();
        pq.pop();
        sum -= y;
        ans += (sum);
        cur = x + 1;
      } else {
        if (x > cur) {
          long long y = pq.top();
          pq.pop();
          cur = cur + 1;
          sum -= y;
          ans += (sum);
        } else {
          while (i < n && a[i].first == x) {
            sum += a[i].second;
            pq.push(a[i].second);
            i++;
          }
          long long y = pq.top();
          pq.pop();
          cur = cur + 1;
          sum -= y;
          ans += (sum);
        }
      }
      if (pq.empty()) cur = 0;
      ;
    }
    while (!pq.empty()) {
      long long y = pq.top();
      sum -= y;
      ans += sum;
      pq.pop();
    }
    cout << ans << '\n';
  }
  timecalculater();
  return 0;
}
