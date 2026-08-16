import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-9;

	int k;
	int m;

	void run(){
		for(;;){
			k=sc.nextInt();
			if(k==0){
				break;
			}
			solve();
		}
	}

	void solve(){
		m=0;
		boolean[] visited=new boolean[10000];
		int mod=12345678;
		Cell leader=new Cell(k);
		int maxNum=1;
		for(int k=1;; k++){
			LinkedList<Cell> que=new LinkedList<Cell>();
			que.offer(leader);
			fill(visited, false);
			visited[leader.v]=true;
			// debug("bfs");
			for(; !que.isEmpty();){
				Cell c=que.poll();
				int n=c.n*3+1;
				for(; n%2==0;){
					n/=2;
				}
				n%=mod;
				c.candidate=n>c.n&&(c.size()==0||(c.size()==1&&c!=leader));
				// debug(c.n, "->", n, c.v, c.candidate, c.size());
				c.n=n;
				if(c.n==1){
					if(c==leader){
						println(k+" "+maxNum);
						return; // Æè ¦¸D
					}
					Cell par=null;
					for(Cell d : c){
						if(visited[d.v]){
							par=d;
						}
						d.remove(c);
					}
					if(false){
						debug("e", par.n);
						for(Cell e : par){
							debug("", e.n, e==c);
						}
						debug("Á");
						for(Cell e : c){
							debug("", e.n, e==par);
						}
					}

					c.remove(par);
					if(c.size()==1){
						Cell child=c.getFirst();
						par.add(child);
						child.add(par);

						que.offer(child);
						visited[child.v]=true;
					}
				}else{
					for(Cell d : c){
						if(!visited[d.v]){
							que.offer(d);
							visited[d.v]=true;
						}
					}
				}
			}
			// debug("update");
			// dfs(leader);
			// debug();

			int num=0;

			// Vµ­¶Þ
			fill(visited, false);
			Cell newLeader=new Cell(0);
			boolean overlap=false;
			que.offer(leader);
			visited[leader.v]=true;
			for(; !que.isEmpty();){
				Cell c=que.poll();
				num++;
				for(Cell d : c){
					if(!visited[d.v]){
						que.offer(d);
						visited[d.v]=true;
					}
				}
				if(c.n>newLeader.n){
					newLeader=c;
					overlap=false;
				}else if(c.n==newLeader.n){
					overlap=true;
				}
				if(c.candidate&&((c.size()==1&&c!=leader)||c.size()==0)){
					Cell d=new Cell(((c.n+1)/2)|1);
					if(d.n!=1){
						c.add(d);
						d.add(c);
						num++;
						// debug("child leaf:", c.n, d.n, d.v);
					}
				}
			}
			// debug("overlap", newLeader.n, overlap);
			if(!overlap){
				leader=newLeader;
				Cell c=new Cell(((leader.n+1)/2-1)|1);
				if(c.n!=1){
					leader.add(c);
					c.add(leader);
					num++;
					// debug("leader", c.n, c.v);
				}
			}
			maxNum=max(maxNum, num);

			// debug(k);
			// debug("new");
			// dfs(leader);
			// debug();
		}
	}

	void bfs(Cell leader){
		LinkedList<Cell> que=new LinkedList<Cell>();
		que.offer(leader);
		boolean[] visited=new boolean[10000];
		visited[leader.v]=true;
		leader.tab="";
		for(; !que.isEmpty();){
			Cell c=que.poll();
			debug(c.tab, c.n, c.v);
			for(Cell d : c){
				if(!visited[d.v]){
					que.offer(d);
					visited[d.v]=true;
					d.tab=c.tab+"  ";
				}
			}
		}
	}

	boolean[] visited=new boolean[10000];

	void dfs(Cell leader){
		fill(visited, false);
		dfs(leader, "");
	}

	void dfs(Cell c, String tab){
		debug(tab, c.n, c.size(), c.v);
		visited[c.v]=true;
		for(Cell d : c){
			if(!visited[d.v]){
				dfs(d, tab+"  ");
			}
		}
	}

	class Cell extends LinkedList<Cell>{
		int n, v;
		boolean candidate;
		String tab;

		Cell(int n){
			this.n=n;
			this.v=m++;
		}

		@Override
		public int hashCode(){
			return v;
		}

		@Override
		public boolean equals(Object o){
			return hashCode()==((Cell)o).hashCode();
		}
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}