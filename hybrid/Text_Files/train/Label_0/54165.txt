import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int w[]=new int[n];
		int sum=0;
		for(int i=0;i<n;i++) {
			w[i]=scan.nextInt();
			sum+=w[i];
		}
		scan.close();
		int sum2=0;
		int min=Integer.MAX_VALUE;
		for(int i=0;i<n;i++) {
			sum2+=w[i];
			if(min>Math.abs(sum-sum2*2))min=Math.abs(sum-sum2*2);

		}
		System.out.println(min);
	}
}