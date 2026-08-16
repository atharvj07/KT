#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> l_l;
typedef pair<l_l, l_l> llll;
typedef pair<int, int> i_i;
template<class T>
inline bool chmax(T &a, T b) {
    if(a < b) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
inline bool chmin(T &a, T b) {
    if(a > b) {
        a = b;
        return true;
    }
    return false;
}

//const ll mod = 1000000007;
const ll INF = 1e17;
ll N;
ll R[2005], A[2005], W[2005], T[2005];
ll Prev[4005];
ll Next[4005];
ll Next2[4005];
vector<llll> v;

int main() {
    //cout.precision(10);
    cin.tie(0);
    ios::sync_with_stdio(false);
    cin >> N;
    v.resize(N);
    for(int i = 0; i < N; i++) {
        cin >> v[i].second.second >> v[i].second.first >> v[i].first.second >> v[i].first.first;
        v[i].first.first += v[i].second.second;
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < N; i++) {
        v[i].first.first -= v[i].second.second;
        R[i+1] = v[i].second.second;
        A[i+1] = v[i].second.first;
        W[i+1] = v[i].first.second;
        T[i+1] = v[i].first.first;
    }
    //for(int i = 0; i <= 4000; i++) Prev[i] = -INF;
    Prev[1] = 0;
    for(int song = 1; song <= N; song++) {
        for(int j = 0; j <= 4000; j++) {
            Next[j] = -INF;
            Next2[j] = -INF;
        }
        for(int j = 1; j <= 4000; j++) {
            if(j - 2 * R[song] >= 1 && j - R[song] <= T[song]) Next[j] = Prev[j - 2 * R[song]] + W[song] + A[song];
            else Next[j] = -INF;
        }
        for(int j = 1; j <= 4000; j++) {
            if(j - R[song] >= 1 && j - R[song] <= T[song]) chmax(Next[j], Next[j - R[song]] + W[song]);
        }
        for(int j = 4000; j >= 0; j--) {
            if(j - R[song] >= 1 && j - R[song] <= T[song]) chmax(Prev[j], Prev[j - R[song]] + A[song]);
            chmax(Prev[j], Next[j]);
        }
    }
    ll ans = 0;
    for(int i = 0; i <= 4000; i++) {
        chmax(ans, Prev[i]);
    }
    cout << ans << endl;
    return 0;
}

