#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define reps(i, s, n) for (int i = (int)(s); i < (int)(n); i++)
const ll mod = ll(1e9) + 7;
const int INF = int(1e9);
int vector_finder(std::vector<int> vec, int number)
{
    auto itr = std::find(vec.begin(), vec.end(), number);
    size_t index = std::distance(vec.begin(), itr);
    if (index != vec.size())
    { // 発見できたとき
        return 1;
    }
    else
    { // 発見できなかったとき
        return 0;
    }
}
int main()
{
    vector<int> res;
    while (1)
    {
        int N, M;
        cin >> N >> M;
        if (N == 0 && M == 0)
            break;
        vector<int> score(N);
        vector<int> S(M);
        vector<vector<int>> C(M);
        rep(i, M)
        {
            cin >> S[i];
            int k;
            cin >> k;
            rep(j, k)
            {
                int c;
                cin >> c;
                c--;
                C[i].push_back(c);
                score[c] += S[i];
            }
        }
        int ans_max = 0;
        int highest = 0;
        rep(i, N)
        {
            if (ans_max < score[i])
            {
                ans_max = score[i];
                highest = i;
            }
        }
        rep(i, N) score[i] = 0;
        rep(i, M)
        {
            if (vector_finder(C[i], highest))
                continue;
            if (C[i].size() == 1)
            {
                score[C[i][0]] += S[i];
            }
        }
        int ans_min = INF;
        int lowest = 0;
        rep(i, N)
        {
            if (ans_min > score[i] && i != highest)
            {
                ans_min = score[i];
                lowest = i;
            }
        }
        res.push_back(ans_max - ans_min + 1);
    }
    rep(i, res.size()) cout << res[i] << endl;
    return 0;
}
