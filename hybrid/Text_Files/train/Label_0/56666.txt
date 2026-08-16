import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        while(true) {
        	int n = sc.nextInt();
        	if(n == 0) break;
        	int[] a = new int[n];
        	for(int i=0;i<n;i++) {
        		a[i] = sc.nextInt();
        	}
        	Arrays.sort(a);
        	int min = Integer.MAX_VALUE;
        	for(int i=0;i<n-1;i++) {
        		min = Math.min(Math.abs(a[i] - a[i+1]), min);
        	}
        	System.out.println(min);
        }
    }
}
