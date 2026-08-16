import java.util.Scanner;

/**
 * チャンパーノウン定数クラス
 * 0.1234567891011121314...
 * 1-indexed
 * 
 */
public class Main {

	 //10^18
	//at(DIGIT_LIMIT) = 594771241830065 [3] 5
	long DIGIT_LIMIT = 1000000000000000000L;
	
	//DIGIT_LIMITを含む整数MAX_NUMBER
	//この整数の先頭は 999999999999999985 番目である
	//[10^17, MAX_NUMBER]
	long MAX_NUMBER = 59477124183006535L;
	
	//endK[k]: 10^k未満の末尾までのインデックス数
	//便宜的にendK[18]=DIGIT_LIMIT, endK[0]=-1;
	long[] endK;
	
	//k==0: ten[0] = 0
	//1<=k: ten[k] = 10^k
	long[] ten;
	
	//チャンパーノウンクラスの機能を使う前に1度だけ呼び出す初期化処理
	void init(){
		endK = new long[20];
		endK[0] = 0;
		long num = 9;
		for(int k=1;k<=17;k++,num*=10){
			endK[k] = endK[k-1]+k*num;
		}
		endK[18] = DIGIT_LIMIT;
		endK[0] = -1;
		ten = new long[20];
		ten[0] = 0;
		ten[1] = 10;
		for(int k=2;k<=17;k++)ten[k]=ten[k-1]*10;
	}
	
