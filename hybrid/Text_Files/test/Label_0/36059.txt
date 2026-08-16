import java.io.*;
import java.util.*;
public class Landmarks {
	static int n, k;
	static int[] pos, right, left;
	static int[][] spleft;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		pos = new int[n+2];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n+2; i++){
			pos[i] = Integer.parseInt(st.nextToken());
		}
		int[] dur = new int[n+2];
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i < n+1; i++){
			dur[i] = Integer.parseInt(st.nextToken());
		}
		right = new int[n+2]; Arrays.fill(right, 0);
		right[0] = Integer.MAX_VALUE;
		LinkedList<Integer> stack = new LinkedList<>(); stack.addLast(0);
		boolean full = false;
		for(int i = 1; i < n+2; i++){
			while(true){
				int k = stack.getLast();
				if(pos[i] - pos[k] >= 2*dur[i]) break;
				if(right[k] >= pos[i]){
					stack.add(i);
					right[i] = 2*dur[i] + pos[k]; 
					if(right[i] >= pos[n+1]) full = true;
					break;
				} else {
					stack.removeLast();
				}
			}
			if(full) break;
		}
		if(full){
			System.out.println(0); return;
		}
		left = new int[n+2]; Arrays.fill(left, Integer.MAX_VALUE);
		left[n+1] = 0;
		stack = new LinkedList<>(); stack.addLast(n+1);
		for(int i = n+1; i >= 0; i--){
			while(true){
				int k = stack.getLast();
				if(pos[k]-pos[i] >= 2*dur[i]) break;
				if(left[k] <= pos[i]){
					stack.addLast(i);
					left[i] = pos[k] - 2*dur[i]; break;
				} else {
					stack.removeLast();
				}
			}
		} 
		int aux = n+2; k = 0;
		while(aux > 0){ aux >>= 1; k++; }
		spleft = new int[k][n+2];
		for(int i = 0; i < n+2; i++) spleft[0][i] = left[i];
		
		for(int l = 1; l < k; l++){
			int d = 1 << (l-1);
			for(int i = 0; i+d < n+2; i++){
				spleft[l][i] = Integer.min(spleft[l-1][i], spleft[l-1][i+d]);
			}
		}
		
		double a = 0, b = Integer.MAX_VALUE; //tutorial said to use double pointers but i could not figure out how to do that
		while(Math.abs(a-b) > 1e-5){
			double c = (a+b)/2; 					//c = 30;
			if(!check(c)) a = c;
			else b = c;
		}
		System.out.println(a);
	}
	static boolean check(double d){
		for(int i = 0; i < n+1; i++){
			if(right[i] == 0) continue;
			int a = i, b = n+2;
			while(Math.abs(a-b)>1){
				int c = (a+b)/2;
				if(pos[c] <= pos[i] + 2*d) a = c;
				else b = c;
			}
			if(a < i+1) continue;
			if(query(i+1, a) == Integer.MAX_VALUE) continue;
			if(query(i+1, a) <= right[i]) return true;
		}
		return false;
	}
	static int query(int i, int j){
		int r = j-i+1, min = Integer.MAX_VALUE, l = 0, d = 0;
		while(r>0){
			if((r & 1) == 1){
				min = Integer.min(min, spleft[l][i+d]);
				d += 1 << l;
			}
			r >>= 1; l++;
		}
		return min;
	}
}
