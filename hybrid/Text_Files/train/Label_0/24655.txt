//    .------------------------------------------------------------.
//    |                     K U S A Y A R O U                      |
//    |                                                            |
//    |        ---|---|---      ___   ____       _\_   ___         |
//    |          _______       |_|_|     /      |___| |  /         |
//    |         |_______|      |_|_|    \       |___| | /          |
//    |         |_______|        |   _____      |     |  \         |
//    |        _____|_____     __|__   | /      |  \  | __\        |
//    |             |            |     |        | / \ |            |
//    |             |          __|__  \|        |/    |            |
//    |                                                            |
//    |------------------------------------------------------------|
//    |                      .------------.                        |
//    |                      | KerakTelor |                        |
//    |                      |------------|                        |
//    |                      | 2021-04-21 |                        |
//    |                      '------------'                        |
//    '------------------------------------------------------------'

// OPTIM - Desperate optimizations
//
// #pragma GCC optimize("Ofast,unroll-loops")
// #pragma GCC target("tune=native")

// BASE - STL, debug helper, aliases

#include <bits/stdc++.h>

#define DEBUG(...)
#define fi first
#define se second

using namespace std;

using ll = long long;
using ld = long double;

template<class T>
using vec = vector<T>;
template<class T>
using v2d = vector<vector<T>>;
template<class T>
using v3d = vector<vector<vector<T>>>;
template<class T>
using v4d = vector<vector<vector<vector<T>>>>;
template<class T>
using prq = priority_queue<T>;
template<class T>
using rpq = priority_queue<T, vector<T>, greater<T>>;

// PBDS - find_by_order, order_of_key
//
// #include <ext/pb_ds/assoc_container.hpp> 
// #include <ext/pb_ds/tree_policy.hpp> 
//
// using namespace __gnu_pbds; 
//
// template<class T>
// using ost = tree<T, null_type, less<T>, rb_tree_tag,
//                  tree_order_statistics_node_update>;
// template<class T, class U>
// using omp = tree<T, U, less<T>, rb_tree_tag,
//                  tree_order_statistics_node_update>;

// RNG - rand_int(min, max), inclusive
//
// mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
//
// template<class T>
// T rand_int(T mn, T mx)
// {
//     return uniform_int_distribution<T>(mn, mx)(rng);
// }

// MATH - lcm, gcd, power, powmod
//
// ll gcd(ll a, ll b)
// {
//     return b ? gcd(b, a % b) : a;
// }
//
// ll lcm(ll a, ll b)
// {
//     return a / gcd(a, b) * b;
// }
//
// ll powi(ll a, ll b)
// {
//     if(!b)
//     {
//         return 1;
//     }
//     if(b & 1)
//     {
//         return a * powi(a, b ^ 1);
//     }
//     ll x = powi(a, b >> 1);
//     return x * x;
// }
// 
// ll powm(ll a, ll b, ll m)
// {
//     if(!b)
//     {
//         return 1;
//     }
//     if(b & 1)
//     {
//         return (a * powm(a, b ^ 1, m)) % m;
//     }
//     ll x = powm(a, b >> 1, m);
//     return (x * x) % m;
// }

// CODE - Brain damage starts here
//     「とにかくやれぇぇ！」

int main()
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        int n, m, k;
        scanf("%d %d %d", &n, &m, &k);
        int ans = (n - 1) + n * (m - 1);
        printf("%s\n", ans == k ? "YES" : "NO");
    }
}

