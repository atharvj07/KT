#include <bits/stdc++.h>
using namespace std;
struct pkt {
  long long x, c;
  bool jest;
};
const long long INF = 1000000000000000000;
void Dijkstra(long long k, vector<long long>& skoki,
              set<pair<long long, long long> >& S, vector<pkt>& a) {
  vector<long long> D(k, INF);
  D[0] = 0;
  set<pair<long long, long long> > Q;
  for (int i = 0; i < k; ++i) Q.insert(make_pair(D[i], i));
  while (Q.size() != 0) {
    pair<long long, long long> akt = *Q.begin();
    Q.erase(Q.begin());
    for (int i = 0; i < skoki.size(); ++i) {
      long long nowa_dl = akt.first + skoki[i];
      if (nowa_dl < D[nowa_dl % k]) {
        D[nowa_dl % k] = nowa_dl;
        Q.insert(make_pair(nowa_dl, nowa_dl % k));
      }
    }
  }
  for (int i = 0; i < a.size(); ++i) {
    if (!a[i].jest && D[a[i].x % k] <= a[i].x) {
      S.insert(make_pair(-a[i].c, i));
      a[i].jest = true;
    }
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  long long h, n, m, k;
  cin >> h >> n >> m >> k;
  vector<pkt> a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i].x >> a[i].c;
    --a[i].x;
    a[i].jest = false;
  }
  vector<long long> skoki;
  skoki.push_back(k);
  set<pair<long long, long long> > S;
  Dijkstra(k, skoki, S, a);
  for (int i = 0; i < m; ++i) {
    int op;
    cin >> op;
    if (op == 1) {
      long long x;
      cin >> x;
      skoki.push_back(x);
      Dijkstra(k, skoki, S, a);
    }
    if (op == 2) {
      long long x, y;
      cin >> x >> y;
      --x;
      if (S.find(make_pair(-a[x].c, x)) != S.end()) {
        S.erase(make_pair(-a[x].c, x));
        S.insert(make_pair(-a[x].c + y, x));
      }
      a[x].c -= y;
    }
    if (op == 3) {
      if (S.size() != 0) {
        pair<long long, long long> t = *S.begin();
        cout << -t.first << endl;
        S.erase(S.begin());
      } else
        cout << "0" << endl;
    }
  }
  return 0;
}
