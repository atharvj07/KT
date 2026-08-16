import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Work[] work = new Work[N];
		Main main = new Main();
		for (int i=0;i<N;i++) {
			Work temp = main.new Work();
			temp.a = sc.nextLong();
			temp.b = sc.nextLong();
			work[i] = temp;
		}
		Arrays.sort(work);
		long now =0;
		for (int i=0;i<N;i++) {
			now+=work[i].a;
			if (now>work[i].b) {
				System.out.println("No");
				return ;
			}
		}
		System.out.println("Yes");
	}

	public class Work implements Comparable<Work> {
		long a;
		long b;
		@Override
		public int compareTo(Work o) {
			if (this.b>o.b)
				return 1;
			if (this.b==o.b) {
				return 0;
			}
			return -1;
		}

	}
}