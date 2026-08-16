import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

//Poor Mail Forwarding
public class Main{

	final int SEND = 0, BACK = 1, INFORM = 2;
	int INF = 1<<29;
	int[][] e, next;
	boolean[] exist;
	int[] from, to;
	String[] letter;
	LinkedList<P>[] post;
	
	class T{
		int from;
		List<Integer> list;
		public T(int from) {
			this.from = from;
			list = new ArrayList<Integer>();
		}
	}
	class P implements Comparable<P>{
		int at, id, t;
		public P(int at, int id, int t) {
			this.at = at;
			this.id = id;
			this.t = t;
		}
		public int compareTo(P o) {
			return t!=o.t?t-o.t:next[at][to[id]]-next[at][to[o.id]];
		}
		@Override
		public String toString() {
			String r = "";
			r+="Pos:"+at+" Letter id:"+id+" Time:"+t;
			return r;
		}
	}
	class E implements Comparable<E>{
		int type, data, t;
		T con;
		public E(int type, int data, int t, T c) {
			this.type = type;
			this.data = data;
			this.t = t;
			con = c;
		}
		public int compareTo(E o) {
			return t!=o.t?t-o.t:type-o.type;
		}
		@Override
		public String toString() {
			String r = "";
			r+=type==BACK?"BACK":type==SEND?"SEND":"INFORM";
			r+=" at:"+data+" time:"+t;
			return r;
		}
	}
	class R implements Comparable<R>{
		String s;
		int t;
		public R(String s, int t) {
			this.s = s;
			this.t = t;
		}
		public int compareTo(R o) {
			return t!=o.t?t-o.t:s.compareTo(o.s);
		}
	}
	
	@SuppressWarnings("unchecked")
	void run(){
		Scanner sc = new Scanner(System.in);
		boolean head = true;
		for(;;){
			int n = sc.nextInt(), m = sc.nextInt();
			if((n|m)==0)break;
			if(!head)System.out.println();
			head = false;
			e = new int[n][n];
			int[][] adj = new int[n][n];
			for(int[]a:e)Arrays.fill(a, INF);
			for(int[]a:adj)Arrays.fill(a, INF);
			while(m--!=0){
				int s = sc.nextInt()-1, t = sc.nextInt()-1, d = sc.nextInt();
				e[s][t] = e[t][s] = d;
				adj[s][t] = adj[t][s] = d;
			}
			for(int i=0;i<n;i++)e[i][i]=0;
			for(int k=0;k<n;k++)for(int i=0;i<n;i++)for(int j=0;j<n;j++)e[i][j]=Math.min(e[i][j], e[i][k]+e[k][j]);
			next = new int[n][n];
			for(int i=0;i<n;i++)for(int j=0;j<n;j++){
				if(i==j||e[i][j]==INF)continue;
				for(int k=0;k<n;k++){
					if(i==k||adj[i][k]==INF)continue;
					if(e[i][j]==adj[i][k]+e[k][j]){
						next[i][j] = k; break;
					}
				}
			}
			PriorityQueue<R> res = new PriorityQueue<R>();
			exist = new boolean[n];
			Arrays.fill(exist, true);
			PriorityQueue<E> q = new PriorityQueue<E>();
			int L = sc.nextInt();
			from = new int[L]; to = new int[L]; letter = new String[L];
			post = new LinkedList[n];
			for(int i=0;i<n;i++)post[i] = new LinkedList<P>();
			for(int i=0;i<L;i++){
				from[i] = sc.nextInt()-1; to[i] = sc.nextInt()-1;
				int time = sc.nextInt();
				letter[i] = sc.next();
				post[from[i]].add(new P(from[i], i, time));
				q.add(new E(INFORM, from[i], time, null));
			}
			while(!q.isEmpty()){
				E event = q.poll();
//				System.out.println(event);
//				System.out.println(post[1]);
				int pos = event.data;
				if(event.type==BACK){
					if(post[pos].isEmpty()){
						exist[pos] = true; continue;
					}
					Collections.sort(post[pos]);
					if(event.t<post[pos].peek().t){
						exist[pos] = true; continue;
					}
					exist[pos] = false;
					T t = new T(pos);
					P p = post[pos].remove(0);
					t.list.add(p.id);
					int nx = next[pos][to[p.id]];
					for(int i=0;i<post[pos].size();i++){
						P tmp = post[pos].get(i);
						if(event.t<tmp.t)break;
						if(nx==next[pos][to[tmp.id]]){
							post[pos].remove(i);
							t.list.add(tmp.id);
							i--;
						}
					}
					int nt = event.t+e[pos][nx];
					q.add(new E(SEND, nx, nt, t));
					q.add(new E(INFORM, nx, nt, null));
				}
				else if(event.type==INFORM){
					if(!exist[pos])continue;
					if(post[pos].isEmpty())continue;
					Collections.sort(post[pos]);
					if(event.t<post[pos].peek().t)continue;
					exist[pos] = false;
					T t = new T(pos);
					P p = post[pos].remove(0);
					t.list.add(p.id);
					int nx = next[pos][to[p.id]];
					for(int i=0;i<post[pos].size();i++){
						P tmp = post[pos].get(i);
						if(event.t<tmp.t)break;
						if(nx==next[pos][to[tmp.id]]){
							post[pos].remove(i);
							t.list.add(tmp.id);
							i--;
						}
					}
					int nt = event.t+e[pos][nx];
					q.add(new E(SEND, nx, nt, t));
					q.add(new E(INFORM, nx, nt, null));
				}
				else if(event.type==SEND){
					T t = event.con;
					q.add(new E(BACK, t.from, event.t+e[pos][t.from], null));
					boolean offer = false;
					for(int id:t.list){
						if(pos==to[id]){
							res.add(new R(letter[id], event.t)); continue;
						}
						if(!offer)q.add(new E(INFORM, pos, event.t, null));
						offer = true;
						post[pos].add(new P(pos, id, event.t));
					}
				}
			}
			while(!res.isEmpty()){
				R r = res.poll();
				System.out.println(r.s+" "+r.t);
			}
		}
	}
	
	void debug(Object...o){
		System.out.println(Arrays.deepToString(o));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}