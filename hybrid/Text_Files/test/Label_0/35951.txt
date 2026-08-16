import java.util.*;

public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		new Problem_B();
	}

	class Problem_B{
		int h,w,ph,pw;
		int[][] a;
		boolean[][] b;
		boolean[][] c;

		int sum(int start_x,int start_y){
			int result = 0;
			for(int s=0;s<ph;s++)for(int i=0;i<pw;i++){
				if(c[s][i]==b[s+start_y][i+start_x]){
					result+=a[s+start_y][i+start_x];
				}else return Integer.MIN_VALUE;
			}
			return result;
		}

		public Problem_B() {
			h = in.nextInt();
			w = in.nextInt();
			a = new int[h][w];
			b = new boolean[h][w];
			for(int i=0;i<h;i++)for(int s=0;s<w;s++)a[i][s] = in.nextInt();
			for(int i=0;i<h;i++)for(int s=0;s<w;s++)b[i][s] = in.nextInt()==1;
			ph = in.nextInt();
			pw = in.nextInt();
			c = new boolean[ph][pw];
			for(int i=0;i<ph;i++)for(int s=0;s<pw;s++)c[i][s] = in.nextInt()==1;
			int result = Integer.MIN_VALUE;
			for(int s=0;s<h-ph+1;s++){
				for(int i=0;i<w-pw+1;i++){
					if(b[s][i]==c[0][0])result=Math.max(result,sum(i,s));
				}
			}
			System.out.println(result!=Integer.MIN_VALUE? result:"NA");
		}
	}
}
