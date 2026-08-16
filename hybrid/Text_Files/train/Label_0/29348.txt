#include <iostream>
#include <vector>

constexpr int REVERSE   = 0;
constexpr int INCREMENT = 1;
constexpr int HALF      = 2;

bool cover(int l, int r, int x)
{
    return l <= x && x <= r;
}

int reverse(int l, int r, int x)
{
    return r + l - x;
}

int main()
{
    int N, a, d, M;
    std::cin >> N >> a >> d >> M;

    std::vector<int> x(M), y(M), z(M);
    for (int i = 0; i < M; i++) {
        std::cin >> x[i] >> y[i] >> z[i];
    }

    int K;
    std::cin >> K;

    for (int i = M - 1; i >= 0; i--) {
        if (x[i] == REVERSE && cover(y[i], z[i], K)) {
            K = reverse(y[i], z[i], K);
        }
    }

    int val = a + (K - 1) * d;
    for (int i = 0; i < M; i++) {
        if (!cover(y[i], z[i], K)) {
            continue;
        }
        
        switch (x[i]) {
            case REVERSE:
                K = reverse(y[i], z[i], K);
                break;
                
            case INCREMENT:
                val++;
                break;

            case HALF:
                val /= 2;
                break;
        }
    }

    std::cout << val << std::endl;
    
    return 0;
}