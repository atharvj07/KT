import java.util.*;
import static java.lang.Math.*;

public class Main {
	final Scanner sc=new Scanner(System.in);
	public static void main(String[] args) {
		new Main().init();
	}
	void init(){
		//long start=System.currentTimeMillis();
		new AOJ1252();
		//System.out.println(" ["+ (System.currentTimeMillis()-start) +"msec]");
	}
	
	// Confusing Login Names
	class AOJ1252{
		AOJ1252(){
			while(true){
				int N=sc.nextInt();
				if(N==0)	break;
				solve(N);
			}
		}
		void solve(int N){
			int D=sc.nextInt();
			String[] names=new String[N];
			for(int i=0; i<N; i++)	names[i]=sc.next();
			Arrays.sort(names);
			ArrayList<TreeSet<String>> state1=new ArrayList<TreeSet<String>>(),state2=new ArrayList<TreeSet<String>>();
			for(int i=0; i<N; i++){
				TreeSet<String> tmp=new TreeSet<String>();
				for(int j=0; j<names[i].length(); j++){
					tmp.add(new StringBuilder(names[i]).deleteCharAt(j).toString());
					for(int k=0; k<26; k++){
						char c=(char)('a'+k);
						tmp.add(new StringBuilder(names[i]).insert(j, c).toString());
						StringBuilder sb=new StringBuilder(names[i]);
						sb.setCharAt(j, c);
						tmp.add(sb.toString());
					}
					tmp.add(swap(j,min(j+1,names[i].length()-1),names[i]));
				}
				for(int k=0; k<26; k++)	tmp.add(names[i]+(char)('a'+k));
				//System.out.println(tmp);
				state1.add(tmp);
			}
			if(D>1)	state2=state1;
			else{
				for(int i=0; i<N; i++){
					TreeSet<String> tmp=new TreeSet<String>();
					tmp.add(names[i]);
					state2.add(tmp);
				}
			}
			
			TreeSet<Pair> ans=new TreeSet<Main.AOJ1252.Pair>();
			for(int i=0; i<N; i++){
				for(int j=i+1; j<N; j++){
					if(names[i].length()-names[j].length()>4)	continue;
					for(String s:state1.get(i)){
						if(state2.get(j).contains(s))	ans.add(new Pair(names[i],names[j]));
					}
				}
			}
			for(Pair p:ans)	System.out.println(p);
			System.out.println(ans.size());
		}
		String swap(int a,int b,String str){
			StringBuilder sb=new StringBuilder(str);
			char tmp=sb.charAt(a);
			sb.setCharAt(a, sb.charAt(b));
			sb.setCharAt(b, tmp);
			return sb.toString();
		}
		class Pair implements Comparable<Pair>{
			String s1,s2;
			Pair(String s1,String s2){
				this.s1=s1;
				this.s2=s2;
			}
			@Override public int compareTo(Pair p){
				if(s1==p.s2 && s2==p.s1)	return 0;
				return s1.compareTo(p.s1)!=0?s1.compareTo(p.s1) :s2.compareTo(p.s2);
			}
			@Override public String toString(){
				return s1+","+s2;
			}
		}
	}
	
	
	// Gap
	class AOJ1245{
		AOJ1245(){
			int N=sc.nextInt();
			while(--N>=0)	solve();
		}
		void solve(){
			StringBuilder init=new StringBuilder(),fin=new StringBuilder();
			for(int i=1; i<=4; i++){
				init.append("##");
				for(int j=1; j<=7; j++){
					init.append(sc.nextInt());
					fin.append(i);	fin.append(j);
				}
				fin.append("##");
			}
			for(int i=0; i<32; i++){
				if(init.charAt(i*2+1)=='1')	nSwap(i*2,(init.charAt(i*2)-'0'-1)*16,init);
			}
			int ans=-1;
			PriorityQueue<State1> open=new PriorityQueue<State1>();
			open.add(new State1(init,0));
			HashMap<String,Integer> closed=new HashMap<String, Integer>();
			closed.put(init.toString(),0);
			while(!open.isEmpty()){
				State1 now=open.poll();
				if(now.sb.toString().equals(fin.toString())){
					ans=now.step;
					break;
				}
				for(int i=0; i<32; i++){
					if(now.sb.charAt(i*2)=='#' && now.sb.charAt((i-1)*2)!='#'){
						int s=now.sb.charAt((i-1)*2)-'0',v=now.sb.charAt((i-1)*2+1)-'0';
						if(v>=7)	continue;
						boolean bf=false;
						for(int j=0; j<32; j++){
							if(now.sb.charAt(j*2)-'0'==s && now.sb.charAt(j*2+1)-'0'==v+1){
								StringBuilder tmp=new StringBuilder(now.sb);
								nSwap(i*2,j*2,tmp);
								if(tmp.toString().equals(fin.toString())){
									ans=now.step+1;
									open.clear();
									bf=true;
									break;
								}
								if(closed.containsKey(tmp.toString()) && closed.get(tmp.toString())<=now.step+1)	break;
								open.add(new State1(tmp,now.step+1));
								closed.put(tmp.toString(),now.step+1);
								break;
							}
						}
						if(bf)	break;
					}
				}
			}
			System.out.println(ans);
		}
		void nSwap(int a,int b,StringBuilder sb){
			if(a==b)	return;
			swap(a,b,sb);
			swap(++a,++b,sb);
		}
		void swap(int a,int b,StringBuilder sb){
			char tmp=sb.charAt(a);
			sb.setCharAt(a, sb.charAt(b));
			sb.setCharAt(b, tmp);
		}
		class State1 implements Comparable<State1>{
			StringBuilder sb;
			int step;
			State1(StringBuilder sb,int step){
				this.sb=sb;	this.step=step;
			}
			@Override public int compareTo(State1 o) {
				return this.step-o.step;
			}
		}
	}
	
