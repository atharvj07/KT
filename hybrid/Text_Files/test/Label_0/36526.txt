import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		// 入力は，次の形式で与えられる．
		//
		// N T H L
		// t1 h1
		// t2 h2
		// ...
		// tN hN
		// Nは2DRespectersの人数であり，1 <= N <= 100である． TとHはそれぞれ，
		// 10円玉ストレージと100円玉ストレージに最初に保存されている硬貨の枚数であり，0 <= T, H <= 100である．
		// Lは10円玉ストレージの保存可能枚数の上限であり，T <= L <= 100である． 1 <= i <= Nのとき，tiは，
		// 2DRespectersのメンバーiの10円玉の所持枚数を表し，hiは100円玉の所持枚数を表す．0 <= ti, hi <=
		// 100である．
		int N = sc.nextInt();
		int T = sc.nextInt();
		int H = sc.nextInt();
		int L = sc.nextInt();
		int[] ts = new int[N + 1];
		int[] hs = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			ts[i] = sc.nextInt();
			hs[i] = sc.nextInt();
		}
		int rest = 0;
		int ans = 0;
		while (true) {
			for (int i = 1; i <= N; i++) {
				// ． 自販機には，硬貨を一度に一枚しか投入できず，投入された硬貨は，硬貨に対応する内部のストレージに保存される．
				// 自販機の残金表示は，始め0円になっており，硬貨を投入すると，投入した硬貨の金額分，自販機の残金が増加する．
				// 硬貨を投入した結果，自販機の残金が，90円以上になったならば，1本の缶ジュースがジュースの取り出し口に出てくると同時に，自販機の残金から90円を引いた額とちょうど同じ額の硬貨が釣銭として釣銭の取り出し口に出てくる．
				// このときの釣銭は，内部のストレージにある硬貨で払える範囲で，できるだけ多くの10円玉を用いて支払われる．
				// 釣銭が支払われた後，自販機の残金は0円に戻る．
				// // 硬貨の投入は，10円玉を持っている場合は必ず10円玉を投入し，
				// 10円玉を持っていない場合は100円玉を投入するものとする． メンバーiが硬貨を投入したとき，
				// 釣銭の取り出し口に釣銭が出てきた場合は，その全ての釣銭をメンバーiが受け取り，
				// 取り出し口に何もない状態にしてから，次のメンバーのターンに移る．
				if (ts[i] != 0) {
					ts[i]--;
					rest += 10;
					T++;
					if (T > L) {
						ans = i;
						break;
					}
				} else if (hs[i] != 0) {
					hs[i]--;
					rest += 100;
					H++;
				} else {
					ans = i;
					break;
				}
				if (rest >= 90) {
					rest -= 90;
					if (rest != 0 && T == 0 && H == 0) {
						ans = i;
						break;
					}
					if (T != 0) {
						int t = Math.min(rest / 10, T);
						T -= t;
						ts[i] += t;
						rest -= 10 * t;
					}
					if (H != 0) {
						int h = Math.min(rest / 100, H);
						H -= h;
						hs[i] += h;
						rest -= 10 * h;
						if (rest != 0) {
							ans = i;
							break;
						}
					}
				}
			}
			if (ans != 0)
				break;
		}
		System.out.println(ans);
	}
}