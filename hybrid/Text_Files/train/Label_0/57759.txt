import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0;
		int[] a = new int[210];

		for(int i = 0; i < N; i++) a[i] = sc.nextInt();

		while(true){
			boolean exit_odd = false;
			for(int i = 0; i < N; i++){
				if(a[i] % 2 != 0) exit_odd = true;
			}

			if(exit_odd) break;

			for(int i = 0; i < N; i++){
				a[i] /= 2;
			}
			count++;
		}

		System.out.println(count);
	}
}
