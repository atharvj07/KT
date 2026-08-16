#include <iostream>
#include <queue>
#include <map>

using namespace std;

int main()
{
    int n, q;
    int max_id = 0, max_num = 0;

    cin >> n >> q;
    map<int, int> data;
    for (int i = 1; i <= n; ++i)
        data.insert(map<int, int>::value_type(i, 0));

    int a, v;
    while (q--) {
        cin >> a >> v;
        data[a] += v;

        if (a == max_id) {
            max_num = data[a];

            if (v < 0) {
                map<int, int>::iterator it = data.begin();
                for ( ; it != data.end(); ++it) {
                    if ((*it).second > max_num) {
                        max_num = (*it).second;
                        max_id = (*it).first;
                    }
                    else if ((*it).second == max_num && (*it).first < max_id) {
                        max_id = (*it).first;
                    }
                }
            }
        }
        else if (data[a] > max_num ||
                 (data[a] == max_num && a < max_id)) {
            max_id = a;
            max_num = data[a];
        }

        cout << max_id << " " << max_num << endl;
    }

    return 0;
}