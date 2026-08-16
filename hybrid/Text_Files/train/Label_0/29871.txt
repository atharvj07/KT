#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int, int> ii;

struct Node {
    int c;
    bool d;
    vector<int> tos;
};

const int INF = 1 << 30;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {-1, 0, 1, 0};
int w, h;
int c[102][102];
vector<string> ms;

int n;
vector<Node> ns;

int dijkstra(int s, int t) {
    for (int i = 1; i <= n; i++) {
        ns[i].c = INF;
        ns[i].d = false;
    }
    ns[s].c = 0;
    priority_queue<ii, vector<ii>, greater<ii> > q;
    q.push(make_pair(0, s));
    while (!q.empty()) {
        int i = q.top().second;
        q.pop();
        if (ns[i].d) {
            continue;
        }
        ns[i].d = true;
        if (i == t) {
            return ns[i].c;
        }
        int cost = ns[i].c + 1;
        for (vector<int>::iterator it = ns[i].tos.begin(); it != ns[i].tos.end(); it++) {
            if (!ns[*it].d && cost < ns[*it].c) {
                ns[*it].c = cost;
                q.push(make_pair(cost, *it));
            }
        }
    }
    return -1;
}

void fillC(int x, int y, int id) {
    c[y][x] = id;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < w+2 && 0 <= ny && ny < h+2 && c[ny][nx] == 0) {
            if ((id < 0 && ms[ny][nx] == '#') || (id > 0 && (ms[ny][nx] == '.' || ms[ny][nx] == '&'))) {
                fillC(nx, ny, id);
            }
        }
    }
}

int main() {
    while (cin >> w >> h, w|h) {
        ms.clear();
        string s0(w+2, '.');
        ms.push_back(s0);
        for (int i = 0; i < h; i++) {
            string str;
            cin >> str;
            ms.push_back("." + str + ".");
        }
        ms.push_back(s0);
        for (int y = 0; y < h+2; y++) {
            for (int x = 0; x < w+2; x++) {
                c[y][x] = 0;
            }
        }
        int id[2] = {0, 0};
        ii ts;
        for (int y = 0; y < h+2; y++) {
            for (int x = 0; x < w+2; x++) {
                if (ms[y][x] == '&') {
                    ts.first = y;
                    ts.second = x;
                }
                if (c[y][x] != 0) {
                    continue;
                }
                if (ms[y][x] == '#') {
                    fillC(x, y, --id[1]);
                } else {
                    fillC(x, y, ++id[0]);
                }
            }
        }
        int e = -id[1];
        vector<set<int> > es(e+1);
        for (int y = 1; y < h+2; y++) {
            for (int x = 1; x < w+2; x++) {
                int i, v;
                if (c[y][x] != c[y][x-1]) {
                    i = min(c[y][x], c[y][x-1]);
                    v = max(c[y][x], c[y][x-1]);
                    es[-i].insert(v);
                }
                if (c[y][x] != c[y-1][x]) {
                    i = min(c[y][x], c[y-1][x]);
                    v = max(c[y][x], c[y-1][x]);
                    es[-i].insert(v);
                }
            }
        }
        set<ii> ess;
        for (int i = 1; i <= e; i++) {
            for (set<int>::iterator it = es[i].begin(); it != es[i].end(); it++) {
                for (set<int>::iterator jt = it; jt != es[i].end(); jt++) {
                    if (*it != *jt) {
                        ess.insert(make_pair(*it, *jt));
                    }
                }
            }
        }
        n = id[0];
        ns.clear();
        ns.resize(n+1);
        for (set<ii>::iterator it = ess.begin(); it != ess.end(); it++) {
            ns[it->first].tos.push_back(it->second);
            ns[it->second].tos.push_back(it->first);
        }
        cout << dijkstra(1, c[ts.first][ts.second]) << endl;
    }
}