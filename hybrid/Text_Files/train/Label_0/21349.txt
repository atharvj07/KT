/*
05:46 - 06:33 飯休憩
06:54 - 寝落ち
 */
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<deque>
#include<cassert>
#include<climits>
#include<map>
#include<set>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define IINF (INT_MAX)
#define MAX 20

using namespace std;

typedef pair<int,int> ii;

struct Data{
  int cur;
  double remain;
  int phase;
  Data(int cur=IINF,double remain=IINF,double phase=IINF):cur(cur),remain(remain),phase(phase){}
};

int w,h,fx,fy,l,px,py,V;
double fq,t;
double p[MAX][MAX],divide[MAX*MAX],tank[MAX*MAX],cap[MAX*MAX],area[MAX*MAX],coef[MAX*MAX][MAX*MAX];
vector<int> G[MAX*MAX];
int Index[MAX][MAX];
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

inline bool isValid(int x,int y){ return ( 0 <= x && x < w && 0 <= y && y < h ); }

void dfs(int x,int y,int index){
  if(Index[y][x] != -1)return;
  Index[y][x] = index;
  area[index]++;
  rep(i,4){
    int nx = x + dx[i];
    int ny = y + dy[i];
    if(!isValid(nx,ny))continue;
    if(p[y][x] != p[ny][nx])continue;
    dfs(nx,ny,index);
  }
}

void printIndex(){
  rep(i,h){
    rep(j,w){
      cout << "(" << j << "," << i << ") = " << Index[i][j] << endl;
    }
  }
  cout << endl;
}

void INIT(){
  rep(i,h)rep(j,w)G[j+i*w].clear(),Index[i][j] = -1;
  rep(i,h*w)divide[i] = cap[i] = -1, area[i] = 0;
  rep(i,h*w)rep(j,h*w)coef[i][j] = 0;
  int dex = 0;
  rep(y,h)rep(x,w){
    if(Index[y][x] != -1)continue;
    if(p[y][x] == 0)continue;
    dfs(x,y,dex);
    cap[dex] = 30.0 * 30.0 * 30.0 * area[dex];
    dex++;
  }

  //printIndex();

  V = dex;
  //cout << "V = " << V << endl;
  set<int> edge[dex];
  set<ii> cost[dex];
  set<ii> COEF[V][V];
  int tmp=IINF;
  rep(y,h){
    rep(x,w){
      //cout << "(" << x << "," << y << ")" << endl;
      if(p[y][x] == 0)continue;
      rep(k,4){
	int nx = x + dx[k];
	int ny = y + dy[k];
	//cout << "nx = " << nx << "," << ny << " k = " << k << endl;
	if(!isValid(nx,ny)){
	  cost[Index[y][x]].insert(ii(tmp,tmp));
	  tmp--;
	  continue;
	}
	if(p[ny][nx] == 0){
	  cost[Index[y][x]].insert(/*ii(nx,ny)*/ii(tmp,tmp));
	  tmp--;
	  continue;
	}
	if(Index[ny][nx] == Index[y][x])continue;
	if(p[y][x] <= p[ny][nx])continue;
	//cout << "k = " << k << endl;
	assert(Index[ny][nx] != -1);
	//cout << "COEF[" << Index[y][x] << "][" << Index[ny][nx] << "] = " << endl;
	COEF[Index[y][x]][Index[ny][nx]].insert(/*ii(nx,ny)*/ii(tmp,tmp));
	tmp--;

	cost[Index[y][x]].insert(/*ii(nx,ny)*/ii(tmp,tmp));
	tmp--;
	edge[Index[y][x]].insert(Index[ny][nx]);

      }
    }
  }

  rep(from,V){
    for(int to : edge[from]){
      G[from].push_back(to);
    }
    rep(i,G[from].size()){
      assert(!COEF[from][G[from][i]].empty());
      coef[from][G[from][i]] = (double)COEF[from][G[from][i]].size();
    }
    divide[from] = (double)cost[from].size();
  }


  /*
  rep(sp,V) cout << "divide[" << sp << "] = " << divide[sp] << endl;
  rep(sp,V) cout << "cap[" << sp << "] = " << cap[sp] << endl;
  rep(sp,V) cout << "area[" << sp << "] = " << area[sp] << endl;
  rep(sp,V){
    rep(gp,V){
      cout << "coef[" << sp << "][" << gp << "] = " << coef[sp][gp] << endl;
    }
    cout << endl;
  }
  rep(sp,V){
    cout << "sp = " << sp << endl;
    rep(i,G[sp].size()){
      cout << G[sp][i] << " ";
    } cout << endl;
  }
  */


}

int main(){
  while(cin >> w >> h,w|h){
    cin >> fx >> fy >> fq;
    rep(i,h)rep(j,w)cin >> p[i][j];

    INIT();
    //cout << "------------" << endl;
    cin >> l;
    rep(_,l){
      cin >> t >> px >> py;
      if(p[py][px] == 0){
	cout << 0 << endl;
	continue;
      }
      assert(p[py][px] != 0);
      deque<Data> deq;
      deq.push_back(Data(Index[fy][fx],fq*t,0));
      int cphase = 0;
      //cout << "start sumilate" << endl;
      double store[V];
      rep(i,V)store[i] = tank[i] = 0;
      while(true){
	if(deq.empty()){
	  bool update = false;
	  rep(i,V){
	    //cout << "store[" << i << "] = " << store[i]  << endl;
	    if(store[i] == 0)continue;
	    //cout << "store[" << i << "]+tank[" << i << "] <= cap[" << i << "] : " << store[i]+tank[i] << " <= " << cap[i] << endl;
	    if(store[i]+tank[i] <= cap[i]){
	      tank[i] += store[i];
	    } else {

	      if(G[i].empty()){
		tank[i] = cap[i];
		continue;
	      }
	      update = true;
	      //deq.push_back(Data(i,store[i]+tank[i]-cap[i]));
	      //assert(divide[i] != 0);
	      double cost = (store[i]+tank[i]-cap[i])/divide[i];

	      //cout << i << " -th : cost => " << cost << " ( = ( " << store[i] << "+" << tank[i] << "-" << cap[i] << " ) / " << divide[i] << ")" << endl; 
	      tank[i] = cap[i];

	      rep(j,G[i].size()){
		int next = G[i][j];
		//cout << "deq <= Data(" << next << "," << cost*coef[i][next] << ")" << endl;
		assert(coef[i][next] != 0);
		deq.push_back(Data(next,cost*coef[i][next]));
	      }
	    }

	  }
	  /*
	  cout << "update = " << update << endl;
	  cout << "phase-------" << endl;
	  rep(k,V)cout << "tank[" << k << "] = " << tank[k] << endl;
	  cout << endl;
	  */
	  if(!update)break;
	  rep(i,V)store[i] = 0; 


	}

	Data data = deq.front(); deq.pop_front();
	//cout << "(" << data.cur << "," << data.remain << ")" << endl;

	double remain = data.remain;
	double limit = cap[data.cur] - tank[data.cur];
	assert(limit >= 0);
	//cout << "remain = " << remain << " limit = " << limit << endl;
	store[data.cur] += remain;
	/*
	if(limit >= remain){
	  store[data.cur] += remain;
	} else {
	  store[data.cur] += limit;
	  double cost = ( remain - limit ) / divide[data.cur];
	  rep(i,G[data.cur].size()){
	    int next = G[data.cur][i];
	    store[next] += cost;
	  }
	}
	*/
      }

      cout << floor(tank[Index[py][px]]/(30.0*30.0)/area[Index[py][px]]) << endl;

    }

  }
  return 0;
}