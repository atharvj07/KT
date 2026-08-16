import java.awt.geom.*;
import java.io.*;
import java.util.*;
public class Main {
	double EPS = 1.0e-08;
	int [][] a;
	int ymin, ymax, n;
	
	class L implements Comparable<L>{
		int left, right;

		public L(int left, int right) {
			this.left = left;
			this.right = right;
		}

		public int compareTo(L o) {
			if(this.left < o.left) return -1;
			if(this.left > o.left) return 1;
			if(this.right < o.right) return -1;
			if(this.right > o.right) return 1;
			return 0;
		}
		
	}

	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			n = sc.nextInt();
			if(n == 0)break;
			Point2D [] data = new Point2D[n];
			ymin = 1 << 24;
			ymax = 0;
			a = new int[n][2];
			for(int i =0; i < n; i++){
				int x = sc.nextInt(), y = sc.nextInt();
				data[i] = new Point2D.Double(x, y);
				ymin = Math.min(ymin, y);
				ymax = Math.max(ymax, y);
				a[i][0] = x;
				a[i][1] = y;
			}
			
			int area = 0;
			for(int y = ymin; y < ymax; y++){
				
				ArrayList<L> list = new ArrayList<L>();
				for(int i = 0 ;i < n; i++){
					int nextind = (i + 1) % n;
					if((a[i][1] <= y && a[nextind][1] <= y) || (a[i][1] >= y+1 && a[nextind][1] >= y+1)){
						continue;
					}
					int [] resa = computeX(i, y);
					int [] resb = computeX(i, y+1);
					list.add(new L(Math.min(resa[0], resb[0]), Math.max(resa[1], resb[1])));
				}
				
				Collections.sort(list);
				int k = list.size();
				int prev = -2000;
				for(int i = 0 ; i < k; i+= 2){
					area += list.get(i+1).right - Math.max(list.get(i).left, prev);
					prev = list.get(i+1).right;
				}
			}
			System.out.println(area);
			
		}
	}

	private int[] computeX(int i, int y) {
		int [] res = new int[2];
		int den, num, w;
		int nextind = (i + 1) % n;
		den = a[nextind][1] - a[i][1];
		num = (y - a[i][1]) * (a[nextind][0] - a[i][0]);
		w = a[i][0] + num / den;
		if(num % den == 0){
			res[0] = w;
			res[1] = w;
		}
		else if((num % den) * den < 0){
			res[0] = w-1;
			res[1] = w;
		}
		else{
			res[0] = w;
			res[1] = w + 1;
		}
		return res;
	}

	public static void main(String [] args){
		new Main().doit();
	}
}