	class AOJ1258{
		final int INF=Integer.MAX_VALUE/4;
		AOJ1258(){
			while(true){
				int M=sc.nextInt(),C=sc.nextInt(),N=sc.nextInt();
				if(((M|C)|N)==0)	break;
				System.out.println(solve(M,C,N));
			}
		}
		int solve(int M,int C,int N){
			LinkedList<LinkedList<Integer>> q=new LinkedList<LinkedList<Integer>>();
			for(int i=0; i<N; i++){
				q.add(new LinkedList<Integer>());
				int K=sc.nextInt();
				for(int j=0; j<K; j++)	q.getLast().add(sc.nextInt());
			}
			Store store=new Store(M,C);
			int ans=0;
			while(!q.isEmpty()){
				int r=q.getFirst().poll();
				ans+=store.take(r);
				ans+=store.put(r);
				//debug
				//System.out.println(store);
				if(q.getFirst().isEmpty())	q.removeFirst();
				else	q.addLast(q.poll());
			}
			return ans;
		}
		class Store{
			int M,C,time;
			ArrayList<ArrayList<Book>> desks;
			Store(int m,int c){
				this.M=m;	this.C=c;	this.time=0;
				desks=new ArrayList<ArrayList<Book>>();
				for(int i=0; i<M; i++)	desks.add(new ArrayList<Book>());
			}
			int take(int r){
				int ret=M+1;
				for(int i=0; i<M; i++){
					for(int j=0; j<desks.get(i).size(); j++){
						if(desks.get(i).get(j).id==r){
							desks.get(i).remove(j);
							ret=i+1;
							break;
						}
					}
					if(ret<M+1)	break;
				}
				return ret;
			}
			int put(int r){
				int ret=M+1;
				if(desks.get(0).size()<C){
					desks.get(0).add(new Book(r,time++));
					ret=1;
				}else{
					ret=0;
					Pair tmpIdx=new Pair(M,0);
					for(int i=1; i<M; i++){
						if(desks.get(i).size()<C){
							tmpIdx.first=i;
							desks.get(i).add(new Book(INF,INF));
							tmpIdx.second=desks.get(i).size()-1;
							break;
						}
					}
					ret+=tmpIdx.first+1;
					int oldestTime=desks.get(0).get(0).t,oldestIdx=0;
					for(int i=1; i<desks.get(0).size(); i++){
						if(oldestTime>desks.get(0).get(i).t){
							oldestTime=desks.get(0).get(i).t;
							oldestIdx=i;
						}
					}
					Book oldest=desks.get(0).remove(oldestIdx);
					ret+=1;
					int empIdx=M;
					for(int i=1; i<M; i++){
						if(desks.get(i).size()<C){
							desks.get(i).add(oldest);
							empIdx=i;
							break;
						}
					}
					ret+=empIdx+1;
					if(tmpIdx.first<M)	desks.get(tmpIdx.first).remove(tmpIdx.second);
					ret+=tmpIdx.first+1;
					desks.get(0).add(new Book(r,time++));
					ret+=1;
				}
				return ret;
			}
			@Override public String toString(){return desks.toString();}
		}
		class Book{
			int id,t;
			Book(int id,int t){this.id=id;this.t=t;}
			@Override public String toString(){return "ID"+id+" T"+t;}
		}
		class Pair implements Comparable<Pair>{
			int first,second;
			Pair(int first,int second){this.first=first; this.second=second;}
			@Override public String toString(){return "("+first+","+second+")";}
			@Override public int compareTo(Pair p){
				if(this.first<p.first)	return -1;
				if(this.first>p.first)	return 1;
				if(this.second<p.second)	return -1;
				if(this.second>p.second)	return 1;
				return 0;
			}
			@Override public int hashCode(){
				return 17+31*first+second;
			}
			@Override public boolean equals(Object obj){
				if(this==obj)	return true;
				if(obj==null)	return false;
				if(this.getClass() != obj.getClass())	return false;
				Pair p=(Pair)obj;
				if(this.first==p.first&&this.second==p.second)	return true;
				return false;
			}
		}
	}
	
