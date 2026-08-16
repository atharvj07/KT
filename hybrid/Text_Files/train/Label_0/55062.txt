import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Competencia3 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] X = new int[n];
		int[] Y = new int[n];
		for(int i = 0; i < n; i++) {
			X[i] = scan.nextInt();
			Y[i] = scan.nextInt();
			
		}
		
		int res = 0;
		for(int i = 0; i < n; i++) {
			for(int j = i + 1; j < n; j++) {
				int punto1 = X[j] - X[i];
                int punto2 = Y[j] - Y[i];
                int punto3 = X[j] * Y[i] - Y[j] * X[i];
				for(int k = j + 1; k < n; k++) {
					if(punto1 * Y[k] - punto2 * X[k] != punto3) {
						res++;
					}
				}
			}
		}
		System.out.println(res);
		scan.close();
	}
}