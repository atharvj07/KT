#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> A;
    A.reserve(n); //要素数を予約
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        A.push_back(make_pair(x, y));
    }
    sort(A.begin(), A.end());

    for (auto it = A.begin(); it != A.end(); it++)
    {
        // pair<int, int> P = *it;
        cout << it->first << ' ' << it->second << endl;
    }
}
