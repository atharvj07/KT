import java.util.Scanner;

public class Main {

	Scanner sc = new Scanner(System.in);
	public void run() {
		int q = sc.nextInt();
		for(int i = 0; i < q; i++){
			int n = sc.nextInt();
			calc(n);
		}
	}
	public void calc(int n){
		if(n < 10) System.out.println(0);
		else{
			int[] retsu = new int[(int)Math.pow(10, 6) + 1];
			retsu[n] = 1;
			iter(n, 0, retsu);
		}
	}
	
	public void iter( int n, int count, int[] retsu){
		if(n < 10){
			System.out.println(count);
		}
		else{
			int max = 0;
			for(int i = 1; i <= 6; i++){
				int t = (int) Math.pow(10, i);
				if(n >= t){
					int a = n / t;
					int b = n - (a * t);
					if(a * b > max) max = a * b;
				}
			}
			if(retsu[max] == 1) System.out.println(-1);
			else{
				retsu[max] = 1;
				iter(max, count+1, retsu);
			}
		}
	}
	public static void main(String[] args) {
		new Main().run();
	}
}