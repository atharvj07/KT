#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

class SuffixArray {
public:
	typedef char Alpha;
	typedef int Index;

	void build(const Alpha *str, Index n, int AlphaSize);
	void build(const Alpha *str, Index n);
	inline Index getKThSuffix(Index k) const { return suffixArray[k]; }
	inline Index length() const { return static_cast<Index>(suffixArray.size() - 1); }
	std::vector<Index> suffixArray;
	template<typename AlphaT> void sa_is(const AlphaT *str, Index n, int AlphaSize, Index *sa, std::vector<Index> &bucketOffsets);
	template<typename AlphaT> void inducedSort(const AlphaT *str, Index n, int AlphaSize, const std::vector<bool> &types, Index *sa, std::vector<Index> &bucketOffsets);
	template<typename AlphaT> void countAlphabets(const AlphaT *str, Index n, int AlphaSize, std::vector<Index> &bucketOffsets, bool b = false);
	template<typename AlphaT> void getBucketOffsets(const AlphaT *str, Index n, bool dir, int AlphaSize, std::vector<Index> &bucketOffsets);
};

void SuffixArray::build(const Alpha *str, Index n, int AlphaSize) {
	suffixArray.resize(n + 1);
	if(n == 0) suffixArray[0] = 0;
	else {
		//I = sizeof(Index) * CHAR_BITS ??¨??????
		//suffixArray + bucketOffsets + types + ??¢??°?????????????????°
		//= n*I + max(AlphaSize, n/2)*I + 2*n + O(log n) bits
		//I = 4 * 32??§AlphaSize??????????°?????????¨????????¨:
		//(6+1/16) * n + O(log n) bytes
		std::vector<Index> bucketOffsets(std::max(AlphaSize, (n + 1) / 2) + 1);
		sa_is<Alpha>(str, n, AlphaSize, &suffixArray[0], bucketOffsets);
	}
}

void SuffixArray::build(const Alpha *str, Index n) {
	Alpha maxElem = *std::max_element(str, str + n);
	assert(maxElem + 0 < std::numeric_limits<int>::max());
	build(str, n, (int)(maxElem + 1));
}

//str???[0,n)???????????§???????????????????????????sa???[0,n]?????????
template<typename AlphaT>
void SuffixArray::sa_is(const AlphaT *str, Index n, int AlphaSize, Index *sa, std::vector<Index> &bucketOffsets) {
	std::vector<bool> types(n + 1);
	types[n - 1] = 0; types[n] = 1;
	for(Index i = n - 2; i >= 0; i --)
		types[i] = str[i] < str[i + 1] || (str[i] == str[i + 1] && types[i + 1]);

	countAlphabets(str, n, AlphaSize, bucketOffsets);
	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	std::fill(sa, sa + n + 1, -1);
	for(Index i = 1; i < n; i ++)
		if(types[i] && !types[i - 1]) sa[-- bucketOffsets[(int)str[i]]] = i;
	sa[0] = n;
	inducedSort(str, n, AlphaSize, types, sa, bucketOffsets);

	Index n1 = 0;
	for(Index i = 0; i <= n; i ++) {
		Index j = sa[i];
		if(j > 0 && types[j] && !types[j - 1]) sa[n1 ++] = j;
	}

	//LMS substrings????????????????????????sa[0..n1-1]??????????????????????????????
	//?????¢???????????????sa???????????????????????????????????¨?????????
	//?????????????????§pos???????????§??´??°????????????????????¨?????????????????????
	//????????§LMS substring?????£?¶????????????????????????¨???LMS substring?????°???n/2??\?????§???????????¨????????¨??????????????¨???1??????????????§??????
	Index *buffer = sa + n1;
	std::fill(buffer, sa + n + 1, -1);
	Index uniqueLMSCount = 0, prevPos = -1;
	assert(sa[0] == n);
	buffer[sa[0] / 2] = uniqueLMSCount ++;	//'$'
	for(Index i = 1; i < n1; i ++) {
		Index pos = sa[i]; bool diff = false;
		if(prevPos == -1) diff = true;
		else for(Index j = pos, k = prevPos; ; j ++, k ++) {
			if(str[j] != str[k] || types[j] != types[k]) {
				diff = true;
				break;
			} else if(j != pos && ((types[j] && !types[j - 1]) || (types[k] && !types[k - 1])))
				break;
		}
		if(diff) {
			uniqueLMSCount ++;
			prevPos = pos;
		}
		buffer[pos / 2] = uniqueLMSCount - 1;
	}
	for(Index i = n, j = n; i >= n1; i --)
		if(sa[i] >= 0) sa[j --] = sa[i];

	Index *sa1 = sa, *s1 = sa + n + 1 - n1;
	if(uniqueLMSCount == n1)
		for(Index i = 0; i < n1; i ++) sa1[s1[i]] = i;
	else
		sa_is<Index>(s1, n1 - 1, uniqueLMSCount, sa1, bucketOffsets);

	countAlphabets(str, n, AlphaSize, bucketOffsets);
	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	for(Index i = 1, j = 0; i <= n; i ++)
		if(types[i] && !types[i - 1]) s1[j ++] = i;
	for(Index i = 0; i < n1; i ++) sa1[i] = s1[sa1[i]];
	std::fill(sa + n1, sa + n + 1, -1);
	for(Index i = n1 - 1; i >= 1; i --) {
		Index j = sa[i]; sa[i] = -1;
		sa[-- bucketOffsets[(int)str[j]]] = j;
	}
	inducedSort(str, n, AlphaSize, types, sa, bucketOffsets);
}

