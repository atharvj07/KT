import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(),M = sc.nextInt();
		String[] ns = new String[N];
		String[] ms = new String[M];
		for(int i = 0;i < N;i++) {
			ns[i] = sc.next();
		}
		for(int i = 0;i < M;i++) {
			ms[i] = sc.next();
		}

		boolean match = false;
		for(int i = 0; i <= N - M; i++) {
			for(int j  =0; j <= N - M;j++) {
				for(int m = 0; m < M; m++) {
					if(!ns[i+m].substring(j, j+M).equals(ms[m])) {
						match = false;
						break;
					}
					match = true;
				}
				if(match) {
					System.out.println("Yes");
						return;
				}
			}
		}
		System.out.println("No");
	}
}