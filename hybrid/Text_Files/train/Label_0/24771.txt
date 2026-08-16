#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using P = pair<int, int>;
const double eps = 1e-8;
const ll MOD = 1000000007;
const int INF = INT_MAX / 2;
const ll LINF = LLONG_MAX / 2;
template<typename T1, typename T2>
bool chmax(T1 &a, const T2 &b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
template<typename T1, typename T2>
bool chmin(T1 &a, const T2 &b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template<typename T1, typename T2>
ostream &operator<<(ostream &os, const pair<T1, T2> p) {
  os << p.first << ":" << p.second;
  return os;
}
template<class T>
ostream &operator<<(ostream &os, const vector<T> &v) {
  for(int i=0;i<((int)(v.size()));++i) {
    if (i) os << " ";
    os << v[i];
  }
  return os;
}
struct Node {
  int h = 0, w;
  int l, r;
  double rem = 0;
  shared_ptr<Node> lch = nullptr, rch = nullptr, par = nullptr;
  Node(int l, int r, int w): l(l), r(r), w(w) {}
};
void solve() {
  int n;
  cin >> n;
  vi b(n);
  vector<P> h1(n), h2(n);
  for(int i=0;i<(n);++i) {
    cin >> h1[i].first >> h1[i].second;
    h2[i].first = h1[i].second;
    h2[i].second = h1[i].first;
  }
  sort((h1).begin(),(h1).end());
  sort((h2).begin(),(h2).end());
  int m;
  cin >> m;
  vi f(m);
  vector<double> a(m);
  for(int i=0;i<(m);++i) {
    cin >> f[i] >> a[i];
    a[i] /= 30;
  }
  int l;
  cin >> l;
  vector<pair<P, int>> p(l);
  for(int i=0;i<(l);++i) {
    cin >> p[i].first.second >> p[i].first.first;
    p[i].second = i;
  }
  sort((p).begin(),(p).end());
  vector<shared_ptr<Node>> nodes(n+1);
  for(int i=0;i<(n);++i) {
    if(i == 0) {
      nodes[i] = make_shared<Node>(Node(i, i+1, h1[i].first));
      nodes[i]->rem = nodes[i]->h * nodes[i]->w;
    } else {
      nodes[i] = make_shared<Node>(Node(i, i+1, h1[i].first - h1[i-1].first));
      nodes[i]->rem = nodes[i]->h * nodes[i]->w;
    }
  }
  nodes[n] = make_shared<Node>(Node(n, n+1, 100 - h1[n-1].first));
  nodes[n]->rem = nodes[n]->h * nodes[n]->w;
  vector<shared_ptr<Node>> leaves(n+1);
  for(int i=0;i<(n+1);++i) {
    leaves[i] = nodes[i];
  }
  for(int i=0;i<(n);++i) {
    int nowh = h2[i].first;
    int nowb = h2[i].second;
    auto it = lower_bound((h1).begin(),(h1).end(), make_pair(nowb, 0));
    int pos = distance(h1.begin(), it);
    shared_ptr<Node> node1 = nodes[pos];
    shared_ptr<Node> node2 = nodes[pos+1];
    auto newnode = make_shared<Node>(Node(node1->l, node2->r, node1->w + node2->w));
    node1->h += nowh;
    node2->h += nowh;
    node1->rem = node1->h * node1->w;
    node2->rem = node2->h * node2->w;
    newnode->h = -nowh;
    newnode->lch = node1;
    newnode->rch = node2;
    node1->par = newnode;
    node2->par = newnode;
    for(int j=(node1->l);j<(node2->r);++j) {
      nodes[j] = newnode;
    }
  }
  shared_ptr<Node> head = nodes[0];
  head->h += 50;
  head->rem = head->h * head->w;
  vector<map<shared_ptr<Node>, bool>> mp(m);
  vector<shared_ptr<Node>> nodepos(m);
  for(int i=0;i<(m);++i) {
    int idx = 0;
    if(f[i] < h1[0].first) {
      idx = 0;
    } else {
      auto it = upper_bound((h1).begin(),(h1).end(), make_pair(f[i], 0));
      int pos = distance(h1.begin(), it);
      idx = pos;
    }
    mp[i][leaves[idx]] = true;
    nodepos[i] = leaves[idx];
  }
  int nowt = 0;
  vector<double> out(l);
  for(int i=0;i<(l);++i) {
    for(int j=0;j<(m);++j) {
      double diff = p[i].first.first - nowt;
      diff *= a[j];
      auto nownode = nodepos[j];
      while (diff > eps) {
        if(diff < nownode->rem - eps) {
          nownode->rem -= diff;
          nodepos[j] = nownode;
          break;
        }
        diff -= nownode->rem;
        nownode->rem = 0;
        if(nownode->par == nullptr) break;
        if(nownode == nownode->par->lch) {
          nownode = nownode->par;
          if(!mp[j][nownode->rch]) {
            nownode = nownode->rch;
            while(nownode->lch != nullptr) {
              nownode = nownode->lch;
            }
          }
        } else if(nownode == nownode->par->rch) {
          nownode = nownode->par;
          if(!mp[j][nownode->lch]) {
            nownode = nownode->lch;
            while(nownode->rch != nullptr) {
              nownode = nownode->rch;
            }
          }
        } else {
          nownode = nownode->par;
        }
        mp[j][nownode] = true;
        nodepos[j] = nownode;
      }
    }
    nowt = p[i].first.first;
    auto it = upper_bound((h1).begin(),(h1).end(), make_pair(p[i].first.second, 0));
    int pos = distance(h1.begin(), it);
    shared_ptr<Node> nownode = leaves[pos];
    double ans = 50;
    while(1) {
      ans -= nownode->rem / nownode->w;
      if(nownode->par == nullptr) {
        break;
      } else {
        nownode = nownode->par;
      }
    }
    out[p[i].second] = ans;
  }
  for(int i=0;i<(l);++i) {
    cout << out[i] << endl;
  }
}
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout << fixed << setprecision(10);
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
}

