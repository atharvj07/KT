#include <iostream>
#include <vector>

template<class T>
using vec = std::vector<T>;

int rec(int S, int N, int K, int money, vec<int> &a, vec<int> &b)
{
    if (__builtin_popcount(S) == K) {
        return money;
    }
    
    int res = 0;
    for (int i = 0; i < N; i++) {
        if (S >> i & 1) continue;
        int m = std::min(b[i], money);
        res = std::max(res,
                  rec(S | (1 << i), N, K, money - m, a, b) + a[i] * m);
    }
    return res;
}

int main()
{
    int N, M, K;
    std::cin >> N >> M >> K;
    
    vec<int> a(N), b(N);
    for (int i = 0; i < N; i++) {
        std::cin >> a[i];
    }
    
    for (int i = 0; i < N; i++) {
        std::cin >> b[i];
    }
    
    std::cout << rec(0, N, K, M, a, b) << std::endl;
    return 0;
}