#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <random>
#include <chrono>
#include <queue>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
#define fs first
#define sc second
#define INF 1000000000
#define MOD 1000000007
#define EPS 0.00000001



int main() {
    int V, E; cin >> V >> E;
    vector<vector<int>> to(V);
    vector<int> Nyuji(V);
    for(int i=0; i<E; i++){
        int s, t; cin >> s >> t;
        to[s].push_back(t);
        Nyuji[t]++;
    }
    
    vector<PII> S;
    for(int i=0; i<V; i++){
        if(Nyuji[i]==0) S.push_back({i, 1});
    }
    
    vector<int> ans;
    int done = 0;
    while(S.size()){
        PII p = S.back();
        done++;
        ans.push_back(p.fs);
        S.pop_back();
        for(int t:to[p.fs]){
            Nyuji[t]--;
            if(Nyuji[t]==0){
                S.push_back({t, p.sc+1});
            }
        }
    }
    
    if(done!=V){
        cout << 1 << endl;
        return 0;
    }
    
//    for(int a:ans) cout <<  << endl;
    cout << 0 << endl;
    
    return 0;
}


