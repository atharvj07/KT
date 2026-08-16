import java.util.*;

class Main{
    void solve(){
	Scanner sc = new Scanner(System.in);
	int h1 = sc.nextInt();
	int h2 = sc.nextInt();
	int k1 = sc.nextInt();
	int k2 = sc.nextInt();
	int a = sc.nextInt();
	int b = sc.nextInt();
	int c = sc.nextInt();
	int d = sc.nextInt();
	int hiroshi = h1*a + h2*b + (h1/10)*c + (h2/20)*d;
	int kenjiro = k1*a + k2*b + (k1/10)*c + (k2/20)*d;
	
	if ( hiroshi > kenjiro ) System.out.println("hiroshi");
	else if ( hiroshi < kenjiro ) System.out.println("kenjiro");
	else System.out.println("even");
	
    }

    public static void main(String[] args){
	new Main().solve();
    }
}

