#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct cards
{
	int num = 0;
	char mrk = 'D';
	int idx = 0;
};

int partition(vector<cards>& ary, int p, int r) {
	cards x, sw;
	int  i = 0;
	x = ary[r];
	i = p - 1;

	for (int j = p;j < r;j++) {
		if (ary[j].num <= x.num) {
			i = i + 1;
			sw = ary[i];
			ary[i] = ary[j];
			ary[j] = sw;
		}
	}
	sw = ary[i + 1];
	ary[i + 1] = ary[r];
	ary[r] = sw;
	return i + 1;
}

void quickSort(vector<cards>& ary, int p, int r) {
	int q = 0;
	if (p < r) {
		q = partition(ary, p, r);
		quickSort(ary, p, q - 1);
		quickSort(ary, q + 1, r);
	}
	return;
}

int main() {

	int n = 0, cnt = 0, mid = 0;
	cin >> n;
	vector<cards> ary(n);

	for (int i = 0;i < n;i++) {
		cards crd;
		cin >> crd.mrk >> crd.num;
		crd.idx = i;

		ary[i] = crd;
	}

	quickSort(ary, 0, n - 1);
	bool stable = true;
	for (int i = 0;i < n - 1;i++) {
		if (ary[i].num == ary[i + 1].num && ary[i].idx > ary[i + 1].idx) stable = false;
	}

	if (stable)		cout << "Stable" << endl;
	else cout << "Not stable" << endl;

	for (int i = 0;i < n;i++) {

		cout << ary[i].mrk << " " << ary[i].num << endl;
	}

	return 0;
}

