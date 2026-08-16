import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

class Main {

	/*
	 * 着席位置：２列目の真ん中あたり
	 */

	private static BufferedReader br;

	public static void main(String args[]) throws Exception{
		br = new BufferedReader(new InputStreamReader(System.in));

		for(;;){
			//入力
			String input = br.readLine();
			if(input.equals("0 0 0")) break;

			Scanner scanner = new Scanner(input);
			int oldRate = scanner.nextInt();
			int newRate = scanner.nextInt();
			int sum_before_change = scanner.nextInt();
			scanner.close();

			/*
			 * 新税率での合計価格の最大値を総当たりで調べる
			 * けど実際に計算するのは半分まででいい、
			 * と最初は思ったけれどそうでもない気がしたので
			 * ２つ目の商品の税抜価格を計算して０以下になったら
			 * ループを抜けることにしました。
			 *
			 * price1, price2は２つの商品の税抜価格
			 *
			 * 問題文には１つの商品の税抜価格として
			 * 1円から((変更前の合計価格)-1)円まで考慮に入れろと書いてあったけれど
			 * 税抜で((変更前の合計価格)-1)円の商品があったら絶対に
			 * 変更前の合計価格が与えられたより大きくなるように思うのですが
			 * 変更前の合計価格が小さい時はそういうこともあるのでしょうか…
			 *
			 * そしてprice2を計算する時に
			 * 最後に小数点以下を切り上げる処理が要ることに気づいたので
			 * 丸めるメソッドを作りました。
			 *
			 * 書けたと思って入力サンプルで試したところ答えが全然違ったので
			 * 処理のロジック的な間違いを探したけれど見当たらず、
			 * 切り上げ処理がうまくできていないのではないかと思って
			 * roundUpメソッドのコメントアウトしているような処理を入れてみたところ、
			 * (eclipseのデバッグ機能に慣れてないせいでデバッグ時に値を覗きたい時は
			 * いつも標準出力に出力させています)
			 * 引数の時点ですでに切り捨てられていた(valの値が45.0とかになっていた)
			 * ので、そういえばint型同士では除法でもint型で返ってくる
			 * (=intにキャストされている=切り捨てられている)ことを思い出したので
			 * intとdoubleの計算にしてdouble型で返させるために
			 * 100+oldRateをdoubleにキャストしました。
			 *
			 * それでもいくつかのケースで答えが違ってました。
			 * よく見ると違っているのはどれも１〜２円高い値が出ているので
			 * 違うとすればやはりprice2だろうと思い、
			 * もともとの和とprice1とprice2の税込の和を比べたところ
			 * 後者の方が１だけ大きい場合がありました。
			 *
			 * 厳密にそうだと示すのは難しいように思いますが、
			 * 1円から((変更前の合計価格)-1)円までのそれぞれのprice1に対して
			 * 必ずしも整数値のprice2が存在するとは限らないのではないかと思ったので
			 * 検算の処理を入れたら
			 */
			int max_sum = 0;
			for(int price1=1; ; price1++){
				int price2 = roundUp((sum_before_change -tax(oldRate, price1)) *100 / (double)(100+oldRate));
				if(price2<=0) break;
				if(sum_before_change != tax(oldRate, price1) +tax(oldRate, price2)) continue;
				//System.out.printf("%d %d", sum_before_change, tax(oldRate, price1) +tax(oldRate, price2));
				//System.out.println();
				int sum = tax(newRate, price1) +tax(newRate, price2);
				if(max_sum < sum) max_sum = sum;
			}
			System.out.println(max_sum);
		}

		br.close();
	}

	//税込価格を計算
	private static int tax(int rate, int price_without_tax){
		return price_without_tax*(100+rate)/100;//切り捨てなのでOK
	}

	//切り上げ処理 多分合ってる…
	private static int roundUp(double val){
		int ret = (int) val;
		//System.out.print(val);
		//System.out.print(" ");
		if(val-ret > 0) ret++;
		//System.out.println(ret);
		return ret;
	}
}

