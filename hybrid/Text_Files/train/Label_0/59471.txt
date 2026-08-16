import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.TreeMap;

/**
 *
 * @author ehab
 */
public class JavaApplication1 {

    
      

   
    
    static long totalcost [] , saving[] , indcost [] ;
    static boolean is[] ;
    static int getMin(){
     int ind = -1 ;   
    long min = Integer.MAX_VALUE ;
        for(int i = 0 ; i < totalcost.length ; i++)
          if(!is[i])
          {
           if(totalcost[i]-(saving[i]*indcost[i]) < min)
           {
            min = totalcost[i]-(saving[i]*indcost[i]) ;
            ind = i ;
           }
          }
    
    return ind ;
    }
    public static void main(String[] args) throws Exception
    {
        Reader.init(System.in);

        StringBuilder ans = new StringBuilder() ;
        String s = Reader.next() ;
        PriorityQueue<pair> pr = new PriorityQueue<pair>() ;
        for(int i = 0 ; i < s.length() ; i++)
            pr.add(new pair(s.charAt(i) , i)) ;

        Stack<pair> st = new Stack<pair>() ;
        st.add(new pair(s.charAt(0) , 0));
        int stakInd = 1 ;
       
        while(!pr.isEmpty())
        {
         pair p = pr.poll() ;
         while(!st.isEmpty() && st.peek().a <= p.a)
         {
          ans.append( (char)(st.pop().a) +"") ;
         
         }
         if(stakInd <= p.b)
         {
           for(int i = stakInd ; i <= p.b ; i++ , stakInd++)
            st.push(new pair(s.charAt(stakInd) , i)) ;
           ans.append((char)st.pop().a) ;

               
         
         }
         
        }
        System.out.println(ans);
        
        }
        
         
    }
        
        
        
        
        
    
    


 class pair implements Comparable<pair>
    {
     int  a , b; 
     
     
    pair(int a , int b)
    {
    this.a = a ;
    this.b = b ;
    
    
   
  
    }
  
    public int compareTo(pair t) {
        if(t.a < a)
            return 1 ;
        else if(t.a > a)
            return -1;
        else if(t.b < b ) return 1 ;
        else if(t.b > b) return -1 ;
        else return 0 ;
    }
    
    
    
    }



class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    
    static void init(InputStream input) {
        reader = new BufferedReader(
                     new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }

   
    static String next() throws IOException {
        while ( ! tokenizer.hasMoreTokens() ) {
            
            tokenizer = new StringTokenizer(
                   reader.readLine() );
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt( next() );
    }
	 static int nextShort() throws IOException {
        return Short.parseShort(next() );
    }
    static double nextDouble() throws IOException {
        return Double.parseDouble( next() );
    }
    static long nextLong() throws IOException{
    return Long.parseLong(next()) ;
    }
}