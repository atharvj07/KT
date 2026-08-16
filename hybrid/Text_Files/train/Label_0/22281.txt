#include <iostream>

using namespace std;

int main(void) {
    int n,h,w;

    cin >> n >> h >> w;

    cout << (n-h+1)*(n-w+1) << endl;
}
