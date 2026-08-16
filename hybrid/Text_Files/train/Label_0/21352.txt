#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>

#define f first
#define s second

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))
#define print(x) printf("%d\n",x)

using namespace std;

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};

int getInt(){
  int a; scanf("%d", &a); return a;
}

int p[10][10];
int id[10][10];
int w, h;
int cnt[100];
int all[100];
int g[100][100];
int idcnt;
double cap[100];

void dfs(int y, int x, int ids){
  id[y][x] = ids;

  REP(i,4){
    int yy = y + _dy[i];
    int xx = x + _dx[i];

    if(ISIN(xx, yy, w, h) && id[yy][xx] == -1 && p[yy][xx] == p[y][x]){
      dfs(yy, xx, ids);
    }
  }
}

const double eps = 1e-10;
void doflow(int i, double f){
  if(f < eps) return;
  double rest = (30.0 - cap[i]) * (cnt[i] * 30.0 * 30.0);

  if(rest < f){
    cap[i] = 30.0;
    f -= rest;
  }else{
    cap[i] += f / (cnt[i] * 30.0 * 30.0);
    f = 0.0;
  }

  if(f > eps){
    REP(j,idcnt) if(g[i][j] > 0){
      doflow(j, f * g[i][j] / all[i]);
    }
  }
}

int main(){
  while(true){
    w = getInt();
    h = getInt();

    if(w + h == 0) break;

    int fx = getInt();
    int fy = getInt();
    int fp = getInt();

    REP(i,h) REP(j,w){
      p[i][j]  = getInt();
      id[i][j] = -1;
    }

    int l = getInt();

    vector<pair<int, pair<int, int> > > q(l);

    REP(i,l){
      q[i].f   = getInt();
      q[i].s.f = getInt();
      q[i].s.s = getInt();
    }

    // ID
    idcnt = 0;
    REP(i,h) REP(j,w) if(id[i][j] == -1 && p[i][j] != 0){
      dfs(i,j,idcnt++);
    }

    REP(i, idcnt){
      cnt[i] = 0;
      all[i] = 0;
      REP(j, idcnt){
        g[i][j] = 0;
      }
    }

    REP(y,h) REP(x,w) if(id[y][x] != -1){
      cnt[id[y][x]]++;

      REP(k,4){
        int yy = y + _dy[k];
        int xx = x + _dx[k];

        if(ISIN(xx, yy, w, h) && id[yy][xx] == id[y][x]){
        }else{
          if(ISIN(xx, yy, w, h) && id[yy][xx] != -1){
            if(p[y][x] > p[yy][xx]){
              all[id[y][x]]++;
              g[id[y][x]][id[yy][xx]]++;
            }else{
            }
          }else{
            all[id[y][x]]++;
          }
        }
      }
    }

    int sid  = id[fy][fx];
    REP(i,l){
      int t = q[i].f;
      int x = q[i].s.f;
      int y = q[i].s.s;

      REP(i,idcnt) cap[i] = 0.0;
      doflow(sid, fp * t);

      printf("%d\n", (int)floor(cap[id[y][x]] + eps));
    }
  }

  return 0;
}