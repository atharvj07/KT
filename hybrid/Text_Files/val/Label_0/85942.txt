#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> l_l;
typedef pair<int, int> i_i;

#define EPS (1e-7)
#define INF (1e9)
#define PI (acos(-1))
//const ll mod = 1000000007;
int N, M, K;
int D[20];
int v[105][105];
int inv[105];
int dist[1<<17];

bool chmin(int &a, int b) {
    if(a > b) {
        a = b;
        return true;
    }
    return false;
}

int main() {
    //cout.precision(10);
    cin >> N >> M >> K;
    for(int i = 0; i < (1 << M); i++) dist[i] = INF;
    for(int i = 0; i <= N; i++) inv[i] = -1;
    for(int i = 0; i < M; i++) {
        cin >> D[i];
        inv[D[i]] = i;
    }
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= K; j++) {
            cin >> v[i][j];
        }
    }
    dist[(1 << M) - 1] = 0;
    queue<int> que;
    que.push((1 << M) - 1);
    while(!que.empty()) {
        int now = que.front();
        que.pop();
        for(int j = 1; j <= K; j++) {
            int newbit = 0;
            for(int i = 0; i < M; i++) {
                if(!(now & (1 << i))) continue;
                int next = v[D[i]][j];
                if(inv[next] == -1) continue;
                newbit |= (1 << inv[next]);
            }
            if(chmin(dist[newbit], dist[now] + 1)) que.push(newbit);
        }
    }
    cout << dist[0] << endl;
    return 0;
}

