import java.util.Scanner;

public class Main {
	private static Scanner sc=new Scanner(System.in);
	public static void main(String[] args){
		int a=sc.nextInt();
		int b=sc.nextInt();
		solveEuclid(a,b);
	}
	public static void solveEuclid(int a,int b){
		int r_0=a, r_1=b;
		int a_0=1, a_1=0;
		int b_0=0, b_1=1;
		while(r_1>0){
			int q_1=r_0/r_1;
			int r_2=r_0%r_1;
			int a_2=a_0-q_1*a_1;
			int b_2=b_0-q_1*b_1;
			r_0=r_1;
			r_1=r_2;
			a_0=a_1;
			a_1=a_2;
			b_0=b_1;
			b_1=b_2;
		}
		System.out.println(a_0+" "+b_0);
	}

}