import java.util.Arrays;
import java.util.Scanner;

public class Main {

	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		new RitProA().doIt();
	}
	class RitProA{
		void doIt(){
			int N = in.nextInt();
			int a[] = new int [N]; 
			long sum[] = new long[1000002];
			for(int i = 0;i < N;i++){
				a[i] = in.nextInt();
			}
			Arrays.sort(a);
			long cnt = 0;
			for(int i = 0;i < N;i++){
				cnt = cnt + a[i];
				sum[a[i]] = cnt;
			}
			for(int i = 0;i < 1000000;i++){
				if(sum[i+1] == 0){
					sum[i+1] = sum[i];
				}
			}
			int M = in.nextInt();
			int b[] = new int [M];
			long c[] = new long [M];
			for(int i = 0;i < M;i++){
				b[i] = in.nextInt();
			}
			for(int i = 0;i < M;i++){
				c[i] = in.nextLong();
			}
			for(int i = 0;i < M;i++){
				if(sum[b[i]] >=c[i]){
					System.out.println("Yes");
				}else{
					System.out.println("No");
				}
			}
		}
	}
}