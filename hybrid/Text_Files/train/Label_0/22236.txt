#include <bits/stdc++.h>
using namespace std;
int int_pow(int x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  int tmp = int_pow(x, p / 2);
  if (p % 2 == 0)
    return tmp * tmp;
  else
    return x * tmp * tmp;
}
void fill(istream& in, vector<int>& a, int n) {
  int elm;
  for (int i = 0; i < n; ++i) {
    in >> elm;
    a.push_back(elm);
  }
}
void fill(istream& in, vector<long long>& a, int n) {
  long long elm;
  for (int i = 0; i < n; ++i) {
    in >> elm;
    a.push_back(elm);
  }
}
void fill(vector<int>& a, int n, int val) {
  for (int i = 0; i < n; ++i) {
    a.push_back(val);
  }
}
void fill(vector<long long>& a, int n, long long val) {
  for (int i = 0; i < n; ++i) {
    a.push_back(val);
  }
}
int sum(vector<int> arr) {
  int s = 0;
  for (auto& x : arr) s += x;
  return s;
}
int max(vector<int> a) { return *max_element(a.begin(), a.end()); }
int min(vector<int> a) { return *min_element(a.begin(), a.end()); }
void print(ostream& out, vector<int> a) {
  for (auto& x : a) {
    out << x << " ";
  }
  out << endl;
}
void print(ostream& out, vector<long long> a) {
  for (auto& x : a) {
    out << x << " ";
  }
  out << endl;
}
void print(ostream& out, vector<vector<int> > a) {
  for (auto& x : a) {
    print(out, x);
  }
}
int dx[] = {0, 0, 1, -1, 1, -1, 1, -1};
int dy[] = {1, -1, 0, 0, -1, 1, 1, -1};
long long gcd(long long a, long long b) { return !b ? a : gcd(b, a % b); }
long long lcm(long long a, long long b) { return (a / gcd(a, b)) * b; }
unsigned long long power(unsigned long long a, unsigned long long b,
                         unsigned long long ret = 1LL) {
  while (b--) ret = (ret * a);
  return ret;
}
#pragma GCC target("avx2")
#pragma GCC optimization("O3")
#pragma GCC optimization("unroll-loops")
static auto speedup = []() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  return 0;
}();
class BFixYou {
 public:
  static void solve(std::istream& in, std::ostream& out) {
    int t, n, m, left, top, ch;
    in >> t;
    string s;
    while (t--) {
      in >> n >> m;
      vector<vector<int> > g;
      vector<int> a(m + 1, 1024);
      for (int _ = 0; _ < n + 1; ++_) g.push_back(a);
      g[0][1] = 0;
      vector<string> mat;
      s = string(m + 1, 'D');
      mat.push_back(s);
      for (int row = 0; row < n; ++row) {
        in >> s;
        mat.push_back("R" + s);
      }
      mat[0][1] = 'D';
      ch = 0;
      for (int row = 1; row < n; ++row) {
        if (mat[row][m] == 'R') {
          ch += 1;
          mat[row][m] = 'D';
        }
      }
      for (int col = 1; col < m + 1; ++col) {
        if (mat[n][col] == 'D') {
          ch += 1;
          mat[n][col] = 'R';
        }
      }
      for (int row = 1; row < n + 1; ++row) {
        for (int col = 1; col < m + 1; ++col) {
          left = g[row][col - 1] + (mat[row][col - 1] == 'D');
          top = g[row - 1][col] + (mat[row - 1][col] == 'R');
          g[row][col] = min(left, top);
        }
      }
      out << g[n][m] + ch << endl;
    }
  }
};
int main() {
  BFixYou solver;
  std::istream& in(std::cin);
  std::ostream& out(std::cout);
  solver.solve(in, out);
  return 0;
}
