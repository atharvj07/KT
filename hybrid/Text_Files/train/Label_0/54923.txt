import java.util.Scanner;

class Main{
	public static void main(String[] ag) {
		Scanner sc=new Scanner(System.in);

		int N=sc.nextInt();
		int K=sc.nextInt();
		int[] x=new int[N];
		int sum=0;

		int ans=0;
		int inp=0;
		for(int i=0; i<N; i++) {
			inp=sc.nextInt();
			ans=Math.min(inp, K-inp);
			sum+=ans*2;
		}
		System.out.println(sum);
	}
}