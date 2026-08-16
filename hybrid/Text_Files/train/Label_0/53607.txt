import java.util.*;
import java.math.*;
import java.awt.geom.*;
import java.io.*;
    
    
public class Main {
	static int INF = 2 << 27;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int l = sc.nextInt();
		int[] x = new int[n];
		int[] a = new int[n];
		for(int i = 0; i < n; i++) {
			x[i] = sc.nextInt();
		}
		for(int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		int[][] dp = new int[n+1][l+1];
		BinaryIndexedTree[] bit = new BinaryIndexedTree[n+1];
		for(int i = 0; i < n+1; i++) {
			bit[i] = new BinaryIndexedTree(l+2,l+2);
		}
		bit[n].add(1, 1);
		for(int i = n - 1; i >= 0; i--) {
			for(int j = 0; ; j++) {
				if(a[i] == 0) {
					bit[i].add(l + 1 - x[i], bit[i+1].sum(l + 1 - x[i] + 1) % 1000000007);
					break;
				}
				else {
					if(a[i] * j + x[i] > l) break;
					bit[i].add(l + 1 - (x[i] + a[i] * j), bit[i+1].sum(l + 1 - (x[i] + a[i] * j + 1)) % 1000000007);
				}
			}
		}
		
		System.out.println(bit[0].sum(l+1));
		
		
		
		
	}
	
	
	
}

class BinaryIndexedTree {
	int MAX_N;
	int[] bit = new int[MAX_N+1];
	int n;
	
	BinaryIndexedTree(int MAX_N, int n) {
		this.MAX_N = MAX_N;
		this.bit = new int[MAX_N+1];
		this.n = n;
	}
	
	
	int sum(int i) {
		int s = 0;
		while(i > 0) {
			s += bit[i];
			s %= 1000000007;
			i -= i & -i;
		}
		return s;
	}
	
	void add(int i , int x) {
		while(i <= n) {
			bit[i] += x ;
			bit[i] %= 1000000007;
			i += i & -i;
		}
	}
}