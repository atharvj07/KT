#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<double, double> P;

int main(){
  int N; double W; cin >> N >> W;
  vector<P> items;
  for(int i=0; i<N; i++){
    double v, w; cin >> v >> w;
    items.push_back(P(v, w));
  }
  sort(items.begin(), items.end(), [](const P &a, const P &b){
    return a.first/a.second > b.first/b.second;
  });
  double k = 0;
  for(int i=0; i<N; i++){
    if(W == 0) break;
    if(items[i].second < W){
      k += items[i].first;
      W -= items[i].second;
    }
    else{
      k += ((items[i].first)/(items[i].second)) * W;
      W = 0;
    }
  }
  cout << fixed << k << endl;
}
