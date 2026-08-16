import java.util.*;
import java.lang.*;
import java.io.*;
public class MAIN {

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
	static class triple
	{
		int x , y ,z ;
		
		triple(int x ,int y ,int z)
		{
			this.x=x;
			this.y=y;
			this.z=z;
		}
	}
	static class Graph{
		int n ;
		ArrayList<Integer>[] a;
		
		Graph(int n)
		{
			this.n = n;
			a = new ArrayList[n];
			for(int i =0;i<n;i++)
			{
				a[i] = new ArrayList<>();
			}
			
			
		}
		
		void BFS(Graph g,int n ,PrintWriter out)
		{
		}
	}

	public static void main(String[] args){
		// TODO Auto-generated method 
		OutputStream outputStream = System.out;
        FastReader sc = new FastReader();
        PrintWriter out = new PrintWriter(outputStream);
        int n = sc.nextInt();
        Graph g = new Graph(n);
        int m = sc.nextInt();
        
        //Graph g = new Graph(n);
        for(int i = 0;i<m;i++)
        {
        	int x = sc.nextInt()-1;
        	int y = sc.nextInt()-1;
        	g.a[x].add(y);
        	g.a[y].add(x);
        }

		boolean[] visited = new boolean[n];
		Arrays.fill(visited, false);
		PriorityQueue<Integer> q = new PriorityQueue();
		visited[0]=true;
		q.add(0);
		while(!q.isEmpty())
		{
			int item = q.poll();
			out.print((item+1)+" ");
			
			Iterator<Integer> i = g.a[item].iterator();
			while(i.hasNext())
			{
				int temp = i.next();
				if(visited[temp]!=true)
				{
					q.add(temp);
					visited[temp]=true;
				}
			}
			//out.println(q.toString());
			
		}
        /*for(int i =0;i<n;i++)
        	out.print(g.a[i].toString());*/
        g.BFS(g,n,out);
        		out.close();
		

	}

}
