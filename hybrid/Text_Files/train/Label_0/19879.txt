#include <iostream>
using namespace std;

int main(void) {
    int h, w, count = 0;
    cin >> h >> w;
    for (int i = 0; i < h * w; i++) {
        char c;
        cin >> c;
        if (c == '#') {
            count++;
        }
    }
    cout << (count == h + w - 1 ? "Possible" : "Impossible") << endl;
    return 0;
}
