#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<functional>
 
using namespace std;

/* constant */

const int MAX_W = 100;
const int MAX_H = 100;
const int MAX_HW = MAX_H * MAX_W;

const int INF = 1 << 30;

const int dxs[] = {  1,  0, -1,  0 };
const int dys[] = {  0,  1,  0, -1 };

/* typedef */

struct Signal {
  int nst, ewt, itv, s;
};

struct Stat {
  int d, pos, drc;
  Stat() {}
  Stat(int _d, int _pos, int _drc) { d = _d, pos = _pos, drc = _drc; }
  bool operator<(const Stat& st0) const { return d > st0.d; }
  void print() { printf("d=%d, pos=%d, drc=%d\n", d, pos, drc); }
};

enum { D_NS = 0, D_EW = 1 };

typedef vector<Stat> vs;

/* global variables */

int w, h, hw;
int dws[MAX_W], dhs[MAX_H];
Signal sgnls[MAX_HW + 2];

vs nbrs[MAX_HW + 2];
int dists[MAX_HW + 2][2];

/* subroutines */

void onroad(int x, int n, int *ds, int& i, int& dx) {
  i = 0, dx = x;
  while (i < n && dx >= ds[i]) dx -= ds[i], i++;
}

int time_go(Signal& sgnl, int t, int drc) {
  int rt = t % sgnl.itv;
  int tg = -1;
  
  if (sgnl.s == D_NS) {	// nst -> ewt
    if (drc == D_NS) tg = (rt < sgnl.nst) ? t : sgnl.itv * (t / sgnl.itv + 1);
    else tg = (rt >= sgnl.nst) ? t : (t / sgnl.itv) * sgnl.itv + sgnl.nst;
  }
  else {	// ewt -> nst
    if (drc == D_EW) tg = (rt < sgnl.ewt) ? t : sgnl.itv * (t / sgnl.itv + 1);
    else tg = (rt >= sgnl.ewt) ? t : (t / sgnl.itv) * sgnl.itv + sgnl.ewt;
  }

  return tg;
}

/* main */

int main() {
  for (;;) {
    cin >> w >> h;
    if (w == 0) break;

    hw = h * w;
    
    for (int i = 0; i < w - 1; i++) cin >> dws[i];
    for (int i = 0; i < h - 1; i++) cin >> dhs[i];

    for (int y = 0; y < h; y++)
      for (int x = 0; x < w; x++) {
	int pos = y * w + x;
	Signal& sgnl = sgnls[pos];
	cin >> sgnl.nst >> sgnl.ewt >> sgnl.s;
	sgnl.itv = sgnl.nst + sgnl.ewt;

	nbrs[pos].clear();

	for (int di = 0; di < 4; di++) {
	  int x0 = x + dxs[di];
	  int y0 = y + dys[di];
	  if (x0 >= 0 && x0 < w && y0 >= 0 && y0 < h) {
	    int pos0 = y0 * w + x0;
	    int ec, edrc;
	    if (x0 != x) {
	      ec = dws[(x0 < x) ? x0 : x];
	      edrc = D_EW;
	    }
	    else {
	      ec = dhs[(y0 < y) ? y0 : y];
	      edrc = D_NS;
	    }
	    nbrs[pos].push_back(Stat(ec, pos0, edrc));
	  }
	}
      }

    int sx, sy;
    cin >> sx >> sy;

    int sxi, syi, sdx, sdy;
    onroad(sx, w - 1, dws, sxi, sdx);
    onroad(sy, h - 1, dhs, syi, sdy);
    //printf("(sxi,syi)=(%d,%d), (sdx,sdy)=(%d,%d)\n", sxi, syi, sdx, sdy);
    
    nbrs[hw].clear();
    
    if (sdx != 0) {
      int pos0 = syi * w + sxi, pos1 = pos0 + 1;
      nbrs[hw].push_back(Stat(sdx, pos0, D_EW));
      nbrs[hw].push_back(Stat(dws[sxi] - sdx, pos1, D_EW));
      sgnls[hw].nst = 0;
      sgnls[hw].ewt = 1;
      sgnls[hw].itv = 1;
      sgnls[hw].s = D_EW;
    }
    else {
      int pos0 = syi * w + sxi, pos1 = pos0 + w;
      nbrs[hw].push_back(Stat(sdy, pos0, D_NS));
      nbrs[hw].push_back(Stat(dhs[syi] - sdy, pos1, D_NS));
      sgnls[hw].nst = 1;
      sgnls[hw].ewt = 0;
      sgnls[hw].itv = 1;
      sgnls[hw].s = D_NS;
    }

    int gx, gy;
    cin >> gx >> gy;

    int gxi, gyi, gdx, gdy;
    onroad(gx, w - 1, dws, gxi, gdx);
    onroad(gy, h - 1, dhs, gyi, gdy);
    //printf("(gxi,gyi)=(%d,%d), (gdx,gdy)=(%d,%d)\n", gxi, gyi, gdx, gdy);

    if (gdx != 0) {
      int pos0 = gyi * w + gxi, pos1 = pos0 + 1;
      nbrs[pos0].push_back(Stat(gdx, hw + 1, D_EW));
      nbrs[pos1].push_back(Stat(dws[gxi] - gdx, hw + 1, D_EW));
    }
    else {
      int pos0 = gyi * w + gxi, pos1 = pos0 + w;
      nbrs[pos0].push_back(Stat(gdy, hw + 1, D_NS));
      nbrs[pos1].push_back(Stat(dhs[gyi] - gdy, hw + 1, D_NS));
    }

    if (sxi == gxi && syi == gyi) {
      if (sdy == 0 && gdy == 0) {
	int dx = (gdx > sdx) ? gdx - sdx : sdx - gdx;
	nbrs[hw].push_back(Stat(dx, hw + 1, D_EW));
      }
      else if (sdx == 0 && gdx == 0) {
	int dy = (gdy > sdy) ? gdy - sdy : sdy - gdy;
	nbrs[hw].push_back(Stat(dy, hw + 1, D_NS));
      }
    }
    
    for (int pos = 0; pos < hw + 2; pos++)
      for (int drc = 0; drc < 2; drc++)
	dists[pos][drc] = INF;

    dists[hw][0] = dists[hw][1] = 0;

    priority_queue<Stat> q;
    q.push(Stat(0, hw, sgnls[hw].s));

    int mind = INF;
    
    while (! q.empty()) {
      Stat u = q.top();
      q.pop();
      //u.print();
      
      if (u.d != dists[u.pos][u.drc]) continue;
      if (u.pos == hw + 1) {
	mind = u.d;
	break;
      }

      int ud = time_go(sgnls[u.pos], u.d, u.drc);
      vs& nbru = nbrs[u.pos];

      for (vs::iterator vit = nbru.begin(); vit != nbru.end(); vit++) {
	Stat& v = *vit;
	int vd =  ud + v.d;

	if (dists[v.pos][v.drc] > vd) {
	  dists[v.pos][v.drc] = vd;
	  q.push(Stat(vd, v.pos, v.drc));
	}
      }
    }

    cout << mind << endl;
  }

  return 0;
}