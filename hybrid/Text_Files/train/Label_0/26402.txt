#include <bits/stdc++.h>
using namespace std;
double EPS = 1e-9;
int INF = 1000000005;
long long INFF = 1000000000000000005LL;
double PI = acos(-1);
int dirx[8] = {-1, 0, 0, 1, -1, -1, 1, 1};
int diry[8] = {0, 1, -1, 0, -1, 1, -1, 1};
int spf[10001];
inline string IntToString(long long a) {
  char x[100];
  sprintf(x, "%lld", a);
  string s = x;
  return s;
}
inline long long StringToInt(string a) {
  char x[100];
  long long res;
  strcpy(x, a.c_str());
  sscanf(x, "%lld", &res);
  return res;
}
inline string GetString(void) {
  char x[1000005];
  scanf("%s", x);
  string s = x;
  return s;
}
inline string uppercase(string s) {
  int n = (int)s.size();
  for (int(i) = (0); (i) < (n); ++(i))
    if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
  return s;
}
inline string lowercase(string s) {
  int n = (int)s.size();
  for (int(i) = (0); (i) < (n); ++(i))
    if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
  return s;
}
inline void OPEN(string s) {
  freopen((s + ".in").c_str(), "r", stdin);
  freopen((s + ".out").c_str(), "w", stdout);
}
void sieve() {
  spf[1] = 1;
  for (int i = 2; i < 10001; i++) spf[i] = i;
  for (int i = 4; i < 10001; i += 2) spf[i] = 2;
  for (int i = 3; i * i < 10001; i++) {
    if (spf[i] == i) {
      for (int j = i * i; j < 10001; j += i)
        if (spf[j] == j) spf[j] = i;
    }
  }
}
unordered_map<int, long long int> getFactorization(int x) {
  unordered_map<int, long long int> make_pair;
  while (x != 1) {
    if (make_pair.find(spf[x]) == make_pair.end()) {
      make_pair[spf[x]] = 1;
    } else {
      make_pair[spf[x]]++;
    }
    x = x / spf[x];
  }
  return make_pair;
}
unsigned long long int power(unsigned long long int x,
                             unsigned long long int y) {
  unsigned long long int temp;
  if (y == 0) return 1;
  temp = power(x, y / 2);
  if (y % 2 == 0)
    return temp * temp;
  else {
    if (y > 0)
      return x * temp * temp;
    else
      return (temp * temp) / x;
  }
}
unsigned long long int gcd(unsigned long long int a, unsigned long long int b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
unsigned long long int lcm(unsigned long long int a, unsigned long long int b) {
  return (a * b) / gcd(a, b);
}
class DisjSet {
  int *rank, *parent, n;

 public:
  DisjSet(int n) {
    rank = new int[n];
    parent = new int[n];
    this->n = n;
    makeset();
  }
  void makeset() {
    for (int i = 0; i < n; i++) {
      parent[i] = i;
      rank[i] = 1;
    }
  }
  int root(int x) {
    while (parent[x] != x) {
      x = parent[x];
    }
    return parent[x];
  }
  void union_(int x, int y) {
    int root_x = root(x);
    int root_y = root(y);
    if (rank[root_x] < rank[root_y]) {
      parent[root_x] = root_y;
      rank[root_y] += rank[root_x];
    } else {
      parent[root_y] = root_x;
      rank[root_x] += rank[root_y];
    }
  }
  vector<int> gh() {
    vector<int> fin(n);
    for (int i = 0; i < n; i++) {
      fin[i] = rank[root(i)];
    }
    return fin;
  }
};
bool bo(pair<int, int> a, pair<int, int> b) {
  if (a.first == b.first) {
    return a.second < b.second;
  }
  return a.first < b.first;
}
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  int t;
  t = 1;
  vector<int> sol;
  for (int u = 0; u < t; u++) {
    int n;
    cin >> n;
    vector<string> arr(n);
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
    }
    int k = 0;
    for (int i = 1; i < n - 1; i++) {
      for (int j = 1; j < n - 1; j++) {
        if (arr[i][j] == 'X') {
          if (arr[i - 1][j + 1] == 'X' && arr[i + 1][j - 1] == 'X' &&
              arr[i - 1][j - 1] == 'X' && arr[i + 1][j + 1] == 'X') {
            k++;
          }
        }
      }
    }
    cout << k << endl;
  }
}
