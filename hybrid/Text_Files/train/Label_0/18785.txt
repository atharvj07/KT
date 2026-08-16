#include <bits/stdc++.h>

int ri() {
	int n;
	scanf("%d", &n);
	return n;
}

struct PartiallyPersistentArray {
	std::vector<std::vector<std::pair<int, int> > > data;
	int time = 0;
	PartiallyPersistentArray (int n) : data(n, {{0, 0}}) {}
	void go_time() { time++; }
	void assign(int i, int val) {
		if (data[i].size() && data[i].back().first == time) {
			data[i].back().second = val;
		} else data[i].push_back({time, val});
	}
	int get(int i, int time) {
		auto itr = std::upper_bound(data[i].begin(), data[i].end(), std::pair<int, int>{time, 1000000000});
		return std::prev(itr)->second;
	}
	void swap(int i, int j) {
		int tmp = get(i, time);
		assign(i, get(j, time));
		assign(j, tmp);
	}
};

int main() {
	int n = ri(), k = ri(), q = ri();
	PartiallyPersistentArray a(n), b(n);
	for (int i = 0; i < n; i++) a.assign(i, i), b.assign(i, i);
	for (int i = 0; i < k; i++) {
		a.go_time();
		b.go_time();
		int x = ri() - 1;
		int y = ri() - 1;
		b.swap(a.get(x, a.time), a.get(y, a.time));
		a.swap(x, y);
	}
	for (int i = 0; i < q; i++) {
		int type = ri();
		int l = ri() - 1;
		int r = ri();
		int x = ri() - 1;
		if (type == 1) {
			std::cout << b.get(a.get(x, r), l) + 1 << std::endl;
		} else {
			std::cout << b.get(a.get(x, l), r) + 1 << std::endl;
		}
	}
	return 0;
}

