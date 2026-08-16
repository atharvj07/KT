import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] a = new int[N];
		for(int i=0; i<N; i++)
			a[i] = sc.nextInt();
		
		int ans = 0;
		int last = 0;
		for(int i=0; i<N; i++) {
			int num=0;
			while(1<<(num+1)<=a[i])
				num++;
			int additional = 1<<num<a[i] ? 1 : 0;
			if(last<=num) {
				ans += num+additional-last;
				last = num+additional;
			} else {
				last = num;
			}
		}
		
		System.out.println(ans);
		
		sc.close();
	}
}
