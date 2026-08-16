#include <iostream>
#include <vector>

using namespace std;

bool is_decreasing(int v)
{
    int d = v % 10;
    v /= 10;
    while (v > 0)
    {
        if (d - 1 != v % 10)
        {
            return false;
        }
        d = v % 10;
        v /= 10;
    }
    return true;
}

int main()
{
    int n;
    cin >> n;
    vector<int> vs(n);
    for (int &v : vs)
    {
        cin >> v;
    }
    int max_val = -1;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (is_decreasing(vs[i] * vs[j]))
            {
                max_val = max(max_val, vs[i] * vs[j]);
            }
        }
    }
    cout << max_val << endl;
}
