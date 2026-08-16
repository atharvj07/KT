import java.util.Scanner;

//Rational Irrationals
public class Main{

	static long gcd(long a, long b){
		if(a < b){
			long tmp = a;
			a = b;
			b = tmp;
		}
		while(b!=0){
			long r = a%b;
			a = b;
			b = r;
		}
		return a;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int p = sc.nextInt();
			int n = sc.nextInt();
			if((p|n)==0)break;
			double rp = Math.sqrt(p);
			int num = 1;
			int den = 1;
			boolean up = true;
			int x, y, u, v;
			x = y = u = v = 0;
			double d1, d2;
			d1 = -n;
			d2 = n;
			while(num<=n&&den<=n){
				double d = num*1.0/den-rp;
				if(d<0){
					up = true;
					if(d1<d&&gcd(num,den)==1){
						d1 = d;
						u = num;
						v = den;
					}
				}
				else{
					up = false;
					if(d<d2&&gcd(num,den)==1){
						d2 = d;
						x = num;
						y = den;
					}
				}
				num += up?1:0;
				den += up?0:1;
			}
			System.out.println(x+"/"+y+" "+u+"/"+v);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}