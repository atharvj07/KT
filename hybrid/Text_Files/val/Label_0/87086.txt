import java.util.*;
import java.io.*;
import java.lang.*;
import java.net.*;


  
public class Main
{ 
    static class FastReader 
    { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastReader() 
        { 
            br = new BufferedReader(new
                     InputStreamReader(System.in));;;;;
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
  
        int cint() 
        { 
            return Integer.parseInt(next()); 
        } 
        
        long clong() 
        { 
            return Long.parseLong(next()); 
        } 
  
        double cdouble() 
        { 
            return Double.parseDouble(next()); 
        } 
  
        String cline() 
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
    static class mycomp implements Comparator<Integer>{
        public int compare(Integer a, Integer b){
            return b-a;
        }
    }
    static boolean contains(int l,int r,int ans_l,int ans_r){
        if(r<ans_l||l>ans_r)return false;
        else return true;
    }

    
   public static void main(String[] args){
       FastReader f=new FastReader();
       int t=f.cint();
       while(t-->0){
           int n,x,m;int ans_l,ans_r;
           n=f.cint();
           x=f.cint();
           m=f.cint();ans_l=x;ans_r=x;
           for(int i=0;i<m;i++){
               int l,r;
               l=f.cint();r=f.cint();              
                   if(contains(l,r,ans_l,ans_r)){
                       ans_l=Math.min(l,ans_l);
                       ans_r=Math.max(r,ans_r);
                   
               }
           }
           System.out.println(ans_r-ans_l+1);
       }
    }
}
      