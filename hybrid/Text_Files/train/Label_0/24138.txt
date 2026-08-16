#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <climits>

#define rep(i, m, n) for(int i=int(m);i<int(n);i++)
#define EACH(i, c) for (auto &(i): c)
#define all(c) begin(c),end(c)
#define EXIST(s, e) ((s).find(e)!=(s).end())
#define SORT(c) sort(begin(c),end(c))
#define pb emplace_back
#define MP make_pair
#define SZ(a) int((a).size())

//#define LOCAL 0
//#ifdef LOCAL
//#define DEBUG(s) cout << (s) << endl
//#define dump(x)  cerr << #x << " = " << (x) << endl
//#define BR cout << endl;
//#else
//#define DEBUG(s) do{}while(0)
//#define dump(x) do{}while(0)
//#define BR
//#endif


//改造
typedef long long int ll;
using namespace std;
#define INF (1 << 30) - 1
#define INFl (ll)5e15
#define DEBUG 0 //デバッグする時1にしてね
#define dump(x)  cerr << #x << " = " << (x) << endl
#define MOD 1000000007

//ここから編集する
class Dijkstra {
public:
    struct edge {
        ll to, cost;
    };
    typedef pair<ll, ll> P;//firstは最短距離、secondは頂点の番号

    int V;//超点数
    vector<vector<edge> > G;//グラフ,G[i]はiから出る辺の集合,G[i][j]はiから出る辺のj番目の辺
    vector<ll> d; //最短距離

    //0origin
    Dijkstra(int N) {
        V = N;
        G = vector<vector<edge> >(N);
        d = vector<ll>(N);
    };

    void dijkstra(int s) {
        priority_queue<P, vector<P>, greater<P> > que;
        fill(d.begin(), d.end(), INFl);
        d[s] = 0;
        que.push(P(0, s));

        while (!que.empty()) {
            P p = que.top();
            que.pop();
            ll v = p.second;
            if (d[v] < p.first) continue;
            for (int i = 0; i < G[v].size(); i++) {
                edge e = G[v][i];
                if (d[e.to] > d[v] + e.cost && !(d[e.to] == INFl && d[v] == INFl)) {
                    d[e.to] = d[v] + e.cost;
                    que.push(P(d[e.to], e.to));
                }
            }
        }

    }

    /* 頂点fromに頂点toに達するコストcostの辺を貼る */
    void addEdge(int from, int to, int cost) {
        edge e;
        e.to = to;
        e.cost = cost;
        G[from].push_back(e);
    }
};


int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int H, W;
    char s, t;
    cin >> H >> W >> s >> t;
    vector<vector<char> > ch(H + 2, vector<char>(W + 2, '.'));

    rep(i, 1, H + 1) {
        rep(j, 1, W + 1) {
            cin >> ch[i][j];
        }
    }

    Dijkstra dij(26);

    for (int i = 1; i < H + 1; i++) {
        for (int j = 1; j < W + 1; j++) {
            char c = ch[i][j];
            if (c >= 'A' && c <= 'Z') {
                for (int di = 1; ch[i + di][j] != '.' && ch[i + di][j] != '-'; di++) {
                    if (ch[i + di][j] >= 'A' && ch[i + di][j] <= 'Z') {
                        dij.addEdge(c - 'A', ch[i + di][j] - 'A', 1);
                        dij.addEdge(ch[i + di][j] - 'A', c - 'A', 1);
                        break;
                    }
                }
                for (int dj = 1; ch[i][j + dj] != '.' && ch[i][j + dj] != '|'; dj++) {
                    if (ch[i][j + dj] >= 'A' && ch[i][j + dj] <= 'Z') {
                        dij.addEdge(c - 'A', ch[i][j + dj] - 'A', 1);
                        dij.addEdge(ch[i][j + dj] - 'A', c - 'A', 1);
                        break;
                    }
                }
            }
        }
    }
    dij.dijkstra(s - 'A');
    cout << dij.d[t - 'A'] << endl;


    return 0;
}

