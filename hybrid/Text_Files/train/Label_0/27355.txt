#include <bits/stdc++.h>
using namespace std;
using ll = int_fast64_t;
const int mod = 1e9 + 7;
const int inf = (1 << 30) - 1;
const ll infll = (1LL << 61) - 1;
#define fast() ios::sync_with_stdio(false), cin.tie(nullptr)
#define digit(N) cout << fixed << setprecision((N))
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

ll cost(vector<pair<int, ll>> v)
{
   int N = v.size();
   for (auto &p : v)
      p.first = min(p.first, N);
   sort(v.rbegin(), v.rend());

   priority_queue<ll> pq;
   ll res = 0;

   for (int i = N, j = 0; i > 0; i--)
   {
      while (j < N && v[j].first == i)
      {
         pq.push(v[j].second);
         j++;
      }

      if (pq.empty())
         continue;
      res += pq.top();
      pq.pop();
   }

   return res;
}

int main()
{
   int t;
   cin >> t;
   while (t--)
   {
      int N;
      cin >> N;
      vector<pair<int, ll>> left, right;

      ll ans = 0;

      for (int i = 0; i < N; i++)
      {
         ll k, l, r, m;
         cin >> k >> l >> r;
         ans += min(l, r);
         if (l > r)
            left.emplace_back(k, l - r);
         if (r > l)
            right.emplace_back(N - k, r - l);
      }
      ans += cost(left);
      ans += cost(right);
      cout << ans << "\n";
   }
}