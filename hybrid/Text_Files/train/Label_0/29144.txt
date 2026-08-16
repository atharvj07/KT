#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

const int N = 50;
const double EPS = 1e-8;

int n;
vector<pair<double, int> > data;

bool equals(double a, double b){ return abs(a - b) < EPS; }

int solve(){
  pair<double, double> dist[N];
  int round[N], res;
  for(int i=0;i<n;i++){
    dist[i] = make_pair(0.0, 0.0);
    round[i] = 1;
  }
  for(res=0;;res++){
    for(int i=0;i<n;i++) if(data[i].second) goto CONT; break;
    CONT:
    for(int i=0;i<n;i++){
      if(data[i].second == 0) continue;
      dist[i] = make_pair(dist[i].second, dist[i].second + data[i].first);
      for(int j=0;j<i;j++){
        if(data[j].second == 0) continue;
        if(round[i] != round[j]) continue;
        if(equals(dist[i].first, 0.0) && equals(dist[j].first, 0.0)) continue;
        if(!equals(dist[j].first, dist[i].first) && dist[j].first < dist[i].first) continue;
        if(!equals(dist[i].first, dist[j].second) && dist[i].first < dist[j].second) dist[i].second = min(dist[i].second, dist[j].second);
      }
      dist[i].second = min(dist[i].second, 1.0);
      if(equals(dist[i].second, 1.0)){
        dist[i].second = 0.0;
        if(round[i] == 0) data[i].second--;
        round[i] = 1 - round[i];
      }
    }
  }
  return res;
}

int main(){
  while(cin >> n && n){
    data.clear();
    for(int i=0;i<n;i++){
      int a, b;
      cin >> a >> b;
      data.push_back(make_pair(1.0 / a, b));
    }
    sort(data.begin(), data.end());
    cout << solve() << endl;
  }
}