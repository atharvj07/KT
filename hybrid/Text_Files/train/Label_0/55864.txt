
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] tmpArray = br.readLine().split(" ");
		
		int n = Integer.parseInt(tmpArray[0]);
		int k = Integer.parseInt(tmpArray[1]);
		
		int[] array = new int[n];
		
		tmpArray = br.readLine().split(" ");
		for(int i = 0; i < n; i++) {
			array[i] = Integer.parseInt(tmpArray[i]);
		}
		
		long total = 0;
		for(int i = 0; i < k; i++) {
			total += array[i];
		}
//		System.out.println(total);
		
		long tmp = total;
		
		for(int i = 1; i + k <= n; i++) {
			tmp -= array[i - 1];
			tmp += array[i + k - 1];
			
			total = Math.max(tmp, total);
			
//			System.out.println(total);
		}
		System.out.println((total + k)/2.0);
	}

}
