import java.util.Arrays;
import java.util.Scanner;

public class Main {

	private void doIt() {
		Scanner sc = new Scanner(System.in);

		final int MAX = 1000000;
		boolean [] isprime = new boolean[MAX+1];
		int [] acc = new int[MAX+1];
		Arrays.fill(isprime, true);
		for(int i = 2; i <= MAX; i++){
			acc[i] = acc[i-1];
			if(isprime[i]){
				acc[i]++;
				for(int j = i * 2; j <= MAX; j += i){
					isprime[j] = false;
				}
			}
		}

		while(true){
			int n = sc.nextInt();
			if(n == 0){
				break;
			}
			int sum = 0;
			int [][] data = new int[n][2];
			for(int i=0; i < n ;i++){
				int p = sc.nextInt();
				int m = sc.nextInt();
				int max = p+m;
				int min = p-m;
				data[i][0] = Math.max(min, 2);
				data[i][1] = Math.min(Math.max(max, 2), 1000000);
			}
			for(int i=0; i < n ;i ++){
				int pat = acc[data[i][1]] - acc[data[i][0]- 1];
				sum += pat - 1;
			}
			System.out.println(sum);
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doIt();
	}

}