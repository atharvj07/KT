#include <bits/stdc++.h>
#define l2 array<ll,2>
using namespace std;
typedef long long ll;
const int N = 800100;
multiset<ll> lft, rgt;
ll ans = 0;
l2 pts[N];
int n;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);

#ifdef _LOCAL
    freopen("in.txt","r",stdin);
#endif // _LOCAL

    cin >> n;

    for (int i = 0; i < n; i++){
        ll x, y; cin >> x >> y;

        ll nx = x - y;
        ll ny = x + y;

        nx -= ny;

        assert(nx % 2 == 0);
        nx /= 2;

//        pts[i] = {nx, ny};
        pts[i] = {ny, nx};
    }

    sort(pts, pts + n);

    /// add first

    lft.insert(pts[0][1] + pts[0][0]);
    rgt.insert(pts[0][1]);

    for (int it = 1; it < n; it++){
        ll cx = pts[it][1];
        ll cy = pts[it][0];

        ll lef = (*(--lft.end())) - cy;
        ll rit = (*rgt.begin());

        if (cx >= lef && cx <= rit){
            lft.insert(cx + cy);
            rgt.insert(cx);
        } else if (cx < lef){
            ans += lef - cx;

            lft.erase(--lft.end());
            rgt.insert(lef);

            lft.insert(cx + cy);
            lft.insert(cx + cy);
        } else {
            ans += cx - rit;

            rgt.erase(rgt.begin());
            lft.insert(rit + cy);

            rgt.insert(cx);
            rgt.insert(cx);
        }
    }

    cout << ans;

    return 0;
}
