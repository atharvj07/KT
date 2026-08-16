import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	Scanner sc = new Scanner(System.in);
	int[] memo = new int[60];
	public void run(){
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		calc(a, b, c);
	}
	public void calc(int a, int b, int c){
		int sum = c;
		int okita = 0;
		memo[okita] = 1;
		int neta = a;
		
		while(true){
			if(okita <= sum && sum <= neta){
				break;
			}
			else{
				okita += a+b;
				neta += a+b;
				if(memo[okita % 60]==1) {
					sum = -1;
					break;
				}
				else{
					if(okita > sum) sum += 60;
					memo[okita % 60] = 1;
				}
			}
		}
		System.out.println(sum);
	}
	
	public static void main(String[] args){
		new Main().run();
	}
	
}