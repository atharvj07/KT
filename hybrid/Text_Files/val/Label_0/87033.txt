import java.util.*;
import java.util.Arrays;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
      	int a[] = new int[n];
      	int s = 0;
      	for (int i = 0; i < n; i++){
          	a[i] = sc.nextInt();
        }
        Arrays.sort(a);
        s = a[n/2] - a[n/2-1];
        System.out.println(s);
    }
}