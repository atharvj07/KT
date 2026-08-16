import java.util.Scanner;
import java.io.*;
import java.util.*;
import java.math.*;
import java.lang.*;
import static java.lang.Math.*;
 
public class Main implements Runnable{
 
	static class InputReader
	{
		private InputStream stream;
		private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;
		private SpaceCharFilter filter;
		
		public InputReader(InputStream stream)
		{
			this.stream = stream;
		}
		
		public int read()
		{
			if (numChars==-1) 
				throw new InputMismatchException();
			
			if (curChar >= numChars)
			{
				curChar = 0;
				try 
				{
					numChars = stream.read(buf);
				}
				catch (IOException e)
				{
					throw new InputMismatchException();
				}
				
				if(numChars <= 0)				
					return -1;
			}
			return buf[curChar++];
		}
	 
		public String nextLine()
		{
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
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
		public int nextInt()
		{
			int c = read();
			
			while(isSpaceChar(c)) 
				c = read();
			
			int sgn = 1;
			
			if (c == '-') 
			{
				sgn = -1;
				c = read();
			}
			
			int res = 0;
			do 
			{
				if(c<'0'||c>'9') 
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			while (!isSpaceChar(c)); 
			
			return res * sgn;
		}
		
		public long nextLong() 
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') 
			{
				sgn = -1;
				c = read();
			}
			long res = 0;
			
			do 
			{
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			while (!isSpaceChar(c));
				return res * sgn;
		}
		
		public double nextDouble() 
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			int sgn = 1;
			if (c == '-') 
			{
				sgn = -1;
				c = read();
			}
			double res = 0;
			while (!isSpaceChar(c) && c != '.') 
			{
				if (c == 'e' || c == 'E')
					return res * Math.pow(10, nextInt());
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res *= 10;
				res += c - '0';
				c = read();
			}
			if (c == '.') 
			{
				c = read();
				double m = 1;
				while (!isSpaceChar(c)) 
				{
					if (c == 'e' || c == 'E')
						return res * Math.pow(10, nextInt());
					if (c < '0' || c > '9')
						throw new InputMismatchException();
					m /= 10;
					res += (c - '0') * m;
					c = read();
				}
			}
			return res * sgn;
		}
		
		public String readString() 
		{
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do 
			{
				res.appendCodePoint(c);
				c = read();
			} 
			while (!isSpaceChar(c));
			
			return res.toString();
		}
	 
		public boolean isSpaceChar(int c) 
		{
			if (filter != null)
				return filter.isSpaceChar(c);
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
	 
		public String next() 
		{
			return readString();
		}
		
		public interface SpaceCharFilter 
		{
			public boolean isSpaceChar(int ch);
		}
	}
	static LinkedList <Integer> adj[];
    
    static void Check2(int n){
        adj=new LinkedList[n+1];
        for(int i=0;i<=n;i++){
            adj[i]=new LinkedList();
        }
        
    }
    static void add(int i,int j){
       // if(!adj[i].contains(j))
        adj[i].add(j);
   // if(!adj[j].contains(i))
        adj[j].add(i);
        
     //   adj[j].add(i);
        
    }
	  public static void main(String[] args) throws Exception { 
    new Thread(null, new Main(), "Check2", 1<<26).start();// to increse stack size in java 
  }
    static int flag2=1;
    static int ne=0;
  public void run(){
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        //Scanner in=new Scanner(System.in);
    InputReader in=new InputReader(System.in);		
		PrintWriter w=new PrintWriter(System.out);
	
 
		
      
   int n=in.nextInt();
      
      
      int k=in.nextInt();
      
      int a[]=new int[n];
      for(int i=0;i<n;i++)
      {
          a[i]=in.nextInt();
      }
      
      
   if(k>=n){
       HashMap <Integer,Integer> map=new HashMap();
          for(int i=0;i<n;i++){
             
              map.put(a[i],1);
             // cost++;
          }
          
       w.println(map.size());
   }   
      else{
          
          
          int cost=0;
          
          HashMap <Integer,Integer> map=new HashMap();
          for(int i=0;i<k;i++){
             
              map.put(a[i],1);
             // cost++;
          }
          
          cost=map.size();
          for(int i=k;i<n;i++)
          {
              
              int f[]=new int[n+1];
                      HashMap <Integer,Integer> map2=new HashMap();
  if(map.containsKey(a[i])){
      continue;
  }
              else if(map.size()<k){
              
                  map.put(a[i],i);
                  cost++;
                  continue;
              }
              
              
              int flag=0;
              
             for (Map.Entry<Integer,Integer> entry : map.entrySet()) {
     Integer key = entry.getKey();
    
                 
                 
                for(int j=i+1;j<n;j++){
                    if(a[j]==key){
                        flag=1;
                        if(!map2.containsKey(a[j]))
                        map2.put(a[j],j);
                    }
                } 
                
                 
                if(!map2.containsKey(key)){
                    map2.put(key,1000);
                }
                    
             } 
              if(flag==1){
                  int max=0;
                  int id=-1;
                       for (Map.Entry<Integer,Integer> entry : map2.entrySet()) {
     Integer key = entry.getKey();
                           int val=entry.getValue();
                           
              //     System.out.println(key+" "+val);        
                           if(val>max){
                               max=val;
                               id=key;
                           }
                           
                           
                           
                       }
      //            System.out.println(id+" "+i);
                  map.remove(id);
                  cost++;
              }
              else{
                  
                  
                  int id=-1;
                       for (Map.Entry<Integer,Integer> entry : map2.entrySet()) {
     Integer key = entry.getKey();
                           id=key;
                           break;
                           //int val=entry.getValue();
                       }
                  map.remove(id);
                  
                  
                  
                  
                  cost++;
                  
                  
                  
                  
                  
                  
                  
              }
              
              
              
              
              
              
              
              
              
              
              map.put(a[i],i);
              
              
              
              
              }
          
          
          
          
          
          w.println(cost);
          
          
          
          
          
          
          
      }
      
      
      
      
      
      
        w.close();
        
           
    }
    static class node{
        
        int y;
        int val;
        
        node(int a,int b){
            
            y=a;
            val=b;
            
        }
        
        
    }
    
} 
 