#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
using namespace std;

int main() {
    int y1, m1, d1, y2, m2, d2;
    while ( cin >> y1 >> m1 >> d1 >> y2 >> m2 >> d2 && y1 != -1 ) {
        int res = 0;
        const int days[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        for ( int y = y1; y <= y2; ++ y ) {
            int ms = 1;
            int me = 12;
            if ( y == y1 ) ms = m1;
            if ( y == y2 ) me = m2;
            for ( int m = ms; m <= me; ++ m ) {
                int ds = 1;
                int de = days[m];
                if ( m == 2 && y % 4 == 0 ) {
                    if ( y % 100 != 0 || y % 400 == 0 ) {
                        de ++;
                    }
                }
                if ( y == y1 && m == m1 ) ds = d1;
                if ( y == y2 && m == m2 ) de = d2;
                for ( int d = ds; d <= de; ++ d ) {
                    // cout << y << "/" << m << "/" << d << endl;
                    res ++;
                }
            }
        }
        cout << res - 1 << endl;
    }
    return 0;
}