import java.util.*;
 
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int H = sc.nextInt();
		int W = sc.nextInt();
		String[] s = new String[H];
		int whites = -1;
		for(int i=0;i<H;++i){
			s[i] = sc.next();
			for(int j=0;j<W;++j){
				if(s[i].charAt(j)=='.') whites++;
			}
		}
		
		int ans = solve(s,H,W);
		if(ans==-1) System.out.println(-1);
		else System.out.println(whites-ans);
		return;
	}
	
	public static int solve(String[] s,int h,int w){
		int count = 0;
		int[] dx = {1,0,-1,0};
		int[] dy = {0,1,0,-1};
		boolean[][] visited = new boolean[h][w];
		visited[0][0] = true;
		ArrayDeque<Integer> queX = new ArrayDeque<Integer>();
		ArrayDeque<Integer> queY = new ArrayDeque<Integer>();		
		queX.offer(0);
		queY.offer(0);
		
		int validWays = 1;
		while(!queX.isEmpty()){
			int ways = 0;
			for(int i=0;i<validWays;++i){
				int x = queX.poll();
				int y = queY.poll();
				if(x==w-1&&y==h-1) return count;
				for(int j=0;j<4;j++){
					if((x+dx[j]>=0&&x+dx[j]<w)&&(y+dy[j]>=0&&y+dy[j]<h)
							&& s[y+dy[j]].charAt(x+dx[j]) == '.' && !visited[y+dy[j]][x+dx[j]] ){
						visited[y+dy[j]][x+dx[j]] = true;
						queX.offer(x+dx[j]);
						queY.offer(y+dy[j]);
						ways++;
					}
				}
			}
			validWays = ways;
			count++;
		}
		return -1;
	}
}