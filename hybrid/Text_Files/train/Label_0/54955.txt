import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

//Hexerpents of Hexwamp
public class Main{

	int[][] dir = {{0,-1},{1,-1},{1,0},{0,1},{-1,1},{-1,0}};

	class Snake{
		int x, y;
		String s;
		public Snake(int x, int y, String s) {
			this.x = x;
			this.y = y;
			this.s = s;
		}
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + getOuterType().hashCode();
			result = prime * result + ((s == null) ? 0 : s.hashCode());
			result = prime * result + x;
			result = prime * result + y;
			return result;
		}
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Snake other = (Snake) obj;
			if (!getOuterType().equals(other.getOuterType()))
				return false;
			if (s == null) {
				if (other.s != null)
					return false;
			} else if (!s.equals(other.s))
				return false;
			if (x != other.x)
				return false;
			if (y != other.y)
				return false;
			return true;
		}
		private Main getOuterType() {
			return Main.this;
		}

	}

	class S{
		int dx, dy;
		String s;
		public S(int dx, int dy, String s) {
			this.dx = dx;
			this.dy = dy;
			this.s = s;
		}
	}

	Map<String, Set<S>> adj;
	int n;
	long FIX = 1000000, M = 10000000;
	Set<Long> rock;
	Set<String> valid;

	//·³lenÌÖÌÌÅLøÈàÌðìé = validðßé
	void make(int k, char[] s, int len){
		if(k>=1){
			int[][] p = new int[k+1][2];
			p[0][0]=p[0][1]=0;
			for(int i=1;i<=k;i++){
				int x = s[i-1]-'0';
				p[i][0] = p[i-1][0]+dir[x][0]; p[i][1] = p[i-1][1]+dir[x][1];
			}
			if(!valid(p, k))return;
		}
		if(k==len){
			String state = new String(s);
			valid.add(state);
			adj.put(state, new HashSet<S>());
			return;
		}
		for(char d='0';d<='5';d++){
			s[k] = d;
			make(k+1, s, len);
		}
	}

	//±ÌÌÌ\¢©ç1XebvÅHèÂ¯éóÔðT·
	void find(String state){
		int N = state.length()+1;
		int[][] p = new int[N][2];
		for(int i=0;i<N-1;i++){
			int d = state.charAt(i)-'0';
			p[i+1][0] = p[i][0] + dir[d][0]; p[i+1][1] = p[i][1] + dir[d][1];
		}
		dfs(0, N, p, state);
	}
	void dfs(int k, int N, int[][] p, String state){
		if(N<=k){
			int dx = p[0][0], dy = p[0][1];
			String s = "";
			for(int i=1;i<N;i++){
				for(int d=0;d<6;d++){
					if(p[i][0]==p[i-1][0]+dir[d][0]&&p[i][1]==p[i-1][1]+dir[d][1]){
						s += d; break;
					}
				}
			}
			if(!valid.contains(s))return;
			adj.get(state).add(new S(dx, dy, s));
			return;
		}
		dfs(k+1, N, p, state);
		int px = p[k][0], py = p[k][1];
		for(int d=0;d<6;d++){
			p[k][0]+=dir[d][0]; p[k][1]+=dir[d][1];
			if(valid(p, Math.min(k+1, N-1))){
				dfs(k+2, N, p, state);
			}
			p[k][0] = px; p[k][1] = py;
		}
	}

	//p[0]`p[len]ÜÅÜÁÄ¢éB±êÍLøÈóÔ©?
	boolean valid(int[][] p, int len){
		//Ì1ÂÈçÈñ¾ÁÄ¢¢
		if(len==0)return true;
		String s = "";
		for(int i=0;i<len;i++){
			boolean f = false;
			for(int d=0;d<6;d++){
				if(p[i][0]+dir[d][0]==p[i+1][0]&&p[i][1]+dir[d][1]==p[i+1][1]){
					s += d;
					f = true; break;
				}
			}
			if(!f)return false;
		}
		boolean ok = true;
		for(int i=0;i<=len;i++)for(int j=i+1;j<=len;j++){
			if(p[i][0]==p[j][0]&&p[i][1]==p[j][1]){
				ok = false; break;
			}
		}
		if(!ok)return false;
		int[] adj = new int[len+1];
		for(int i=0;i<=len;i++){
			for(int j=0;j<=len;j++){
				if(i==j)continue;
				for(int d=0;d<6;d++){
					if(p[i][0]+dir[d][0]==p[j][0]&&p[i][1]+dir[d][1]==p[j][1]){
						adj[i]++;
					}
				}
			}
			if((i==0||i==len)&&adj[i]!=1)return false;
			if(0<i&&i<len&&adj[i]!=2)return false;
		}
		return true;
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		valid = new HashSet<String>();
		adj = new HashMap<String, Set<S>>();
		for(int N=1;N<=8;N++){
			make(0, new char[N-1], N-1);
		}
		for(String s:valid)find(s);
		for(;;){
			n = sc.nextInt();
			if(n==0)break;
			int[][] p = new int[n][2];
			for(int i=0;i<n;i++)for(int j=0;j<2;j++)p[i][j]=sc.nextInt();
			int k = sc.nextInt();
			rock = new HashSet<Long>();
			while(k--!=0){
				long x = sc.nextInt()+FIX, y = sc.nextInt()+FIX;
				rock.add(x*M+y);
			}
			int gx = sc.nextInt(), gy = sc.nextInt();
			int x = p[0][0], y = p[0][1];
			String s = "";
			for(int i=0;i<n-1;i++){
				for(int d=0;d<6;d++){
					if(p[i][0]+dir[d][0]==p[i+1][0]&&p[i][1]+dir[d][1]==p[i+1][1]){
						s += d; break;
					}
				}
			}
			Snake start = new Snake(x, y, s);
			List<Snake> list = new ArrayList<Snake>();
			list.add(start);
			Set<Snake> used = new HashSet<Snake>();
			used.add(start);
			int step = 0;
			while(!list.isEmpty()&&step<=20){
				List<Snake> nextState = new ArrayList<Snake>();
				for(Snake v:list){
					if(v.x==gx&&v.y==gy){
						System.out.println(step);
						nextState.clear(); break;
					}
					for(S a:adj.get(v.s)){
						Snake z = new Snake(v.x+a.dx, v.y+a.dy, a.s);
						if(used.contains(z))continue;
						int[][] pos = new int[n][2];
						pos[0][0] = z.x; pos[0][1] = z.y;
						for(int i=1;i<n;i++){
							int d = z.s.charAt(i-1)-'0';
							pos[i][0] = pos[i-1][0] + dir[d][0]; pos[i][1] = pos[i-1][1] + dir[d][1];
						}
						boolean ok = true;
						for(int i=0;i<n;i++){
							if(rock.contains((pos[i][0]+FIX)*M+pos[i][1]+FIX)){
								ok = false; break;
							}
						}
						if(!ok)continue;
						used.add(z);
						nextState.add(z);
					}
				}
				list = nextState;
				step++;
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}