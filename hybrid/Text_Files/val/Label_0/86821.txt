import java.util.*;

class Main{
	public static void main(String[] args){
		Scanner stdIn = new Scanner(System.in);
		int n = stdIn.nextInt();
		int m = stdIn.nextInt();
		int[] money = new int[10];
		int[] ans = new int[n];
		int min = 10000;
		int minNumber = -1;

		for(int i=0; i<10; i++){
			money[i] = stdIn.nextInt();
			if(money[i] < min){
				min = money[i];
				minNumber = i;
			}
		}

		Arrays.fill(ans,minNumber);

		if((m -= money[minNumber] * n) < 0){
			System.out.println("NA");
			return;
		}

/*		for(int i=0; i<n; i++){
			System.out.print(ans[i]);
		}
		System.out.println();
*/
		for(int i=0; i<10; i++){
			for(int j=0; j<n; j++){
				if( ((m - money[i] + money[ans[j]]) >= 0) && (i < ans[j])){
					m = m - money[i] + money[ans[j]];
					ans[j] = i;
				}
			}
		}

		Arrays.sort(ans);

		for(int i=0; i<n; i++){
			System.out.print(ans[i]);
		}
		System.out.println();
	}
}
