import java.util.Arrays;
import java.util.Scanner;

//Modular Query
public class Main{

	public void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), q = sc.nextInt();
		boolean[] a = new boolean[300001];
		for(int i=0;i<n;i++)a[sc.nextInt()]=true;
		while(q--!=0){
			int m = sc.nextInt();
			int res = m-1;
			while(0<res){
				boolean e = false;
				for(int i=res;i<=300000;i+=m)if(a[i]){
					e = true; break;
				}
				if(e)break;
				res--;
			}
			System.out.println(res);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}