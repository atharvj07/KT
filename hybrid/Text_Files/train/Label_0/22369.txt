#include<bits/stdc++.h>

using namespace std;

bool isPrime[(int)1e7 + 1];

int main()
{
    fill_n(isPrime, 1e7 + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= 1e4; i++)
    {
        if(!isPrime[i]) continue;
        for (int j = 2; i * j <= 1e7; j++)
        {
            isPrime[i * j] = false;
        }
    }
    int N;
    while (cin >> N, N)
    {
        for (int i = N; i >= 8; i--)
        {
            if (isPrime[i] && isPrime[i - 2] && isPrime[i - 6] && isPrime[i - 8])
            {
                printf("%d\n", i);
                break;
            }
        }
    }
    return 0;
}