template<typename AlphaT>
void SuffixArray::inducedSort(const AlphaT *str, Index n, int AlphaSize, const std::vector<bool> &types, Index *sa, std::vector<Index> &bucketOffsets) {
	getBucketOffsets(str, n, false, AlphaSize, bucketOffsets);
	for(Index i = 0; i < n; i ++) {
		Index j = sa[i] - 1;
		if(j >= 0 && !types[j]) sa[bucketOffsets[(int)str[j]] ++] = j;
	}

	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	for(Index i = n; i >= 1; i --) {
		Index j = sa[i] - 1;
		if(j >= 0 && types[j]) sa[-- bucketOffsets[(int)str[j]]] = j;
	}
}

template<typename AlphaT>
void SuffixArray::countAlphabets(const AlphaT *str, Index n, int AlphaSize, std::vector<Index> &bucketOffsets, bool b) {
	if(b || (int)bucketOffsets.size() / 2 >= AlphaSize) {
		std::vector<Index>::iterator alphabetCounts =
			b ? bucketOffsets.begin() : bucketOffsets.begin() + AlphaSize;
		std::fill(alphabetCounts, alphabetCounts + AlphaSize, 0);
		for(Index i = 0; i < n; i ++)
			alphabetCounts[(int)str[i]] ++;
	}
}

template<typename AlphaT>
void SuffixArray::getBucketOffsets(const AlphaT *str, Index n, bool dir, int AlphaSize, std::vector<Index> &bucketOffsets) {
	//AlphaSize?????§????????´?????????bucketOffset?±????????????????alphabet?????°???????????¢??????????°?????????????
	//AlphaSize????°?????????´?????????bucketOffset???alphabetCounts??¨??\?????´?????????????????¨????????????
	std::vector<Index>::iterator alphabetCounts;
	if((int)bucketOffsets.size() / 2 < AlphaSize) {
		countAlphabets(str, n, AlphaSize, bucketOffsets, true);
		alphabetCounts = bucketOffsets.begin();
	} else alphabetCounts = bucketOffsets.begin() + AlphaSize;
	Index cumsum = 1;	//'$'??????
	if(dir) {
		for(int i = 0; i < AlphaSize; i ++) {
			cumsum += alphabetCounts[i];
			bucketOffsets[i] = cumsum;
		}
	} else {
		for(int i = 0; i < AlphaSize; i ++) {
			Index x = alphabetCounts[i];
			bucketOffsets[i] = cumsum;
			cumsum += x;
		}
	}
}

template<typename T>
struct integer_iterator : iterator<random_access_iterator_tag,T,T> {
	typedef T value_type;
	typedef T difference_type;
	T val;
	integer_iterator() : val() {}
	explicit integer_iterator(T val) : val(val) {}
	T operator*() const { return val; }
	operator T() const { return val; }
	bool operator==(integer_iterator that) const { return val == that.val; }
	bool operator!=(integer_iterator that) const { return val != that.val; }
	bool operator<(integer_iterator that) const { return val < that.val; }
	bool operator>(integer_iterator that) const { return val > that.val; }
	bool operator<=(integer_iterator that) const { return val <= that.val; }
	bool operator>=(integer_iterator that) const { return val >= that.val; }
	integer_iterator &operator++() { ++ val; return *this; }
	integer_iterator &operator++(int) { integer_iterator t = *this; ++ *this; return t; }
	integer_iterator &operator+=(T diff) { val += diff; return *this; }
	integer_iterator operator+(T diff) const { return integer_iterator(val + diff); }
	friend integer_iterator operator+(T diff, integer_iterator that) { return that + diff; }
	integer_iterator &operator-=(T diff) { val -= diff; return *this; }
	integer_iterator operator-(T diff) const { return integer_iterator(val - diff); }
	difference_type operator-(integer_iterator that) const { return val - that.val; }
};

template<typename T>
struct integer_range {
	T left, right;
	integer_range(T left, T right) : left(left), right(right) {}
	integer_iterator<T> begin() const { return integer_iterator<T>(left); }
	integer_iterator<T> end() const { return integer_iterator<T>(right); }
};

template<typename T> integer_range<T> range(T left, T right) {
	return integer_range<T>(left, right);
}
template<typename T> integer_range<T> range(T right) {
	return integer_range<T>(T(), right);
}

