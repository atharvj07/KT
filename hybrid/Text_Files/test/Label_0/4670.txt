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

const int INF = INT_MAX / 2;

int h, w;
vector<int> dy, dx;
vector<vector<int> > ns, ew, s;

void add(int& y, int& x)
{
    int y2 = 1;
    while(y > 0){
        y -= dy[y2];
        ++ y2;
    }
    int x2 = 1;
    while(x > 0){
        x -= dx[x2];
        ++ x2;
    }

    if(y != 0 || x != 0){
        if(y == 0){
            dx[x2-1] += x;
            dx.insert(dx.begin()+x2, -x);
            for(int i=0; i<h+2; ++i){
                ns[i].insert(ns[i].begin()+x2, 1);
                ew[i].insert(ew[i].begin()+x2, INF);
                s[i].insert(s[i].begin()+x2, 1);
            }
            ++ w;
        }else{
            dy[y2-1] += y;
            dy.insert(dy.begin()+y2, -y);
            ns.insert(ns.begin()+y2, vector<int>(w+2, INF));
            ew.insert(ew.begin()+y2, vector<int>(w+2, 1));
            s.insert(s.begin()+y2, vector<int>(w+2, 0));
            ++ h;
        }
    }

    y = y2;
    x = x2;
}

int main()
{
    for(;;){
        cin >> w >> h;
        if(h == 0)
            return 0;

        dx.assign(w+1, INF);
        dy.assign(h+1, INF);
        for(int i=1; i<w; ++i)
            cin >> dx[i];
        for(int i=1; i<h; ++i)
            cin >> dy[i];

        ns = ew = s = vector<vector<int> >(h+2, vector<int>(w+2, 1));
        for(int i=1; i<=h; ++i){
            for(int j=1; j<=w; ++j){
                cin >> ns[i][j] >> ew[i][j] >> s[i][j];
            }
        }

        int sy, sx, gy, gx;
        cin >> sx >> sy >> gx >> gy;
        int sy0 = sy;
        int sx0 = sx;
        add(sy0, sx0);
        add(gy, gx);
        add(sy, sx);

        vector<vector<vector<int> > > dp(h+2, vector<vector<int> >(w+2, vector<int>(2, INF)));
        for(int i=0; i<h+2; ++i)
            dp[i][0][1] = dp[i][w+1][1] = -1;
        for(int i=0; i<w+2; ++i)
            dp[0][i][0] = dp[h+1][i][0] = -1;

        multimap<int, pair<pair<int, int>, int> > mm;
        dp[sy][sx][0] = dp[sy][sx][1] = 0;
        mm.insert(make_pair(0, make_pair(make_pair(sy, sx), 0)));
        mm.insert(make_pair(0, make_pair(make_pair(sy, sx), 1)));

        while(!mm.empty()){
            int t = mm.begin()->first;
            int y = mm.begin()->second.first.first;
            int x = mm.begin()->second.first.second;
            int d = mm.begin()->second.second;
            mm.erase(mm.begin());
            if(t > dp[y][x][d])
                continue;

            if(s[y][x] == 0){
                int t2 = t % (ns[y][x] + ew[y][x]);
                if(d == 0){
                    if(t2 >= ns[y][x])
                        t += -t2 + (ns[y][x] + ew[y][x]);
                }else{
                    if(t2 < ns[y][x])
                        t += -t2 + ns[y][x];
                }
            }else{
                int t2 = t % (ew[y][x] + ns[y][x]);
                if(d == 0){
                    if(t2 < ew[y][x])
                        t += -t2 + ew[y][x];
                }else{
                    if(t2 >= ew[y][x])
                        t += -t2 + (ew[y][x] + ns[y][x]);
                }
            }

            if(y == gy && x == gx && t < INF){
                cout << t << endl;
                break;
            }

            for(int i=0; i<2; ++i){
                int t2 = t + dy[y-1+i];
                int y2 = y - 1 + 2*i;
                int x2 = x;
                int d2 = 0;
                if(t2 < dp[y2][x2][d2]){
                    dp[y2][x2][d2] = t2;
                    mm.insert(make_pair(t2, make_pair(make_pair(y2, x2), d2)));
                }
            }
            for(int i=0; i<2; ++i){
                int t2 = t + dx[x-1+i];
                int y2 = y;
                int x2 = x - 1 + 2*i;
                int d2 = 1;
                if(t2 < dp[y2][x2][d2]){
                    dp[y2][x2][d2] = t2;
                    mm.insert(make_pair(t2, make_pair(make_pair(y2, x2), d2)));
                }
            }
        }
    }
}