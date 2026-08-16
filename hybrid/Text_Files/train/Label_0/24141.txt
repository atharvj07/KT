#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <typeinfo>
#include <numeric>
#include <functional>
#include <unordered_map>

using namespace std;
using ll = long long;
using ull = unsigned long long;

const ll INF = 1e16;
const ll MOD = 1e9 + 7;

#define REP(i, n) for(int i = 0; i < n; i++)



using P = pair<long long, long long>;

struct edge{
    long long to, cost;
};

class dijkstra
{
private:
    long long vertex;   // 頂点数
    vector<vector<edge>> list;  //隣接リスト
    vector<long long> distance;    // 距離
public:
    void init(long long n);  // nは頂点の数
    void add_edge(long long v1, long long v2, long long cost);    // 頂点v1から頂点v2に辺を張る
    void run(long long s);        // sは開始地点。
    long long get_distance(long long v);    // 頂点vへの距離を返す
};

void dijkstra::init(long long n){
    vertex = n;
    list.resize(n);
}

void dijkstra::add_edge(long long v1, long long v2, long long cost){
    list[v1].push_back({ v2, cost });
}

void dijkstra::run(long long s){
    priority_queue<P, vector<P>, greater<P>> que;
    distance = vector<long long>(vertex, INF);
    distance[s] = 0;    // 開始点の距離は0
    que.push(P(0, s));
    
    while(!que.empty()){
        P p = que.top(); que.pop();
        long long v = p.second;
        if(distance[v] < p.first) continue;
        for(auto e : list[v]){
            if(distance[e.to] > distance[v] + e.cost){
                distance[e.to] = distance[v] + e.cost;
                que.push(P(distance[e.to], e.to));
            }
        }
    }
}

long long dijkstra::get_distance(long long v){
    return distance[v];
}

 
int main() {
    int h, w;
    string s, t, a[55];
    
    cin >> h >> w >> s >> t;
    REP(i, h){
        cin >> a[i];
    }
    
    int ss = s[0] - 'A', tt = t[0] - 'A';
    // cout << ss << ' ' << tt << endl;
    
    dijkstra dik;
    dik.init(2500);
    
    REP(i, h){
        REP(j, w){
            if(a[i][j] != '.' && a[i][j] != 'o' && a[i][j] != '-' && a[i][j] != '|'){
                if(j > 1){
                    if(a[i][j - 2] == '-'){
                        for(int k = j - 2; k >= 0; k--){
                            if(a[i][k] != '.' && a[i][k] != 'o' && a[i][k] != '-' && a[i][k] != '|'){
                                dik.add_edge(a[i][j] - 'A', a[i][k] - 'A', 1);
                                dik.add_edge(a[i][k] - 'A', a[i][j] - 'A', 1);
                                // cout << a[i][j] - 'A' << ' ' << a[i][k] - 'A' << endl;
                                goto aaa;
                            }
                        }
                    }
                }
            aaa:
                
                if(j < w - 2){
                    if(a[i][j + 2] == '-'){
                        for(int k = j + 2; k < w; k++){
                            if(a[i][k] != '.' && a[i][k] != 'o' && a[i][k] != '-' && a[i][k] != '|'){
                                dik.add_edge(a[i][j] - 'A', a[i][k] - 'A', 1);
                                dik.add_edge(a[i][k] - 'A', a[i][j] - 'A', 1);
                                // cout << a[i][j] - 'A' << ' ' << a[i][k] - 'A' << endl;
                                goto bbb;
                            }
                        }
                    }
                }
            bbb:
                
                if(i > 1){
                    if(a[i - 2][j] == '|'){
                        for(int k = i - 2; k >= 0; k--){
                            if(a[k][j] != '.' && a[k][j] != 'o' && a[k][j] != '-' && a[k][j] != '|'){
                                dik.add_edge(a[i][j] - 'A', a[k][j] - 'A', 1);
                                dik.add_edge(a[k][j] - 'A', a[i][j] - 'A', 1);
                                // cout << a[i][j] - 'A' << ' ' << a[k][j] - 'A' << endl;
                                goto ccc;
                            }
                        }
                    }
                }
            ccc:
                
                if(i < h - 2){
                    if(a[i + 2][j] == '|'){
                        for(int k = i + 2; k < h; k++){
                            if(a[k][j] != '.' && a[k][j] != 'o' && a[k][j] != '-' && a[k][j] != '|'){
                                dik.add_edge(a[i][j] - 'A', a[k][j] - 'A', 1);
                                dik.add_edge(a[k][j] - 'A', a[i][j] - 'A', 1);
                                // cout << a[i][j] - 'A' << ' ' << a[k][j] - 'A' << endl;
                                break;
                            }
                        }
                    }
                }
            }
        }
    }
    
    dik.run(ss);
    
    cout << dik.get_distance(tt) << endl;
}