struct BitVectorRank {
	typedef unsigned u32;
	typedef size_t Index;
	Index length, blockslength, count;
	vector<u32> blocks;
	vector<Index> ranktable;
	BitVectorRank(Index len = 0) { init(len); }
	void init(Index len) {
		length = len;
		blockslength = (len + 31) / 32 + 1;
		blocks.assign(blockslength, 0);
	}
	inline void set(Index i) { blocks[i / 32] |= 1 << i % 32; }
	void build() {
		count = 0;
		if(length == 0) return;
		ranktable.assign(blockslength + 1, 0);
		for(Index i = 0; i < blockslength; i ++) {
			ranktable[i] = count;
			count += popcount(blocks[i]);
		}
		ranktable[blockslength] = count;
	}
	inline bool access(Index pos) const { return blocks[pos / 32] >> pos % 32 & 1; }
	inline Index rank(Index pos) const {	//[0..pos)???1????????°
		int block_idx = pos / 32;
		return ranktable[block_idx] + popcount(blocks[block_idx] & (1U << pos % 32) - 1);
	}
	inline Index rank(bool b, Index pos) const { return b ? rank(pos) : pos - rank(pos); }
	inline Index rank(bool b, Index left, Index right) const { return rank(b, right) - rank(b, left); }
private:
	static inline int popcount(u32 x) {
		x = x - ((x >> 1) & 0x55555555);
		x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
		return ((x + (x >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;
	}
};

struct WaveletMatrix {
	typedef BitVectorRank BitVector;
	typedef unsigned int Val;
	typedef size_t Index;
	int bitnum; Index length; Val maxval;
	vector<BitVector> bitvectors;
	vector<Index> mids;

	WaveletMatrix() { init(vector<Val>()); }
	void init(const vector<Val> &data) {
		length = data.size();
		maxval = length == 0 ? 0 : *max_element(data.begin(), data.end());
		bitnum = 1; while((maxval >> 1 >> (bitnum - 1)) != 0) ++ bitnum;

		bitvectors.assign(bitnum, BitVector(length));
		mids.resize(bitnum);

		vector<Val> cur = data, next; next.resize(length);
		for(int i = 0; i < bitnum; i ++) {
			Val mask = Val(1) << (bitnum - 1 - i);
			Index zeros = 0;
			for(Index j = 0, n = length; j < n; j ++)
				zeros += (cur[j] & mask) == 0;
			mids[i] = zeros;

			BitVector &bv = bitvectors[i];
			Index zeroPos = 0, onePos = zeros;
			for(Index j = 0, n = length; j < n; j ++) {
				bool b = (cur[j] & mask) != 0;
				if(b) next[onePos  ++] = cur[j], bv.set(j);
				else  next[zeroPos ++] = cur[j];
			}
			bv.build();
			next.swap(cur);
		}
	}
	int rank_all(Val val, int left, int right, int &res_lt, int &res_gt) const {
		if(val > maxval) {
			res_lt = right - left;
			res_gt = 0;
			return 0;
		}
		res_lt = res_gt = 0;
		for(int i = 0; i < bitnum; i ++) {
			const BitVector &bv = bitvectors[i];
			bool dir = val >> (bitnum - i - 1) & 1;
			int leftcount = bv.rank(dir, left), rightcount = bv.rank(dir, right);
			(dir ? res_lt : res_gt) += (right - left) - (rightcount - leftcount);
			left = leftcount, right = rightcount;
			if(dir) left += mids[i], right += mids[i];
		}
		return right - left;
	}
	int rank_lt(Val val, int left, int right) const {
		int lt, dummy;
		rank_all(val, left, right, lt, dummy);
		return lt;
	}
	int rangefreq(int left, int right, Val top, Val bottom) const {
		return rank_lt(bottom, left, right) - rank_lt(top, left, right);
	}
};



int main() {
	char *S = new char[100001];
	char *T = new char[100001];
	int Q;
	while(~scanf("%s%d", S, &Q)) {
		int N = strlen(S);
		SuffixArray sa;
		sa.build(S, N);
		vector<uint32_t> data(N + 1);
		rep(i, N + 1) data[i] = sa.suffixArray[i];
		WaveletMatrix wm;
		wm.init(data);
		rep(i, Q) {
			int l, r;
			scanf("%d%d%s", &l, &r, T), ++ r;
			int len = strlen(T);
			auto p = equal_range(all(range(N + 1)), -1, [&](int dummy, int k) {
				if(dummy == -1) {
					int i = sa.suffixArray[k];
					return lexicographical_compare(T, T + len, S + i, S + i + min(len, N + 1 - i));
				} else {
					swap(dummy, k);
					int i = sa.suffixArray[k];
					return lexicographical_compare(S + i, S + i + min(len, N + 1 - i), T, T + len);
				}
			});
			int ans = r - l >= len ? wm.rangefreq(p.first, p.second, l, r - len + 1) : 0;
			printf("%d\n", ans);
		}
	}
	return 0;
}