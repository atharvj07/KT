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

const int MAX_T = 20000;
const int INT_T = 1000;

const int MAX_M = 100;
const int MAX_N = 100;

const int PKT_HDR = 3;

/* typedef */

struct Answer {
  int p, t, size;
  Answer() {}
  Answer(int _p, int _t, int _size) { p = _p, t = _t, size = _size; }
  bool operator<(const Answer& a0) const { return t < a0.t; }
  void print() { printf("Answer:p=%d,t=%d,size=%d\n", p, t, size); }
};

typedef vector<Answer> va;

/* global variables */

int m, n, l;
int ds[MAX_M];
int ssent, srecv, csents[MAX_M], crecvs[MAX_M];
va vans;
int ansed[MAX_M], newansed[MAX_M];

/* subroutines */

/* main */

int main() {
  for (bool first = true;; first = false) {
    cin >> m >> n;
    if (m == 0) break;

    ssent = srecv = 0;
    memset(csents, 0, sizeof(csents));
    memset(crecvs, 0, sizeof(crecvs));

    for (int i = 0; i < m; i++)
      cin >> ds[i];

    while (n--) {
      vans.clear();
      
      cin >> l;
      for (int i = 0; i < l; i++) {
	int p, t;
	string ans;
	cin >> p >> t >> ans;
	vans.push_back(Answer(p, t + 2 * ds[p], ans.length()));
      }
      sort(vans.begin(), vans.end());

      // problem-start
      for (int i = 0; i < m; i++) {
	ssent += PKT_HDR;
	crecvs[i] += PKT_HDR;
      }

      int ai = 0;
      int nansed = 0, sum = 0;
      memset(ansed, 0, sizeof(ansed));
      
      for (int t = 0; t <= MAX_T; t += INT_T) {
	//printf("t=%d\n", t);
	int nnewansed = 0, newsum = 0;
	memset(newansed, 0, sizeof(newansed));

	// receive Answer
	while (ai < l && vans[ai].t < t) {
	  Answer& vai = vans[ai];
	  //vai.print();
	  
	  int data = 2 + vai.size;
	  csents[vai.p] += PKT_HDR + data;
	  srecv += PKT_HDR + data;
	  ansed[vai.p] = newansed[vai.p] = data;
	  nansed++;
	  nnewansed++;
	  sum += data;
	  newsum += data;
	  ai++;
	}

	// notification
	if (nnewansed > 0) {
	  for (int i = 0; i < m; i++) {
	    if (ansed[i] == 0) {	// type A
	      int pkt = PKT_HDR + 1 + nnewansed;
	      ssent += pkt;
	      crecvs[i] += pkt;
	      //printf("  t=%d: type A->%d, %d byte\n", t, i, pkt);
	    }
	    else if (newansed[i] > 0 && nansed > 1) {	// type B (exclude)
	      int pkt = PKT_HDR + 1 + sum - newansed[i];
	      ssent += pkt;
	      crecvs[i] += pkt;
	      //printf("  t=%d: type B(excl)->%d, %d byte\n", t, i, pkt);
	    }
	    else if (newansed[i] == 0 && ansed[i] > 0) {	// type B
	      int pkt = PKT_HDR + 1 + newsum;
	      ssent += pkt;
	      crecvs[i] += pkt;
	      //printf("  t=%d: type B->%d, %d byte\n", t, i, pkt);
	    }
	  }
	}
      }

      // problem-end
      for (int i = 0; i < m; i++) {
	ssent += PKT_HDR + 1;
	crecvs[i] += PKT_HDR + 1;
      }
    }

    if (! first) cout << endl;
    
    printf("%d %d\n", ssent, srecv);
    for (int i = 0; i < m; i++)
      printf("%d %d\n", csents[i], crecvs[i]);
  }

  return 0;
}