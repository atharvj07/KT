import java.io.*;
import java.math.BigInteger;
import java.util.*;
public class Sequence {

	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int[] dp = new int[100];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int cur, cnt;
		for(int i = 0; i < n; i++) {
			cnt = 0;
			cur = Integer.parseInt(st.nextToken());
			while(cur != 0) {
				while( cur % 2 == 0 ) cur /= 2;
				cur--;
				cnt++;
			}
			dp[cnt]++;
		}
		BigInteger ans = new BigInteger("0");
		for(int i = 0; i < 100; i++) {
			if(dp[i] == 0) continue;
			BigInteger aux = new BigInteger(dp[i]+"");
			ans = ans.add(aux.multiply(aux.subtract(BigInteger.ONE)).divide(BigInteger.ONE.add(BigInteger.ONE)));
		}
		System.out.println(ans);
		
	}
	
	
}
