import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class Main{
	static String[] S;
	static String[] T;
	static int N;

	public static void main(String args[]) throws IOException {
		Scanner scan = new Scanner(System.in);
		int ansDiv = 1000000007;

		//標準入力からの受取
		N = Integer.parseInt(scan.nextLine());

		String s = scan.nextLine();
		String t = scan.nextLine();

		S = s.split("");
		T = t.split("");

		//確認用配列の初期化
		//先頭のみ1、それ以外は0を代入
		//long[] check = new long[N];
		//Arrays.fill(check, 0) ;
		//check[0] = 1;
		//for(int i = 1;i < N;i++) {
		//for(int j = 0;j < i;j++) {
		//		if(S[j].equals(T[i])) {
		//			check[i] += check[j];
		//			check %= ansDiv;
		//		}
		//	}
		//}

		HashMap<String , Integer> hash = new HashMap<String,Integer>();
		hash.put(S[0], 1);

		//配列を先頭から順番に見て
		//入口と出口が一致する場所を確認する
		for(int i = 1;i < N - 1;i++) {
			if(!hash.containsKey(S[i])) {hash.put(S[i], 0);	}
			if(!hash.containsKey(T[i])) {hash.put(T[i], 0);	}
			
			hash.put(S[i], (hash.get(T[i]) + hash.get(S[i])) % ansDiv);
		}
		System.out.println(hash.get(T[N-1]));

		scan.close();
	}

}

