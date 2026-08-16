import java.io.*;
import java.util.*;
import java.math.*;

public class Competitive_1 {
	
	static char cost[];
	static int n, m;
	static boolean visited[];
	static boolean haveLoop=false;
	static int max = 0;
	static HashSet<Integer> list[];
	static HashSet<Integer> notRoots = new HashSet<Integer>();
	static Stored data[];
	
	public static void main(String[] args){
		FastReader in = new FastReader();
		n=in.nextInt();
		m=in.nextInt();
		cost = in.next().toCharArray();
		visited = new boolean[n];
		list = new HashSet[n];
		data = new Stored[n];
		
		for(int i=0; i<n; i++){
			list[i] = new HashSet<Integer>();
			data[i] = new Stored();
		}
		
		for(int i=0; i<m; i++){
			int x=in.nextInt()-1;
			int y=in.nextInt()-1;
			if(x==y)
				haveLoop = true;
			list[x].add(y);
			notRoots.add(y);
		}
		
		if(haveLoop || notRoots.size()==n){
			System.out.println(-1);
			return;
		}
		
		for(int i=0; i<n; i++){
			if(!visited[i] && !notRoots.contains(i)){
				int root = i;
//				HashSet<Integer> temp = new HashSet<Integer>();
//				temp.add(root);
//				while(findRoot(root)!=-1){
//					root = findRoot(root);
//					if(temp.contains(root)){
//						haveLoop = true;
//						break;
//					}else{
//						temp.add(root);
//					}
//				}
				
				if(haveLoop){
					System.out.println(-1);
					return;
				}
				
				//int freq[] = new int[26];
				//DFS(root, -1, new HashSet<Integer>(), freq);
				DFS(root, -1, new HashSet<Integer>());
				
				if(haveLoop){
					System.out.println(-1);
					return;
				}
				
				for(int j=0; j<26; j++)
					max = Math.max(max, data[root].count[j]);
				
			}
		}
		
		System.out.println(max);
	}
	
	static int findRoot(int node){
		for(int i=0; i<n; i++)
			if(list[i].contains(node) && i!=node)
				return i;
		
		return -1;
	}
	
	//static void DFS(int node, int prev, HashSet<Integer> stack, int freq[]){
	static void DFS(int node, int prev, HashSet<Integer> stack){
		if(visited[node]){
			if(stack.contains(node))
				haveLoop = true;
			return;
		}
		
		visited[node] = true;
		stack.add(node);
		//freq[cost[node]-'a']++;
		//max = Math.max(max, freq[cost[node]-'a']);
		
		for(int x:list[node]){
			if(x!=prev){
				//DFS(x, node, stack, freq);
				DFS(x, node, stack);
				for(int i=0; i<26; i++)
					data[node].count[i] = Math.max(data[node].count[i], data[x].count[i]);
			}
		}
		
		stack.remove(node);
		data[node].count[cost[node]-'a']++;
		//freq[cost[node]-'a']--;
	}
	
	static class Stored{
		int count[] = new int[26];
	}
	
	
	
	
	
	
	
	
	
	
	
	
	static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader()
        {
            br = new BufferedReader(new
                     InputStreamReader(System.in));
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt()
        {
            return Integer.parseInt(next());
        }
 
        long nextLong()
        {
            return Long.parseLong(next());
        }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
	
	
}
