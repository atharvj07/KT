//package round_31;

import java.util.Scanner;

public class A {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int []a = new int[n+1];
		for (int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}
		for (int i = 1; i <=n; i++) {
			for (int j = 1; j <= n; j++) {
				for (int j2 = 1; j2 <= n; j2++) {
					if(j!=j2 && i!=j && i!=j2 &&  a[i]==a[j]+a[j2]){
						System.out.println(i+" "+j+" "+j2);
						sc.close();
						return;
					}
				}
			}
		}
		System.out.println("-1");
		sc.close();
	}
}
//class Pair{
//	int value;
//	int index;
//	Pair(int value, int index){
//		this.value = value;
//		this.index = index;
//	}
//}
