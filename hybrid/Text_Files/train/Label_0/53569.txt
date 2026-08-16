
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Main p = new Main();
	}

	public Main() {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int w = sc.nextInt();
			int d = sc.nextInt();
			if(n==0 && w==0 && d==0)
				break;
			
			int[] p = new int[n];
			int[] s = new int[n];
			for(int i=0;i<n;i++){
				p[i] = sc.nextInt();
				s[i] = sc.nextInt();
			}
			solve(n, w, d, p, s);
		}
	}

	public void solve(int n, int w, int d, int[] p, int[] s) {
		List<int[]> l = new LinkedList<int[]>();
		l.add(new int[]{w, d, w*d, -1});
		
		for(int i=0;i<p.length;i++){
			int[] c = l.remove(p[i]-1);
			int cp = s[i]%(c[0]+c[1]);
			if(cp<c[0]){
				int no = (c[0]-cp)*c[1]<cp*c[1] ? 0 : 1;
				l.add(new int[]{c[0]-cp, c[1], (c[0]-cp)*c[1], i*2+no});
				l.add(new int[]{cp, c[1], cp*c[1], i*2+1-no});
			}else{
				cp -= c[0];
				int no = c[0]*cp<c[0]*(c[1]-cp) ? 0 : 1;
				l.add(new int[]{c[0], cp, c[0]*cp, i*2+no});
				l.add(new int[]{c[0], c[1]-cp, c[0]*(c[1]-cp), i*2+1-no});
			}
			Collections.sort(l, new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					return o1[3]-o2[3];
				}
			});
		}
		
		Collections.sort(l, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[2]-o2[2];
			}
		});
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<l.size()-1;i++){
//			System.out.println(Arrays.toString(l.get(i)));
			sb.append(l.get(i)[2]+" ");
		}
		sb.append(l.get(l.size()-1)[2]);
		System.out.println(sb.toString());
		
	}

}