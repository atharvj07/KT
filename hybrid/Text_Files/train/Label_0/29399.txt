#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, m;
    int a[10], count[10], tmp[10];
    string id;
    cin >> n >> id >> m;
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }
    count[0] = 1;
    for (int i = 1; i < 10; ++i) {
        count[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 10; ++j) {
            tmp[j] = 0;
        }
        if ((n - i) % 2 == 0) {
            if (id[i] == '*') {
                for (int j = 0; j < m; ++j) {
                    for (int k = 0; k < 10; ++k) {
                        int x = (a[j] < 5? a[j] * 2: a[j] * 2 - 10 + 1);
                        tmp[(k + x) % 10] += count[k];
                    }
                }
            } else {
                for (int j = 0; j < 10; ++j) {
                    int x = (id[i] < '5'? (id[i] - '0') * 2: (id[i] - '0') * 2 - 10 + 1);
                    tmp[(j + x) % 10] += count[j];
                }
            }
        } else {
            if (id[i] == '*') {
                for (int j = 0; j < m; ++j) {
                    for (int k = 0; k < 10; ++k) {
                        tmp[(k + a[j]) % 10] += count[k];
                    }
                }
            } else {
                for (int j = 0; j < 10; ++j) {
                    tmp[(j + id[i] - '0') % 10] += count[j];
                }
            }
        }
        for (int j = 0; j < 10; ++j) {
            count[j] = tmp[j];
        }
    }
    cout << count[0] << endl;

    return 0;
}