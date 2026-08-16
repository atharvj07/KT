import java.util.Scanner;
import java.util.Arrays;
public class Main{
	public static void main(String[] args){
		new Main().run();
	}
	public void run(){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int a = scan.nextInt();
		int b = scan.nextInt();
		int cal = scan.nextInt();
		int max = cal / a;
		int[] t = new int[n];
		for(int i = 0;i < n;i++){
			t[i] = scan.nextInt();
		}
		Arrays.sort(t);
		int tc;
		for(int k = 1,i = n-1;i >= 0;i--,k++){
			cal += t[i];
			tc = cal / (k*b + a);
			if(max <= tc){
				max = tc;
			}else{
				break;
			}
		}
		System.out.println(max);
	}
}