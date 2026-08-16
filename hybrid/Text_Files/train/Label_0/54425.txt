import java.util.*;
 
public class Main {
    //最小公倍数lcm
    static long lcm (int a, int b) {
    	int temp;
    	long c = a;
    	c *= b;
    	while((temp = a%b)!=0) {
    		a = b;
    		b = temp;
    	}
    	return c/b;
    }
    //最大公約数
    static int gcd (int a, int b) {
    	int temp;
    	while((temp = a%b)!=0) {
    		a = b;
    		b = temp;
    	}
    	return b;
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long LCM = lcm(N,M);//N,Mの最小公倍数
        String S = sc.next();
        String T = sc.next();
        int g = gcd(N,M);
        for(int i = 0; i < g; i++){
            if(!(S.substring(N/g*i,N/g*i+1).equals(T.substring(M/g*i,M/g*i+1)))){
                LCM = -1;
            }
        }
        System.out.println(LCM);
    }
}