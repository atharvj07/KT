#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<cassert>
#include<climits>
#include<deque>
#include<cstring>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef pair<int,int> ii; // ii(num,sp)

struct Data {
  int cur;
  ii cost;
  bool operator < ( const Data &data ) const {
    if( cost != data.cost ) return cost > data.cost;
    return cur > data.cur;
  }
};

#define MAX_V 10100
#define IINF INT_MAX
int V,E,A,B,C;
int grade[MAX_V];
vector<int> G[MAX_V];
ii mini[MAX_V];

bool pattern1() {
  int state = 0;
  rep(i,V) if( grade[i] ) rep(j,(int)G[i].size()) {
      int &e = G[i][j];
      if( grade[e] && grade[i] != grade[e] ) {
	state = state | (1<<grade[i]) | (1<<grade[e]);
	if( state == 14 ) {
	  return true;
	}
      }
    }
  return false;
}

ii dijkstra_for_pattern2(int sp_grade) {
  rep(i,V) mini[i] = ii(IINF,IINF);
  priority_queue<Data> Q;
  rep(i,V) if( grade[i] == sp_grade ) {
    ii v = ii(0,i);
    Q.push((Data){i,v});
    mini[i] = v;
  }
  while( !Q.empty() ) {
    Data data = Q.top(); Q.pop();
    rep(i,(int)G[data.cur].size()) {
      int &e = G[data.cur][i];
      ii ncost = data.cost;
      ++ncost.first, ncost.second = min(ncost.second,e);
      if( ncost < mini[e] ) {
	mini[e] = ncost;
	Q.push((Data){e,ncost});
      }
    }
  }
  ii ans = ii(IINF,IINF);
  rep(i,V) if( grade[i] && grade[i] != sp_grade ) {
    ans = min(ans,mini[i]);
  }
  return ans;
}

vector<ii> bfs(int sp_grade) {
  vector<ii> ans(V,ii(IINF,IINF));
  deque<Data> deq;
  rep(i,V) if( grade[i] == sp_grade ) {
    deq.push_back((Data){i,ii(0,i)});
    ans[i] = ii(0,i);
  }
  while( !deq.empty() ) {
    Data tmp = deq.front(); deq.pop_front();
    ii cur = tmp.cost;
    rep(i,(int)G[tmp.cur].size()) {
      int &e = G[tmp.cur][i];
      ii nex = ii(cur.first+1,min(cur.second,e));
      if( ans[e] > nex) {
	ans[e] = nex;
	deq.push_back((Data){e,nex});
      }
    }
  }
  return ans;
}

ii star() {
  vector<ii> vec[3];
  rep(i,3) vec[i] = bfs(i+1);
  /*
  rep(i,V) {
    cout << "node " << i << " | " << vec[0][i].first << " " << vec[1][i].first << " " << vec[2][i].first << endl;
  }
  */
  assert( vec[0].size() == vec[1].size() && vec[1].size() == vec[2].size() );
  ii ans = ii(IINF,IINF);
  rep(i,V) if( !( vec[0][i].first == IINF || vec[1][i].first == IINF || vec[2][i].first == IINF ) ) {
    ii v = ii(vec[0][i].first+vec[1][i].first+vec[2][i].first,
	      min(vec[0][i].second,min(vec[1][i].second,vec[2][i].second)));
    ans = min(ans,v);
  }
  return ans;
}


ii dijkstra(int sp_grade,int ep_grade) {
  priority_queue<Data> Q;
  rep(i,V) mini[i] = ii(IINF,IINF);
  rep(i,V) if( grade[i] == sp_grade ) {
    Q.push((Data){i,ii(0,i)});
    mini[i] = ii(0,i);
  }
  while( !Q.empty() ) {
    Data data = Q.top(); Q.pop();
    rep(i,(int)G[data.cur].size()) {
      int &e = G[data.cur][i];
      ii ncost = ii(data.cost.first+1,min(e,data.cost.second));
      if( mini[e] > ncost ) {
	mini[e] = ncost;
	Q.push((Data){e,ncost});
      }
    }
  }
  ii ans = ii(IINF,IINF);
  rep(i,V) if( grade[i] == ep_grade ) {
    ans = min(ans,mini[i]);
  }
  return ans;
}

ii dijkstra_for_pattern3() {
  ii ans = ii(IINF,IINF);
  REP(i,1,4) {
    ii v1 = ii(0,IINF);
    rep(j,V) if( grade[j] == i ) v1.second = min(v1.second,j);
    REP(j,1,4) if( i != j ) {
      ii v2 = dijkstra(i,j);
      v1.first += v2.first;
      v1.second = min(v1.second,v2.second);
    }
    ans = min(ans,v1);
  }
  return ans;
}

void compute() {
  if( pattern1() ) { 
    int sp = IINF;
    rep(i,V) if( grade[i] ) sp = min(sp,i+1);
    assert( sp != IINF );
    cout << 2 << " " << sp << endl;
    return;
  }

  ii ans = ii(IINF,IINF);
  rep(i,V) if( grade[i] ) {
    rep(j,(int)G[i].size()) {
      int &e = G[i][j];
      if( grade[e] && grade[i] != grade[e] ) {
	ii v = dijkstra_for_pattern2(1+2+3-grade[i]-grade[e]);
	ans = min(ans,ii(v.first+1,v.second));
	//cout << ans.first+1 << " " << ans.second+1 << endl;
      }
    }
  }
  
  ii v1 = star();
  ii v2 = dijkstra_for_pattern3();
  ii v3 = min(v1,v2);
  ans = min(ans,v3);
  cout << ans.first << " " << ans.second+1 << endl;
}

int main() {
  cin >> V >> A >> B >> C;
  rep(i,A) { int tmp; cin >> tmp; --tmp; grade[tmp] = 1; }
  rep(i,B) { int tmp; cin >> tmp; --tmp; grade[tmp] = 2; }
  rep(i,C) { int tmp; cin >> tmp; --tmp; grade[tmp] = 3; }
  cin >> E;
  rep(i,E) {
    int x,y;
    cin >> x >> y;
    --x, --y;
    G[x].push_back(y);
    G[y].push_back(x);
  }
  compute();
  return 0;
}