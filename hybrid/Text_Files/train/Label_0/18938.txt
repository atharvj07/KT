#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a[3], chk;

    while (cin >> a[0] >> a[1] >> a[2], a[0] || a[1] || a[2]) {
        sort(a, a + 3);
        chk = a[0] * a[0] + a[1] * a[1];

        int n;        
        cin >> n;
        while (n--) {
            int r;

            cin >> r;
            if (4 * r * r > chk)
                cout << "OK" << endl;
            else
                cout << "NA" << endl;
        }
    }
    
    return 0;
}