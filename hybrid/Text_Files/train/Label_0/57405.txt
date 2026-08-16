import java.util.Arrays;
import java.util.Scanner;

//Cosmic Market
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		boolean[] r = new boolean[50000], c = new boolean[50000];
		int[] a = new int[50000], b = new int[50000], o = new int[50000];
		for(;;){
			int R = sc.nextInt(), C = sc.nextInt(), Q = sc.nextInt();
			if((R|C|Q)==0)break;
			Arrays.fill(r, false);
			Arrays.fill(c, false);
			long res = 0;
			for(int i=0;i<Q;i++){
				a[i] = sc.nextInt(); b[i] = sc.nextInt(); o[i] = sc.nextInt();
			}
			for(int i=Q-1;i>=0;i--){
				if(o[i]==0){
					if(a[i]==0){
						if(r[b[i]])continue;
						r[b[i]] = true;
						R--;
					}
					else{
						if(c[b[i]])continue;
						c[b[i]] = true;
						C--;
					}
				}
				else{
					if(a[i]==0){
						if(r[b[i]])continue;
						r[b[i]] = true;
						res+=C;
						R--;
					}
					else{
						if(c[b[i]])continue;
						c[b[i]] = true;
						res+=R;
						C--;
					}
				}
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}