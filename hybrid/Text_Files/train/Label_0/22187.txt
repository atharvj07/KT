#include <bits/stdc++.h>
using namespace std;
mt19937 rnd(chrono::high_resolution_clock::now().time_since_epoch().count());
const int N = 5e5 + 7;
const int M = 1e9 + 7;
const int MEM = 1e7;
int c[MEM];
int ptr = 0;
struct Vector {
  int* v;
  int n = 0;
  Vector() { v = &c[ptr]; }
  int size() const { return n; };
  int& operator[](const int i) {
    assert(i < n);
    return v[i];
  }
  int& back() { return v[n - 1]; };
  void push_back(int val) {
    v[n] = val;
    ptr++;
    n++;
  }
  int* begin() { return &v[0]; }
  int* end() { return &v[n - 1] + 1; }
};
vector<int> g[N];
vector<int> eg[N], erg[N];
int mul(int a, int b) { return (a * (long long)b) % M; }
int add(int a, int b) {
  int c = a + b;
  if (c < 0) c += M;
  if (c >= M) c -= M;
  return c;
}
int pw(int a, int n) {
  int res = 1;
  while (n) {
    if (n % 2 == 0) {
      a = mul(a, a);
      n /= 2;
    } else {
      res = mul(res, a);
      n--;
    }
  }
  return res;
}
int inv(int x) { return pw(x, M - 2); }
int tin[N], tout[N], park[N];
bool par(int a, int b) { return tin[a] <= tin[b] && tout[a] >= tout[b]; }
int tt = 0;
void dfs(int v, int pr) {
  tin[v] = tt++;
  for (int to : g[v]) {
    if (to != pr) {
      park[to] = v;
      dfs(to, v);
    }
  }
  tout[v] = tt++;
}
Vector gen_path(int a, int b) {
  Vector ret;
  while (!par(a, b)) {
    ret.push_back(a);
    a = park[a];
  }
  ret.push_back(a);
  vector<int> go;
  while (b != a) {
    go.push_back(b);
    b = park[b];
  }
  reverse(go.begin(), go.end());
  for (int v : go) {
    ret.push_back(v);
  }
  return ret;
}
int vis[N];
void zhfs(int v) {
  vis[v] = 1;
  for (int to : eg[v]) {
    if (!vis[to]) {
      zhfs(to);
    } else if (vis[to] == 1) {
      cout << 0 << '\n';
      exit(0);
    }
  }
  vis[v] = 2;
}
struct hsh {
  int operator()(const pair<int, int>& a) const {
    return a.first * (long long)1e9 + a.second;
  }
};
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  unordered_map<pair<int, int>, int, hsh> mp;
  unordered_map<pair<int, int>, int, hsh> nxt;
  for (int i = 1; i < n; i++) {
    int a, b;
    cin >> a >> b;
    a--, b--;
    g[a].push_back(b);
    g[b].push_back(a);
    mp[{a, b}] = mp[{b, a}] = i;
  }
  dfs(0, -1);
  auto add_edge = [&](int s, int t) {
    eg[s].push_back(t);
    erg[t].push_back(s);
  };
  vector<int> arr(n);
  vector<int> first(n, -1);
  vector<int> last(n, -1);
  long long tot = 0;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
    arr[i]--;
    if (arr[i] != -1) {
      if (i == arr[i]) {
        cout << 0 << '\n';
        exit(0);
      }
      ptr = 0;
      auto b = gen_path(i, arr[i]);
      tot += b.size();
      if (tot > 3 * n) {
        cout << 0 << '\n';
        return 0;
      }
      Vector ids;
      for (int i = 1; i < (int)b.size(); i++) {
        ids.push_back(mp[{b[i - 1], b[i]}]);
      }
      for (int i = 1; i < (int)ids.size(); i++) {
        if (nxt.count({b[i], ids[i - 1]})) {
          cout << 0 << '\n';
          return 0;
        }
        nxt[{b[i], ids[i - 1]}] = ids[i];
      }
      first[i] = ids[0];
      last[arr[i]] = ids.back();
    }
    ptr = 0;
  }
  int ans = 1;
  for (int i = 0; i < n; i++) {
    ptr = 0;
    Vector ids;
    map<int, int> t;
    map<int, int> d;
    for (int j : g[i]) {
      ids.push_back(mp[{i, j}]);
    }
    set<int> q;
    for (int x : ids) {
      t[x] = 0;
      q.insert(x);
    }
    set<int> nq;
    map<int, int> mp;
    function<int(int)> get = [&](int v) {
      if (!mp.count(v)) {
        mp[v] = v;
      }
      if (mp[v] == v) {
        return v;
      } else {
        return mp[v] = get(mp[v]);
      }
    };
    for (int x : ids) {
      if (nxt.count({i, x}))
        if (t.count(nxt[{i, x}])) {
          d[nxt[{i, x}]] = x;
          t[nxt[{i, x}]]++;
          if (get(nxt[{i, x}]) == get(x)) {
            cout << 0 << '\n';
            return 0;
          }
          mp[get(nxt[{i, x}])] = get(x);
          q.erase(nxt[{i, x}]);
        }
    }
    for (auto& c : t) {
      if (c.second > 1) {
        cout << 0 << '\n';
        return 0;
      }
    }
    int need = q.size();
    if (first[i] != -1) {
      need--;
      if (t[first[i]] > 0) {
        cout << 0 << '\n';
        return 0;
      }
    }
    if (last[i] != -1) {
      need--;
      if (nxt.count({i, last[i]})) {
        cout << 0 << '\n';
        return 0;
      }
    }
    if (first[i] != -1 && last[i] != -1 && get(first[i]) == get(last[i]) &&
        q.size() > 1) {
      cout << 0 << '\n';
      return 0;
    }
    for (int i = 1; i <= need; i++) {
      ans = mul(ans, i);
    }
  }
  cout << ans << endl;
}
