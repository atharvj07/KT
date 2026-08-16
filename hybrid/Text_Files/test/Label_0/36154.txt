/*
 * 高橋君は、N 以下の正の整数の 2 つ組 (a,b) を持っていましたが、忘れてしまいました。 高橋君は、a を b で割ったあまりが K 以上であったことを覚えています。
 * 高橋君が持っていた組としてあるうるものの個数を求めてください。
 */

import java.util.*;
	public class Main{
		public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            //入力
            long n = Integer.parseInt(sc.next());
            long k = Integer.parseInt(sc.next());
            long ret = 0;
            
            // b(iとおいている)はkより大きくn以下
            for(int i=(int)k+1; i<=n; i++){
            	// n/iの商の個数だけ等しく(i-k)個条件を満たすものが存在、n%iの余りの分については余りの個数がMath.max(k-1, 0)を越えている分だけ余分に足す
            	ret += (n/i) * (i-k) + Math.max(0, n%i - Math.max(k, 1) + 1);
            }
            
            System.out.println(ret);
            sc.close();
		}
    }
	