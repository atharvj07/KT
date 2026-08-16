#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
const ll INF = 1LL << 28;

ll N;
vector<ll> num;
map<ll,ll> memo;
queue<ll> q;
function<ll(ll)> seki;

int main() {
    cin >> N;
    q.push(2LL); q.push(8LL);
    while (q.size()) {
        ll n = q.front(); q.pop();
        num.push_back(n);
        if (n <= 1e18) {
            q.push(n * 10LL + 8LL);
            q.push(n * 10LL + 2LL);
        }
    }


    sort(num.begin(), num.end());

    seki = [&](ll n) -> ll {
        if (memo.find(n) != memo.end()) return memo[n];

        int i = (int)(lower_bound(num.begin(), num.end(), n) - num.begin());
        memo[n] = -INF;
        if (num[i] == n) memo[n] = 1;
        for (; i > -1; i--) {
            if (n % num[i] == 0 ) {
                memo[n] = max(memo[n], seki(n / num[i]) + seki(num[i]));
            }
        }


        return memo[n];
    };

    int ans = seki(N);
    if (ans > 0) cout << ans << endl;
    else cout << -1 << endl;

    return 0;
}