#include <set>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <climits>

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  int nA = getInt();
  int nB = getInt();
  int W  = getInt();

  vector<pair<int, int> > cmA(nA);
  vector<pair<int, int> > cmB(nB);

  vector<int> cs; cs.reserve(nA + nB);

  REP(i,nA){
    cmA[i].second = getInt();
    cmA[i].first  = getInt();
  }
  REP(i,nB){
    cmB[i].second = getInt();
    cmB[i].first  = getInt();
  }
  sort(cmA.begin(), cmA.end());
  sort(cmB.begin(), cmB.end());

  REP(i,nA) cs.push_back(cmA[i].first);
  REP(i,nB) cs.push_back(cmB[i].first);

  sort(cs.begin(), cs.end());
  cs.erase(unique(cs.begin(), cs.end()), cs.end());

  int ans = INT_MAX;

  for(int i = 0; i < cs.size(); i++){
    set<int> candA; candA.insert(0);
    set<int> candB; candB.insert(0);
    vector<int> candAA; candAA.reserve(W + 1); candAA.push_back(0);
    vector<int> candBB; candBB.reserve(W + 1); candBB.push_back(0);
    vector<bool> flagA(W + 1);
    vector<bool> flagB(W + 1);

    int ptrA = 0;
    int ptrB = 0;

    for(int j = i; j < cs.size(); j++){
      int c1 = cs[i];
      int c2 = cs[j];

      if(c2 - c1 >= ans) break;

      {
        int cai = candAA.size();
        while(ptrA != nA && cmA[ptrA].first < c2) ptrA++;
        while(ptrA != nA && cmA[ptrA].first == c2){
          int cnt = 0;
          for(int i = 0; i < cai; ++i){
            int ww = cmA[ptrA].second + candAA[i];
            if(ww <= W && !flagA[ww]){
              flagA[ww] = true;
              candAA.push_back(ww);
              candA.insert(ww);
              cnt++;
            }
          }
          ptrA++;
          cai += cnt;
        }
      }

      {
        int cbi = candBB.size();
        while(ptrB != nB && cmB[ptrB].first < c2) ptrB++;
        while(ptrB != nB && cmB[ptrB].first == c2){
          int cnt = 0;
          for(int i = 0; i < cbi; i++){
            int ww = cmB[ptrB].second + candBB[i];
            if(ww <= W && !flagB[ww]){
              flagB[ww] = true;
              candBB.push_back(ww);
              candB.insert(ww);
              cnt++;
            }
          }
          ptrB++;
          cbi += cnt;
        }
      }

      int diff = INT_MAX;

      if(candAA.size() != 1 && candBB.size() != 1){
        FOR(itA, candA) if(*itA != 0){
          set<int>::iterator itB = lower_bound(candB.begin(), candB.end(), *itA);
          if(itB != candB.end() && *itB != 0)
            diff = min(diff, abs(*itA - *itB));
          if(itB != candB.begin()) --itB;
          if(*itB != 0) diff = min(diff, abs(*itA - *itB));
        }
      }

      // if(c2 - c1 <= 1 && diff != INT_MAX) printf("%d %d\n", c2 - c1, diff);
      ans = min(ans, max(diff, c2 - c1));
    }
  }

  printf("%d\n", ans);

  return 0;
}