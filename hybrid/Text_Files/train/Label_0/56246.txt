import java.io.* ;
import java.util.*;

import static java.lang.Math.* ;
import static java.util.Arrays.* ;

public class C {
	
	public static void main(String[] args) throws IOException {
		
		new C().solveProblem();
		
		out.close();
	}

	static Input in = new Input() ;
	static PrintStream out = new PrintStream(new BufferedOutputStream(System.out));	
	static Output out2 = new Output(out) ;
	
	
    public void solveProblem() throws IOException {     
    
        int h1 = in.nextInt();
        int h2 = in.nextInt();
        
        int n = in.nextInt();
       

        int max = 0;
        ArrayList<Spiegel> boven = new ArrayList<C.Spiegel>();
        ArrayList<Spiegel> onder = new ArrayList<C.Spiegel>();
        
        for( int i =0; i < n ; i++){
            int p = in.nextInt();
            String s = in.next();
            Spiegel sp = new Spiegel(in.nextInt(),in.nextInt(),p);
            if( s.equals("F"))
                onder.add(sp);
            else
                boven.add(sp);
        }
        
        //p( g(onder,boven,100-h1,100-h2));
        //;
        max = max( g(boven,onder,h1,h2),g(onder,boven,100-h1,100-h2));
        out.println(max);
    }
    
    private int g(ArrayList<Spiegel> boven, ArrayList<Spiegel> onder, int h1,
            int h2) {
        
        int max = 0;
        for( int h = 1; h <= 100; h++){
            
            for( Spiegel sp : boven)
                sp.gone = false;
            for( Spiegel sp : onder)
                sp.gone = false;
            //h = 6;
            int he = h * 100;
            
            if( h%2==1)
                he += 100-h2;
            else
                he += h2;
        
            double r = 100000./ (double) (he - h1) ;
            double l = r*(double) (100-h1);
       
            int p = 0;
            for( int k = 1; k <= h ; k++){
             

                
                Spiegel sp = k % 2 == 1 ? cont(boven,l) : cont(onder,l);
                if( sp == null){
                    p = 0;
                    break;
                }else{           
                
                sp.gone = true;
                p += sp.w;
       
                }
             
                if( k < h)
                    l += r*100.;
            }
            
            l += 28.*r;
           // p(l);
            max = max(p,max);
           //break;
            
        }
        
        return max;
    }

    private Spiegel cont(ArrayList<Spiegel> boven, double l) {
        
        for( Spiegel s : boven){
  
            if( !s.gone && s.van - eps < l && l < s.tot + eps)
                return s;
        }
        return null;
    }

    double eps = 1e-9;
    class Spiegel{
        double van;
        double tot;
        int w;
        
        boolean gone = false;
        
        public Spiegel(int van, int tot, int w) {
            super();
            this.van = van;
            this.tot = tot;
            this.w = w;
        }
        
        
    }
	
	static void p( Object ...p){
		System.out.println(Arrays.deepToString(p));
	}
	
	static class Input {	
		
		BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer tokens ;
		
		public int nextInt(){
			return Integer.parseInt(next()) ;
		}

		public int[] nextInt(int n ){
			int[] res = new int[n] ;
			for( int i = 0 ; i < n ; i++ )
				res[i] = nextInt() ;
			return res ;
		}

		public long nextLong(){
			return Long.parseLong(next()) ;
		}

		public long[] nextLong(int n ){
			long[] res = new long[n] ;
			for( int i = 0 ; i < n ; i++ )
				res[i] = nextLong() ;
			return res ;
		}
		
		public double nextDouble(){
			return Double.parseDouble(next()) ;
		}
		
		public String next(){
			
			try{
				while( tokens == null || !tokens.hasMoreTokens() )
					tokens = new StringTokenizer(buf.readLine()) ;
			}catch( Exception e ){
				e.printStackTrace() ;
			}
			
			return tokens.nextToken() ;
		}

		public String nextLine(){
		    try {
                return buf.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
		    return null;
		}
	}

	static class Output {
		
		PrintStream out ;
		
		public Output(PrintStream out) {
			this.out = out;
		}

		void wr( int[] rij ){
			for( int i = 0 ; i < rij.length - 1 ; i++ ) 
				out.print(rij[i] + " ") ;
			out.println(rij[rij.length-1]);		
		}

		void wr( long[] rij ){
			for( int i = 0 ; i < rij.length - 1 ; i++ ) 
				out.print(rij[i] + " ") ;
			out.println(rij[rij.length-1]);		
		}
		
		void wr( char[] rij){
			out.println(new String(rij)) ;
		}
		
	}
}
