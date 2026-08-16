#include <cstdio>
#include <cmath>

double rad(double ang)
{
    return ang / 180.0 * acos(-1);
}

int main()
{
    double n, k;
    scanf("%lf %lf", &n, &k);
    printf("%.10f\n",
           n * sin(rad(180 / n)) * cos(rad(180 * k / n)) / cos(rad(180 * (k - 1) / n)));
    return 0;
}