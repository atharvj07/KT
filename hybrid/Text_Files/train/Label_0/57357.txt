import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int D=sc.nextInt();
		int X=sc.nextInt();
		int[] A=new int[N];
		for(int i=0;i<A.length;i++) {
			A[i]=sc.nextInt();
		}
		int sum=0;
		for(int i=0;i<A.length;i++) {
			sum++;
			sum+=(D-1)/A[i];
		}
		System.out.println(sum+X);


	}
}
