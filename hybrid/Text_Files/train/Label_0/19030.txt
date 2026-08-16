#include <bits/stdc++.h>
using namespace std;
class Debugger {
 public:
  Debugger(const std::string& _separator = ", ")
      : first(true), separator(_separator) {}
  template <typename ObjectType>
  Debugger& operator,(const ObjectType& v) {
    if (!first) cerr << separator;
    cerr << v;
    first = false;
    return *this;
  }
  ~Debugger() { cerr << "\n"; }

 private:
  bool first;
  string separator;
};
template <typename T1, typename T2>
inline ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
  return os << "(" << p.first << ", " << p.second << ")";
}
template <typename T>
inline ostream& operator<<(ostream& os, const vector<T>& v) {
  bool first = true;
  os << "[";
  for (unsigned long long i = 0; i < v.size(); i++) {
    if (!first) os << ", ";
    os << v[i];
    first = false;
  }
  return os << "]";
}
template <typename T>
inline ostream& operator<<(ostream& os, const set<T>& v) {
  bool first = true;
  os << "[";
  for (typename set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
    if (!first) os << ", ";
    os << *ii;
    first = false;
  }
  return os << "]";
}
template <typename T1, typename T2>
inline ostream& operator<<(ostream& os, const map<T1, T2>& v) {
  bool first = true;
  os << "[";
  for (typename map<T1, T2>::const_iterator ii = v.begin(); ii != v.end();
       ++ii) {
    if (!first) os << ", ";
    os << *ii;
    first = false;
  }
  return os << "]";
}
long long n, m, k;
long long sparse_table[6][100010][20];
long long massiv[100010][6];
long long lg[100010];
long long ans[100010];
long long maxxx = 0;
long long maxx(long long l, long long r, long long ind) {
  long long k = lg[r - l + 1];
  return max(sparse_table[ind][l][k], sparse_table[ind][r - (1LL << k) + 1][k]);
}
long long f(long long leftt, long long rightt) {
  long long sum = 0;
  for (long long i = 1; i <= m; i++) {
    sum += maxx(leftt, rightt, i);
  }
  return sum;
}
int main() {
  ios_base::sync_with_stdio(0);
  ;
  cin >> n >> m >> k;
  for (long long i = 2; i <= n; i++) lg[i] = lg[i >> 1] + 1;
  for (long long i = 1; i <= n; i++) {
    for (long long j = 1; j <= m; j++) {
      cin >> massiv[i][j];
    }
  }
  for (long long ind = 1; ind <= m; ind++) {
    for (long long i = 1; i <= n; i++) {
      sparse_table[ind][i][0] = massiv[i][ind];
    }
  }
  for (long long ind = 1; ind <= m; ind++) {
    for (long long j = 1; (1LL << j) <= n; j++) {
      for (long long i = 1; i + (1LL << (j - 1)) <= n; i++) {
        sparse_table[ind][i][j] =
            max(sparse_table[ind][i][j - 1],
                sparse_table[ind][i + (1LL << (j - 1))][j - 1]);
      }
    }
  }
  long long leftt = 1;
  long long rightt = n;
  for (long long i = 1; i <= n; i++) {
    leftt = i;
    rightt = n;
    while (leftt <= rightt) {
      long long mid = (leftt + rightt) / 2;
      long long cis = f(i, mid);
      if (cis > k) {
        rightt = mid - 1;
      } else {
        if (mid - i + 1 > maxxx) {
          maxxx = mid - i + 1;
          for (long long j = 1; j <= m; j++) ans[j] = maxx(i, mid, j);
        }
        leftt = mid + 1;
      }
    }
  }
  for (long long i = 1; i <= m; i++) {
    cout << ans[i] << " ";
  }
  cout << "\n";
  return 0;
}
