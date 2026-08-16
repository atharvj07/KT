// AOJ 2331
import java.util.Scanner;
 
public class Main{
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] m = new int[100001];
        for(int i = 0; i < n; i++) {
        	int a = sc.nextInt();
        	int b = sc.nextInt();
        	for(int j = a; j <= b; j++) {
        		m[j - 1]++;
        	}
        }
        int max = 0;
        for(int i = 0; i <= n; i++) {
        	//System.out.println(m[i]);
        	if(i <= m[i]) {
        		max = Math.max(i, max);
        	}
        }
        System.out.println(max);
    }
}
