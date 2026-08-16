#include <bits/stdc++.h>
using i64 = long long;

int main() {
    constexpr i64 mod = 1000000007;
    int n;
    std::cin >> n;

    i64 ret = 1;
    int ss[] { 0, 0, 0 };
    for (int i = 0; i < n; i++) {
        int a;
        std::cin >> a;
        i64 f = 0;
        for (int &s : ss) if (s == a && !f++) s++;
        ret = ret * f % mod;
    }

    std::cout << ret << std::endl;

    return 0;
}
