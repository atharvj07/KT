#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
typedef pair<int, int> pint;
struct town{
    int x, y;
    map<string, int> shop;
    town() {
        x = y = -1;
        shop.clear();
    }
    town(int x, int y) : x(x), y(y){ shop.clear();}
};
int N, M, W, T;
map<string, pint> products;
vector<town> towns;
int dp1[1 << 7][7];//dp[S][i] := ??????s???????????£???i???????????´??????????????????
int dist[1 << 7];
void salesman(){
    rep(i, 1 << N) rep(j, N) dp1[i][j] = INF;
    rep(i, 1 << N) dist[i] = INF;
    rep(i, N)
      dp1[1 << i][i] = abs(towns[i].x) + abs(towns[i].y);
    rep(s, 1 << N)
      rep(i, N) if(1 & (s >> i))
        rep(j, N) if(!(s >> j & 1))
          dp1[s | (1 << j)][j] = min(dp1[s | (1 << j)][j], dp1[s][i] + abs(towns[i].x - towns[j].x) + abs(towns[i].y - towns[j].y));
    rep(s, 1 << N)
      rep(i, N) if((s >> i) & 1)
        dist[s] = min(dist[s], dp1[s][i] + abs(towns[i].x) + abs(towns[i].y));
}

ll nap[1 << 7];
ll zack[10001];
void nap_zack(int s){
    memset(zack, 0, sizeof(zack));
    rep(i, N){
        if(!((s >> i) & 1)) continue;
        for(auto pro : towns[i].shop){
            pint temp = products[pro.first];
            int val = temp.second - pro.second, wei = temp.first;
            for(int j = wei; j <= W; j++)
              zack[j] = max(zack[j], zack[j - wei] + val);
        }
    }
    nap[s] = zack[W];
    return;
}
ll dp2[10001];
ll solve(){
    memset(dp2, 0, sizeof(dp2));
    rep(i, T + 1)
      rep(s, 1 << N)
        if(i >= dist[s])
          dp2[i] = max(dp2[i], dp2[i - dist[s]] + nap[s]);
    return dp2[T];
}
int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    cin >> N >> M >> W >> T;
    int pn = 0;//????????????
    rep(i, M){
        string a;
        int b, c;
        cin >> a >> b >> c;
        products[a] = pint(b, c);
    }
    rep(i, N){
        int pnum, x, y;
        cin >> pnum >> x >> y;
        town temp(x, y);
        rep(j, pnum){
            string a;
            int b;
            cin >> a >> b;
            temp.shop[a] = b;
        }
        towns.push_back(temp);
    }
    salesman();
    rep(s, 1 << N) nap_zack(s);
    cout << solve() << endl;
    return 0;
}