	class AOJ1262{
		final double INF=Double.MAX_VALUE/4.0;
		AOJ1262(){
			while(true){
				int N=sc.nextInt();
				if(N==0)	break;
				System.out.printf("%.4f\n",solve(N));
			}
		}
		double solve(int N){
			int[] a=new int[N+1];
			for(int i=1; i<=N; i++)	a[i]=sc.nextInt();
			double b=sc.nextDouble();
			int r=sc.nextInt();
			double v=sc.nextDouble(),e=sc.nextDouble(),f=sc.nextDouble();
			double[][] dp=new double[N+1][N+1];
			for(int i=1; i<=N; i++)for(int j=0; j<=N; j++)dp[i][j]=INF;
			//flash(dp,N);
			double tmp=0.0;
			for(int i=0; i<a[1]; i++)	tmp+=exp(i,r,v,e,f);
			dp[1][0]=tmp;
			for(int w=1; w<N; w++){
				for(int h=0; h<w; h++){
					int d=a[w+1]-a[w],x=a[w]-a[h];
					double exp=0.0;
					for(int i=0; i<d; i++)	exp+=exp(x++,r,v,e,f);
					//debug
					//System.out.println(exp);
					dp[w+1][h]=dp[w][h]+exp;
					double exp2=0.0;
					for(int i=0; i<d; i++)	exp2+=exp(i,r,v,e,f);
					dp[w+1][w]=min(dp[w+1][w], dp[w][h]+exp2+b);
				}
				//debug
				//System.out.println("new "+dp[w+1][w]);
			}
			//flash(dp,N);
			double ans=INF;
			for(int i=0; i<=N; i++)	ans=min(ans,dp[N][i]);
			return ans;
		}
		double exp(int x,double r,double v,double e,double f){
			return x>=r?(1/(v-e*(x-r))):(1/(v-f*(r-x)));
		}
		void flash(double[][] dp,int N){
			for(int y=0; y<=N; y++){
				for(int x=0; x<=N; x++)	System.out.printf("%3.3f ",dp[x][y]>=INF?-1:dp[x][y]);
				System.out.println();
			}
		}
	}
}