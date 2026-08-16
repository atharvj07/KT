import java.util.Scanner;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int l[] = new int[n];
		for(int i = 0; i < n; i++) {
			l[i] = sc.nextInt();
		}
		int ans = 0;
		
		Arrays.sort(l);
//		for(int i = 0; i < n; i++) {
//			System.out.print(l[i]);
//		}
		for(int i = 0; i < n ; i++) {
			for(int j = i + 1; j < n; j++) {
				for(int k = j + 1; k < n; k++) {
					if(l[i] + l[j] > l[k]) {
						ans++;
					} else break;
				}
			}
		}
		System.out.println(ans);
	}
}
