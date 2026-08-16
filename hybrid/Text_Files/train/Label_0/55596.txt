import java.util.Scanner;
public class Main {
	long Q;
	long r,l;
	public void solve() {
		Scanner cin = new Scanner(System.in);
		Q = cin.nextLong();
		r = 0;
		l = 0;
		for(int i = 0;i < Q;i++){
			long p = cin.nextLong();
			String c = cin.next();
			long n = cin.nextLong();
			
			if(c.equals("(")){
				r += n;
			}else{
				l += n;
			}
			
			if(r == l){
				System.out.println("Yes");
			}else{
				System.out.println("No");
			}
		}
		cin.close();
	}
 
	public static void main(String[] args) {
		new Main().solve();
	}
}