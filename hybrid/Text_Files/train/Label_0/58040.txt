import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	Scanner sc = new Scanner(System.in);
	public void run(){
		while(true){
			int r0 = sc.nextInt();
			int w0 = sc.nextInt();
			int c = sc.nextInt();
			int r = sc.nextInt();
			if(r0 == 0 && w0 == 0 && c == 0 && r == 0)break;
			calc(r0, w0, c, r);
		}
	}
	public void calc(int r0, int w0, int c, int r){
		int ans = 0;
		while(true){
			int x = (r0 + r * ans)/ w0;
			if (x >= c) break;
			ans=ans+1;
		}
		
		System.out.println(ans);
	}
	
	public static void main(String[] args){
		new Main().run();
	}
	
}