	//Verify: AOJ2177 Euler040
	//x番目の桁の数字を得る
	//条件: 1 <= x <= 10^18
	int at(long x){
		//x番目の桁を含むような整数の区間[L, R)
		//R==MAX_NUMBERの場合は閉区間になるけど、どーでもいい
		long L=0, R=0;
		int k;
		//LとRの値を決めるため、 xを含むインデックス数の閉区間 [endK[k]+1, endK[k+1]] のkを求める
		for(k=17;k>=0;k--)if(endK[k] < x){
			//xを含む数値の両端を計算
			//LとRの数値の桁数は全て同じで、その桁数は(k+1)
			L = ten[k];
			R = k==17?MAX_NUMBER:ten[k+1];
			break;
		}
		//2分探索によってxの場所を検索
		for(;;){
			long m = (R+L)/2;
			//数値mの開始インデックス p を計算
			long p = endK[k]+1+(k+1)*(m-ten[k]);
			//インデックスxは数値mの中にあるかチェック
			if(p<=x&&x<p+k+1){
				String s = m+"";
				for(int i=0;i<s.length();i++)if(p+i==x)return s.charAt(i)-'0';
			}
			else if(x < p)R=m;
			else L=m;
		}
	}
	//Verify: AOJ2323
	//数xが現れる位置を求める
	long findNumber(long x){
		if(x<=0||MAX_NUMBER<x)return DIGIT_LIMIT;
		if(x<10)return x;
		int k = (x+"").length()-1;
		return endK[k]+1+(k+1)*(x-ten[k]);
	}
	//Verify: AOJ2323(答えが10^16未満に限定)
	//文字列targetが現れる位置を求める
	//targetにMAX_NUMBERを超える文字列が入っている場合はサポート外なので、DIGIT_LIMIT付近が答えになるtargetは動作保証はない
	long findString(String target){
		boolean allzero = true;
		for(char ch:target.toCharArray())allzero&=ch=='0';
		//targetがk個の0が並んでいる形の場合、targetが出現するのは10^kの中である
		if(allzero)return findNumber(Long.parseLong("1"+target))+1;
		int len = target.length();
		//targetが"1"〜"9"の場合、ただちに答えが求まる
		if(len==1){
			return findNumber(Long.parseLong(target));
		}
		long res = DIGIT_LIMIT;
		int lenMax = Math.min(17, len);
		for(int h=0;h<lenMax;h++)for(int k=1;k<=lenMax;k++)res = Math.min(res, findStringSub(target, h, k));
		return res;
	}
	//findStringの補助メソッド
	private long findStringSub(String target, int h, int k){
		//リーディング0ならアウト
		if(target.charAt(h)=='0')return DIGIT_LIMIT;
		//targetのprefix部分
		String sub = target.substring(0, h);
		//targetの[h, k)にくる数字を計算
		String s = "";
		for(int i=h;i<h+k;i++){
			//targetをはみ出さないならそのまま追記する
			if(i<target.length())s+=target.charAt(i);
			//targetをはみ出すなら、prefix部分の末尾から足りない文字数を取ってくる。足りない文字数はLである
			//このとき、prefixの後ろL文字を整数として解釈し、+1したものをsに追記する
			else {
				int L = h+k-i;
				String r = (Long.parseLong(sub.substring(sub.length()-L))+1)+"";
				//prefixの後ろL文字がリーディング0の場合、不具合が生じるので0をパディングする
				while(r.length()-L<0)r="0"+r;
				s+=r.substring(r.length()-L); break;
			}
		}
		//targetの位置hから始まる整数はbaseとする
		long base = Long.parseLong(s);
		//MAX_NUMBERを超えるのはサポート外なので解なしとする
		if(MAX_NUMBER<base)return DIGIT_LIMIT;
		//targetと比較する文字列matchを作る
		//targetとうまく比較するために、matchの前にくっつける文字列と、後ろにくっつける文字列を考える
		String match = base+"";
		int pos = h;
		//matchの前に何文字くっつけたかは必要な情報になるのでaddLenに入れておく
		int addLen = 0;
		//matchの前にくっつけるべき整数 b
		long b = base-1;
		//必要な文字数分だけくっつける
		while(pos>0){
			//負の数になってしまった場合は無効な文字列なので解なし
			if(b<=0)return DIGIT_LIMIT;
			String add = b-- +"";
			pos-=add.length();
			addLen+=add.length();
			match = add+match;
		}
		//同様に後ろの部分を考える
		b = base+1;
		pos = h+k;
		while(pos < target.length()){
			//このif文は要らない気がしてきたのでカット
//			if(MAX_NUMBER<b)return DIGIT_LIMIT;
			String add = b++ +"";
			pos+=add.length();
			match+=add;
		}
		//targetとmatchの比較
		for(int i=0;i<target.length();i++)if(target.charAt(i)!=match.charAt(addLen-h+i))return DIGIT_LIMIT;
		//findNumber(base)が、hの位置のインデックスなので、hだけ引けばすなわちtargetの先頭の位置のインデックスになる
		return findNumber(base)-h;
	}
	
//MAX_NUMBERを算出したときの産物、ゴミともいう
//	void calc_maxnum(){
//		init();
//		long L = ten[16], R = L*10;
//		while(R-L>1){
//			long m = (R+L)/2;
//			long p = endK[16]+1 + 17*(m-ten[16]);
//			System.out.println("M:"+m+" P:"+p);
//			if(p<=DIGIT_LIMIT && DIGIT_LIMIT<p+17){
//				System.out.println("M:"+m);
//				break;
//			}
//			if(DIGIT_LIMIT < p)R=m;
//			else L=m;
//		}
//	}
	//使い方例
	void test(){
		//初期化処理を最初に呼ぶ
		init();
		//N番目からK文字を出力する (AOJ2177)
//		int N = 10000, K = 100;
		Scanner cin=new Scanner(System.in);
		while(true){

			int N=cin.nextInt();
			int K=cin.nextInt();
			if(N+K==0)break;
			for(int i=0;i<K;i++)System.out.print(at(N+i)+(i==K-1?"\n":""));			
		}

		//文字列Sに一致する最初の場所を出力する (AOJ2323)
//		System.out.println(findString("5947712418300653459477124183006535"));
	}
	
	public static void main(String[] args) {
		new Main().test();
	}
}