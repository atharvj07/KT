#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll N, K; cin >> N >> K;
    vector<ll> A(N); for (int i = 0; i < N; i++) cin >> A[i];
    vector<ll> cum(N); cum[0] = (K + A[0] - 1) % K;
    for (int i = 1; i < N; i++) cum[i] = (K + A[i] + cum[i-1] - 1) % K;
    ll ans = 0;
    map<ll, ll> group;

    group[0]++;
    for (int i = 0; i < N; i++) {
        if (i == K-1) group[0]--;
        if (i >= K) group[cum[i-K]]--;
        ans += group[cum[i]]++;
    }
    cout << ans << endl;
}
