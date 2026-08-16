
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <string>
#define repd(i,a,b) for (int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repd(i,0,n)
#define all(x) (x).begin(),(x).end()
#define mod 1000000007
#define inf 2000000007
#define mp make_pair
#define pb push_back
typedef long long ll;
using namespace std;
template <typename T>
inline void output(T a, int p) {
    if(p) cout << fixed << setprecision(p)  << a << "\n";
    else cout << a << "\n";
}
// end of template
struct query{
    int q, l, r;
};

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    int N, a, d, M, K;
    cin >> N >> a >> d >> M;
    vector<query> Q(M);
    rep(i, M){
        int x, y, z;
        cin >> x >> y >> z;
        Q[i] = query{x, y, z};
    }
    cin >> K;
    for(int i = M - 1; i >= 0; i--){
        if (Q[i].q == 0 && Q[i].l <= K && Q[i].r >= K) {
            K = Q[i].l + Q[i].r - K;
        }
    }
    int ret = a + (K - 1) * d;
    
    rep(i, M){
        if (!(Q[i].l <= K && Q[i].r >= K)) continue;
        if (Q[i].q == 0) {
            K = Q[i].l + Q[i].r - K;
        }
        if (Q[i].q == 1) {
            ret++;
        }
        if (Q[i].q == 2) {
            ret /= 2;
        }
    }
    
    output(ret, 0);
    return 0;
}