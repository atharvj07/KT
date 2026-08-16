#include <bits/stdc++.h>
#include <cmath>

using namespace std;
typedef long long ll;
//typedef unsigned long long ll;

//#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep(i, n) for (ll i = 0; i < (n); ++i)
//#define sz(x) ll(x.size())
//typedef pair<ll, int> P;
//typedef pair<ll, ll> P;
const double INF = 1e10;
//const ll INF = LONG_LONG_MAX / 10;
//const ll INF = 1e15;
const ll MINF = LONG_LONG_MIN;
//const int INF = INT_MAX / 10;
#define cmin(x, y) x = min(x, y)
#define cmax(x, y) x = max(x, y)

bool contain(set<char> &s, int a) { return s.find(a) != s.end(); }

//ifstream myfile("C:\\Users\\riku\\Downloads\\0_00.txt");
//ofstream outfile("log.txt");
//outfile << setw(6) << setfill('0') << prefecture << setw(6) << setfill('0') << rank << endl;
// std::cout << std::bitset<8>(9);

typedef pair<double, double> P;

void print_line(vector<int> &line) {
    if (line.size() == 0ll) {
        cout << endl;
        return;
    }
    for (ll i = 0; i < line.size(); i++) {
        cout << line[i];
        if (i == line.size() - 1) cout << endl;
        else cout << ' ';
    }
}


typedef priority_queue<long long, vector<long long>, greater<long long>> PQ_ASK;
const int mod = 1000000007;

int main() {
    int n;


    cin >> n;
    vector<P> ks(n + 1, P(0, 0));
    vector<vector<double>> p_sum(n + 1, vector<double>(n + 1, 0));
    vector<vector<double>> q_sum(n + 1, vector<double>(n + 1, 0));
    vector<vector<double>> dp(n + 1, vector<double>(n + 1, 0));;

    for (int i = 0; i < n; ++i) cin >> ks[i].first;
    for (int i = 0; i < n + 1; ++i) cin >> ks[i].second;
    for (int i = 0; i < n + 1; ++i) dp[i][i] = ks[i].second;

    for (int i = 0; i < n; ++i) {
        p_sum[i][i] = ks[i].first;
        for (int j = i + 1; j < n; ++j) {
            p_sum[i][j] = p_sum[i][j - 1] + ks[j].first;
        }
    }

    for (int i = 0; i < n + 1; ++i) {
        q_sum[i][i] = ks[i].second;
        for (int j = i + 1; j < n + 1; ++j) {
            q_sum[i][j] = q_sum[i][j - 1] + ks[j].second;
        }
    }

    for (int i = 1; i < n + 1; ++i) {
        for (int j = 0; j < (n + 1) - i; ++j) {
            dp[j][j + i] = INF;
            for (int k = 0; k < i; ++k) {
                double t = dp[j][j + k] + dp[j + k + 1][j + i] + p_sum[j][j + i - 1] + q_sum[j][j + i];
                dp[j][j + i] = min(dp[j][j + i], t);
            }
        }
    }

    printf("%.20f\n", dp[0][n]);

}


