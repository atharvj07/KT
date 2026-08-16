#include <bits/stdc++.h>
#define range(i, a, n) for(int (i) = (a); (i) < (n); (i)++)
#define rep(i, n) for(int (i) = 0; (i) < (n); (i)++)
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main(void){
    int n, m, k; cin >> n >> m >> k;
    int M = (1 << m) - 1;

    vi d2l(n);
    rep(i, n) d2l[i] = m;
    rep(i, m){
        int v; cin >> v;
        v--;

        d2l[v] = i;
    }

    vvi edge_r2r(m, vi(k));
    rep(i, n){
        rep(j, k){
            int v; cin >> v;
            v = d2l[v - 1];
            int u = d2l[i];

            if(u < m) edge_r2r[u][j] = v;
        }
    }

    vvi edge(1 << m);
    rep(i, 1 << m){
        rep(j, k){
            int next = 0;
            rep(l, m){
                if(!((i >> l) & 1)) continue;
                int v = edge_r2r[l][j];
                if(v < m) next |= (1 << v);
            }
            if(i != next){
                edge[i].push_back(next);
            }
        }
    }

    vi used(1 << m);
    
    // (cost, v)
    queue<pair<int, int>> q;
    q.push(make_pair(0, M));

#define F first
#define S second

    int res = -1;
    while(q.size()){
        int cur_c = q.front().F;
        int cur_v = q.front().S;
        q.pop();

        if(used[cur_v]) continue;
        used[cur_v] = true;

        if(cur_v == 0){
            res = cur_c;
            break;
        }

        for(auto && e : edge[cur_v]){
            int next_c = cur_c + 1;
            int next_v = e;

            if(used[next_v]) continue;

            q.push(make_pair(next_c, next_v));
        }
    }

    cout << res << endl;

	return 0;
}