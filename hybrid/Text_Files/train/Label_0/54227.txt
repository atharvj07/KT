import java.util.Scanner;

public class Main {
	private static Scanner sc=new Scanner(System.in);
	private static int[] a=new int[6];
	private static int questionLength;
	public static void main(String[] args){
		for(int i=0;i<a.length;i++){
			a[i]=sc.nextInt();
		}
		questionLength=sc.nextInt();
		for(int i=0;i<questionLength;i++){
			int a=sc.nextInt();
			int b=sc.nextInt();
			check(a,b);
		}
	}
	private static void check(int u,int f){
		if((u==a[1]&&f==a[2])||(u==a[2]&&f==a[4])||(u==a[3]&&f==a[1])||(u==a[4]&&f==a[3])){
			System.out.println(a[0]);
		}
		if((u==a[0]&&f==a[3])||(u==a[2]&&f==a[0])||(u==a[3]&&f==a[5])||(u==a[5]&&f==a[2])){
			System.out.println(a[1]);
		}
		if((u==a[0]&&f==a[1])||(u==a[1]&&f==a[5])||(u==a[4]&&f==a[0])||(u==a[5]&&f==a[4])){
			System.out.println(a[2]);
		}
		if((u==a[0]&&f==a[4])||(u==a[1]&&f==a[0])||(u==a[4]&&f==a[5])||(u==a[5]&&f==a[1])){
			System.out.println(a[3]);
		}
		if((u==a[0]&&f==a[2])||(u==a[2]&&f==a[5])||(u==a[3]&&f==a[0])||(u==a[5]&&f==a[3])){
			System.out.println(a[4]);
		}
		if((u==a[1]&&f==a[3])||(u==a[2]&&f==a[1])||(u==a[3]&&f==a[4])||(u==a[4]&&f==a[2])){
			System.out.println(a[5]);
		}
	}
}