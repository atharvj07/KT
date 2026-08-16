import java.util.*;
import java.util.Map.Entry;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Longest Increasing Sequence
// 2012/09/22
public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int n;
	long[] a;

	void run(){
		n=sc.nextInt();
		a=new long[n+1];
		for(int i=0; i<n; i++){
			a[i+1]=sc.nextInt();
		}
		a[0]=Long.MIN_VALUE;
		solve();
	}

	@SuppressWarnings("unchecked")
	void solve(){
		TreeMap<Long, Integer>[] dp=new TreeMap[n+1];
		HashMap<Long, Integer>[] cuts=new HashMap[n+1]; // if use TreeMap,
														// you'll receive TLE,
														// HAHAHA!!!
		for(int i=0; i<=n; i++){
			dp[i]=new TreeMap<Long, Integer>();
			cuts[i]=new HashMap<Long, Integer>();
		}
		dp[0].put(Long.MIN_VALUE, 0);

		for(int j=1; j<=n; j++){
			long sum=a[j];
			for(int i=j-1; i>=0; i--){
				// merge (i, j]
				Entry<Long, Integer> entry=dp[i].lowerEntry(sum);
				if(entry!=null){
					int value=cuts[j].containsKey(sum)?dp[j].get(sum):-1;
					if(entry.getValue()+1>value){
						dp[j].put(sum, entry.getValue()+1);
						cuts[j].put(sum, i);
					}
				}
				sum+=a[i];
			}
			// remove unnecessary entry from dp[j]
			int max=-1;
			ArrayList<Long> remove=new ArrayList<Long>();
			for(Entry<Long, Integer> entry : dp[j].entrySet()){
				long key=entry.getKey();
				int value=entry.getValue();
				if(value>max){
					max=value;
				}else{
					// unnecessary entry
					remove.add(key);
				}
			}
			for(long key : remove){
				dp[j].remove(key);
				cuts[j].remove(key);
			}
		}

		// restore "Longest Increasing Sequence"
		LinkedList<Integer> list=new LinkedList<Integer>();
		int cut;
		long sum;
		for(cut=n, sum=Long.MAX_VALUE; cut>=1;){
			list.addFirst(cut);
			sum=dp[cut].lowerKey(sum);
			cut=cuts[cut].get(sum);
		}
		list.removeLast();
		StringBuilder sb=new StringBuilder();
		sb.append(list.size()+1);
		sb.append('\n');
		for(int i : list){
			sb.append(i);
			sb.append(' ');
		}
		if(sb.charAt(sb.length()-1)==' '){
			sb.deleteCharAt(sb.length()-1);
		}
		println(sb.toString());
	}

	class Scanner{
		BufferedReader br;
		StringTokenizer st;

		Scanner(InputStream in){
			br=new BufferedReader(new InputStreamReader(in));
			eat("");
		}

		void eat(String s){
			st=new StringTokenizer(s);
		}

		String nextLine(){
			try{
				return br.readLine();
			}catch(IOException e){
				throw new IOError(e);
			}
		}

		boolean hasNext(){
			while(!st.hasMoreTokens()){
				String s=nextLine();
				if(s==null)
					return false;
				eat(s);
			}
			return true;
		}

		String next(){
			hasNext();
			return st.nextToken();
		}

		int nextInt(){
			return Integer.parseInt(next());
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}