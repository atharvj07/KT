#include <cstdio>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
using namespace std;

const int dy[] = {0, 0, 1, -1};
const int dx[] = {1, -1, 0, 0};

const int INF = INT_MAX / 4;

class Data{
public:
    int y, x, n;
    bool mato, key;
    Data(int y0, int x0, int n0, bool mato0, bool key0){
        y = y0;
        x = x0;
        n = n0;
        mato = mato0;
        key = key0;
    }
    Data(int y0, int x0, int n0){
        y = y0;
        x = x0;
        n = n0;
        mato = key = false;
    }
    int toInt(){
        return ((((y/2-1) * 20 + (x/2-1)) * 101 + n) * 2 + (mato? 1:0)) * 2 + (key? 1:0);
    }
};

int main()
{
    for(;;){
        int h, w; // 幅、高さ
        cin >> w >> h;
        if(h == 0)
            return 0;

        vector<string> s(2*h+3, string(2*w+3, '#')); // 迷路
        for(int i=2; i<=2*h; ++i){
            for(int j=2; j<=2*w; ++j){
                s[i][j] = '.';
            }
        }

        for(int i=0; i<h; ++i){
            for(int j=0; j<w-1; ++j){
                int a;
                cin >> a;
                if(a == 1)
                    s[2*i+2][2*j+3] = '#';
            }
            if(i < h -1){
                for(int j=0; j<w; ++j){
                    int a;
                    cin >> a;
                    if(a == 1)
                        s[2*i+3][2*j+2] = '#';
                }
            }
        }

        int sx, sy, mx, my, kx, ky, gx, gy; // スタート、マトクリーム、鍵、ゴール
        cin >> sx >> sy >> mx >> my >> kx >> ky >> gx >> gy;
        sx = sx * 2 + 2;
        sy = sy * 2 + 2;
        mx = mx * 2 + 2;
        my = my * 2 + 2;
        kx = kx * 2 + 2;
        ky = ky * 2 + 2;
        gx = gx * 2 + 2;
        gy = gy * 2 + 2;

        int n;
        cin >> n; // 壁を壊せる回数

        // [i][j][k] : (i, j)にいてk回壁を壊せる時に、鍵の入手に必要な最小の移動回数
        vector<vector<vector<int> > > getKey(2*h+3, vector<vector<int> >(2*w+3, vector<int>(n+1, INF)));
        getKey[ky][kx][0] = 0;
        queue<Data> q;
        q.push(Data(ky, kx, 0));
        while(!q.empty()){
            Data d0 = q.front();
            q.pop();
            for(int i=0; i<4; ++i){
                Data d = d0;
                d.y += dy[i];
                d.x += dx[i];
                if(s[d.y][d.x] == '#'){
                    ++ d.n;
                    if(d.n > n)
                        continue;
                }

                d.y += dy[i];
                d.x += dx[i];
                if(s[d.y][d.x] != '#' && getKey[d.y][d.x][d.n] == INF){
                    getKey[d.y][d.x][d.n] = getKey[d0.y][d0.x][d0.n] + 1;
                    q.push(d);
                }
            }
        }

        multimap<int, Data> mm;
        mm.insert(make_pair(0, Data(sy, sx, 0, false, false)));
        vector<int> dp(20*20*101*2*2, INF);
        dp[Data(sy, sx, 0, false, false).toInt()] = 0;

        for(;;){
            int cost0 = mm.begin()->first;
            Data d0 = mm.begin()->second;
            mm.erase(mm.begin());
            if(cost0 > dp[d0.toInt()])
                continue;

            if(d0.y == gy && d0.x == gx && d0.key){
                cout << cost0 << endl;
                break;
            }

            for(int i=0; i<4; ++i){ // 上下左右に1マス移動
                int cost = cost0 + 1;
                Data d = d0;
                d.y += dy[i];
                d.x += dx[i];
                if(s[d.y][d.x] == '#'){ // 壁
                    -- d.n;
                    if(d.n < 0)
                        continue;
                }

                d.y += dy[i];
                d.x += dx[i];
                if(s[d.y][d.x] == '#'){ // 領域外
                    continue;
                }else if(d.y == my && d.x == mx && !d.mato){ // マトクリーム
                    d.mato = true;
                    d.n = n;
                }else if(d.y == ky && d.x == kx && !d.key){ // 鍵
                    d.key = true;
                }

                if(cost < dp[d.toInt()]){
                    dp[d.toInt()] = cost;
                    mm.insert(make_pair(cost, d));
                }
            }

            if(d0.key)
                continue;

            for(int i=1; i<=d0.n; ++i){ // 鍵をとって現在の位置に戻る
                int cost = cost0 + getKey[d0.y][d0.x][i] * 2;
                Data d = d0;
                d.key = true;
                d.n -= i;

                if(cost < dp[d.toInt()]){
                    dp[d.toInt()] = cost;
                    mm.insert(make_pair(cost, d));
                }
            }
        }
    }
}