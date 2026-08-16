import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int w = sc.nextInt();
		int d = sc.nextInt();
		int n = sc.nextInt();
		
		char[][] map = new char[h][w];
		int sy = -1;
		int sx = -1;
		for(int i=0;i<h;i++){
			String s = sc.next();
			for(int j=0;j<w;j++){
				if(s.charAt(j)=='D'){
					sy = i;
					sx = j;
				}
				map[i][j] = s.charAt(j);
			}
		}
		
		int[] r = new int[d];
		for(int i=0;i<d;i++){
			r[i] = sc.nextInt();
		}
		
		int[][] cnt = new int[h][w];
		for(int k=0;k<n;k++){
			int x = sc.nextInt();
			int y = sc.nextInt();
			int s = sc.nextInt();
			
			int sty, edy, stx, edx;
			
			if(s==d){
				for(int i=0;i<=h-1;i++){
					for(int j=0;j<=w-1;j++){
						cnt[i][j]++;
					}
				}
			}
			if(s!=d){
				sty = Math.max(0, y-r[s]);
				edy = Math.min(h-1, y+r[s]);
				stx = Math.max(0, x-r[s]);
				edx = Math.min(w-1, x+r[s]);
				for(int i=sty;i<=edy;i++){
					for(int j=stx;j<=edx;j++){
						cnt[i][j]++;
					}
				}
			}
			if(s!=0){
				sty = Math.max(0, y-r[s-1]);
				edy = Math.min(h-1, y+r[s-1]);
				stx = Math.max(0, x-r[s-1]);
				edx = Math.min(w-1, x+r[s-1]);
				for(int i=sty;i<=edy;i++){
					for(int j=stx;j<=edx;j++){
						cnt[i][j]--;
					}
				}
			}
			
		}
		
		boolean f1 = false;
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				if(cnt[i][j]==n) f1 = true;
			}
		}
		
		String ans = "";
		if(f1){
			boolean[][] vst = new boolean[h][w];
			int[] a = new int[]{1,-1,0,0};
			int[] b = new int[]{0,0,1,-1};
			ArrayDeque<Integer> y = new ArrayDeque<Integer>();
			ArrayDeque<Integer> x = new ArrayDeque<Integer>();
			y.offer(sy);
			x.offer(sx);
			vst[sy][sx] = true;
			while(!y.isEmpty()){
				int ty = y.poll();
				int tx = x.poll();
				for(int i=0;i<4;i++){
					int ny = ty+a[i];
					int nx = tx+b[i];
					if(ny>=0 && ny<h && nx>=0 && nx<w && !vst[ny][nx] && map[ny][nx]!='#'){
						y.offer(ny);
						x.offer(nx);
						vst[ny][nx] = true;
					}
				}
			}
			
			boolean f2 = false;
			boolean f3 = false;
			for(int i=0;i<h;i++){
				for(int j=0;j<w;j++){
					if(map[i][j]!='#' && cnt[i][j]==n){
						if(vst[i][j]) f2 = true;
						else f3 = true;
					}
				}
			}
			
			if(f2 && f3) ans = "Unknown";
			else if(f2) ans = "Yes";
			else if(f3) ans = "No";
		}else{
			ans = "Broken";
		}
		
		System.out.println(ans);

	}	
}