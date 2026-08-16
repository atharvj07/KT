//package abc175;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] ip = br.readLine().split(" ");
		
		long X = Long.parseLong(ip[0]);
		long K = Long.parseLong(ip[1]);
		long D = Long.parseLong(ip[2]);
		
		long ans = 0;
		
		if(X > 0) {
			long tmp_k = Math.min(K, Math.abs(X)/D + 1);
			K -= tmp_k;
			X -= tmp_k*D;
		}else {
			long tmp_k = Math.min(K, Math.abs(X)/D + 1);
			K -= tmp_k;
			X += tmp_k*D;
		}
		ans = Math.abs(X);
		if(K > 0) {
			if(K%2 == 1) {
				if(X > 0) {
					ans = Math.abs(X-D);
				}else {
					ans = Math.abs(X+D);
				}
			}
		}
		
		System.out.println(ans);
	}
	
}
