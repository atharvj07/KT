#include <map>
#include <algorithm>
#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <queue>
#include <set>
#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

bool one(double x){
  return x + 1e-9 > 1.0;
}

int main(){
  const int n = getInt();
  const int m = getInt();

  vector<vector<int> > v(n);
  vector<vector<int> > r(n);
  vector<int> intmp;
  vector<int> in(n);
  vector<int> out(n);
  vector<pair<int, int> > e(m);
  map<int, map<int, int> > memo;

  REP(i,m){
    const int a = e[i].first  = getInt() - 1;
    const int b = e[i].second = getInt() - 1;

    v[a].push_back(b);
    in[b]++;

    r[b].push_back(a);
    out[a]++;

    memo[a][b] = memo[b][a] = i;
  }
  intmp = in;

  vector<int> dist(n);
  queue<int> q;

  REP(i,n) if(in[i] == 0){
    q.push(i);
  }

  while(q.size()){
    const int pos = q.front(); q.pop();

    for(const int next : v[pos]){
      dist[next] = max(dist[next], dist[pos] + 1);
      --in[next];
      if(in[next] == 0) q.push(next);
    }
  }

  const int mx = *max_element(dist.begin(), dist.end());
  vector<int> chain(m);
  vector<int> valid(n);

  REP(i,n) if(dist[i] == mx){
    valid[i] = 1;
  }

  REP(i,n) if(out[i] == 0){
    q.push(i);
  }

  while(q.size()){
    const int pos = q.front(); q.pop();

    for(const int next : r[pos]){
      if(dist[pos] == dist[next] + 1){
        if(valid[pos]){
          valid[next] = 1;
          chain[memo[pos][next]] = 1;
        }
      }

      --out[next];
      if(out[next] == 0) q.push(next);
    }
  }

  vector<double> wp(n);
  vector<double> w(m);
  in = intmp;

  int cnt = 0;
  REP(i,n) if(in[i] == 0 && valid[i]){
    cnt++;
  }

  REP(i,n) if(in[i] == 0 && valid[i]){
    wp[i] = 1.0 / cnt;
  }

  REP(i,n) if(in[i] == 0){
    q.push(i);
  }

  while(q.size()){
    const int pos = q.front(); q.pop();

    int cnt = 0;
    for(const int next : v[pos])
      if(chain[memo[pos][next]]) cnt++;

    for(const int next : v[pos]){
      if(chain[memo[pos][next]]){
        wp[next] += wp[pos] / cnt;
        w[memo[pos][next]] += wp[pos] / cnt;
      }
      --in[next];
      if(in[next] == 0) q.push(next);
    }
  }

  bool b = false;
  REP(i,m){
    if(one(w[i])){
      printf("%d\n", i + 1);
      b = true;
    }
  }

  if(!b) puts("-1");

  return 0;
}