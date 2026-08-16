#include <cstdio>

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", n%2 ==0 ? n : n*2);
    return 0;
}