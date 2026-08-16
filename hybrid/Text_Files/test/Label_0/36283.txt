import java.util.*;
import static java.lang.Math.*;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		// 入力
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] x = new int[n];
		for(int i = 0; i < n; i++){
		    x[i] = sc.nextInt();
		}
		
		// 計算
		int result = Integer.MAX_VALUE;
		for(int i = 0; i < n-k+1; i++){
		    if(x[i] < 0 && x[i+k-1] > 0){
		        result = min(result, min(abs(x[i])*2 + abs(x[i+k-1]), abs(x[i]) + abs(x[i+k-1])*2));
		    }else{
		        result = min(result, max(abs(x[i]), abs(x[i+k-1])));
		    }
		}
		
		// 出力
		System.out.println(result);
	}
}
