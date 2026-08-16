import java.util.Scanner;

//Lying about Your Age
public class Main{

	int INF = 1<<29;
	
	int f(int x, int b){
		String res = "";
		while(x>0){
			int r = x%b;
			if(10<=r)return INF;
			res = r+res;
			x/=b;
		}
		return Integer.parseInt(res);
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int[][] a = new int[201][17];
		for(int i=1;i<=200;i++)for(int j=2;j<=16;j++)a[i][j]=f(i, j);
		for(;;){
			int A = sc.nextInt(), B = sc.nextInt(), C = sc.nextInt();
			if(A<0)break;
			int res = INF;
			for(int j=2;j<=16;j++)if(a[A][j]==B)res=B;
			for(int i=A+1;i<=C;i++){
				int next = INF;
				for(int j=2;j<=16;j++)if(res<=a[i][j])next = Math.min(next, a[i][j]);
				res = next;
			}
			System.out.println(res==INF?-1:res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}